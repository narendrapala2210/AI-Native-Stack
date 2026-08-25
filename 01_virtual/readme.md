# Python Virtual Environments

This lesson shows how to create and use an isolated Python environment for a project.

## Create the environment

Run these commands from the `01_virtual` folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow scripts for the current user and try again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Run the example

With the environment activated:

```powershell
python src\run.py
```

The example prints the Python version, executable path, and environment prefix. The executable should point inside this project's `.venv` folder.

## Install packages

Install packages while the environment is active so they stay isolated from other projects:

```powershell
python -m pip install --upgrade pip
python -m pip install <package-name>
```

When the project is finished, leave the environment with:

```powershell
deactivate
```
