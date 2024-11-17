import streamlit as st
from PIL import Image
import style
import os

st.title("Style Transfer")

# Image selection or upload
st.sidebar.write("### Select or Upload an Image")

# Predefined images
img_source = st.sidebar.radio(
    "Image Source:",
    options=("Use Predefined Image", "Upload Image")
)

if img_source == "Use Predefined Image":
    img = st.sidebar.selectbox(
        'Select Image',
        ('amber.jpg', 'stata.jpg','chicago')
    )
    input_image = f"images/content-images/{img}"
else:
    uploaded_file = st.sidebar.file_uploader("Upload Your Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        input_image = f"images/content-images/{uploaded_file.name}"
        with open(input_image, "wb") as f:
            f.write(uploaded_file.getbuffer())
    else:
        st.warning("Please upload an image.")
        st.stop()

# Style selection
style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

# Prepare model and output paths
model = f"saved_models/{style_name}.pth"
file_extension = input_image.split('.')[-1]  # Get file extension
output_image = f"images/output-images/{os.path.basename(input_image).split('.')[0]}-{style_name}.{file_extension}"

# Display source image
st.write("### Source Image:")
image = Image.open(input_image)
st.image(image, width=400)

# Stylize button
if st.button("Stylize"):
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    # Display output image
    st.write("### Output Image:")
    output_img = Image.open(output_image)
    st.image(output_img, width=400)

    # Enable download of the stylized image
    with open(output_image, "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name=f"stylized-{os.path.basename(output_image)}",
            mime=f"image/{file_extension}"
        )