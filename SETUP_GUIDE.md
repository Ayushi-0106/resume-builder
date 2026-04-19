# AI Resume Builder - Setup Guide

## Prerequisites

1. **Python 3.8+** - Download from [python.org](https://python.org)
2. **MongoDB** - Download from [mongodb.com](https://mongodb.com) or use MongoDB Atlas
3. **Web Browser** - Chrome, Firefox, Safari, or Edge

## Quick Start

### Option 1: Using Batch Files (Windows)
1. Double-click `start_backend.bat` to start the backend server
2. Double-click `start_frontend.bat` to open the frontend in your browser

### Option 2: Using PowerShell (Windows)
1. Right-click and "Run with PowerShell" on `start_backend.ps1`
2. Right-click and "Run with PowerShell" on `start_frontend.ps1`

### Option 3: Manual Setup

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python run.py
```

#### Frontend Setup
```bash
cd frontend
# Open index.html in your web browser
```

## Configuration

### 1. MongoDB Setup
- **Local MongoDB**: Install MongoDB locally and ensure it's running on port 27017
- **MongoDB Atlas**: Create a free account and get your connection string
- Update `backend/.env` file with your MongoDB URI:
  ```
  MONGO_URI=mongodb://localhost:27017/resume_builder
  # OR for MongoDB Atlas:
  MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/resume_builder
  ```

### 2. OpenAI API (Optional)
- Get your API key from [OpenAI](https://platform.openai.com/api-keys)
- Add it to `backend/.env`:
  ```
  OPENAI_API_KEY=your-api-key-here
  ```

### 3. JWT Secret
- Generate a strong secret key for JWT tokens
- Update `backend/.env`:
  ```
  JWT_SECRET=your-super-secret-jwt-key-here
  ```

## Features

### ✅ Implemented Features
- **User Authentication**: Sign up and login with JWT tokens
- **Resume Builder**: Interactive form with live preview
- **Multiple Templates**: Minimal, Professional, and Modern designs
- **AI Suggestions**: Get AI-powered content improvements (requires OpenAI API)
- **PDF Export**: Download resumes as PDF files
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Preview**: See changes as you type

### 🎯 How to Use

1. **Start the Application**:
   - Run the backend server (port 5000)
   - Open the frontend in your browser

2. **Create an Account**:
   - Click "Sign Up" on the login page
   - Enter your details and create an account

3. **Build Your Resume**:
   - Fill in personal information
   - Add professional summary
   - Add work experience, education, skills, and projects
   - Use AI suggestions to improve your content
   - Choose from different templates

4. **Export Your Resume**:
   - Click "Save" to save your progress
   - Click "Download PDF" to export your resume

## Troubleshooting

### Backend Issues
- **Port 5000 already in use**: Change the port in `backend/.env` or `backend/run.py`
- **MongoDB connection failed**: Check if MongoDB is running and the URI is correct
- **Module not found**: Run `pip install -r requirements.txt` in the backend directory

### Frontend Issues
- **CORS errors**: Ensure the backend is running on the correct port
- **API calls failing**: Check browser console for error messages
- **Styling issues**: Clear browser cache and refresh the page

### PDF Generation Issues
- **WeasyPrint installation**: On Windows, you might need to install GTK+ libraries
- **Template not found**: Check if template files exist in `backend/templates/pdf/`

## Development

### Project Structure
```
Resume builder/
├── backend/                 # Flask API server
│   ├── app.py              # Main Flask application
│   ├── run.py              # Server startup script
│   ├── services/           # Business logic
│   │   ├── ai_service.py   # OpenAI integration
│   │   └── pdf_service.py  # PDF generation
│   ├── templates/          # HTML templates
│   └── requirements.txt    # Python dependencies
├── frontend/               # React-like vanilla JS frontend
│   ├── index.html          # Login/signup page
│   ├── builder.html        # Resume builder interface
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript modules
└── start_*.bat/ps1         # Startup scripts
```

### API Endpoints
- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `POST /api/resume` - Create/update resume
- `GET /api/resume` - Get user's resumes
- `GET /api/resume/{id}/pdf` - Download resume as PDF
- `POST /api/ai/suggest` - Get AI suggestions

## Support

If you encounter any issues:
1. Check the console logs for error messages
2. Verify all dependencies are installed
3. Ensure MongoDB is running
4. Check the `.env` file configuration

## License

This project is for educational purposes. Feel free to modify and use as needed.
