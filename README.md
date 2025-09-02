                                                                          
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
Chronica is designed to help users explore historical events by date . The application retrieves and presents data interactively, allowing users to sort, filter, search history. By leveraging external APIs, it delivers meaningful insights and user-friendly functionality.

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
- Backend: Flask (Python), Requests
- Flask management: Systemd
- APIs: History_today
- Deployment: Nginx, Ubuntu
- servers management: SSH
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

# Deployment to Servers
## Prerequisites
- Ensure SSH access to the servers.
- Install necessary software: Python, Flask, gunicorn and Nginx.
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

      ssh ubuntu@#YOUR_IP
- Update the Nginx configuration:

      upstream flask_app {
          server #YOUR_IP:5000;  # -web-01
          server #YOUR_IP :5000;  # -web-02
      }

          server {
                 listen 80;
                 server_name #your LB IP;

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
