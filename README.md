Chronica - Explore Historical Events by Date
Chronica is a Flask-powered web application that allows users to explore historical events based on specific dates. Whether you're looking for major milestones or curious about what happened on your birthday, Chronica offers a user-friendly interface with robust search functionality.


Features
Search Historical Events: Fetches historical data from the History Today API for any given date.
Supplementary Events: Includes hardcoded historical highlights (e.g., Apollo 11 Moon Landing).
Smart Event Ranking: Events are ranked by year and keyword relevance for an engaging user experience.
Interactive Frontend: Designed with responsive and appealing styles for enhanced usability.
Technologies Used
Backend
Python (Flask): To handle routing, API integration, and business logic.
Requests Library: To interact with external APIs.
Frontend
HTML5 & CSS3: For structuring and styling the web application.
JavaScript: To enhance interactivity and dynamic behaviors.
Responsive Design: Ensures accessibility on various devices.
How to Use
Visit the Homepage
Start by navigating to the homepage to explore what Chronica has to offer.
URL: http://your-domain-or-localhost:8000/

Search by Date
Enter a specific date (e.g., YYYY-MM-DD) in the search box to discover events from that day in history.

View Results
Results will be displayed in chronological order, highlighting significant milestones.

Navigate and Interact
Use the intuitive interface to explore further details or click on links for in-depth information.

Installation and Setup
Follow these steps to set up Chronica on your local machine:

Prerequisites
Python 3.8+
Flask
Requests Library
Installation Steps
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/chronica.git
cd chronica
Set Up a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install Required Packages

bash
Copy code
pip install -r requirements.txt
Run the Application

bash
Copy code
flask run --host=127.0.0.1 --port=8000
Access Chronica Visit http://127.0.0.1:8000/ in your browser.

File Structure
Here’s the project’s directory structure:

graphql
Copy code
chronica/
├── static/
│   ├── css/
│   │   └── style.css  # Styles for the application
│   ├── js/
│   │   └── script.js  # Dynamic JavaScript
│   └── images/
│       └── banner.png  # Hero image for the homepage
├── templates/
│   ├── base.html      # HTML template for layout
│   ├── home.html      # Homepage
│   └── search.html    # Search results page
├── app.py             # Flask application logic
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
API Integration
Chronica uses the History Today API to fetch event data.
API URL: https://history.muffinlabs.com/date/{month}/{day}

Fallback Events
In cases where the API does not return significant results, Chronica includes supplementary hardcoded events for key historical moments.

Screenshots
Homepage

Search Results

Future Enhancements
User Authentication: Allow users to save and bookmark favorite events.
Advanced Filters: Search by specific keywords or event types.
Multiple APIs: Integrate additional APIs for richer historical data.
Contributing
Contributions are welcome! Follow these steps to contribute:

Fork the repository.
Create a new branch for your feature:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature-name"
Push to your branch:
bash
Copy code
git push origin feature-name
Open a pull request.
License
This project is licensed under the Eclipse Public License - v 2.0. See the LICENSE file for more details.

Contact
For questions or feedback, feel free to reach out:

Author: Nanen Miracle Mbanaade
Email: 002nasya@gmail.com
GitHub: Miranics
Project Repository: Chronica
Acknowledgments
History Today API for providing historical event data.
Open-source libraries and frameworks that made this project possible.

           Thank you for your interest in Chronica!