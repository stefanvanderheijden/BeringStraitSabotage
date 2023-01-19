from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

load_dotenv('./.flaskenv')

app = Flask(__name__,
            static_url_path='',
            static_folder = "../bssclient/dist",
            template_folder = "../bssclient/dist")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()	

