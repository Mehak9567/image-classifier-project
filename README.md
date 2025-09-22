# image-classifier-project
Step 1: Professional README.md

Here’s a draft you can use directly in your repo:

# 🖼️ Image Classifier Web App

A simple **Flask-based web application** that allows users to upload an image and get real-time predictions using a **Hugging Face Vision Transformer (ViT)** model.

---

## ✨ Features
- Upload an image (`.jpg`, `.jpeg`, `.png`) via a web UI.
- Sends the image to **Hugging Face API** for classification.
- Displays the **top prediction** (highlighted) and other predictions with confidence scores.
- Clean UI with preview of uploaded image.

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Model API:** Hugging Face Inference API
- **Other Tools:** dotenv, requests

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/image-classifier-flask.git
cd image-classifier-flask

2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # for Mac/Linux
venv\Scripts\activate      # for Windows
pip install -r requirements.txt

3. Set up environment variables

Create a .env file in the project root and add:

HUGGING_FACE_API_URL=https://api-inference.huggingface.co/models/google/vit-base-patch16-224
HUGGING_FACE_API_KEY=your_api_key_here

4. Run the app
python web.py


Visit http://127.0.0.1:81
 in your browser.
📸 Screenshots

Home Page
<img width="1920" height="1080" alt="Screenshot (112)" src="https://github.com/user-attachments/assets/ad03d767-3a23-4078-8568-7c694f8183a3" />
Prediction Result
<img width="1920" height="1080" alt="Screenshot (111)" src="https://github.com/user-attachments/assets/7cdd5eff-0eda-4edb-a842-ecd1f9812701" />

