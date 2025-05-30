import subprocess
import re
import shutil
from pathlib import Path


def get_latest_python_version():
    try:
        result = subprocess.run([
            'python3', '-c', 
            'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")'
        ], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            result = subprocess.run([
                'python', '-c', 
                'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")'
            ], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "3.11.0"


def update_python_version():
    latest_version = get_latest_python_version()
    
    env_file = Path('environment.yml')
    if env_file.exists():
        content = env_file.read_text()
        updated_content = re.sub(
            r'python=\d+\.\d+\.\d+',
            f'python={latest_version}',
            content
        )
        env_file.write_text(updated_content)
        print(f"✓ Updated environment.yml to use Python {latest_version}")
    else:
        print("⚠ environment.yml not found")


def setup_git_repo():
    try:
        subprocess.run(['git', 'init'], check=True, capture_output=True)
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        subprocess.run([
            'git', 'commit', '-m', 'feat: initial project setup'
        ], check=True, capture_output=True)
        print("✓ Initialised git repository with initial commit")
    except subprocess.CalledProcessError:
        print("⚠ Failed to initialise git repository")
    except FileNotFoundError:
        print("⚠ Git not found - skipping repository initialisation")


def remove_pytest_files():
    use_pytest = "{{ cookiecutter.use_pytest }}"
    if use_pytest.lower() not in ['y', 'yes']:
        env_file = Path('environment.yml')
        if env_file.exists():
            content = env_file.read_text()
            lines = content.split('\n')
            filtered_lines = [
                line for line in lines 
                if 'pytest' not in line.lower()
            ]
            env_file.write_text('\n'.join(filtered_lines))
            print("✓ Removed pytest dependencies from environment.yml")
        test_dir = Path('tests')
        if test_dir.exists():
            shutil.rmtree(test_dir)
            print("✓ Removed tests directory")

def main():
    print("🚀 Setting up your Python project...")
    
    update_python_version()
    remove_pytest_files()
    setup_git_repo()
    
    print("\n✅ Project setup complete!")
    print(f"\nNext steps:")
    print(f"1. cd {{cookiecutter.project_name}}")
    print(f"2. conda env create -f environment.yml")
    print(f"3. conda activate {{cookiecutter.project_name}}")
    print(f"4. Start coding!")


if __name__ == "__main__":
    main()