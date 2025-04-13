
# Geospan Codebases

This repository contains the primary codebases for **Geospan**, including modular components for sensor integration, geographic zone mapping, and vehicle-based smart infrastructure.

---

## Project Structure

```
geospan_codebases/
├── smart_sensors/      # Code for sensor integrations (e.g., field_aware, road_pulse, vehicle_pulse)
├── zone_mapping/       # Code for geographic zone analysis and mapping
├── shared/             # (Optional) Common utilities, configuration, and logging modules
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Create a Virtual Environment

Run the following commands in your project root:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

> **Note:** If you encounter an execution policy error in PowerShell, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 2. Install Dependencies

Make sure to install your project dependencies using:

```bash
python -m pip install -r requirements.txt
```

---

## Code Quality and Formatting

To maintain a consistent and PEP8-compliant codebase, we use the following tools:

- **Black** – automatic code formatter
- **isort** – import sorter
- **flake8** – linter for Python
- **mypy** – static type checker

### Run Manually:

```bash
black .
isort .
flake8 .
mypy geospan_codebases/
```

---

## Pre-commit Hooks

Pre-commit hooks ensure that code is linted and formatted **before every commit**.

### Setup Pre-commit Hooks:

```bash
pre-commit clean
pre-commit install
```

### To Run on All Files (Optional):

```bash
pre-commit run --all-files
```

---

## Coding Standards

- Follow **PEP8** for code style.
- Use `snake_case` for filenames and functions.
- Use `PascalCase` for class names.
- Place any shared modules in the `shared/` folder if they are used across multiple components.

---

## Additional Information

For further information or contribution guidelines, please refer to the additional documentation or reach out via the repository's issue tracker.
