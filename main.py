
# [START app]
import logging

# [START imports]
from flask import Flask, current_app, request
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='')
# [END create_app]


@app.route('/')
def main():
    return current_app.send_static_file('index.html')
# [END form]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
