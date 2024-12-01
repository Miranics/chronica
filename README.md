
# Chronica
Chronica is a web application that leverages external APIs to provide a valuable and meaningful service to users. This project involves both local implementation and deployment on web servers with load balancing for efficient and reliable accessibility.

- Table of Contents
- Project Overview
- Features
- Technologies Used
- APIs Used
- Setup and Installation
- Local Setup
- Deployment to Servers
- Challenges and Solutions
- Credits
- License
- Contact
## Project Overview
Chronica is designed to address [insert the core problem your app solves]. The application retrieves and presents data interactively, allowing users to [e.g., sort, filter, search]. By leveraging external APIs, it delivers meaningful insights and user-friendly functionality.

## The project is divided into:

- Part 1: Local implementation of the application.
- Part 2: Deployment on web servers with load balancing.
## Features
- Data Fetching: Retrieves real-time data from external APIs.
- User Interaction: Enables users to sorting, filtering, etc..
- Scalable Deployment: Distributed across two web servers with a load balancer for reliability.
- Error Handling: Manages API errors and downtime gracefully.
## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Servers: Ubuntu 20.04
- Load Balancer: Nginx
- Version Control: Git/GitHub

# Setup and Installation
## Local Setup
- Clone the Repository:

      git clone https://github.com/Miranics/chronica.git
      cd chronica
Install Dependencies: Ensure you have Python 3 installed. Then, install required packages:

     pip install -r requirements.txt
Run the Application:


     python app.py
Access the application at http://127.0.0.1:8000.

# Deployment to Servers
## Prerequisites
- Ensure SSH access to the servers.
- Install necessary software: Python, Flask, and Nginx.
## Steps
Deploy Application on Web Servers:

-Clone the repository on both web servers:

    git clone https://github.com/Miranics/chronica.git
    cd chronica
    pip install -r requirements.txt
- Start the Flask application:

      nohup python app.py 
## Configure Nginx Load Balancer:

- SSH into the load balancer server:

      ssh ubuntu@98.80.10.162
- Update the Nginx configuration:

      upstream flask_app {
          server 54.165.255.68:5000;  # 6327-web-01
          server 54.237.192.135:5000;  # 6327-web-02
      }

          server {
                 listen 80;
                 server_name 98.80.10.162;

      location / {
         proxy_pass http://flask_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
       }
      }
- Test and reload Nginx:

      sudo nginx -t
      suudo systemctl reload nginx
- Verify Deployment:

      Access the application at http://98.80.10.162.
- Test traffic balancing by stopping one web server and verifying the load balancer redirects traffic to the other.
## Challenges and Solutions
- Challenge: API rate limits during high traffic.
- Solution: Implemented caching to reduce API calls.
- Challenge: Server connection issues.
- Solution: Configured firewall rules and ensured consistent port usage.
## Credits
- External APIs: History_today
- Third-Party Libraries: Flask, Requests.
 Hosting and Load Balancing: Nginx, Ubuntu servers.
## License
This project is licensed under the Eclipse Public License - v 2.0.

# Contact
- Developer: Nanen Miracle Mbanaade
- Email: 002nasya@gmail.com
- Repository: GitHub - Chronica
