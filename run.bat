@echo off
setlocal enabledelayedexpansion

:: Argument: role (server, agent_client, control_client)
set "ROLE=%~1"
set "PROJECT_DIR=%cd%"

if "%ROLE%"=="" (
    echo ❌ Role is missing.
    echo Usage: run.bat [server ^| agent_client ^| control_client]
    exit /b 1
)

set "ROLE_PATH=%PROJECT_DIR%\%ROLE%"
set "VENV_PATH=%ROLE_PATH%\.venv"
set "PYTHON_EXEC=%VENV_PATH%\Scripts\python.exe"
set "MAIN_PATH=%ROLE_PATH%\main.py"

:: Check role directory
if not exist "%ROLE_PATH%" (
    echo ❌ Role folder '%ROLE%' not found.
    exit /b 1
)

:: Check virtual environment
if not exist "%PYTHON_EXEC%" (
    echo ❌ Virtual environment not found in '%VENV_PATH%'.
    echo 💡 Run: python generate_workspace_config.py
    exit /b 1
)

:: Check main.py
if not exist "%MAIN_PATH%" (
    echo ❌ File main.py not found in %ROLE_PATH%
    exit /b 1
)

:: Run using venv's python
echo 🚀 Running role '%ROLE%'...
"%PYTHON_EXEC%" "%MAIN_PATH%"
