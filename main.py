
# [START app]
import logging

# [START imports]
from flask import Flask, current_app, request, render_template
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='')
# [END create_app]

vendors = {
    "meat": [
        {"name": "PUEBLO TRADING CO., INC", "duns": 174473280, "score": 1.0},
        {"name": "US FOODS, INC.", "duns": 795140433, "score": 1.0},
        {"name": "V3", "duns": 12345, "score": 1.0},
        {"name": "V4", "duns": 12345, "score": 1.0},
        {"name": "V5", "duns": 12345, "score": 1.0}
    ],
    "printers": [
        {"name": "V1", "duns": 12345, "score": 1.0},
        {"name": "V2", "duns": 12346, "score": 1.0},
        {"name": "V3", "duns": 12345, "score": 1.0},
        {"name": "V4", "duns": 12345, "score": 1.0},
        {"name": "V5", "duns": 12345, "score": 1.0},
        {"name": "V6", "duns": 12345, "score": 0.827123123},
        {"name": "V1", "duns": 12345, "score": 1.0},
        {"name": "V2", "duns": 12346, "score": 1.0},
        {"name": "V3", "duns": 12345, "score": 1.0},
        {"name": "V4", "duns": 12345, "score": 1.0},
        {"name": "V5", "duns": 12345, "score": 1.0},
        {"name": "V6", "duns": 12345, "score": 0.827123123}
    ],
    "foo": [
        {"name": "V1", "duns": 12345, "score": 1.0},
        {"name": "V2", "duns": 12346, "score": 1.0},
        {"name": "V3", "duns": 12345, "score": 1.0}
    ],
    "bar": [
        {"name": "There can be only one", "duns": 12345, "score": 0.827123123}
    ]
}

@app.route('/')
def main():
    return current_app.send_static_file('index.html')

@app.route('/results', methods=['POST'])
def search():
    req=request.form['req']
    return render_template('results.html', requirement=req, vendors=vendors[req], count=len(vendors[req]))

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
