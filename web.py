from flask import Flask, render_template, request, jsonify
import requests, os
from dotenv import load_dotenv

load_dotenv()

# Load both models
CLASSIFIER_URL = os.getenv("HUGGING_FACE_API_URL_CLASSIFIER")
DETECTOR_URL = os.getenv("HUGGING_FACE_API_URL_DETECTOR")
headers = {'Authorization': f'Bearer {os.getenv("HUGGING_FACE_API_KEY")}'}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    content_type = f"image/{file.filename.split('.')[-1].lower()}"

    if content_type not in ["image/jpeg", "image/jpg", "image/png"]:
        return jsonify({"error": "Only JPG, JPEG, and PNG are supported"})

    img_bytes = file.read()

    # 1️⃣ Image classification
    class_res = requests.post(
        CLASSIFIER_URL,
        headers={**headers, "Content-Type": content_type},
        data=img_bytes
    )

    # 2️⃣ AI-generated detection
    detect_res = requests.post(
        DETECTOR_URL,
        headers={**headers, "Content-Type": content_type},
        data=img_bytes
    )

    try:
        classification = class_res.json()
        detection = detect_res.json()
        return jsonify({
            "classification": classification,
            "ai_detection": detection
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 81))
    app.run(host="0.0.0.0", port=port, debug=True)
