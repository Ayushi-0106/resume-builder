# Resume Builder - Setup Guide

## 🚀 Quick Start

### Option 1: Frontend Only (No Python Required)
1. **Open the frontend directly:**
   - Navigate to `frontend/` folder
   - Double-click `index.html` to open in your browser
   - Or use the provided startup scripts:
     - Windows: `start.bat` or `start.ps1`
     - Mac/Linux: `start.sh`

2. **Features available:**
   - Resume form builder
   - Real-time preview
   - Export to JSON
   - Modern, responsive UI

### Option 2: Full Stack (Python Backend + Frontend)

#### Prerequisites
1. **Install Python 3.8+**
   - Download from [python.org](https://www.python.org/downloads/)
   - **Important:** Check "Add Python to PATH" during installation
   - Verify installation: `python --version`

2. **Install Git** (if not already installed)
   - Download from [git-scm.com](https://git-scm.com/)

#### Backend Setup
1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Update with your API keys if needed

5. **Run the backend:**
   ```bash
   python run.py
   ```
   - Backend will start on `http://localhost:5000`

#### Frontend Setup
1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Open in browser:**
   - Double-click `index.html`
   - Or use the startup scripts provided

## 📁 Project Structure

```
Resume Builder/
├── backend/                 # Flask Python backend
│   ├── app.py              # Main Flask application
│   ├── run.py              # Entry point
│   ├── requirements.txt     # Python dependencies
│   ├── .env                # Environment variables
│   ├── models/             # Data models
│   ├── services/           # Business logic services
│   ├── static/             # Static files
│   └── templates/          # HTML templates
├── frontend/               # HTML/CSS/JavaScript frontend
│   ├── index.html          # Main page
│   ├── builder.html        # Resume builder interface
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   ├── assets/             # Images and other assets
│   └── start.*             # Startup scripts
├── README.md               # Project overview
└── SETUP.md               # This setup guide
```

## 🔧 Configuration

### Environment Variables (.env)
```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-openai-api-key-here
```

### API Keys (Optional)
- **OpenAI API Key:** For AI-powered resume suggestions
- Get from [OpenAI Platform](https://platform.openai.com/)

## 🚀 Running the Application

### Development Mode
1. **Start backend:**
   ```bash
   cd backend
   python run.py
   ```

2. **Start frontend:**
   - Open `frontend/index.html` in browser
   - Or use startup scripts

### Production Mode
1. **Set environment:**
   ```bash
   export FLASK_ENV=production
   ```

2. **Run with production server:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

## 🐛 Troubleshooting

### Common Issues

#### Python Not Found
- **Solution:** Install Python and add to PATH
- **Verify:** `python --version` in terminal

#### Port Already in Use
- **Solution:** Change port in `run.py` or kill existing process
- **Alternative port:** `flask run --port 5001`

#### Dependencies Installation Failed
- **Solution:** Upgrade pip: `python -m pip install --upgrade pip`
- **Alternative:** Use `pip3` instead of `pip`

#### Frontend Not Loading
- **Solution:** Check browser console for errors
- **Alternative:** Open HTML files directly in browser

### Getting Help
1. Check browser console for JavaScript errors
2. Check terminal for Python backend errors
3. Verify all files are in correct locations
4. Ensure Python dependencies are installed

## 📱 Features

### Frontend
- ✅ Responsive design
- ✅ Real-time resume preview
- ✅ Form validation
- ✅ Export to JSON
- ✅ Modern UI components

### Backend (when Python is available)
- ✅ RESTful API
- ✅ PDF generation
- ✅ AI-powered suggestions
- ✅ Data persistence
- ✅ Template system

## 🔄 Updates and Maintenance

### Updating Dependencies
```bash
cd backend
pip install --upgrade -r requirements.txt
```

### Adding New Features
1. Frontend: Edit files in `frontend/` folder
2. Backend: Edit files in `backend/` folder
3. Test changes in browser
4. Commit to version control

## 📞 Support

If you encounter issues:
1. Check this setup guide
2. Review error messages in terminal/browser console
3. Verify file paths and permissions
4. Ensure all prerequisites are installed

---

**Happy Resume Building! 🎉**
