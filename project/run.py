# Importing libraries

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')



df = pd.read_csv('Crop_recommendation.csv')


#Seperating features and target label
features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
#features = df[['temperature', 'humidity', 'ph', 'rainfall']]
labels = df['label']


# Initialzing empty lists to append all model's name and corresponding name
acc = []
model = []


# Splitting into train and test data

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)



#===========================Decision Tree==================================
from sklearn.tree import DecisionTreeClassifier

DecisionTree = DecisionTreeClassifier(criterion="entropy",random_state=2,max_depth=5)

DecisionTree.fit(Xtrain,Ytrain)

predicted_values = DecisionTree.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Decision Tree')
#print("DecisionTrees's Accuracy is: ", x*100)
#print(classification_report(Ytest,predicted_values))



#===============================Guassian Naive Bayes======================
from sklearn.naive_bayes import GaussianNB

NaiveBayes = GaussianNB()

NaiveBayes.fit(Xtrain,Ytrain)

predicted_values = NaiveBayes.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Naive Bayes')
#print("Naive Bayes's Accuracy is: ", x)
#print(classification_report(Ytest,predicted_values))






#=========================Support Vector Machine (SVM)==========================
from sklearn.svm import SVC
# data normalization with sklearn
from sklearn.preprocessing import MinMaxScaler

# fit scaler on training data
norm = MinMaxScaler().fit(Xtrain)
X_train_norm = norm.transform(Xtrain)

# transform testing dataabs
X_test_norm = norm.transform(Xtest)
SVM = SVC(kernel='poly', degree=3, C=1)
SVM.fit(X_train_norm,Ytrain)
predicted_values = SVM.predict(X_test_norm)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('SVM')
#print("SVM's Accuracy is: ", x)
#print(classification_report(Ytest,predicted_values))





#===============================Logistic Regression============================
from sklearn.linear_model import LogisticRegression

LogReg = LogisticRegression(random_state=2)

LogReg.fit(Xtrain,Ytrain)

predicted_values = LogReg.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Logistic Regression')
#print("Logistic Regression's Accuracy is: ", x)
#print(classification_report(Ytest,predicted_values))





#================================Random Forest==================================
from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
#print("RF's Accuracy is: ", x)
#print(classification_report(Ytest,predicted_values))





'''
#=================================XGBoost======================================
import xgboost as xgb
XB = xgb.XGBClassifier()
XB.fit(Xtrain,Ytrain)

predicted_values = XB.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('XGBoost')
print("XGBoost's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

'''
print("\n<---Hi Welcome to our 'Crop Recommendation System'--->\n")

i = 10000
while i > 0:
    print("\t\t\t====================================MENU==========================================")
    print("\t\t\t\t\t\t1.Crop Recommendation\n\t\t\t\t\t\t2.Model Accuracy\n\t\t\t\t\t\t3.Accuaracy Pie_chart\n\t\t\t\t\t\t4.Dataset\n\t\t\t\t\t\t5.Size of Dataset\n\t\t\t\t\t\t6.Shape of Dataset\n\t\t\t\t\t\t7.Exit")
    print("\t\t\t==================================================================================\n")


    ch = int(input("\nEnter ur choice:"))

    if(ch==1):
        print("\nEnter the data")
        print("Nitrogen(N):",end = '')
        N = int(input())
        print("Phosphorous(P):",end = '')
        P = int(input())
        print("Potassium(K):",end = '')
        K = int(input())
        print("Temperature(T):",end = '')
        T = int(input())
        print("Humidity(H):",end = '')
        H = int(input())
        print("pH:",end = '')
        pH = float(input())
        print("Rainfall(R):",end = '')
        R = int(input())
        print("\n")
        print("According to Your Data")
        #print("Nitrgen:{}\nPhosphorous:{}\nPotassium:{}\nTemperature:{}\nHumidity:{}\npH:{}\nRainfall:{}".format(N,P,K,T,H,pH,R))
        data = np.array([[N,P,K,T,H,pH,R]])
        prediction = RF.predict(data)
        print("'",prediction[0],"'",end = '')
        print("is recommonded best suitable crop")
        print("---------------------------------------------------------")
        
    elif(ch==2):
        accuracy_models = dict(zip(model, acc))
        for k, v in accuracy_models.items():
            print("---------------------------------------------")
            print (k,"Accuarcy is:", v)
            print("---------------------------------------------\n")
            
        print("To see the graph of accuracy of model")
        print("| Press 'g': | = ",end='')
        g = 'g'
        r = input()
        if(r==g):
            plt.figure(figsize=[10,5],dpi = 100)
            plt.title('Accuracy Comparison')
            plt.xlabel('Accuracy')
            plt.ylabel('Algorithm')
            sns.barplot(x = acc,y = model,palette='dark')
            plt.show()
        else:
            print("!!!!Error!!!!")
    
    elif(ch==3):
        import matplotlib.pyplot as plt
        import numpy as np
        myexplode = [0,0.1,0,0,0.1]
        y = acc
        mylabels = model
        plt.title("Accuracy Piechart")
        plt.pie(y,labels = mylabels,startangle = 90,shadow = True,explode = myexplode)
        plt.legend(title = "Accuracy:")
        plt.show() 
            
    elif(ch==4):
        print("\nDataset of 'Crop Recommendation:")
        print("-------------------------------------------------------------------")
        print(df)
        print("-------------------------------------------------------------------")
        
    elif(ch==5):
        print("Size of dataset used is:",end='')
        print(df.size)
        print("------------------------------------")
        
    elif(ch==6):
        print("Dataset used contains respective rows & columns")
        print(df.shape)
        print("------------------------------------")
        
    elif(ch==7):
        print("Do you really want to exit 'Y/N':",end='')
        a = input()
        y = 'y'
        n = 'n'
        
        if(a==y):
            print("===========Thank You=============")
            break
        elif(a==n):
            continue
        
    else:
        print("================Oops Wrong choice is enter===============")
        
