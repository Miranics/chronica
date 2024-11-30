Chronica
Chronica is a dynamic Flask-based web application designed to let users explore major historical events by date. It combines data from the History Today API with curated events to deliver a seamless and enriching experience.

Features
Interactive Interface: A visually appealing and responsive design ensures great user experience across devices.
Search Historical Events: Enter a date (in YYYY-MM-DD format) to explore events that occurred on that day.
API Integration: Fetches data from the History Today API, enriched with major curated events.
Sorting and Prioritization: Events are prioritized by relevance, using custom keyword-based sorting.
User-Friendly Navigation: Clear instructions and a welcoming layout make it easy to use.
Technologies Used
Backend
Python: Core backend logic.
Flask: Lightweight web framework for server-side functionality.
Requests: For API interaction with the History Today API.
Frontend
HTML5 & CSS3: Structure and styling.
JavaScript: Adds interactivity (e.g., dynamic date validation, event filtering).
Bootstrap: Ensures responsive and mobile-first design.
APIs
History Today API: Supplies historical events data, enriched with curated events.
Installation
Prerequisites
Python (3.7 or later)
Flask
A modern web browser
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/chronica.git
Navigate to the project directory:

bash
Copy code
cd chronica
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Start the Flask application:

bash
Copy code
flask run
Open your browser and visit:
http://127.0.0.1:8000

Project Structure
plaintext
Copy code
Chronica/
├── static/
│   ├── css/
│   │   └── styles.css      # Custom CSS for styling
│   ├── js/
│   │   └── script.js       # JavaScript for interactivity
│   └── images/
│       └── banner.png      # Homepage banner image
│
├── templates/
│   ├── index.html          # Homepage template
│   ├── results.html        # Template for search results
│   └── error.html          # Template for error messages
│
├── app.py                  # Flask application logic
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
Acknowledgments
This project was made possible thanks to the following tools and resources:

Flask: For powering the server-side logic.
Bootstrap: For ensuring responsive and modern design.
History Today API: For providing a rich dataset of historical events.
Requests Library: For seamless API interaction.
Unsplash: For providing captivating images for banners and visuals.
Contact
For questions, suggestions, or issues, feel free to reach out:

Email: 002nasyagmail.com
