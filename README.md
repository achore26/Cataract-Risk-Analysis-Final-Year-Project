Web-Based Cataract Risk Assessment System Using Deep Learning and Image Processing
Author
Albert Chore

Student ID: SCT221-0787/2020

Jomo Kenyatta University of Agriculture and Technology (JKUAT)

📌 Project Vision and Background: Bridging the Gap in Eye Care
This project is more than just a piece of code—it's a step towards addressing a significant public health issue.

The Problem: According to the World Health Organization, cataracts are the leading cause of blindness worldwide, accounting for nearly 51% of global blindness cases. In countries like Kenya, many individuals, particularly in remote regions, do not seek medical attention until the condition has significantly worsened. This is primarily due to a lack of awareness, financial constraints, and an extremely low ratio of ophthalmologists to the general population. This leads to delayed treatment and, often, avoidable blindness. The existing healthcare infrastructure, especially in rural and underserved areas, struggles to provide widespread, early screening.

The Solution: This project aims to bridge that gap by creating an accessible, web-based tool for preliminary cataract risk assessment. The system allows users to upload images of their eyes through a simple website. These images are then analyzed using a trained deep learning model to check for early signs of cataracts. The system's goal is to provide a preliminary risk assessment that encourages high-risk individuals to seek professional medical help early enough for proper treatment.

Our Goal: To use modern, accessible digital technology to empower individuals, particularly in underserved areas, to take control of their eye health. The system is designed to be a simple and convenient first-line screening tool, supporting global efforts to reduce preventable blindness in a scalable way.

✨ Key Features
User Authentication: Secure registration and login functionality via a web interface.

Image Upload Interface: A user-friendly, drag-and-drop interface for uploading eye images (JPG/PNG).

Real-time Risk Prediction: An integrated deep learning model analyzes the uploaded image to provide a cataract risk classification.

Intuitive Results: The system displays a clear result (Low Risk, Moderate Risk, or High Risk) along with a confidence score.

Actionable Recommendations: Provides text-based recommendations and next steps based on the risk level.

Responsive Design: The application is fully compatible with both mobile phones and desktop browsers.

Admin Dashboard (Optional): An administrative view for monitoring system usage, user activity, and prediction logs.

⚙️ Technologies Used
This project leverages a modern, three-tier web architecture to ensure scalability, maintainability, and security.

Backend:

Python: The core programming language for the application logic and machine learning model integration.

Flask: A lightweight and flexible Python web framework for handling server-side requests and routing.

TensorFlow/Keras: The primary deep learning framework used to build and train the Convolutional Neural Network (CNN) model for image analysis.

Frontend:

HTML, CSS, JavaScript: Standard web technologies for building the user interface.

Responsive Design: Ensures the application is usable across various devices and screen sizes.

Database:

SQLite: Used for local development to store user credentials and prediction logs (not permanent image data).

Version Control:

Git & GitHub: For project management, version control, and collaboration.

🚀 Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.8+: The project's core dependencies require this version or higher.

pip: The Python package installer for managing project dependencies.

A code editor: A tool like VS Code or PyCharm is recommended for development.

Installation
Clone the repository:
Start by cloning the project from its GitHub repository to your local machine.

git clone https://github.com/your-username/your-project.git
cd your-project



