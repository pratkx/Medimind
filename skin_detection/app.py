# -*- coding: utf-8 -*-
# Import necessary libraries

from flask import Flask, render_template, request, Response
import numpy as np
import os
import keras 
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model

# Load model

model = load_model("skin.h5")


print("Model Loaded")

# Predict Diseases

def pred_disease(skin):

    # Load image
    test_image = load_img(skin, target_size=(224,224))         
    print("Got image for prediction")
    
    # Convert image to np array and normalize
    test_image = img_to_array(test_image)/255  

    # Change dimension 30 to 40                            
    test_image = np.expand_dims(test_image, axis = 0)                       
    
    result = model.predict(test_image).round(3)
    print('Raw result = ',result)
    
    # Get the index of max value
    pred = np.argmax(result)                                                
    
    if(pred == 0):
        # Acne
        return "Atopic_Dermatitis", 'Atopic_Dermatitis.html'
    elif(pred == 1):
        # Eczema
        return "Basil_Cell_Carcinoma", 'Basil_Cell_Carcinoma.html'
    elif(pred == 2): 
        # Melanoma
        return "Eczema", 'Eczema.html'
    elif(pred == 3): 
        # Psoriasis
        return "Melanoma", 'Melanoma.html'
    
    else:
        return "random", 'random.html'
    

# Create flask instance

app = Flask(__name__)

# Render index.html page

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')


# Get input image from user and then predict class and render respective html pages

@app.route("/predict", methods=['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image']
        filename = file.filename        
        print("Input posted = ", filename)
         
        file_path = os.path.join('static/useruploaded', filename)
        file.save(file_path)
 
        print("Predicting class")
        pred, output_page = pred_disease(skin=file_path)
               
        return render_template(output_page, pred_output = pred, user_image = file_path)
        
# For local system and cloud

if __name__ == "_main_":
    app.run(threaded=False)

