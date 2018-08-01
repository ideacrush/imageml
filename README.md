Image Categorization

The project deals with the categorization of images into the categories which are based on the type of 
product they represent.

The project is in python using the various libraries and also is made into GUI Application. The 
major libraries used are Scikit Library, MatplotLib, PyQT and OpenCV.

The project utilizes the OpenCV library to prepare the Image Dataset for the model(curve fitting).

1. Dimensions down to 150*150.
2. Separate RGB components.
3. Plot the histograms and get the bins for RGB.
4. Combine the bins into a 150 long array and this array is instrumental in representing every image in the dataset. This is called a Image-Vector or Vector in general.
5. With every image in our dataset, we have a corresponding category that it falls into. This Category value goes with its respective ImageVector and they together represent a training dataset.
      Scikit Library is a Opensource Library that has implementation of all the major machine learning algorithms in a easy to use package with functions to call and execute the required action.
      In this project a scikit provided classifier called Naive Bayes Classifier is used to create the train the dataset and produce a model for prediction.
6. We pass the collection of ImageVectors and their corresponding categories to the scikit library function to fit the data onto a model which will be called a prediction model.
      Now we get the prediction model (which is a python object with some properties) 
      One important property is the "Accuracy" and it comes into picture when we query the prediction model that we made with the ImageVector of a image (called Validation Image - basically something that helps us identify if the prediction models works well. It is also called Query Image depending on the phase of the application)
7. The image is queried on the prediction model and the model returns the category the image falls in and also the accuracy with which it associate that particular to the the image.
      The accuracy figure is used to determine the if the model is confident in predicting the category and also we can see the accuracy when we change the different aspects associated with the model development( In this case every decision that we took has an effect on the accuracy)
8. We wrapped this into a GUI and that is just for aesthetic purposes.
