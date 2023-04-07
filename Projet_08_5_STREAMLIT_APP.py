# Import relevant Python libraries
import os
import PIL.Image
import streamlit as st
import requests
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import PIL.Image as Image
import io
from io import StringIO


# URL of the API

url = 'https://p8-app-deploy.azurewebsites.net/segment'


st.set_page_config(
    page_title="P8-Image segmentation",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('WELCOME TO PROJECT 8 WEB PAGE ')

col1, col2 = st.columns(2)


with col1:
   st.header("Upload an image")
   file_uploaded = st.file_uploader("Please upload your image from cityscapes dataset:",type=['png'])
   if file_uploaded is not None:
        
        #-------------------------------------------------
        image_bytes = file_uploaded.read()
        st.write(type(image_bytes))
        image_data = {'image': image_bytes}
        r = requests.post(url, files=image_data)
        st.write('URL response state  :', r)
        img_array = cv2.imdecode(np.frombuffer(r.content, np.uint8), -1)
        st.image(image_bytes, width=256,caption='Original image')
        
        st.image(img_array,caption='Mask on Grayscale')
        plt.imsave('test.png',img_array,cmap='viridis')
        st.image('test.png', caption ='Mask on colored aspect')


with col2:
    list_photos = os.listdir('input_images')
    st.header("Choose an image within selectbox")
    option = st.selectbox('Pick your cityscapes image :',list_photos)
    if option == '....png':
        st.write("Didn't pick your image yet....." )

    else :
         st.write('You selected:', option)
         path=('./input_images/')
         
         img = PIL.Image.open(path+option, mode='r')
        

         b = io.BytesIO()
         img.save(b, 'png')
         im_bytes = b.getvalue()
         
         image_data = {'image': im_bytes}
         
         r = requests.post(url, files=image_data)
         st.write('URL response state  :', r)
         img_array = cv2.imdecode(np.frombuffer(r.content, np.uint8), -1)
         st.image(img, width=256,caption='Original image')
         
         st.image(img_array,caption='Mask on Grayscale')

         plt.imsave('test.png',img_array,cmap='viridis')
         st.image('test.png', caption ='Mask on colored aspect')
