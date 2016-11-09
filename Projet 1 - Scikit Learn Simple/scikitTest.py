from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# import some data to play with
iris = datasets.load_iris()

X = iris.data  # we only take the first two features.
Y = iris.target

clf=RandomForestClassifier()

clf.fit(X,Y)

def scoringIris(event, context):
    return clf.score(X,Y)