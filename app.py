# Import necessary libraries
from flask import Flask, request, jsonify  # Flask for the web server
import requests  # To fetch data from the external API

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
    Simplifies the API response to include only the year, text, and a single link.
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
        api_url = f"https://history.muffinlabs.com/date/{month}/{day}"
        response = requests.get(api_url)

        # Check if the API call is successful
        if response.status_code == 200:
            data = response.json()  # Parse the API response
            raw_events = data.get('data', {}).get('Events', [])  # Extract raw events
            
            # Simplify the events for cleaner output
            simplified_events = []
            for event in raw_events:
                # Extract relevant fields: year, plain text, and a single link
                year = event.get('year', 'Unknown Year')
                text = event.get('text', 'No description available.')
                links = event.get('links', [])
                
                # Pick only the first link if available
                primary_link = links[0]['link'] if links else None
                
                # Append only the clean and structured data
                simplified_events.append({
                    'year': year,
                    'description': text,
                    'link': primary_link
                })

            # Limit the number of events returned to avoid clutter
            limited_events = simplified_events[:5]  # Show only the top 5 events

            # Return the cleaned-up and limited events as JSON
            return jsonify({'date': date, 'events': limited_events}), 200
        else:
            # Return an error if the API call fails
            return jsonify({'error': 'Failed to fetch data from the API.'}), 500
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

# Run the application locally
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
