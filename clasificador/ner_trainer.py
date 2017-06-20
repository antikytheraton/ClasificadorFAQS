import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from sklearn import cross_validation, svm
from sklearn.metrics import accuracy_score

df=pd.read_csv("final_data.csv")
tags=df['tags'].tolist()[1:]
words=df['words'].tolist()[1:]

def prepara_frase(tags,words):
    features=[]
    feature={}
    targets=[]
    for ind,tag in enumerate(tags):
        if tag!='-':
            feature['0']=words[ind-2]
            feature['1']=words[ind-1]
            feature['2']=words[ind]
            feature['3']=words[ind+1]
            feature['4']=words[ind+2]
            features.append(feature)
            feature={}
            targets.append(tag)
    return features,targets

features,targets=prepara_frase(tags,words)
vectorizer = DictVectorizer(sparse=False)
vectorizer.fit(features)
joblib.dump(vectorizer, 'vectorizer.pkl')


transformed=vectorizer.transform(features)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(transformed, targets, test_size=0.1, random_state=42)
lin_svc = svm.LinearSVC(C=1).fit(X_train, y_train)

print(len(X_test))
print(accuracy_score(y_test, lin_svc.predict(X_test)))
joblib.dump(lin_svc, 'clasifier.pkl')