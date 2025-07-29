@echo off
setlocal enabledelayedexpansion

:: ------- Config -------
set "ROLE=%1"
set "PROJECT_DIR=%~dp0"
set "ROLE_PATH=%PROJECT_DIR%%ROLE%"
set "VENV_PATH=%ROLE_PATH%\.venv"
set "ACTIVATE=%VENV_PATH%\Scripts\activate.bat"
set "MAIN_PATH=%ROLE_PATH%\main.py"

:: ------- Check arg -------
if "%ROLE%"=="" (
    echo ❌ Role tidak diberikan.
    echo Gunakan: run.bat [server ^| agent_client ^| control_client]
    exit /b 1
)

:: ------- Check folder role -------
if not exist "%ROLE_PATH%" (
    echo ❌ Folder role '%ROLE%' tidak ditemukan.
    exit /b 1
)

:: ------- Check venv -------
if not exist "%VENV_PATH%" (
    echo ❌ .venv belum dibuat untuk '%ROLE%'.
    echo 💡 Jalankan: python generate_project_setup.py
    exit /b 1
)

:: ------- Check main.py -------
if not exist "%MAIN_PATH%" (
    echo ❌ File main.py tidak ditemukan di %ROLE_PATH%
    exit /b 1
)

:: ------- Jalankan -------
echo 🚀 Menjalankan role '%ROLE%'...
call "%ACTIVATE%"
python "%MAIN_PATH%"
