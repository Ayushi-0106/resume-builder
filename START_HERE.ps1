Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Resume Builder - Quick Start" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Choose an option:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Open Frontend (No Python Required)" -ForegroundColor Green
Write-Host "2. Setup Python Backend" -ForegroundColor Green
Write-Host "3. View Project Structure" -ForegroundColor Green
Write-Host "4. Exit" -ForegroundColor Green
Write-Host ""

$choice = Read-Host "Enter your choice (1-4)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Opening frontend in browser..." -ForegroundColor Green
        Start-Process "frontend\index.html"
        Write-Host "Frontend opened! You can now build resumes." -ForegroundColor Green
        Write-Host ""
        Read-Host "Press Enter to continue"
    }
    "2" {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "    Python Backend Setup" -ForegroundColor Cyan
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "1. Install Python 3.8+ from python.org" -ForegroundColor Yellow
        Write-Host "2. Make sure to check 'Add Python to PATH'" -ForegroundColor Yellow
        Write-Host "3. Open a new terminal and run:" -ForegroundColor Yellow
        Write-Host "   cd backend" -ForegroundColor Gray
        Write-Host "   python -m venv venv" -ForegroundColor Gray
        Write-Host "   venv\Scripts\activate" -ForegroundColor Gray
        Write-Host "   pip install -r requirements.txt" -ForegroundColor Gray
        Write-Host "   python run.py" -ForegroundColor Gray
        Write-Host ""
        Write-Host "See SETUP.md for detailed instructions." -ForegroundColor Cyan
        Write-Host ""
        Read-Host "Press Enter to continue"
    }
    "3" {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "    Project Structure" -ForegroundColor Cyan
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Resume Builder/" -ForegroundColor Yellow
        Write-Host "├── backend/          # Flask Python backend" -ForegroundColor Gray
        Write-Host "├── frontend/         # HTML/CSS/JavaScript" -ForegroundColor Gray
        Write-Host "├── README.md         # Project overview" -ForegroundColor Gray
        Write-Host "├── SETUP.md          # Detailed setup guide" -ForegroundColor Gray
        Write-Host "└── START_HERE.ps1   # This file" -ForegroundColor Gray
        Write-Host ""
        Write-Host "Frontend files:" -ForegroundColor Yellow
        Write-Host "├── index.html        # Main page" -ForegroundColor Gray
        Write-Host "├── builder.html      # Resume builder" -ForegroundColor Gray
        Write-Host "├── css/              # Stylesheets" -ForegroundColor Gray
        Write-Host "├── js/               # JavaScript" -ForegroundColor Gray
        Write-Host "└── assets/           # Images" -ForegroundColor Gray
        Write-Host ""
        Read-Host "Press Enter to continue"
    }
    "4" {
        Write-Host "Goodbye!" -ForegroundColor Green
        exit
    }
    default {
        Write-Host "Invalid choice. Please try again." -ForegroundColor Red
        Read-Host "Press Enter to continue"
    }
}
