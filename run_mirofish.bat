@echo off
title MiroFish Swarm Intelligence Engine Launcher
echo ====================================================================
echo   MiroFish Swarm Intelligence Engine Launcher
echo ====================================================================
echo.

:: Navigate to script directory to ensure relative paths work
cd /d "%~dp0"

:: Check for .env file
if not exist ".env" (
    echo [WARNING] .env file not found in the root directory!
    echo Please make sure you copy .env.example to .env and configure your API keys.
    echo.
    pause
    exit /b
)

echo Starting Backend API and Frontend Dev Server...
echo The app will open in your browser automatically shortly.
echo.
echo Press Ctrl+C in this window at any time to stop the application.
echo ====================================================================
echo.

:: Open the browser to localhost:3000 after 3 seconds
timeout /t 3 /nobreak >nul
start "" http://localhost:3000

:: Start the concurrently npm run dev task
npm run dev

pause
