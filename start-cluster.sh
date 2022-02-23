#!/bin/bash
# delete cluster
#minikube delete --all

# Start minikube
minikube start

#Get secrets specified as base64
echo -n myKUBEcluster | base64

# Apply the secrets
kubectl apply -f secrets.yml

##Confirm secrets are applied
kubectl get secrets.

# PERSISTENT VOLUME
# We used awsElasticBlockStore 
# Create a persistent volume file (persistent-volume.yml) and add it to the cluster
kubectl apply -f persistent-volume.yml

# Confirm volume has been created
kubectl describe pv mysql-pv-volume

#kubectl describe pvc mysql-pv-claim
#Deploy the MySQL server
#Pull the latest MySQL
docker pull mysql

# Create the mysql-deployment.yml file describing the deployment and services
# Deploy the mysql server
kubectl apply -f mysql-deployment.yml

# Check if pod is running
kubectl get pods

#Create database and table
#Set up a MySQL client
# kubectl run -it --rm --image=mysql --restart=Never mysql-client -- mysql --host mysql --password=<non-decoded-password>
# Press enter to get the MYSQL command line

#Deploying the API
#Replicas => number of deployments
# Copy app file (flaskapp.py) and dockerfile into your directory
# Run command below
eval $(minikube docker-env)

# Build docker image
docker build -t flask-api .

# Deploy flaskapp-service
kubectl apply -f flaskapp-deployment.yml

# Confirm all pods are running
kubectl get pods

# Check the service and url
minikube service flask-service

# OR check all services
#minikube service list
# Confirm all pods are running
#kubectl get pods
