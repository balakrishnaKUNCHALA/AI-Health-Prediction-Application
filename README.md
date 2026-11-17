# AI-Powered Health Prediction Application

## 1. Project Overview

The AI-Powered Health Prediction Application is a Python-based web application developed using Streamlit, SQLite, and Google Gemini AI.

The application helps manage patient blood test records, validates patient information, and generates AI-powered general health observations based on blood test values.

**Disclaimer:** This application is developed for educational and demonstration purposes only. It does not provide medical diagnosis or replace professional medical advice.

## 2. Features

- Create new patient records
- View all patient records
- Update patient email addresses
- Delete patient records
- Email format validation
- Date of birth validation
- Future date validation
- Blood test value validation
- Duplicate patient record prevention
- AI-generated health observations
- SQLite database for persistent storage
- Error handling for AI service failures

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| SQLite | Database management |
| Pandas | Data handling |
| Google Gemini API | AI-generated observations |
| python-dotenv | Environment variable management |

## 4. Project Structure

```text
health-prediction-app/
│
├── app.py
├── database.py
├── validators.py
├── ai_service.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/balakrishnaKUNCHALA/AI-Health-Prediction-Application.git
```

### Step 2: Navigate to Project Folder

```bash
cd AI-Health-Prediction-Application
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Gemini API Key

Create a `.env` file in the project directory.

Add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

**Important:** Never upload the `.env` file or API key to GitHub.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 6. Database Management

The application uses SQLite for storing patient records.

The database contains the following fields:

- Patient ID
- Full Name
- Date of Birth
- Email Address
- Glucose
- Haemoglobin
- Cholesterol
- AI Generated Remarks

The database table is created automatically when the application starts.

## 7. AI Integration

Google Gemini API is integrated to generate general health observations using patient blood test values.

The AI service:
- Accepts glucose, haemoglobin, and cholesterol values.
- Generates short general health observations.
- Avoids providing medical diagnoses.
- Recommends consulting a qualified healthcare professional.
- Provides fallback messages when the AI service is unavailable.

## 8. Validation

The application includes:

- Email format validation.
- Date of birth format validation.
- Invalid calendar date rejection.
- Future date rejection.
- Numeric blood value validation.
- Negative value rejection.
- Duplicate patient record prevention.

## 9. Security

- API credentials are stored in environment variables.
- `.env` is excluded using `.gitignore`.
- Local database files are excluded from GitHub.
- Parameterized SQL queries are used to reduce SQL injection risks.

## 10. Disclaimer

This application is intended only for educational and demonstration purposes. AI-generated observations are not medical advice or a medical diagnosis. Users should consult qualified healthcare professionals for medical decisions.

## 11. Developer

Developed as part of the AI Growth and Automation Associate Task 2 project.
