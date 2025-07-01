# Flask Deployer

**Flask Deployer** is a minimal CLI tool for quickly generating and deploying Flask applications. Designed for rapid development and prototyping, it sets up a working Flask project with optional HTML templates and containerization support.

## Features

- Generate a minimal Flask app structure
- Optional Jinja2 template support (`index.html`)
- Auto-generate Dockerfile and docker-compose for containerized deployment
- Local deployment via Flask's development server
- No external dependencies (uses only Python standard library)

## Installation

Clone the repository and install locally:

```bash
git clone https://github.com/hestonhamilton/flask-deployer.git
cd flask-deployer
python3 -m venv venv
source venv/bin/activate
pip install .
```

## Usage

### Initialize a New Flask App

```bash
flask-deployer init my-flask-app
```

With templating support:

```bash
flask-deployer init my-flask-app --with-template
```

This generates:

```
my-flask-app/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### Run Locally

```bash
cd my-flask-app
python app.py
```

### Deploy with Docker

```bash
flask-deployer deploy --docker
```

Or manually:

```bash
docker-compose up --build
```

## Example Template Output

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Hello from Flask!</h1>
</body>
</html>
```

## Requirements

- Python 3.7+
- (Optional) Docker + docker-compose

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the `LICENSE` file for more details.

## Author

Created by Heston Hamilton as a lightweight tool to speed up Flask development.

