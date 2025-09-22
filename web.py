from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("HUGGING_FACE_API_URL")
headers = {'Authorization': f'Bearer {os.getenv("HUGGING_FACE_API_KEY")}'}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    # detect content type dynamically
    content_type = f"image/{file.filename.split('.')[-1].lower()}"
    if content_type not in ["image/jpeg", "image/jpg", "image/png"]:
        return jsonify({"error": "Only JPG, JPEG, and PNG are supported"})

    response = requests.post(
        API_URL,
        headers={**headers, "Content-Type": content_type},
        data=file.read()
    )

    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    try:
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 81))   # use $PORT if provided, otherwise 81
    app.run(host="0.0.0.0", port=port, debug=True)


