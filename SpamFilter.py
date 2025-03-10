from langdetect import detect
import joblib
from Textproc import count_punc, count_cap, length
import numpy as np


modelAng = joblib.load("spam_modelAng.pkl")
modelAb = joblib.load("spam_modelAb.pkl")
modelFr = joblib.load("spam_modelFr.pkl")
Ab_CountVec = joblib.load("tfidf_Abvectorizer.pkl")
Fr_CountVec = joblib.load("tfidf_Frvectorizer.pkl")
Ang_CountVec = joblib.load("tfidf_Angvectorizer.pkl")


text = "hello there"  
language = detect(text)  
print(language)


text = text.lower()


def selectFeatures(lang):
   
    if lang != 'ar':
        
        punc = count_punc(text)
        cap = count_cap(text)
        text_len = length(text)
        additional_features = np.array([[text_len, cap, punc]])  
        
        if lang == 'fr':
            tfidf_features = Fr_CountVec.transform([text])
        else:
            tfidf_features = Ang_CountVec.transform([text])
    else:

        punc = count_punc(text)
        text_len = length(text)
        additional_features = np.array([[text_len, punc]]) 
        tfidf_features = Ab_CountVec.transform([text])
    

    return np.hstack((additional_features, tfidf_features.toarray()))


features = selectFeatures(language)


#if language == 'fr':
 #   print("Using Model 2 (French)")
  #  prediction = modelFr.predict(features)
#elif language == 'en':
 #   print("Using Model 1 (English)")
  #  prediction = modelAng.predict(features)
#elif language == 'ar':
 #   print("Using Model 3 (Arabic)")
  #  prediction = modelAb.predict(features)
#else:
 #   print('Language not supported')


#print(f"Prediction: {prediction}")


print(features.shape)