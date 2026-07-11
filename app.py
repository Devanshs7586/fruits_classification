import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Fruit Classifier", page_icon="🍎")

st.title("🍎 Fresh vs Rotten Fruit Classifier")
st.write("Upload a fruit image, then click Predict.")

# -----------------------------
# Load model
# -----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "fruits_classification_model.keras",
        compile=False
    )

model = load_model()

# -----------------------------
# Image size
# -----------------------------
img_height = 224
img_width = 224

# -----------------------------
# Upload image
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload fruit image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Predict"):
        img = image.resize((img_width, img_height))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        probability = float(prediction[0][0])

        if probability > 0.5:
            result = "Rotten"
            confidence = probability
        else:
            result = "Fresh"
            confidence = 1 - probability

        st.subheader("Prediction Result")
        st.success(f"Prediction: **{result}**")
        st.write(f"Confidence: **{confidence * 100:.2f}%**")
        st.progress(confidence)

        st.write("Raw model output:", prediction)
else:
    st.info("Please upload an image first.")