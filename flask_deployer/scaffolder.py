import os
from pathlib import Path

BASE_REQUIREMENTS = """Flask==2.3.3
"""

APP_PY_CONTENT = """from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") if app.template_folder else "Hello from Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
"""

INDEX_HTML_CONTENT = """<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Hello from Flask!</h1>
</body>
</html>
"""

DOCKERFILE_CONTENT = """FROM python:3.10-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
"""

DOCKER_COMPOSE_CONTENT = """version: "3"
services:
  web:
    build: .
    ports:
      - "5000:5000"
"""

README_CONTENT = """# My Flask App

This app was generated using Flask Deployer.
"""

def scaffold_project(project_name, with_template=False):
    project_path = Path(project_name)
    if project_path.exists():
        print(f"Error: Directory '{project_name}' already exists.")
        return

    # Create directory structure
    print(f"Creating project at {project_path.resolve()}")
    (project_path / "templates").mkdir(parents=True, exist_ok=True) if with_template else project_path.mkdir()

    # Write app.py
    app_path = project_path / "app.py"
    with app_path.open("w") as f:
        f.write(APP_PY_CONTENT if with_template else APP_PY_CONTENT.replace("render_template(\"index.html\")", '"Hello from Flask!"'))

    # Write template if required
    if with_template:
        index_path = project_path / "templates" / "index.html"
        with index_path.open("w") as f:
            f.write(INDEX_HTML_CONTENT)

    # Write requirements.txt
    with (project_path / "requirements.txt").open("w") as f:
        f.write(BASE_REQUIREMENTS)

    # Write Dockerfile
    with (project_path / "Dockerfile").open("w") as f:
        f.write(DOCKERFILE_CONTENT)

    # Write docker-compose.yml
    with (project_path / "docker-compose.yml").open("w") as f:
        f.write(DOCKER_COMPOSE_CONTENT)

    # Write README
    with (project_path / "README.md").open("w") as f:
        f.write(README_CONTENT)

    print("Project scaffolded successfully.")

