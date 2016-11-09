import cPickle as pickle
from sklearn.ensemble import RandomForestClassifier
import boto3

client = boto3.client('s3',region_name="eu-west-1")
response=client.get_object(Bucket='scikitlearn', Key='iris_clf.pkl')
clf=pickle.loads(response['Body'].read())
    
def scoringIris(event, context):
    
    sepalLength = event['record']['sepalLength']
    sepalWidth = event['record']['sepalWidth']
    petalLength = event['record']['petalLength']
    petalWidth = event['record']['petalWidth']
        
    return "Cette fleur appartient a la categorie :", int(clf.predict([[sepalLength,sepalWidth,petalLength,petalWidth]]))