# AirBnB Clone - Application Server Setup

## Project Overview

This project focuses on setting up an application server for the AirBnB clone project. It involves configuring development and production environments using Flask, Gunicorn, and Nginx. The tasks include serving dynamic content, proxying requests, and handling multiple routes.

## Requirements

- All tasks must be performed on Ubuntu 16.04 LTS.
- Use Python 3 for all Python-related tasks.
- All Bash scripts must be executable and pass Shellcheck (version 0.3.7-5~ubuntu16.04.1).
- Proper commenting in all configuration files is mandatory.

## Tasks

### Task 0: Set up Development with Python

1. **SSH Setup**: Ensure SSH access to `web-01`.
2. **Install net-tools**:
    ```bash
    sudo apt update
    sudo apt install -y net-tools
    ```
3. **Clone AirBnB_clone_v2 Repository**:
    ```bash
    git clone https://github.com/yourusername/AirBnB_clone_v2.git
    cd AirBnB_clone_v2
    ```
4. **Configure Flask Application**:
    Edit `web_flask/0-hello_route.py`:
    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/airbnb-onepage/', strict_slashes=False)
    def hello_hbnb():
        return "Hello HBNB!"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    ```
5. **Run Flask Application**:
    ```bash
    python3 -m web_flask.0-hello_route
    ```

### Task 1: Set up Production with Gunicorn

1. **Install Gunicorn**:
    ```bash
    sudo apt install -y gunicorn
    ```
2. **Run Gunicorn Server**:
    ```bash
    gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
    ```

### Task 2: Serve a Page with Nginx

1. **Install Nginx**:
    ```bash
    sudo apt update
    sudo apt install -y nginx
    ```
2. **Configure Nginx**:
    Edit `/etc/nginx/sites-available/default`:
    ```nginx
    server {
        listen 80;
        server_name your_domain_or_IP;

        location /airbnb-onepage/ {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
3. **Restart Nginx**:
    ```bash
    sudo systemctl restart nginx
    ```

### Task 3: Add a Route with Query Parameters

1. **Update Flask Application**:
    Edit `web_flask/6-number_odd_or_even.py`:
    ```python
    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        if n % 2 == 0:
            return f"Number: {n} is even"
        else:
            return f"Number: {n} is odd"
    ```
2. **Run Gunicorn Server for New Route**:
    ```bash
    tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
    ```
3. **Configure Nginx**:
    Edit `/etc/nginx/sites-available/default`:
    ```nginx
    server {
        listen 80;
        server_name your_domain_or_IP;

        location /airbnb-onepage/ {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /airbnb-dynamic/number_odd_or_even/ {
            proxy_pass http://127.0.0.1:5001;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
4. **Restart Nginx**:
    ```bash
    sudo systemctl restart nginx
    ```

### Task 4: Let's do this for your API

1. **Clone AirBnB_clone_v3 Repository**:
    ```bash
    git clone https://github.com/yourusername/AirBnB_clone_v3.git
    cd AirBnB_clone_v3
    ```
2. **Run Gunicorn Server for API**:
    ```bash
    tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
    ```
3. **Configure Nginx**:
    Edit `/etc/nginx/sites-available/default`:
    ```nginx
    server {
        listen 80;
        server_name your_domain_or_IP;

        location /api/ {
            proxy_pass http://127.0.0.1:5002;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
4. **Restart Nginx**:
    ```bash
    sudo systemctl restart nginx
    ```

### Task 5: Serve your AirBnB Clone

1. **Clone AirBnB_clone_v4 Repository**:
    ```bash
    git clone https://github.com/yourusername/AirBnB_clone_v4.git
    cd AirBnB_clone_v4
    ```
2. **Run Gunicorn Server for Web Dynamic**:
    ```bash
    tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'
    ```
3. **Configure Nginx**:
    Edit `/etc/nginx/sites-available/default`:
    ```nginx
    server {
        listen 80;
        server_name your_domain_or_IP;

        location / {
            proxy_pass http://127.0.0.1:5003;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /static/ {
            alias /path/to/your/repo/web_dynamic/static/;
        }
    }
    ```
4. **Reconfigure JavaScript**:
    Edit `web_dynamic/static/scripts/2-hbnb.js` to point to the correct IP.
5. **Restart Nginx**:
    ```bash
    sudo systemctl restart nginx
    ```

### Validation

- Verify each step by using `curl` commands or accessing the endpoints via a browser.
- Check the Developer Tools in your browser for any errors.

---

## Repository

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- **Directories**:
  - `0x1A-application_server`

