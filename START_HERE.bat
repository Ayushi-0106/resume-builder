@echo off
echo ========================================
echo    AI Resume Builder - Quick Start
echo ========================================
echo.
echo Choose an option:
echo.
echo 1. Start Everything (Backend + Frontend)
echo 2. Open Frontend Only (No Backend)
echo 3. Setup Python Backend
echo 4. View Project Structure
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo ========================================
    echo    Starting Full Application
    echo ========================================
    echo.
    echo [1/3] Installing Python dependencies...
    cd backend
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        echo Please check your Python installation
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
    echo.
    echo [2/3] Starting backend server...
    start "Backend Server" cmd /k "cd backend && python run.py"
    timeout /t 5 /nobreak >nul
    echo.
    echo [3/3] Starting frontend...
    cd ..
    start "Frontend" cmd /k "cd frontend && start index.html"
    echo.
    echo ========================================
    echo    Services Started Successfully!
    echo ========================================
    echo.
    echo Backend: http://localhost:5000
    echo Frontend: Opening in your browser...
    echo.
    echo Press any key to exit...
    pause >nul
) else if "%choice%"=="2" (
    echo.
    echo Opening frontend in browser...
    start frontend\index.html
    echo Frontend opened! You can now build resumes.
    echo Note: Some features require the backend server.
    echo.
    pause
) else if "%choice%"=="3" (
    echo.
    echo ========================================
    echo    Python Backend Setup
    echo ========================================
    echo.
    echo 1. Install Python 3.8+ from python.org
    echo 2. Make sure to check "Add Python to PATH"
    echo 3. Open a new terminal and run:
    echo    cd backend
    echo    python -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    echo    python run.py
    echo.
    echo See SETUP.md for detailed instructions.
    echo.
    pause
) else if "%choice%"=="3" (
    echo.
    echo ========================================
    echo    Project Structure
    echo ========================================
    echo.
    echo Resume Builder/
    echo ├── backend/          # Flask Python backend
    echo ├── frontend/         # HTML/CSS/JavaScript
    echo ├── README.md         # Project overview
    echo ├── SETUP.md          # Detailed setup guide
    echo └── START_HERE.bat    # This file
    echo.
    echo Frontend files:
    echo ├── index.html        # Main page
    echo ├── builder.html      # Resume builder
    echo ├── css/              # Stylesheets
    echo ├── js/               # JavaScript
    echo └── assets/           # Images
    echo.
    pause
) else if "%choice%"=="5" (
    echo Goodbye!
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto :eof
)
