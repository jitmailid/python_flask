<!-- Here's a step-by-step guide to set up and deploy a Python Flask "Hello World" API on a Kubernetes cluster using Docker and Minikube, all with free tools. -->


# python_flask

# Flask tutorial :

https://www.youtube.com/watch?v=Z1RJmh_OqeA

Here's a step-by-step guide to set up and deploy a Python Flask "Hello World" API on a Kubernetes cluster using Docker and Minikube, all with free tools.

## Step 1: Prerequisites
Ensure you have the following installed:

Docker: For building images.
Minikube: To create a local Kubernetes cluster.
kubectl: Kubernetes command-line tool for managing the cluster.
Python: To write the Flask API.

Install Flask
<!-- https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download

curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube

~/Downloads/start_wroking_from_here/python_project_ci_cd > minikube start 

~/Downloads/start_wroking_from_here/python_project_ci_cd > minikube status
~/Dow/start_wroking_from_here/python_project_ci_cd > kubectl version



![alt text](image.png)
flask installed in my local ------->
<!-- python3 -m pip install flask
--->

# If you can see the docker image is getting created from docker file and uploaded to dockerhub
~/Dow/s/p/python_flask/flask-docker-app master !1 ?2 > docker build -t flask-docker-app

~/Dow/s/p/python_flask/flask-docker-app master !1 ?2 > docker run -p 5001:5001 flask-docker-app    


# For Kubernets deployment :::
flask-k8s/
├── helloflask.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
├── service.yaml


