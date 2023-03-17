from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def start():
    pass

if __name__=='__main__':
    app.run(debug=True)