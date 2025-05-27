# {{ cookiecutter.project_name.replace('-', ' ').replace('_', ' ').title() }}

{{cookiecutter.description}}

## Quick Start

1. **Clone the repository**:

   - **with https:**

   ```bash
   git clone https://github.com/{{cookiecutter.username}}/{{cookiecutter.project_name}}.git
   cd {{cookiecutter.project_name}}
   ```

   - **with ssh:**

   ```bash
   git clone git@github.com:{{cookiecutter.username}}/{{cookiecutter.project_name}}.git
   cd {{cookiecutter.project_name}}
   ```

2. **Setup environment**

   ```bash
   conda env create -f environment.yml
   conda activate {{cookiecutter.project_name}}
   ```

{% if cookiecutter.use_pytest == 'y' or cookiecutter.use_pytest == 'yes' -%} 3. **Run tests**

```bash
pytest
```

{% endif %}

## Project Structure

```
├── src/             # Code
{% if cookiecutter.use_pytest == 'y' or cookiecutter.use_pytest == 'yes' -%} ├── tests/           # Test files
├── environment.yml  # Conda environment
├── setup.cfg        # Tool configurations
└── pyproject.toml   # Build configuration
```

## Development

- **Code formatting**: `autopep8 --in-place --recursive src/ {% if cookiecutter.use_pytest == 'y' or cookiecutter.use_pytest == 'yes' -%} tests/`
- **Linting**: `flake8 src/ {% if cookiecutter.use_pytest == 'y' or cookiecutter.use_pytest == 'yes' -%} tests/`
  {% if cookiecutter.use_pytest == 'y' or cookiecutter.use_pytest == 'yes' -%}
- **Testing**: `pytest tests/`
- **Coverage**: `pytest --cov=src`
  {% endif %}

## Git Branch Naming

Follow these conventions:

- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `hotfix/critical-fix` - Critical fixes
- `chore/task-description` - Maintenance tasks
- `docs/documentation-update` - Documentation changes

## Commit Messages

Use conventional commits:

- `feat: add new feature`
- `fix: resolve bug`
- `docs: update documentation`
- `style: format code`
- `refactor: restructure code`
- `test: add tests`
- `chore: update dependencies`

## Author

[**{{cookiecutter.username}}**](https://github.com/{{cookiecutter.username}}) - {{cookiecutter.email}}
