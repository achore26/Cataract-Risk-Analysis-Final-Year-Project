from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate  # Added for database migrations
import os
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash  # Added for password hashing
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cataract_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)

# Load the model
model = load_model('models/cataract_model.h5')

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Admin flag
    results = db.relationship('Result', backref='user', lazy=True)

    # Password hashing methods
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    result = db.Column(db.String(50), nullable=False)
    probability = db.Column(db.Float, nullable=False)  # Add this field
    risk_level = db.Column(db.String(20), nullable=False)  # Add this field
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username)
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/admin/upload/<int:result_id>/delete', methods=['POST'])
@login_required
def delete_upload(result_id):
    if not current_user.is_admin:
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('index'))
    result = Result.query.get_or_404(result_id)
    db.session.delete(result)
    db.session.commit()
    flash('Upload deleted successfully.', 'success')
    return redirect(url_for('view_user', user_id=result.user_id))

@app.route('/admin/generate_report')
@login_required
def generate_report():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('index'))
    users = User.query.all()
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Add content to the PDF
    pdf.drawString(100, 750, "System Report")
    y = 730
    for user in users:
        pdf.drawString(100, y, f"User: {user.username} (ID: {user.id})")
        y -= 20
        results = Result.query.filter_by(user_id=user.id).all()
        for result in results:
            pdf.drawString(120, y, f"Upload ID: {result.id}, Result: {result.result}, Date: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            y -= 20
        y -= 10

    # Save the PDF
    pdf.showPage()
    pdf.save()

    # Return the PDF as a downloadable file
    buffer.seek(0)
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='system_report.pdf'
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Check if the user exists and the password is correct
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            
            # Redirect to admin dashboard if the user is an admin
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('upload'))
        else:
            flash('Invalid username or password!', 'danger')
    return render_template('login.html')

@app.route('/admin/user/<int:user_id>')
@login_required
def view_user(user_id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('index'))
    user = User.query.get_or_404(user_id)
    results = Result.query.filter_by(user_id=user.id).order_by(Result.timestamp.desc()).all()
    return render_template('admin/user_details.html', user=user, results=results)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# In the upload route
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded!', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected!', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocess the image and make a prediction
            img = tf.keras.utils.load_img(filepath, target_size=(256, 256))
            img_array = tf.keras.utils.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_array)
            probability = float(prediction[0][0])  # Get the probability score

            # Classify risk level based on probability
            if probability > 0.3:
                risk_level = "Low"
            elif probability > 0.5:
                risk_level = "Moderate"
            else:
                risk_level = "High"

            # Save the result to the database
            new_result = Result(
                user_id=current_user.id,
                image_path=filepath,
                result=f"{risk_level} (Probability: {probability:.2f})",
                probability=probability,
                risk_level=risk_level
)
            db.session.add(new_result)
            db.session.commit()

            return render_template('result.html', probability=probability, risk_level=risk_level, image_url=filepath, result_id=new_result.id)
    return render_template('upload.html')

@app.route('/history')
@login_required
def history():
    results = Result.query.filter_by(user_id=current_user.id).order_by(Result.timestamp.desc()).all()
    return render_template('history.html', results=results)

@app.route('/download_report/<int:result_id>')
@login_required
def download_report(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('You are not authorized to access this report.', 'danger')
        return redirect(url_for('history'))

    # Create a PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Add content to the PDF
    pdf.drawString(100, 750, "Cataract Risk Assessment Report")
    pdf.drawString(100, 730, f"Result: {result.result}")
    pdf.drawString(100, 710, f"Date: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    pdf.drawImage(result.image_path, 100, 400, width=200, height=200)

    # Save the PDF
    pdf.showPage()
    pdf.save()

    # Return the PDF as a downloadable file
    buffer.seek(0)
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'report_{result_id}.pdf'
    )

# Admin Routes
@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('admin/dashboard.html', users=users)

@app.route('/admin/user/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('index'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/user/<int:user_id>/toggle_admin', methods=['POST'])
@login_required
def toggle_admin(user_id):
    if not current_user.is_admin:
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('index'))
    user = User.query.get_or_404(user_id)
    user.is_admin = not user.is_admin
    db.session.commit()
    flash(f'Admin status for {user.username} has been toggled.', 'success')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)