import subprocess
import sys
from pathlib import Path

def deploy_project(use_docker=False):
    if use_docker:
        compose_file = Path("docker-compose.yml")
        if not compose_file.exists():
            print("Error: docker-compose.yml not found in the current directory.")
            sys.exit(1)

        print("Starting Docker deployment...")
        try:
            subprocess.run(["docker", "compose", "up", "--build"], check=True)
        except FileNotFoundError:
            print("Error: Docker is not installed or 'docker compose' is not available in PATH.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Deployment failed with error: {e}")
            sys.exit(1)
    else:
        print("Error: Only Docker deployment is currently supported.")
        sys.exit(1)

