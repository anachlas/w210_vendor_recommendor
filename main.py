
# [START app]
import logging

# [START imports]
from flask import Flask, current_app, request, render_template
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='')
# [END create_app]


@app.route('/')
def main():
    return current_app.send_static_file('index.html')

@app.route('/search', methods=['POST'])
def hello():
    req=request.form['req']
    agency=request.form['agency']
    return render_template('results.html', agency=agency, requirement=req)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
