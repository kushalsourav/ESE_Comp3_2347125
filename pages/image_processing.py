import streamlit as st
from PIL import Image, ImageFilter


st.title("Image Processing")

st.header("Applying filters on Image")


image = Image.open("image1.jpg")

st.write("Original Image")
image.show()
st.write(image)

st.write("resized Image")
resize = image.resize((400,400))
st.write(resize)

st.write("Cropped Image")
cropped_image = image.crop([100,100,200,200])
st.write(cropped_image)

st.write("rotated Image")
image_rotation = image.rotate(45)
st.write(image_rotation)

st.write("grayscaled Image")
grayscale_image = image.convert('L')
st.write(grayscale_image)



