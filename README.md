barua Iko

## Description

Kibarua Iko is a website that links skilled workers with people willing to hire. This project is designed to facilitate user interactions through a feature like tinder where a client swipes left or right to choose a skilled worker that he/she needs. Users will be a ble to create an account by registering and once you login you can either to be a client or skilled worker you will have the option to become both the client or the skilled worker. This project was built using python, the web framework used was Flask and for frontend Javascript, HTML and CSS . This README will guide you through the setup process, including how to configure your email settings.

## Features

- User-friendly contact form
- Email notifications upon form submission
- Customizable email settings

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- A working email account to send notifications

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

2. Install the required packages:
	pip install -r requirements.txt

3. Create a configuration file:
	You need to create a file named configure_password.py in the app directory of the project. This file will store your email credentials, in order for the Contact Us to send a message your email and password will be used as the sender's.

		Email = "your_email@example.com"
		password = 'your_password'

	NOTE - The Email and password variable should be exactly the same, and replace the email and password with your details.

4. Update the recipient email in routes.py:
	Open the routes.py file and locate the line where the recipient's email is defined, this will enable the message to come to your email. Change it to your email address:

		msg = Message(
    subject=f"Mail from: {name}",
    body=f"""
    Name: {name}\n
    E-mail: {email}\n\n\n
    Message: {message}""",
    sender=Email,
    recipients=["your_email@example.com"]  # Change this to your email

5. Run the application:
	Start the application at the root of the directory there is a file run.py, use the command:

	python3 -m run


