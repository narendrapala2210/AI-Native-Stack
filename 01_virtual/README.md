# Python Virtual Environments (venv)

A complete guide to creating, managing, and working with isolated Python environments in modern projects.

---

## 📌 Overview

A **virtual environment** is an isolated Python runtime containing its own Python interpreter, standard libraries, and installed third-party packages.

### Why Use Virtual Environments?
- **Dependency Isolation**: Prevents dependency conflicts between different projects (e.g., Project A needing `requests==2.28` and Project B needing `requests==2.34`).
- **Clean Global Environment**: Avoids cluttering and corrupting your system's global Python installation.
- **Reproducibility**: Makes it easy to share exact package dependencies via a `requirements.txt` file so teammates or deployment servers can replicate the exact environment.

---

## 📁 Directory Structure

```text
01_virtual/
├── .venv/               # Virtual environment directory (isolated Python & libraries)
├── src/                 # Source code folder
│   └── run.py           # Verification script to inspect environment details
├── requirement.txt      # List of project dependencies
└── README.md            # Documentation (this file)
```

> **Note:** Never commit the `.venv` directory to Git. Add `.venv/` or `*/.venv/` to your root `.gitignore`.

---

## 🚀 Step-by-Step Workflow

### 1. Open the Directory in Terminal

Navigate to the lesson folder:

```powershell
cd "01_virtual"
```

---

### 2. Create the Virtual Environment

Run Python's built-in `venv` module to create a new environment in a folder named `.venv`:

```powershell
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

Activation configures your shell session to prioritize the virtual environment's Python binary and package paths.

#### **Windows (PowerShell)**:
```powershell
.\.venv\Scripts\Activate.ps1
```

> ⚠️ **PowerShell Execution Policy Error?**
> If you encounter `cannot be loaded because running scripts is disabled on this system`, run this command once to allow local scripts:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then re-run `.\.venv\Scripts\Activate.ps1`.

#### **Windows (Command Prompt / CMD)**:
```cmd
.\.venv\Scripts\activate.bat
```

#### **macOS / Linux (Bash or Zsh)**:
```bash
source .venv/bin/activate
```

When active, your terminal prompt will display the prefix:
```text
(.venv) PS E:\Learnings\Courses\AI Full Stack\01_virtual>
```

---

### 4. Verify Active Environment

Check that Python is pointing directly to your local `.venv`:

#### On Windows (PowerShell):
```powershell
(Get-Command python).Source
```

#### Verification via Python Script:
You can run `python src/run.py` to inspect runtime details:

```powershell
python src\run.py
```

Expected output:
```text
Python version: 3.x.x
Python executable: ...\01_virtual\.venv\Scripts\python.exe
Environment prefix: ...\01_virtual\.venv
Base Python prefix: ...\Python3xx
Virtual environment: ACTIVE
```

---

### 5. Managing Dependencies

Always upgrade `pip` first inside your active environment:

```powershell
python -m pip install --upgrade pip
```

#### Install from `requirement.txt`:
```powershell
pip install -r requirement.txt
```

#### Install a New Package:
```powershell
pip install <package-name>
```

#### Save Current Dependencies:
When you add or update packages, freeze the versions into `requirement.txt`:
```powershell
pip freeze > requirement.txt
```

---

### 6. Deactivating the Environment

When you are done working on this project, leave the virtual environment:

```powershell
deactivate
```

Your terminal prompt will return to its default state.

---

## 💡 Best Practices & Common Gotchas

1. **Always use `python -m pip`**:
   Using `python -m pip install <package>` guarantees you are invoking the `pip` associated with the active Python interpreter.
2. **Never commit `.venv`**:
   Virtual environment binaries are system-specific and large. Only commit your code and `requirement.txt`.
3. **Recreating the environment**:
   If an environment becomes corrupted or you move machines, delete `.venv` and recreate it cleanly:
   ```powershell
   Remove-Item -Recurse -Force .venv
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirement.txt
   ```
