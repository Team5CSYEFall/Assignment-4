# Assignment-4
## TFX: 
TFX is a Google production scale machine learning platform based on TenserFlow.
It provides a configuration framework and shared libraries to integrate common components needed to define, launch, and monitor your machine learning system.
When you’re ready to move your models from research to production, use TFX to create and manage a production pipeline.

## Goal: to deploy a sentiment analysis model to create a Model-as-a-service for anonymized data. 

## Step 1:Train TensorFlow models using TensorFlow Extended (TFX)
We used the following architecture to train the model for the anonymized data using BERT and it leverages TensorFlow Hub, Tensorflow Transform, TensorFlow Data Validation and Tensorflow Text and Tensorflow Serving

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/tfx.jpg)

### What preprocessing does BERT require?
Transformers like BERT are initially trained with two main tasks in mind:
Masked language models
Next sentence predictions (NSP)
These tasks require an input data structure beyond the raw text. Therefore, the BERT model requires, besides the tokenized input text, a tensor input_type_ids to distinguish between different sentences.
A second tensor input_mask is utilized to note the relevant tokens within the input_word_ids tensor. This is needed because we will expand our input_word_ids tensors with pad tokens to reach the maximum sequence length. 
That way all input_word_ids tensors will have the same lengths but the transformer can distinguish between relevant tokens (tokens from our input sentence) and irrelevant pads (filler tokens).

### The pipeline takes advantage of the broad TensorFlow Ecosystem, including: 
● Loading the IMDB dataset via TensorFlow Datasets 
● Loading a pre-trained model via tf.hub 
● Manipulating the raw input data with tf.text
● Building a simple model architecture with Keras 
● Composing the model pipeline with TensorFlow Extended, e.g. TensorFlow Transform, TensorFlow Data Validation and then consuming the tf.Keras model with the latest Trainer component from TFX.

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/o.png)

We created a BERT model on IMDB dataset and then we exported the trained model to Google Drive.

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/t.png)


The model here is savedmodel.pb

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/th.png)

## Step 2: Use the TENSORFLOW TFX RESTFUL API to serve the model 

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/f.png)

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/fi.png)

## Step 3:Dockerize the API service

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/s.png)

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/se.png)

## Step 4: Build a Reference App in Streamlit to test the API 

![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/e.png)
![picture](https://github.com/Team5CSYEFall/Assignment-4/blob/main/img/n.png)



