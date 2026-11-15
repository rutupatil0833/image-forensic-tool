
import streamlit as st
from PIL import Image
import hashlib
import io

st.title("Digital Image Verification and Authentication Tool")
st.write("CSDF Mini-Project")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image_bytes = uploaded_file.getvalue()
    image = Image.open(io.BytesIO(image_bytes))

    st.image(image, caption="Uploaded Image")

    st.subheader("Image Details")
    st.write("Filename:", uploaded_file.name)
    st.write("Format:", image.format)
    st.write("Dimensions:", image.size)
    st.write("File size:", len(image_bytes), "bytes")

    sha256_hash = hashlib.sha256(image_bytes).hexdigest()

    st.subheader("SHA-256 Hash")
    st.code(sha256_hash)

    st.success("Image analysis completed!")

    st.download_button(
        "Download Hash Report",
        data=f"Filename: {uploaded_file.name}\nSHA-256: {sha256_hash}",
        file_name="forensic_report.txt"
    )
