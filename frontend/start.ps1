Write-Host "Starting AI Resume Builder Frontend..." -ForegroundColor Green
Write-Host ""
Write-Host "Opening http://localhost:8000 in your browser..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host ""

try {
    python -m http.server 8000
} catch {
    Write-Host "Error: Python not found or http.server module not available" -ForegroundColor Red
    Write-Host "Please ensure Python is installed and accessible from PATH" -ForegroundColor Red
}

Read-Host "Press Enter to continue"
