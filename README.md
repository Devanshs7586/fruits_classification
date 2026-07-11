# Fresh and Rotten Fruit Classification Using CNN

## Project Overview

This project uses a Convolutional Neural Network, or CNN, to classify fruit images as either fresh or rotten.

The model learns visual features such as fruit colour, texture, dark spots, mould, and surface damage. After training, the model can predict the condition of a fruit from an uploaded image.

A Streamlit web application is also included so users can upload an image and receive a prediction.

## Objective

The main objectives of this project are:

* To build a CNN model for fruit image classification.
* To identify whether a fruit is fresh or rotten.
* To preprocess and augment image data.
* To evaluate the model using suitable performance metrics.
* To deploy the trained model using Streamlit.

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Pillow
* Scikit-learn
* Streamlit

## Project Workflow

1. Import the required libraries.
2. Load the fresh and rotten fruit image dataset.
3. Resize and normalise the images.
4. Apply data augmentation to improve model generalisation.
5. Divide the dataset into training, validation, and testing sets.
6. Build the CNN architecture.
7. Train the model on the training dataset.
8. Evaluate the model using test data.
9. Save the trained model.
10. Deploy the model using Streamlit.

## CNN Architecture

The CNN model contains:

* Convolutional layers for feature extraction.
* Max-pooling layers for reducing image dimensions.
* Dropout layers for reducing overfitting.
* Flatten layer for converting feature maps into a one-dimensional vector.
* Dense layers for classification.
* Output layer for predicting the fruit category.

## Dataset

The dataset contains images of fresh and rotten fruits.

Example categories may include:

* Fresh Apple
* Rotten Apple
* Fresh Banana
* Rotten Banana
* Fresh Orange
* Rotten Orange

The exact classes depend on the dataset used for training.

## Project Structure

```text
fresh-rotten-fruit-classification/
│
├── app.py
├── train_model.py
├── fruits_classification_model.keras
├── requirements.txt
├── README.md
├── dataset/
│   ├── train/
│   ├── validation/
│   └── test/
└── images/
```

## Installation

Clone the GitHub repository:

```bash
git clone https://github.com/your-username/fresh-rotten-fruit-classification.git
```

Open the project directory:

```bash
cd fresh-rotten-fruit-classification
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Streamlit Application

Use the following command:

```bash
streamlit run app.py
```

The application will open in your web browser.

Upload a fruit image, and the model will predict whether the fruit is fresh or rotten.

## Image Preprocessing

Before prediction, the uploaded image is:

* Converted into RGB format.
* Resized to the input size expected by the CNN model.
* Converted into a NumPy array.
* Normalised by dividing pixel values by 255.
* Expanded into a batch dimension.

## Model Evaluation

The model can be evaluated using:

* Accuracy
* Loss
* Precision
* Recall
* F1-score
* Confusion Matrix
* Training and validation accuracy graphs
* Training and validation loss graphs
## Trained Model

The trained model file is not included in this repository because it exceeds GitHub's file-size limit.

Train the model using `cnn.ipynb`, or place the trained model file in the project directory before running the Streamlit application.


## Challenges Faced

Some of the main challenges faced during the project were:

* Imbalanced numbers of fresh and rotten fruit images.
* Differences in lighting, background, and image quality.
* Similar appearance between slightly rotten and fresh fruits.
* Overfitting during CNN model training.
* Selecting the correct image size and CNN architecture.
* Improving validation and test accuracy.
* Matching preprocessing during training and prediction.
* Saving and loading the trained model correctly.
* Integrating the model with the Streamlit application.
* Handling incorrect image formats and user uploads.

## Future Improvements

The project can be improved by:

* Adding more fruit categories.
* Collecting a larger and more balanced dataset.
* Using transfer learning models such as MobileNetV2, VGG16, or EfficientNet.
* Improving model accuracy through hyperparameter tuning.
* Adding confidence scores with predictions.
* Deploying the application on Streamlit Community Cloud.
* Creating a mobile application for real-time fruit classification.
* Adding camera-based live prediction.

## Applications

This system can be useful in:

* Fruit shops
* Supermarkets
* Warehouses
* Food-processing companies
* Agricultural quality inspection
* Automated fruit-sorting systems
* Inventory and food-waste management

## Conclusion

The Fresh and Rotten Fruit Classification project demonstrates how CNNs can be used for image classification and food-quality inspection.

The trained model can identify the condition of a fruit from an image and provide predictions through a simple Streamlit interface. This project can help automate fruit-quality checking and reduce food waste.

## Author

**Name:** Your Name
**Project:** Fresh and Rotten Fruit Classification
**Technology:** CNN, TensorFlow, Keras and Streamlit
