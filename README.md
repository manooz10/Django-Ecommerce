# Django Ecommerce Website

A full-stack **E-commerce website built using Django and Python**.  
The project provides a simple online shopping platform where users can browse products and view product details.

## 🚀 Features

- 🛍️ Product listing
- 📦 Product detail page
- 🏪 Store application
- 🖼️ Product images and media
- 🎨 Custom CSS styling
- 📱 Responsive web pages
- 👤 Django admin panel
- 🗄️ Database integration
- 📞 Contact page
- 🔐 Django-based backend

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Git
- GitHub

## 📁 Project Structure

```text
electronics/
│
├── electronics/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
├── static/
│   ├── css/
│   └── images/
│
├── media/
│   └── products/
│
├── .gitignore
├── data.json
├── manage.py
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/manooz10/Django-Ecommerce.git
2. Open the project directory
cd Django-Ecommerce
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
5. Install Django

If you have a requirements.txt file:

pip install -r requirements.txt

Otherwise:

pip install django
🗄️ Database Setup

Run Django migrations:

python manage.py makemigrations
python manage.py migrate
👤 Create Admin User

Create a Django superuser:

python manage.py createsuperuser

Enter your:

Username
Email
Password
▶️ Run the Project

Start the Django development server:

python manage.py runserver

Open your browser:

http://127.0.0.1:8000/
🔧 Admin Panel

The Django admin panel is available at:

http://127.0.0.1:8000/admin/

Use the superuser credentials created earlier to log in.

📦 Product Management

Products can be managed through the Django admin panel.

The project uses the store application for handling:

Products
Product information
Product images
Store-related functionality
🖼️ Static and Media Files

Static files are stored in:

static/
├── css/
└── images/

Uploaded product media is stored in:

media/
└── products/
📄 Important Django Files
manage.py

Used to perform Django management commands such as:

python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
models.py

Contains the database models for the store application.

views.py

Contains the application logic and views.

urls.py

Defines URL routes for the website.

settings.py

Contains Django project configuration such as:

Installed applications
Database configuration
Static files
Media files
Templates
Security settings
🔒 Security

Do not upload sensitive information to GitHub.

Make sure your .gitignore contains:

__pycache__/
*.py[cod]
*.sqlite3
.env
venv/
.venv/
media/
staticfiles/
.vscode/

If you want to keep product images in GitHub, you can remove:

media/

from .gitignore.

🚧 Future Improvements
🛒 Shopping cart
🔎 Product search
🔍 Product filtering
⭐ Product reviews and ratings
📦 Order management
👤 User profile
🚀 Deployment to production
👨‍💻 Author

Manoj Bhandari

📜 License

This project is developed for educational and portfolio purposes.


Then run:

git add .
git commit -m "Add README and project files"

After that, connect your GitHub repository and push:

git branch -M main
git remote add origin https://github.com/manooz10/Django-Ecommerce.git
git push -u origin main
