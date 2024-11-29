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
        month, day = date.split('-')[1], date.split('-')[2]
        history_today_url = f"https://history.muffinlabs.com/date/{month}/{day}"
        history_today_response = requests.get(history_today_url)
        history_today_events = []

        if history_today_response.status_code == 200:
            history_today_data = history_today_response.json()
            raw_events = history_today_data.get('data', {}).get('Events', [])
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

        combined_events = history_today_events
        if date == "1969-07-20":
            combined_events.append({
                'year': 1969,
                'description': "Apollo 11 successfully lands on the Moon.",
                'link': "https://en.wikipedia.org/wiki/Apollo_11"
            })

        keywords = ["moon", "Apollo", "discovery", "independence", "treaty", "revolution"]
        sorted_events = sorted(
            combined_events,
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
    app.run(debug=True, host='127.0.0.1', port=8000)
