# Tandem Python Cookiecutter Template

A minimal, opinionated Cookiecutter template for Python projects with conda environment management, testing setup, and development tools.

## Features

- **Conda environment management** with `environment.yml`
- **Optional pytest setup** with coverage reporting
- **Pre-configured development tools** (autopep8, flake8)
- **Git repository initialisation** with conventional commit structure
- **Automatic Python version detection** and environment updates
- **Comprehensive `.gitignore`** for Python/ML projects
- **Project structure** following Python best practices

## Quick Start

1. Install Cookiecutter globally

   - **with homebrew**:

   ```bash
   brew install cookiecutter
   ```

   - **with pip**:

   ```bash
   pip install cookiecutter
   ```

2. Use template

```bash
cookiecutter https://github.com/TandemCreativeDev/tandem-python-template
```

You'll be prompted for:

- `project_name`: Your project name (e.g., "my-awesome-project")
- `username`: Your GitHub username
- `email`: Your email address (optional)
- `description`: Brief project description
- `use_pytest`: Include pytest setup? (y/n)

## What Gets Created

```
my-project/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── __init__.py
├── environment.yml
├── pyproject.toml
├── setup.cfg
├── .gitignore
└── README.md
```

## Post-Generation Setup

The template automatically:

1. **Updates Python version** in `environment.yml` to match your system
2. **Removes pytest dependencies** if you chose not to use them
3. **Initialises git repository** with initial commit

## Development Workflow

```bash
cd your-project
conda env create -f environment.yml
conda activate your-project
```

**Code quality:**

```bash
flake8 src/ tests/
autopep8 --in-place --recursive src/ tests/
```

**Testing** (if enabled):

```bash
pytest
pytest --cov=src
```

## Template Customisation

The template uses these defaults:

- **Python version**: Auto-detected from your system, else uses 3.13.3
- **Line length**: 160 characters
- **Test framework**: pytest (optional)
- **Formatting**: autopep8 with aggressive=2

Modify `cookiecutter.json` to change defaults or add new variables.

## Why This Template?

**Opinionated choices:**

- Conda over pip-only (better for controlled package management)
- 160 character line length (modern screens can handle it)
- Minimal dependencies (only what you actually need)
- Conventional commits and branch naming
- Automated README.md generation

**What's missing (intentionally):**

- No Docker (add if you need it)
- No CI/CD config (project-specific)
- No ML/data science libraries (install as needed)
- No complex project structures (YAGNI principle)

This template gets you coding quickly without the bloat. Add complexity when you actually need it.
