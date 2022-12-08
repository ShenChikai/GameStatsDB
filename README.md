# Project Intro
- The goal of the project is to offer tools to analyze gaming platforms, explore gaming industry companies, and search for games desired by the users given a list of available search, sort, and filter options. The project provides analysis on various popular games on the market along with information of their publisher companies and their platforms based on data from gaming awards, sales, genres, company stock performance, etc. The complete product will be presented in a form of full-stack 3-tier architecture with web-based client, functional and utility server, and relational database each handling their specific tasks.

# MySQL Database with MariaDB
- The project uses **MariaDB 10.6** as its production level database, and this also aligns with the database provided through Ugrad machine
- *NOTE: Database configurations are read from environment variable, so do not foget to include a .env file for that.
- Client Side (Flask)
    - The project will use a client-side **Cursor** to interacting with the database
    - MariaDB is a community-developed, commercially supported fork of the MySQL relational database management system
        - https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
    - Install: ```pip3 install mariadb```
- Database Side (MariaDB)
    - **The MariaDB will be installed on our Ubuntu AWS instance**
    - Check connectivity and port: ```netstat -ant | grep 3306```
    - Installation:
        1.  Installing MariaDB
            ```
            sudo apt update
            sudo apt install mariadb-server
            sudo systemctl start mariadb.service
            ```
        2. Configuring MariaDB
            ```
            sudo mysql_secure_installation
            ```
           - Set 'root' password to 'admin'
        3. Creating an 'admin' User that Employs Password Authentication
            ```
            sudo mariadb
            MariaDB [(none)]> GRANT ALL ON *.* to '<username>'@'%' IDENTIFIED BY '<password>' WITH GRANT OPTION;
            MariaDB [(none)]> FLUSH PRIVILEGES;
            ```
        4. Becuase MariaDB default only listens on localhost:3306, we need to change that to 0.0.0.0
            - Edit MariaDB default configuration file
            ```sudo vim /etc/mysql/mariadb.cnf```
            - Remove/Comment the socket connecting option
            - Add bind-addcress to 0.0.0.0 to open to public remote access
            ```bind-address = 0.0.0.0```
            (If you cannot find 'bind-address', I suggest try ```sudo grep -r 'bind-address' /etc/mysql/*``` to locate it first.)
            - Then restart MariaDB service
            ```sudo systemctl restart mariadb```
        5. Configure Firewall
            - ``` sudo ufw allow 3306``` grant access from any IP address
            - ``` sudo ufw allow from <specific IP> to any port 3306``` grant access from specifc IP address
            - Then ```sudo ufw reload```
    - To interact with MariaDB: ```sudo mariadb```
    - Source: https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04

# FlaskServer
## Flask
- Flask is a **WSGI** application
- https://flask.palletsprojects.com/en/2.2.x/deploying/gunicorn/
- A **WSGI server** is used to run the application, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses
- **Gunicorn** is a pure Python WSGI server with simple configuration and multiple worker implementations for performance tuning
    - https://gunicorn.org/

## Project Dependencies
- Install Requirements under the virtual env: ```pip install -r requirements.txt```
- Created with ```pip freeze > requirements.txt``` under the virtual env

## Setup and AWS Deployment
- ### Create Vitural 
    - Create: ```python -m venv FlaskServer```
    - Activate: ```.\FlaskServer\Scripts\activate``` (for Win)
    - Deactivate: ```deactivate``` (for Win)
- ### Local Setup Flask
    - Install Flask: ```pip install flask```
    - app.py for running the main server logic and routings
    - templates/ folders for HTML template files
    - static/ folders for corresponding JavaScript files
    - static/style for css files
    - Run server: ```python \FlaskServer\app.py```
- ### AWS Depoloyment
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
        - ```sudo systemctl restart FlaskServer```
        - ```sudo systemctl enable FlaskServer```
        - ```sudo service apache2 stop```
        - ```sudo systemctl restart nginx```
        - ```sudo systemctl enable nginx```
    13. Site available through: ```52.14.195.69```
        - Test database connection: ```mysql -u admin -h 52.14.195.69 -p```


    - Source: https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7

# Front End
## JavaScript
- Bootstrap
    - https://getbootstrap.com/docs/5.2/getting-started/introduction/
- Chart.js
    - https://www.chartjs.org/docs/2.9.4/


# TEMP:
    - ssh -v -i D:\Github_Clones\PEMs\Ubuntu.pem ubuntu@ec2-52-14-195-69.us-east-2.compute.amazonaws.com
    - MariaDB admin, shenchikai
\. /home/ubuntu/DB_CREATE/CreationSQL/dropAll.sql
\. /home/ubuntu/DB_CREATE/CreationSQL/createEntities.sql
\. /home/ubuntu/DB_CREATE/CreationSQL/createRelations.sql
\. /home/ubuntu/DB_CREATE/CreationSQL/insertAll.sql