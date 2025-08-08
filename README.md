# HealthDoc

HealthDoc is a modern Django-based healthcare platform that helps patients find hospitals, book appointments with doctors, and get AI-powered health insights. It features role-based dashboards for doctors and patients, appointment management, and a built-in Gemini 2.0 AI chatbot for health queries.

## Features
- **Role-based Login & Registration**: Separate flows for doctors and patients
- **Doctor & Patient Dashboards**: Personalized dashboards for each role
- **Book Appointments**: Patients can browse doctors and book appointments easily
- **Doctor Management**: Doctors can manage their appointments and profile
- **Hospital Directory**: Search and view hospitals with images
- **AI Chatbot**: A Specialized Health chatbot for instant health-related queries
- **Modern UI**: Responsive, mobile-friendly design with Tailwind CSS and FontAwesome

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/SouvagyaDey/HealthDoc.git
cd HealthDoc/HealthDoc
```

### 2. Create and Activate a Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Set Up Gemini API Key
- Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Set it as an environment variable:
```
export GEMINI_API_KEY='YOUR_GEMINI_API_KEY'
```

### 5. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```
python manage.py createsuperuser
```

### 7. Run the Development Server
```
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage
- **Patients**: Register, log in, search for hospitals, view doctor cards, and book appointments.
- **Doctors**: Register, log in, manage your profile, and view/manage appointments.
- **AI Chatbot**: Use the floating chat widget on any page to ask health questions.

## Project Structure
- `accounts/` – User registration, login, profile, dashboards
- `doctors/` – Doctor model, forms, admin
- `appointments/` – Appointment model, booking, management
- `hospitals/` – Hospital directory
- `templates/` – All HTML templates
- `static/` – Static files (CSS, JS, images)
- `HealthDoc/gemini_chat.py` – Gemini API backend integration

## Screenshots
_Add screenshots of the home page, doctor cards, booking flow, and chatbot here._

## License
MIT License

---
Made with by Souvagya Dey
