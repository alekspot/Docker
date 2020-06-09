import os
import json

from flask import Flask

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURSE_DIR = os.path.join(BASE_FOLDER, "resourses")




@app.route('/')
def hello_world():
    while True:
        f = open('./data/res.txt')
        text = f.read()
        return text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