Create a virtual environment:
It is highly recommended to create a virtual environment to manage dependencies and avoid conflicts with other Python projects.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`



Install dependencies:
Install all the required Python libraries and frameworks listed in the requirements.txt file.

pip install -r requirements.txt



Run the Flask development server:
Launch the web application to begin development and testing.

flask run



The application should now be running at http://127.0.0.1:5000/.

📚 Project Methodology and Research
2.0 Literature Review
This project is built on a foundation of existing academic research in the field of AI-driven medical imaging. The literature review was crucial for understanding the state-of-the-art in ophthalmology diagnostics and identifying a critical research gap.

Theoretical Framework: The system draws upon key theories from Machine Learning and Deep Learning. Specifically, it uses Convolutional Neural Networks (CNNs) for image classification, Supervised Learning to train models on labeled datasets, and Transfer Learning to fine-tune pre-trained models.

Image Processing: The system uses techniques like Histogram Equalization to enhance image contrast and Gaussian Filtering to reduce noise, ensuring the images are optimized for the deep learning model.

Research Gaps: The review highlighted a lack of research on AI-driven cataract risk assessment specifically in the Kenyan context, as well as challenges with dataset diversity and model generalizability. This project is a direct effort to address these gaps by creating a localized, accessible, and effective screening tool.

Critique of Existing Work: A comparative analysis of existing studies was performed to understand the strengths and weaknesses of various techniques, datasets, and methodologies, informing the development choices for this project.

3.0 System Analysis and Design
This section outlines the comprehensive approach taken to design the system, translating theoretical concepts into a practical, functional application.

3.1 System Development Methodology
A hybrid methodology was adopted to manage the different components of the project effectively:

Agile Methodology: Used for the web application development (front and back-end) to allow for iterative sprints, rapid prototyping, and continuous feedback from potential users.

CRISP-DM: Employed for the machine learning component, providing a structured and systematic approach to data understanding, preparation, model training, and evaluation.

3.2 Feasibility Study
The project's feasibility was evaluated across four key dimensions:

Technical Feasibility: The system relies on well-documented and widely adopted open-source technologies (Python, Flask, TensorFlow), ensuring a smooth and reliable implementation.

Operational Feasibility: Designed to address a pressing public health problem in Kenya with a user-friendly and intuitive interface, ensuring high potential for user adoption.

Economic Feasibility: The use of open-source tools and free cloud services minimizes the budget, making it viable as a student research project.

Schedule Feasibility: The project follows a clear 8-month timeline, with a Gantt chart detailing each phase from research to deployment.

3.3 Requirement Elicitation & Specification
A user-centered approach was used to gather both functional and non-functional requirements:

Elicitation: Data was collected through structured questionnaires and informal interviews with potential users and optometrists in Nairobi County.

Requirements: This data informed the creation of detailed functional requirements (e.g., user authentication, image upload, risk prediction) and non-functional requirements (e.g., responsive design, security, performance).

3.4 Logical and Physical Design
The system's design was meticulously planned using industry-standard diagrams:

Logical Design: Includes wireframes for key pages (Login, Upload, Results, Admin Dashboard) to define the user interface layout and flow.

Physical Design: Detailed using a Use Case Diagram, Entity Relationship Diagram (ERD), and System Flow Diagram to illustrate the system's architecture, data relationships, and processing logic. This confirms how the components interact to deliver the final product.

🖥️ User Interface Design
Data Visualization and Wireframes
The following diagrams illustrate the project's data insights, user journey, and system architecture.

Gantt Chart - Cataract Risk Assessment System
A Gantt chart outlining the project's schedule, from research and proposal refinement to system deployment and final report submission. It provides a visual timeline of all key tasks and milestones over an 8-month period.
![Gantt Chart - Cataract Risk Assessment System](path/to/your/gantt_chart_image.png)

Bar Chart: Most Requested System Features
This chart presents the results from a user survey, highlighting the most prioritized features for the web application. The data directly informed the functional requirements of the system, emphasizing the need for simplicity, data privacy, and mobile compatibility.
![Bar Chart: Most Requested System Features](path/to/your/bar_chart_features_image.png)

Pie Chart: Internet Access Frequency
This pie chart shows the distribution of internet usage frequency among survey participants. The data confirms a high level of digital readiness within the target population, justifying the development of a web-based solution.
![Pie Chart: Internet Access Frequency](path/to/your/pie_chart_image.png)

Bar Chart: Digital Comfort by Age Group
This visualization illustrates the percentage of users who reported being "comfortable" versus "not comfortable" with digital tools, segmented by age. The data highlights the need for an intuitive and user-friendly interface that accommodates users with varying levels of digital literacy, especially among older demographics.
![Bar Chart: Digital Comfort by Age Group](/home/alby/Desktop/flask trial/images)

Wireframe: Login/Registration Page
A visual blueprint of the login and registration page, outlining the layout and key interactive elements for user authentication.
![Wireframe: Login/Registration Page](path/to/your/login_page_image.png)

Wireframe: Image Upload Page
The wireframe for the core user functionality, showing the interface for uploading eye images and providing clear instructions and guidelines for image quality.
![Wireframe: Image Upload Page](path/to/your/image_upload_page_image.png)

Wireframe: Analysis Results Page
A wireframe that displays the final output of the system's analysis, including the risk prediction, confidence score, and recommended next steps for the user.
![Wireframe: Analysis Results Page](path/to/your/results_page_image.png)

Wireframe: Admin Dashboard
This wireframe shows the administrative interface, providing an overview of system usage, active users, and high-risk cases for monitoring and analysis.
![Wireframe: Admin Dashboard](path/to/your/admin_dashboard_image.png)

📊 System Diagrams
Technical and Logical Diagrams
Use Case Diagram
This diagram illustrates the interactions between the primary actors (User and Admin) and the system. It defines all major functionalities and system boundaries, providing a high-level view of how users will interact with the application.
![Use Case Diagram](path/to/your/use_case_diagram_image.png)

Entity Relationship Diagram (ERD)
The ERD models the relationships between core data entities in the system, including users, prediction logs, and image data. This diagram is crucial for understanding the database structure and how different pieces of information are connected.
![Entity Relationship Diagram](path/to/your/erd_image.png)

System Flow Diagram
This flowchart details the logical flow of the application, from user input to final output. It maps out the sequence of events for user authentication, image validation, model prediction, and result delivery.
![System Flow Diagram](path/to/your/system_flow_diagram_image.png)

🧪 System Testing and Validation
The project was rigorously tested to ensure it meets all functional and non-functional requirements. The testing phase focused on validating the system's correctness, performance, security, and usability.

Unit and Integration Testing: We conducted a total of 48 unit tests and 12 integration tests to verify the correctness of individual functions and end-to-end user flows. All critical scenarios passed, and an edge case related to corrupted image handling was successfully fixed.

Performance Testing: Using simulated load, the system demonstrated a median prediction latency of approximately 3.2 seconds. Under a simulated load of 100 concurrent users, the 95th percentile latency was approximately 9.8 seconds, meeting the non-functional requirement of providing results in less than 10 seconds.

Usability Testing: A pilot usability study with 6 participants yielded a System Usability Scale (SUS) score of ≥70, indicating good usability. Feedback from this phase led to minor interface improvements, such as clearer button labels and help text.

Security Validation: Automated security scans and a static code review were performed. This led to improvements in file upload sanitization and other security measures.

Future Deployment: The codebase has been prepared for a secure cloud deployment, with sensitive information like model weights and API keys externalized to ensure they are not committed to the repository.

🚧 Limitations and Future Work
This section highlights the current limitations and offers recommendations for future development to enhance the system's capabilities and robustness.

Model Generalizability: The current model's accuracy and generalizability could be improved with a larger, more diverse dataset, especially one that is representative of different regions and demographics in Kenya.

Clinical Validation: A critical next step is to conduct a prospective clinical study where the model's predictions are compared against professional ophthalmologist diagnoses to validate its effectiveness in a real-world setting.

Production Hardening: For a full-scale public launch, the system should be deployed in a containerized environment with advanced security measures like rate limiting and strict upload sanitization rules to prevent malicious use. Rate limiting is a control mechanism used to manage network traffic to prevent users from exhausting system resources and mitigate attacks such as Denial of Service (DoS) attacks.

Continuous Improvement: We recommend implementing a system for periodic model retraining with new, anonymized data to continuously improve its accuracy and adapt to new insights.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Please feel free to open a pull request or submit an issue on the repository.
