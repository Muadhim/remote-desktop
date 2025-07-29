#!/bin/bash

set -e

ROLE=$1
PROJECT_DIR=$(pwd)

if [[ -z "$ROLE" ]]; then
  echo "❌ Role tidak diberikan."
  echo "Gunakan: ./run.sh [server|agent_client|control_client]"
  exit 1
fi

ROLE_PATH="$PROJECT_DIR/$ROLE"
VENV_PATH="$ROLE_PATH/.venv"
MAIN_PATH="$ROLE_PATH/main.py"
ACTIVATE="$VENV_PATH/bin/activate"

# Cek folder role
if [ ! -d "$ROLE_PATH" ]; then
  echo "❌ Folder role '$ROLE' tidak ditemukan."
  exit 1
fi

# Cek .venv
if [ ! -d "$VENV_PATH" ]; then
  echo "❌ .venv belum dibuat untuk '$ROLE'."
  echo "💡 Jalankan: python3 generate_project_setup.py"
  exit 1
fi

# Cek main.py
if [ ! -f "$MAIN_PATH" ]; then
  echo "❌ File main.py tidak ditemukan di $ROLE_PATH"
  exit 1
fi

# Jalankan
echo "🚀 Menjalankan role '$ROLE'..."
source "$ACTIVATE"
python "$MAIN_PATH"
