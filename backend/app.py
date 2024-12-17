from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)  # Tambahkan ini untuk mengaktifkan CORS

# Load model
MODEL_PATH = "model_massive.h5"
model = load_model(MODEL_PATH)

# Class names
CLASS_NAMES = ["blight", "common rust", "gray spot", "healthy"]

# Handling tips
HANDLING_TIPS = {
    'common rust': {
        "title": "Tips Mengatasi Common Rust",
        "tips": [
            "1. Gunakan varietas jagung tahan: Pilih benih yang tahan terhadap common rust (BISI-18, Pioneer P27, NK7328).",
            "2. Pengendalian kimia: Semprotkan fungisida berbasis strobilurin atau triazol jika penyakit terdeteksi dini.",
            "3. Rotasi tanaman: Hindari menanam jagung di lahan yang sama secara berturut-turut untuk mengurangi inokulum patogen.",
            "4. Pola tanam yang baik: Jaga jarak tanam agar sirkulasi udara meningkat dan kelembapan berkurang."
        ]
    },
    'gray spot': {
        "title": "Tips Mengatasi Gray Leaf Spot",
        "tips": [
            "1. Varietas tahan penyakit: Tanam varietas jagung yang memiliki ketahanan terhadap gray leaf spot (BISI-2, NK7328).",
            "2. Pemangkasan daun yang terinfeksi: Segera buang daun yang menunjukkan gejala untuk mencegah penyebaran.",
            "3. Fungisida preventif: Gunakan fungisida berbasis azoksistrobin atau propikonazol saat kondisi mendukung infeksi (kelembapan tinggi dan suhu hangat).",
            "4. Hindari irigasi atas yang menyebabkan daun basah.",
            "5. Lakukan pengelolaan sisa tanaman dengan membajak atau membakar sisa tanaman yang terinfeksi."
        ]
    },
    'blight': {
        "title": "Tips Mengatasi Blight",
        "tips": [
            "1. Gunakan benih unggul: Pilih varietas jagung tahan terhadap blight (Pioneer P27, BIMA 20 URI).",
            "2. Fungisida: Semprotkan fungisida sistemik seperti mankozeb, flutriafol, atau propikonazol saat gejala awal muncul.",
            "3. Tanam tepat waktu: Hindari menanam jagung terlalu awal di musim hujan, karena kondisi lembap mendukung infeksi.",
            "4. Pengelolaan sisa tanaman: Hancurkan sisa tanaman yang terinfeksi agar tidak menjadi sumber inokulum.",
            "5. Rotasi tanaman: Tanam tanaman selain jagung (seperti kedelai) untuk memutus siklus hidup patogen."
        ]
    },
    'healthy': {
        "title": "Tanaman Anda Sehat!",
        "tips": [
            "Tanaman Anda sehat! Pastikan untuk terus merawatnya dengan pemupukan dan pengendalian hama secara berkala."
        ]
    }
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        if not file:
            return jsonify({"error": "No file uploaded"}), 400
        
        # Preprocess the image
        image = Image.open(file).convert("RGB")
        image = image.resize((224, 224))  # Mengubah size ke ukuran input model
        image_array = img_to_array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Perform prediction
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = float(np.max(predictions))

        # Get class name and handling tips
        predicted_class_name = CLASS_NAMES[predicted_class]
        handling_tip = HANDLING_TIPS[predicted_class_name]

        # Prepare response
        result = {
            "predicted_class": predicted_class_name,
            "confidence": confidence,
            "handling_tip": handling_tip
        }
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
