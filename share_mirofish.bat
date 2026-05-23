@echo off
title MiroFish Sharing Launcher (Localtunnel)
echo ====================================================================
echo   MiroFish Sharing Launcher - Share with Friends for Free!
echo ====================================================================
echo.

:: Navigate to script directory to ensure relative paths work
cd /d "%~dp0"

:: Start the dev server in a new window
echo [1/2] Starting MiroFish servers (Backend + Frontend)...
start "MiroFish Servers" cmd /c "npm run dev"

echo [2/2] Waiting 6 seconds for servers to fully initialize...
timeout /t 6 /nobreak >nul

echo.
echo ====================================================================
echo   STARTING SECURE SHARING TUNNEL
echo ====================================================================
echo.
echo 1. The URL shown below (ending in .loca.lt) is your public sharing link!
echo 2. Copy and send that URL to your friends. They can open it on their
echo    phones, tablets, or computers from anywhere in the world.
echo 3. Keep this window and the server window open while they use it.
echo.
echo ====================================================================
echo.

:: Launch localtunnel to bridge port 3000 publicly
npx localtunnel --port 3000

pause
