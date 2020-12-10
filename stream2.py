import streamlit as st
import requests
import base64
import json
import tensorflow as tf
import boto3

#radio = st.sidebar.radio(
 #   "Select from options!",
#    ("User Authentication","Predict")
#)

st.markdown('<style>body{background-color: #E0FFFF;}</style>',unsafe_allow_html=True)
loop = 'true'

st.title('User Authentication')
username = st.text_input('Username')
password = st.text_input('Password')
#if radio == 'User Authentication':
    
 #   st.title('User Authentication')

  #  st.subheader('_Please enter valid username and password_')
    

    
if st.button('Authenticate'):

      if username == 'Sahil': 
            if password == 'Sahil123':
               st.write('Authenticated')
                
            else:
                st.write('Please enter the correct username and password')
               
                   
                
#if radio == 'Predict':
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def serialize_text(text):
    example = tf.train.Example(features=tf.train.Features(feature={
    'text': _bytes_feature(text)
    }))
    serialized_example = example.SerializeToString()
    return serialized_example

model_server_url = 'http://localhost:8501/v1/models/half_plus_two:predict'

def predict(text):
    example = serialize_text(text)
    json_data = {
    "signature_name":"serving_default",
    "instances":[
    {
    "examples":{"b64": base64.b64encode(example).decode('utf-8')}
    }
    ]
    }
    resp = requests.post(model_server_url, json=json_data)
    return resp.json()

# def get_data(filename):
    # s3 = boto3.client("s3")
    # bucket = "ass2deidentifiedmessage"
    # # filename = "transcript1"  #input from user
    # key = filename + ".txt"
    # file = s3.get_object(Bucket=bucket, Key=key)
    # paragraph = str(file['Body'].read())

st.title('Prediction')

text = st.text_area("Enter text here", value='', max_chars=None)


if st.button('Predict Sentiment'):
    if username == 'Sahil': 
        if password == 'Sahil123':
            st.write('processing')
            # res = requests.get(f"https://h7xbsv1m5l.execute-api.us-east-1.amazonaws.com/prod/de-identify?ExeName={ExeName}&keyname={keyname}")
            result = predict(bytes(text, encoding='utf8'))
            st.write('Prediction Successful')
            # st.write(res.json())
            st.write(result)
        else:
            st.write('Please enter the correct username and password')
    else:
        st.write('Please enter the correct username and password')