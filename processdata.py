import sys
from sklearn import tree
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB
import pickle
#import graphviz

f = open(sys.argv[1],"r")
if f.mode != "r":
	print("Failed to open file")
	exit()
lines = f.read()
lines = lines.split()
count = 0
for i in lines:
	if i[0].isalpha():
		count += 1
entries = []
for x in range(0,count):
	entries.append(lines[(x*76):(76*x)+76])
index = [3,4,9,10,12,16,19,32,38,40,41,44,51,58]
feature_names = ["Age","Sex","CP","Trestbps","Chol","Fbs","Restecg","Thalach","Exang","Oldpeak","Slope","Ca","Thal"]
class_names = ["No","Yes"]
samples = []
class_data = []
for i in entries:
	sample = []
	for j, val in enumerate(i):
		if any(j == (t-1) for t in index):
			if j == 57:
				if val == "0":
					class_data.append(0.0)
				else:
					class_data.append(1.0)
			else:
				sample.append(float(val))
	samples.append(sample)
for index, i in enumerate(samples):
	print(i,class_data[index])
for i in samples:
	print(i)
print(class_data)
#for i in samples:
#	print(i)
#print(str(class_data))
x_train, x_test, y_train, y_test = train_test_split(samples,class_data,test_size=0.10,random_state=0)
print("Sample Count - %i" % len(class_data))
print("Data Count - %i" % len(x_train))
print("Test Data Count - %i" % len(x_test))

for index,i in enumerate(x_test):
	print(i,y_test[index])

print("Decision Tree Method")
clf = tree.DecisionTreeClassifier(criterion="entropy",splitter="random",random_state=0)
clf = clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("Naive Bayes - Gaussian Method")
gnb = GaussianNB()
gnb.fit(x_train,y_train)
y_pred = gnb.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("K-Nearest Neighbors Method - Without Standardization")
classifier = KNeighborsClassifier(n_neighbors=15)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

print("K-Nearest Neighbors Method - With Standardization")
classifier = KNeighborsClassifier(n_neighbors=15)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("Support Vector Machine Method")
svc = SVC(kernel="linear")
svc.fit(x_train,y_train)
y_pred = svc.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
model_filename = "trained_svm_model.pkl"
with open(("django/hdsite/"+model_filename), 'wb') as file:
	pickle.dump(svc, file)
