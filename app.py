import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
#install flask_bcryt later for hashed passwords

app = Flask(__name__)

# == Routes Here ==

@app.route('/', methods=['GET'])
def get_index():
    return render_template('welcome.html')

# These lines start the server
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
    