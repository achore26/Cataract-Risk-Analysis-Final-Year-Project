# Replace 'admin_username' with the username of the admin
admin_user = User.query.filter_by(username='admin').first()
if admin_user:
    admin_user.is_admin = True
    db.session.commit()
    print(f"Admin status set for {admin_user.username}")
else:
    print("User not found!")