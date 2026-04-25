@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Virtual environment not found. Run setupdev.bat first.
    pause
    exit /b 1
)

echo Starting backend on http://127.0.0.1:8000 ...
start "Library API" cmd /k "cd /d ""%~dp0backend"" && call ..\.venv\Scripts\activate && python -m uvicorn core.main:app --reload"

echo Starting frontend on http://localhost:3000 ...
start "Library Frontend" cmd /k "cd /d ""%~dp0frontend"" && npm start"
