# Import necessary libraries
from flask import Flask, request, jsonify  # Flask for the web server
import requests  # To fetch data from external APIs

# Initialize the Flask application
app = Flask(__name__)

# Define the root route
@app.route('/')
def home():
    """
    Test route to confirm the server is running.
    Returns a welcome message.
    """
    return "Welcome to Chronica - Explore historical events by date!"

# Define the search route
@app.route('/search', methods=['GET'])
def search():
    """
    Fetch historical events based on the user's input date.
    Combines data from History Today API and Wikipedia API for better coverage.
    """
    # Extract the 'date' parameter from the query string
    date = request.args.get('date')
    
    # Validate the date parameter
    if not date:
        return jsonify({'error': 'Please provide a valid date in YYYY-MM-DD format.'}), 400

    try:
        # Extract the month and day from the input date
        month, day = date.split('-')[1], date.split('-')[2]

        # Use the History Today API to fetch events
        history_today_url = f"https://history.muffinlabs.com/date/{month}/{day}"
        history_today_response = requests.get(history_today_url)
        history_today_events = []

        # Check if the History Today API call is successful
        if history_today_response.status_code == 200:
            history_today_data = history_today_response.json()
            raw_events = history_today_data.get('data', {}).get('Events', [])
            
            # Simplify the events from History Today API
            for event in raw_events:
                year = event.get('year', 'Unknown Year')
                text = event.get('text', 'No description available.')
                links = event.get('links', [])
                primary_link = links[0]['link'] if links else None
                
                history_today_events.append({
                    'year': int(year) if year.isdigit() else 0,
                    'description': text,
                    'link': primary_link
                })

        # Use Wikipedia's API to fetch additional events
        wikipedia_url = f"https://en.wikipedia.org/w/api.php"
        wikipedia_params = {
            'action': 'parse',
            'page': f"{month} {day}",
            'prop': 'text',
            'format': 'json',
            'formatversion': 2
        }
        wikipedia_response = requests.get(wikipedia_url, params=wikipedia_params)
        wikipedia_events = []

        # Check if the Wikipedia API call is successful
        if wikipedia_response.status_code == 200:
            wikipedia_data = wikipedia_response.json()
            html_content = wikipedia_data.get('parse', {}).get('text', '')

            # Extract events from the "Events" section in the HTML content
            if 'Events' in html_content:
                import re
                events_section = re.search(r'(?<=<span class="mw-headline" id="Events">Events</span>)(.*?)<h2>', html_content, re.S)
                if events_section:
                    events_list = re.findall(r'<li>(.*?)</li>', events_section.group(1))
                    for event in events_list:
                        # Extract year and description from each event
                        year_match = re.match(r'(\d{1,4}) – (.*)', event)
                        if year_match:
                            year = year_match.group(1)
                            description = re.sub(r'<.*?>', '', year_match.group(2))  # Strip HTML tags
                            wikipedia_events.append({
                                'year': int(year),
                                'description': description,
                                'link': None  # Links can be parsed later if needed
                            })

        # Combine events from both sources and sort by year (descending)
        combined_events = history_today_events + wikipedia_events
        sorted_events = sorted(combined_events, key=lambda e: e['year'], reverse=True)

        # Limit the number of events returned
        limited_events = sorted_events[:5]

        # Return the combined and sorted events as JSON
        return jsonify({'date': date, 'events': limited_events}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

# Run the application locally
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
