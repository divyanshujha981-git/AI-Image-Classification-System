from flask import render_template, Flask, request, jsonify
import os
from classify_image import classify_image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload_files", methods=["POST"])
def upload_files():
    file = request.files["IMAGE_FILE"]

    os.makedirs("./UPLOADSS/", exist_ok=True)
    filePath = "./UPLOADSS/"+file.filename

    file.save(filePath)

    label_class = classify_image(filePath)
    return jsonify("class", label_class)


if __name__ == "__main__":
    app.run(debug=True)