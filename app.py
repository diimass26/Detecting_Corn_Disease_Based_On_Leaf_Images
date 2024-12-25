import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

# Load the pre-trained model
model = load_model("saved_model/model.h5")

# Define class labels (modify as per your model's labels)
class_labels = ["Blight", "Common Rust", "Gray Leaf", "Healthy"]

# Define a function to preprocess the uploaded image
def preprocess_image(image, target_size):
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize to [0, 1]
    return image

# Define a function for making predictions
def predict(image):
    processed_image = preprocess_image(image, target_size=(224, 224))  # Adjust size as per your model
    predictions = model.predict(processed_image)
    if len(predictions.shape) == 2:  # Ensure predictions are in the expected shape
        max_index = np.argmax(predictions[0])
        predicted_class = class_labels[max_index]
        confidence_score = round(float(predictions[0][max_index]) * 100, 2)
        return predicted_class, confidence_score
    else:
        raise ValueError(f"Unexpected predictions shape: {predictions.shape}")


# Streamlit app interface
st.title("Corn Disease Detection App")
st.write("Upload a corn leaf image to detect diseases.")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Perform prediction
    with st.spinner("Analyzing the image..."):
        predicted_class, confidence_score = predict(image)
    
    # Display prediction result
    st.subheader("Prediction Result:")
    st.write(f"{predicted_class}: {confidence_score}% confidence")
