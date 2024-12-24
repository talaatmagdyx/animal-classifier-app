import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np


# Load pre-trained MobileNetV2 model
@st.cache_resource
def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    return model


model = load_model()


# Function to preprocess the image
def preprocess_image(image):
    img = image.resize((224, 224))  # Resize to match model input size
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array


# Function to predict the animal name
def predict_animal(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    return decoded_predictions[0][0][1]  # Get the predicted label (class name)


# Streamlit app
st.title("Animal Classifier")
st.write("Upload an image, and the app will identify the animal!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")

    # Predict the animal name
    prediction = predict_animal(image)
    st.write(f"Prediction: **{prediction}**")
