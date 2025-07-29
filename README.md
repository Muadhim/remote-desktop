# 🖥️ Remote Desktop Project

This is a remote desktop application project composed of three main components:

- `server/` – Handles communication and session management
- `agent_client/` – Runs on the computer that is being remotely controlled
- `control_client/` – Runs on the computer used to control the agent

Each component has its own virtual environment to ensure clean dependencies.

---

## 📦 Requirements

- Python 3.10+
- Git
- Unix shell or Command Prompt / PowerShell
- (Optional) VS Code for development

---

## ⚙️ Project Setup

To set up all roles with their own virtual environments and install dependencies, run the following from the root of the project:

```bash
python generate_project_setup.py
```

This script will:

- Create `.venv` in each role directory
- Install dependencies from `requirements.txt`
- Create default `.env` files if not present
- Generate `.vscode/settings.json` to automatically pick the correct Python interpreter per role

---

## ▶️ Running the Project

You can run each role independently using the launch scripts provided:

### On Linux / macOS:

```bash
./run.sh [server|agent_client|control_client]
```

Example:

```bash
./run.sh agent_client
```

### On Windows:

```cmd
run.bat [server|agent_client|control_client]
```

Example:

```cmd
run.bat control_client
```

---

## 🧪 Project Structure

```
remote-desktop/
├── run.sh
├── run.bat
├── generate_project_setup.py
├── server/
│   ├── .venv/
│   ├── main.py
│   └── requirements.txt
├── agent_client/
│   ├── .venv/
│   ├── main.py
│   └── requirements.txt
├── control_client/
│   ├── .venv/
│   ├── main.py
│   └── requirements.txt
└── shared/
    └── ...
```

---

## 🧠 Tips

- Use VS Code to open the whole `remote-desktop/` folder.
- You can switch between roles in VS Code and it will use the correct `.venv` automatically.
- Do not forget to activate the environment manually if you're not using the launcher script.
