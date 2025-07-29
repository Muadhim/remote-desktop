#!/bin/bash

set -e

ROLE="server"
PROJECT_DIR=$(pwd)
ROLE_PATH="$PROJECT_DIR/$ROLE"
VENV_PATH="$ROLE_PATH/.venv"
ACTIVATE="$VENV_PATH/bin/activate"
MIGRATION_SCRIPT="$ROLE_PATH/migrate.py"

# Cek apakah virtualenv ada
if [ ! -f "$ACTIVATE" ]; then
  echo "❌ Virtual environment not found at $ACTIVATE"
  echo "💡 Run: python3 generate_project_setup.py"
  exit 1
fi

# Cek apakah script migrasi ada
if [ ! -f "$MIGRATION_SCRIPT" ]; then
  echo "❌ Migration script not found: $MIGRATION_SCRIPT"
  exit 1
fi

# Aktifkan venv dan jalankan migrasi
echo "🐍 Activating virtual environment..."
source "$ACTIVATE"

echo "📦 Running database migration..."
python "$MIGRATION_SCRIPT"

# Nonaktifkan venv
deactivate
echo "✅ Migration complete and virtual environment deactivated."
