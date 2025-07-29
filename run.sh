#!/bin/bash

set -e

ROLE=$1
PROJECT_DIR=$(pwd)

if [[ -z "$ROLE" ]]; then
  echo "❌ $ROLE is missing."
  echo "Gunakan: ./run.sh [server|agent_client|control_client]"
  exit 1
fi

ROLE_PATH="$PROJECT_DIR/$ROLE"
VENV_PATH="$ROLE_PATH/.venv"
MAIN_PATH="$ROLE_PATH/main.py"
PYTHON_EXEC="$VENV_PATH/bin/python"

# Cek folder role
if [ ! -d "$ROLE_PATH" ]; then
  echo "❌ Folder '$ROLE' not found."
  exit 1
fi

# Cek .venv
if [ ! -d "$VENV_PATH" ]; then
  echo "❌ .venv not found in '$ROLE'."
  echo "💡 Run: python3 generate_project_setup.py"
  exit 1
fi

# Cek main.py
if [ ! -f "$MAIN_PATH" ]; then
  echo "❌ File main.py not found in $ROLE_PATH"
  exit 1
fi

# Jalankan
echo "🚀 Running role '$ROLE'..."
exec "$PYTHON_EXEC" "$MAIN_PATH"
