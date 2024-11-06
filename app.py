import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

#Load CNN model
model = tf.keras.models.load_model('model.h5')

#indeks class bisa dilihat dari kaggle
class_labels = {
    0: "Common Rust",
    1: "Gray Leaf Spot",
    2: "Blight",
    3: "Healthy"
}

#Preprocessing input image
def preprocess_image(image):
    image = image.resize((224, 224)) 
    image = np.array(image) / 255.0 
    image = np.expand_dims(image, axis=0)
    return image


st.title("Corn Disease CNN Model Testing with Streamlit")
st.write("Upload gambar, pastikan gambar jelas dan tidak blur")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

#Predicition image classification using model
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    processed_image = preprocess_image(image)
    
    prediction = model.predict(processed_image)
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_class_label = class_labels.get(predicted_class_index, "Unknown")
    confidence = np.max(prediction)

    st.write("Prediction:", predicted_class_label)
    st.write("Confidence:", f"{confidence:.2f}")