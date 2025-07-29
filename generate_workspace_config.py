import os
import platform
import subprocess
import json

# --- Config ---
roles = ["server", "agent_client", "control_client"]
workspace_filename = "remote-desktop.code-workspace"

# --- OS detection ---
is_windows = platform.system() == "Windows"
venv_dir = ".venv"

# --- VS Code Extensions ---
vscode_extensions = [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "esbenp.prettier-vscode",
    "editorconfig.editorconfig"
]

# --- Step 1: Setup roles ---
for role in roles:
    print(f"\n[🔧] Setting up role: {role}")
    role_path = os.path.abspath(role)
    venv_path = os.path.join(role_path, venv_dir)
    venv_bin = os.path.join(venv_path, "Scripts" if is_windows else "bin")
    python_exe = os.path.join(venv_bin, "python.exe" if is_windows else "python")

    # Create virtual environment
    if not os.path.exists(venv_path):
        subprocess.run(["python3", "-m", "venv", venv_path], check=True)
        print(f"[✓] Created venv in {venv_path}")
    else:
        print(f"[→] venv already exists in {venv_path}")

    # Install requirements.txt
    req_path = os.path.join(role_path, "requirements.txt")
    if os.path.exists(req_path):
        print(f"[📦] Installing requirements for {role}...")
        subprocess.run([python_exe, "-m", "pip", "install", "-r", req_path], check=True)
    else:
        print(f"[!] No requirements.txt found in {role}")

    # VS Code settings
    vscode_path = os.path.join(role_path, ".vscode")
    os.makedirs(vscode_path, exist_ok=True)
    settings_path = os.path.join(vscode_path, "settings.json")

    settings = {
        "python.pythonPath": os.path.join(".venv", "Scripts" if is_windows else "bin", "python.exe" if is_windows else "python"),
        "editor.formatOnSave": True,
        "python.formatting.provider": "autopep8",
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": True
    }

    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=2)

    print(f"[🧠] VS Code config set at: {settings_path}")

# --- Step 2: Workspace file ---
workspace_data = {
    "folders": [{"path": "."}] + [{"path": role} for role in roles],
    "settings": {
        "python.defaultInterpreterPath": f"{venv_dir}/bin/python" if not is_windows else f"{venv_dir}\\Scripts\\python.exe"
    },
    "extensions": {
        "recommendations": vscode_extensions
    }
}
with open(workspace_filename, "w") as f:
    json.dump(workspace_data, f, indent=2)

print(f"\n[🏁] Workspace created: {workspace_filename}")
print("[💡] You can open it using: code remote-desktop.code-workspace")
