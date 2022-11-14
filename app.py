import os
import shutil
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask_cors import CORS
from model import sar_class_prediction
from utils import save_image


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/x", methods=["POST"])
def generate_nst():
    """
        DESCRIPTION
        ___________
        This function has route endpoint x which only has one request i.e. POST
        It recives the content and style images and returns the files

        RETURNS
        _______
        This function returns the genrated nst image.
    """
    if request.method == "POST":
        sar_ = request.files["sar_image"]
        shutil.rmtree("uploads")
        os.mkdir("uploads")
        sar_file_path_ = save_image(sar_)
        sar_prediction = sar_class_prediction(sar_image_path=sar_file_path_)
        return jsonify(
            prediction = f"Image Belong From SAR Class {sar_prediction}"
        )

if __name__ == "__main__":
    app.run(debug=True, port=7000)
