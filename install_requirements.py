import os
import subprocess
import sys

ALL_ROLES = ["server", "agent_client", "control_client"]
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def install_for_role(role):
    print(f"📦 Installing dependencies for: {role}")
    role_path = os.path.join(PROJECT_DIR, role)
    venv_path = os.path.join(role_path, ".venv")
    req_path = os.path.join(role_path, "requirements.txt")
    python_bin = os.path.join(venv_path, "bin", "python")

    # Validasi
    if not os.path.exists(role_path):
        print(f"❌ Role '{role}' not found.")
        return

    if not os.path.exists(venv_path):
        print(f"❌ Virtual environment not found for '{role}'.")
        print(f"💡 Run: python3 -m venv {venv_path}")
        return

    if not os.path.exists(req_path):
        print(f"⚠️  Skipping '{role}': requirements.txt not found.")
        return

    # Install
    subprocess.run([python_bin, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([python_bin, "-m", "pip", "install", "-r", req_path], check=True)
    print(f"✅ {role} dependencies installed.\n")

if __name__ == "__main__":
    roles = sys.argv[1:]
    if not roles:
        print("🔁 No role specified. Installing for all roles...")
        roles = ALL_ROLES

    for role in roles:
        install_for_role(role)
