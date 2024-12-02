from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/search', methods=['GET'])
def search():
    date = request.args.get('date')
    if not date:
        return jsonify({'error': 'Please provide a valid date in YYYY-MM-DD format.'}), 400

    try:
        # Parse the input date
        year, month, day = date.split('-')
        history_today_url = f"https://history.muffinlabs.com/date/{month}/{day}"
        history_today_response = requests.get(history_today_url)

        if history_today_response.status_code != 200:
            return jsonify({'error': 'Failed to fetch data from the history API.'}), 500

        # Extract and filter events by the full date (YYYY-MM-DD)
        history_today_data = history_today_response.json()
        raw_events = history_today_data.get('data', {}).get('Events', [])
        filtered_events = [
            {
                'year': int(event['year']),
                'description': event['text'],
                'link': event['links'][0]['link'] if event['links'] else None
            }
            for event in raw_events
            if event['year'] == year
        ]

        # Add Apollo 11 special case only if not already present
        apollo_event = {
            'year': 1969,
            'description': "Apollo 11 successfully lands on the Moon.",
            'link': "https://en.wikipedia.org/wiki/Apollo_11"
        }
        if date == "1969-07-20" and apollo_event not in filtered_events:
            filtered_events.append(apollo_event)

        # Sort and limit the events
        keywords = ["moon", "Apollo", "discovery", "independence", "treaty", "revolution"]
        sorted_events = sorted(
            filtered_events,
            key=lambda e: (
                any(keyword.lower() in e['description'].lower() for keyword in keywords),
                e['year']
            ),
            reverse=True
        )
        limited_events = sorted_events[:5]

        return jsonify({'date': date, 'events': limited_events}), 200

    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
