# Using machine learning to detect malisiouse URLs

# Imports
import pandas as pd # Pandas to manipualte datasets
# sklearn libary for ML imports
from sklearn.feature_extraction.text import TfidfVectorizer # TfidfVetorizer used for vectorization on textual data into numerical vectors for NLP.
from sklearn.linear_model import LogisticRegression # ML Model algorithm used for classification brach of ML.
from sklearn.model_selection import train_test_split # Allows splitting of dataset for training/testing.

# Accessing dataset
dataset = pd.read_csv("urldata.csv") # Storing a kaggle dataset including both known bad and good Urls in a variable for the model to learn from.

# Data cleaning and preparing data
y = dataset["label"] # Storing output set (good or bad values) in y by convention

urls = dataset["url"] # Storing input set (urls) in vairable for vectorization due to non numerical values.

vectorizer = TfidfVectorizer() # Storing vectorizer function into variable 

X = vectorizer.fit_transform(urls) # Applying the vectorizer to the dataset urls to encode them to numerical vectors for NLP (ML algorithm can coputate once vectorized). X by convention.

# Training model
# Splitting data set into training/testing sets, then setting test dataset to 20% of entire dataset. Random state to define arbiarty split of data when training, 42 by convention.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Creating model
model = LogisticRegression(max_iter=1000)	# specifying logistic regression algorithm, passinng max itteration 1000 argument to stop iteration error.
model.fit(X_train, y_train) # method using input/output dataset to train model using training datasets.

# Defining a function to predict label of a prvided argument by using previouse training and returning the result.
def ML_Prediction(url):

    # Pass a URL to be labeled
    predictUrl = [url] # specifying url to be predicted and stored in variable.

    predictUrl = vectorizer.transform(predictUrl) # vectorization of predictUrl into numerical vectors for NLP stored in variable.
    prediction = model.predict(predictUrl) # using the model to predict the label of predicUrl vectorized input and stored in variable.

     # if prediction == good return clear else return malicious.

    if prediction == "good":
        return "Clear"
    else:
        return "Malicious"

# Known malicious URLs (https has been removed):
# ://claimmask.com/"
# ://login-dana-id.giixzg.me/"
# ://havkeye14.wixsite.com/my-site-1/
# ://dovzzt.n0c.world/bpost2/
# ://cg96358.tw1.ru/?return_url=://www.orange.fr/portail&_Auth
# ://accshmesrvc0log.github.io/
# ://one.link/annushka_almazova
# ://dev-kejomokkeflushah.pantheonsite.io/att/att.html
# ://havkeye14.wixsite.com/my-site-1/
# ://innovative-divya.github.io/Netflix-clone
    
# Know safe URLs
# https://en.m.wikipedia.org
# https://stackoverflow.com/questions/58356254/machine-learning
# https://www.autotrader.co.uk/car-search?postcode=i77777&price-from=10000&price-to=15000&make=Mercedes-Benz&advertising-location=at_cars&page=1
# https://www.loveholidays.com/sem/cheap.html?WT.mc_id=pgo-35492155817
# https://teams.microsoft.com 
# https://sts.anglia.ac.uk/adfs/ls/idpinitiatedsignon.aspx?SAMLRequest
# https://500px.com/photo/49283436/chicago-looking-up-by-alex-dibrova
# https://kids.nationalgeographic.com/animals
# https://id.cisco.com/
# https://twitter.com/?lang=en