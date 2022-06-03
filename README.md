# PROJECT
## Automating new credit card/loan applications approvals using Machine Learning
### Introduction
Machine Learning, ML is becoming an integral part of all modern organization. In the finance setor, ML can be used to detect fraud, automate approval processes and trading activities, and provide financial advisory services to investors.

## Objectives of the Project
1. Automate approval process of new credit cards/loan applications
2. Provide web-based application interface for our customers
3. Provide instant feedback to customers
4. Collect new data for future system improvements

## Data Source
Project uses an open-source dataset from Kaggle found on this link
https://www.kaggle.com/rikdifos/credit-card-approval-prediction/tasks?taskId=1416

<!-- ## How to deploy the app
#### start minikube
```
minikube start
```

#### Get secrets specified as base64

```
echo -n myKUBEcluster | base64
```
#### Apply the secrets
```
kubectl apply -f secrets.yml
```
#### Confirm secrets are applied
```
kubectl get secret
```

#### Create a persistent volume file (persistent-volume.yml) and add it to the cluster
```
kubectl apply -f persistent-volume.yml
```
#### confirm volume has been created
```
kubectl describe pv mysql-pv-volume
```

#### Pull the latest MySQL
```
docker pull mysql
```

#### Create the mysql-deployment.yml file describing the deployment and services
#### Deploy the mysql server
```
kubectl apply -f mysql-deployment.yml
```

#### Check if pod is running
```
kubectl get pods
```

#### Deploying the API
#### Copy app file (flaskapp.py) and dockerfile into your directory
```
eval $(minikube docker-env)
```

#### Build docker image
```
docker build -t flask-api .
```

#### Deploy flaskapp-service
```
kubectl apply -f flaskapp-deployment.yml
```

#### Confirm all pods are running
```
kubectl get pods
```

#### Check the service and url
```
minikube service flask-service
```
 -->
