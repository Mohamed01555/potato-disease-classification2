# Potato Disease Classification Web App

This web app is designed to classify potato plants into one of three categories: early blight, late blight, or healthy. It uses a machine learning model trained on a dataset of potato plant images to make its predictions.

## Getting Started

To use this web app, simply go to the following URL: <a href="https://mohamed01555.github.io/potato-disease-classification2/">Potato Disease classifier</a>

Once there, you will see a form where you can upload an image of a potato plant. Select an image from your computer, then click "Submit" to upload it to the server.

The server will then process the image using the machine learning model and return a prediction of whether the potato plant is suffering from early blight, late blight, or is healthy.

## Model Details

The machine learning model used in this web app is a convolutional neural network (CNN) trained on a dataset of potato plant images. The model was trained using the Keras deep learning library with a TensorFlow backend.

The dataset used to train the model was obtained from the following sources:

- [Plant_village Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)

The model was trained on Colab with an NVIDIA T4 GPU.

## Dependencies

The following dependencies are required to run this web app:

- Flask
- Keras
- TensorFlow

These dependencies can be installed using pip:

```
pip install -r requirements.txt
```

## Acknowledgments

I would like to thank the creators of the early blight, late blight, and healthy potato datasets for making their data publicly available. I would also like to thank Google for providing the computing resources necessary to train the machine learning model, also [Codebasics](https://www.youtube.com/@codebasics) for teaching me new ideas.
