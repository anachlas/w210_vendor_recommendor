
# [START app]
import logging

# [START imports]
import json

from flask import Flask, current_app, request, render_template
from os import listdir
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='')
# [END create_app]

demo_results = [filename.split('.')[0] for filename in listdir('demo_results')]
demo_results = [result for result in demo_results if result.strip()]

@app.route('/')
def main():
    return current_app.send_static_file('index.html')

@app.route('/demo')
def demo():
    return render_template('demo.html', options=[x.replace("_"," ").capitalize() for x in demo_results])

@app.route('/results', methods=['POST'])
def search():
    req_id=int(request.form['req'])
    print(request.form)
    with open('demo_results/'+ demo_results[req_id] + '.json') as data_file:
        vendors = json.load(data_file)

    return render_template('results.html', requirement=demo_results[req_id].replace("_"," "), vendors=vendors, count=len(vendors))

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
