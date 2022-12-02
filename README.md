# MySQL Database
- The project uses MySQL as its production level database
- The JayDeBeApi module allows to connect from Python code to databases using Java JDBC Driver.
    - https://pypi.org/project/JayDeBeApi/
# Flask
- Flask is a **WSGI** application
- https://flask.palletsprojects.com/en/2.2.x/deploying/gunicorn/
- A **WSGI server** is used to run the application, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses
- **Gunicorn** is a pure Python WSGI server with simple configuration and multiple worker implementations for performance tuning
    - https://gunicorn.org/

# Project Dependencies
- Install Requirements under the virtual env: ```pip install -r requirements.txt```
- Created with ```pip install -r requirements.txt``` under the virtual env

# Setup
- ### Create Vitural 
    - Create: ```python -m venv FlaskServer```
    - Activate: ```.\FlaskServer\Scripts\activate``` (for Win)
- ### Local Setup Flask
    - Install Flask: ```pip install flask```
    - app.py for running the main server logic and routings
    - templates/ folders for HTML template files
    - static/ folders for corresponding JavaScript files
    - static/style for css files
    - Run server: ```python \FlaskServer\app.py```
- ### Depoloyment
    1. The Flask app will be deployed on an Ubuntu EC2 on AWS
    2. Inbound allows HTTP, HTTPS, SSH (with RSA key access)
    3. ```ssh -v -i "/Path to PEM" ubuntu@ec2-52-14-195-69.us-east-2.compute.amazonaws.com```
    4. Activate virtual env on Ubuntu: ```source FlaskServer/Scripts/activate```
    5. Deactivate: ```deactivate```
    6. Install Flask: ```pip install flask```
    - *What's above are all for development. When you “run” flask, you are actually running Werkzeug’s development WSGI server, which forward requests from a web server.*
    7. To have production-ready WSGI server - Install **Gunicorn**: ```sudo pip install gunicorn```
    8. Create ```service``` file to boot and manage gunicornL 
        - ```sudo nano /etc/systemd/system/FlaskServer.service```
        -   ```
            [Unit]
            Description=Gunicorn instance for GameStats app
            After=network.target
            [Service]
            User=ubuntu
            Group=www-data
            WorkingDirectory=/home/ubuntu/GameStatsDB/FlaskServer
            ExecStart=/home/ubuntu/.local/bin/gunicorn -b localhost:8000 app:app
            Restart=always
            [Install]
            WantedBy=multi-user.target
            ```
    9. Enable Service with systemctl
        -   ```
            sudo systemctl daemon-reload
            sudo systemctl start FlaskServer
            sudo systemctl enable FlaskServer
            ```
    10. Set up Nginx as a reverse-proxy to accept the requests from the user and route it to gunicorn
        - Install: ```sudo apt-get install nginx```
        - Start the Nginx service:
            -   ```
                sudo systemctl start nginx
                sudo systemctl enable nginx
                ```
    11. sites-available folder: ```sudo vim /etc/nginx/sites-available/default```
        -   ```
            upstream FlaskServer {
                server 127.0.0.1:8000;
            }
            ```
        -   ```
            location / {
                proxy_pass http://flaskhelloworld;
            }
            ```
    12. To restart service
        - Do step 9.
        - ```sudo service apache2 stop```
        - ```sudo systemctl restart nginx```


    - Source: https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7




- TEMP:
    - ssh -v -i D:\Github_Clones\PEMs\Ubuntu.pem ubuntu@ec2-52-14-195-69.us-east-2.compute.amazonaws.com