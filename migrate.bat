@echo off
setlocal enabledelayedexpansion

set "ROLE=server"
set "PROJECT_DIR=%cd%"
set "ROLE_PATH=%PROJECT_DIR%\%ROLE%"
set "VENV_PATH=%ROLE_PATH%\.venv"
set "ACTIVATE=%VENV_PATH%\Scripts\activate.bat"
set "MIGRATION_SCRIPT=%ROLE_PATH%\migrate.py"

REM Cek venv
if not exist "%ACTIVATE%" (
    echo ❌ Virtual environment not found at %ACTIVATE%
    echo 💡 Run: python generate_project_setup.py
    exit /b 1
)

REM Cek migrate.py
if not exist "%MIGRATION_SCRIPT%" (
    echo ❌ Migration script not found: %MIGRATION_SCRIPT%
    exit /b 1
)

REM Aktifkan venv
call "%ACTIVATE%"
echo 📦 Running database migration...
python "%MIGRATION_SCRIPT%"

REM Nonaktifkan venv
call deactivate.bat
echo ✅ Migration complete and virtual environment deactivated.
