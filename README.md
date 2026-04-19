# 🤖 AI Resume Builder

A modern, AI-powered resume builder that helps you create professional resumes with intelligent suggestions and multiple beautiful templates.

![AI Resume Builder](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=openai)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-4.5.0-green?style=for-the-badge&logo=mongodb)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript)

## ✨ Features

- 🤖 **AI-Powered Suggestions** - Get intelligent content improvements using OpenAI
- 📄 **Multiple Templates** - Choose from Minimal, Professional, and Modern designs
- 💾 **Save & Export** - Save your work and download as PDF
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- 🔐 **Secure Authentication** - JWT-based user authentication
- ⚡ **Real-time Preview** - See changes as you type
- 🎨 **Beautiful UI** - Modern, intuitive interface

## 🚀 Quick Start

### Windows Users
1. **Double-click `START_HERE.bat`** and choose option 1
2. The script will automatically install dependencies and start both services
3. Your browser will open with the application

### Manual Setup
1. **Backend Setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python run.py
   ```

2. **Frontend Setup**:
   - Open `frontend/index.html` in your browser
   - Or run: `start_frontend.bat` (Windows)

## 📋 Prerequisites

- **Python 3.8+** - [Download here](https://python.org)
- **MongoDB** - [Download here](https://mongodb.com) or use [MongoDB Atlas](https://cloud.mongodb.com)
- **Web Browser** - Chrome, Firefox, Safari, or Edge

## ⚙️ Configuration

### 1. MongoDB Setup
- **Local**: Install MongoDB and ensure it's running on port 27017
- **Atlas**: Create a free account and get your connection string
- Update `backend/.env` with your MongoDB URI

### 2. OpenAI API (Optional)
- Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- Add it to `backend/.env` for AI features

### 3. Environment Variables
Create `backend/.env`:
```env
MONGO_URI=mongodb://localhost:27017/resume_builder
JWT_SECRET=your-super-secret-jwt-key-here
OPENAI_API_KEY=your-openai-api-key-here
```

## 🎯 How to Use

1. **Create Account**: Sign up with your email and password
2. **Build Resume**: Fill in your information using the intuitive form
3. **Get AI Help**: Use AI suggestions to improve your content
4. **Choose Template**: Select from Minimal, Professional, or Modern designs
5. **Export PDF**: Download your professional resume

## 🏗️ Project Structure

```
Resume builder/
├── 📁 backend/                 # Flask API server
│   ├── 📄 app.py              # Main Flask application
│   ├── 📄 run.py              # Server startup script
│   ├── 📁 services/           # Business logic
│   │   ├── 🤖 ai_service.py   # OpenAI integration
│   │   └── 📄 pdf_service.py  # PDF generation
│   ├── 📁 templates/          # HTML templates
│   │   └── 📁 pdf/            # PDF templates
│   └── 📄 requirements.txt    # Python dependencies
├── 📁 frontend/               # Frontend application
│   ├── 🌐 index.html          # Login/signup page
│   ├── 🌐 builder.html        # Resume builder interface
│   ├── 📁 css/                # Stylesheets
│   └── 📁 js/                 # JavaScript modules
├── 🚀 START_HERE.bat          # Quick start script
├── 📖 SETUP_GUIDE.md          # Detailed setup guide
└── 🧪 test_backend.py         # Backend testing script
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/signup` | User registration |
| POST | `/api/auth/login` | User login |
| POST | `/api/resume` | Create/update resume |
| GET | `/api/resume` | Get user's resumes |
| GET | `/api/resume/{id}/pdf` | Download resume as PDF |
| POST | `/api/ai/suggest` | Get AI suggestions |

## 🧪 Testing

Run the test script to verify everything is working:

```bash
python test_backend.py
```

This will test:
- ✅ Server connectivity
- ✅ User authentication
- ✅ Resume creation
- ✅ AI suggestions
- ✅ PDF generation

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check if Python is installed and in PATH
- Ensure MongoDB is running
- Verify all dependencies are installed: `pip install -r requirements.txt`

**Frontend shows errors:**
- Make sure backend is running on port 5000
- Check browser console for error messages
- Clear browser cache and refresh

**PDF generation fails:**
- Install WeasyPrint dependencies (GTK+ on Windows)
- Check if template files exist in `backend/templates/pdf/`

**AI suggestions not working:**
- Verify OpenAI API key is set in `.env`
- Check if you have API credits
- AI features work without API key (fallback suggestions)

## 🚀 Deployment

### Local Development
1. Clone the repository
2. Set up MongoDB
3. Configure environment variables
4. Run `START_HERE.bat` or follow manual setup

### Production Deployment
1. Set up a production MongoDB instance
2. Configure environment variables
3. Use a production WSGI server (Gunicorn)
4. Set up reverse proxy (Nginx)
5. Configure SSL certificates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for AI capabilities
- Flask community for the excellent framework
- WeasyPrint for PDF generation
- All contributors and users

## 📞 Support

If you encounter any issues:
1. Check the [troubleshooting section](#-troubleshooting)
2. Review the [setup guide](SETUP_GUIDE.md)
3. Check console logs for error messages
4. Ensure all prerequisites are installed

---

**Made with ❤️ for job seekers everywhere**