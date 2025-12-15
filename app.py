from flask import render_template
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from sketch import image_to_sketch
import io

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/sketch", methods=["POST"])
def sketch():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        return jsonify({"error": "Invalid image"}), 400

    sketch_img = image_to_sketch(img)

    success, buffer = cv2.imencode(".png", sketch_img)
    if not success:
        return jsonify({"error": "Encoding failed"}), 500

    return send_file(
        io.BytesIO(buffer),
        mimetype="image/png"
    )

if __name__ == "__main__":
    app.run(debug=True)
