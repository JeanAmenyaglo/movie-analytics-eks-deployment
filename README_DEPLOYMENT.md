# 📘 **README_DEPLOYMENT.md**  
### *Full Deployment Guide: Flask API + Jupyter Notebook (Movies Dataset)*

---

# 🎬 **Project Overview**

This project contains two applications built around the same movies dataset:

### **1. Flask API (question_1_flask)**
A lightweight REST API that:
- Loads a CSV dataset using pandas  
- Exposes `/movies` endpoint  
- Supports filtering by:
  - `movie_rated` (exact match)
  - `director` (partial match)

### **2. Jupyter Notebook (question_2_jupyter_pandas)**
A data analysis environment that:
- Loads the same dataset  
- Performs filtering, sorting, and visualization  
- Generates bar charts  
- Demonstrates boolean indexing and pandas fundamentals  

Both applications are fully containerized using Docker and orchestrated with Docker Compose.

This guide explains **every way to run, deploy, and automate** the project — from local development to Kubernetes and CI/CD.

---

# 🧱 **1. Prerequisites**

Before running anything, install:

- **Docker Desktop**  
- **Git**  
- **Python 3.11+** (optional for local runs)  
- **kubectl** (for Kubernetes section)  
- **minikube** (optional local Kubernetes cluster)

---

# 🧪 **2. Running the Applications Locally (Without Docker)**

This section is for beginners or instructors reviewing the assignment.

---

## **Flask API (question_1_flask)**

### Create and activate a virtual environment:
```bash
cd question_1_flask
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the API:
```bash
python movie_app.py
```

### Access:
```
http://localhost:5000
```

---

## **Jupyter Notebook (question_2_jupyter_pandas)**

### Create and activate a virtual environment:
```bash
cd question_2_jupyter_pandas
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Start Jupyter:
```bash
jupyter lab
```

---

# 🐳 **3. Running the Applications with Docker**

This is the recommended way to run the project.

---

## **Build the images**
```bash
docker-compose build
```

## **Run the containers**
```bash
docker-compose up
```

## **Access the applications**

| Service | URL |
|--------|-----|
| Flask API | http://localhost:5000 |
| JupyterLab | http://localhost:8888 |

---

# 📦 **4. Docker Hub Images**

Images are published under your Docker Hub account:

- Flask API:  
  ```
  jeankoku/flask_app:v1
  ```

- Jupyter App:  
  ```
  jeankoku/jupyter_app:v1
  ```

# 🚀 **5. GitHub Actions CI/CD (Automated Builds + Automated Deployment)**

This project now includes **three separate GitHub Actions workflows**, each with a clear purpose:

### **1. `deploy-docker.yml` — CI: Build & Push Docker Images**
- Builds **both** Docker images (Flask + Jupyter)
- Pushes them to Docker Hub
- Triggered on push to `main`

### **2. `deploy-flask.yml` — CD: Deploy Flask to AWS EKS**
- Builds Flask image
- Pushes to Docker Hub with commit SHA tag
- Updates the Flask Deployment in AWS EKS
- Rolls out the new version automatically

### **3. `deploy-jupyter.yml` — CD: Deploy Jupyter to AWS EKS**
- Builds Jupyter image
- Pushes to Docker Hub with commit SHA tag
- Updates the Jupyter Deployment in AWS EKS
- Rolls out the new version automatically

---

## **Required GitHub Secrets**

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `AWS_ACCESS_KEY_ID` | IAM access key |
| `AWS_SECRET_ACCESS_KEY` | IAM secret key |
| `AWS_REGION` | Example: `ca-central-1` |
| `EKS_CLUSTER_NAME` | Your EKS cluster name |

---

# ☸️ **6. Kubernetes Deployment (Local Minikube + AWS EKS)**

This project supports **two Kubernetes environments**:

- **Local Minikube** (NodePort)
- **AWS EKS** (LoadBalancer)

---

## **Flask Deployment (AWS EKS)**

`flask-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask
  template:
    metadata:
      labels:
        app: flask
    spec:
      containers:
      - name: flask
        image: jeankoku/flask_app:v1
        ports:
        - containerPort: 5000
```

`flask-service.yaml` (AWS version):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  type: LoadBalancer
  selector:
    app: flask
  ports:
    - port: 5000
      targetPort: 5000
```

After applying:

```
kubectl get svc flask-service
```

You will receive a public AWS LoadBalancer URL:

```
http://<elb-url>:5000
```

---

## **Jupyter Deployment (AWS EKS)**

`jupyter-deployment.yaml` (token disabled):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jupyter-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jupyter
  template:
    metadata:
      labels:
        app: jupyter
    spec:
      containers:
      - name: jupyter-app
        image: jeankoku/jupyter_app:v1
        ports:
        - containerPort: 8888
        args:
          - "jupyter"
          - "lab"
          - "--ip=0.0.0.0"
          - "--no-browser"
          - "--allow-root"
          - "--NotebookApp.token=''"
          - "--NotebookApp.password=''"
```

`jupyter-service.yaml` (AWS version):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: jupyter-service
spec:
  type: LoadBalancer
  selector:
    app: jupyter
  ports:
    - port: 8888
      targetPort: 8888
```

After applying:

```
kubectl get svc jupyter-service
```

Access Jupyter at:

```
http://<elb-url>:8888/lab
```

---

# ☁️ **7. AWS EKS Deployment (Cloud Deployment)**

This project now supports **full cloud deployment** using:

- Docker Hub (image registry)
- AWS EKS (Kubernetes cluster)
- AWS LoadBalancer (public access)
- GitHub Actions (CI/CD automation)

### Deployment Flow:

1. Push code to `main`
2. GitHub Actions builds Docker images
3. Images pushed to Docker Hub
4. GitHub Actions updates EKS Deployments
5. Kubernetes rolls out new pods
6. AWS LoadBalancer exposes both apps publicly

---

# 🧩 **8. Architecture Diagram**

```
                   +-----------------------+
                   |     GitHub Repo       |
                   +-----------+-----------+
                               |
                               | Push to main
                               v
        +-----------------------------------------------+
        |           GitHub Actions Workflows            |
        |-----------------------------------------------|
        | deploy-docker.yml  | Build & Push Images      |
        | deploy-flask.yml   | Deploy Flask to EKS      |
        | deploy-jupyter.yml | Deploy Jupyter to EKS    |
        +-----------+-----------+-----------+-----------+
                                |
                                | Docker Hub Push
                                v
                   +-----------------------+
                   |     Docker Hub        |
                   +-----------+-----------+
                               |
                               v
                   +-----------------------+
                   |       AWS EKS         |
                   |  (Kubernetes Cluster) |
                   +-----------+-----------+
                               |
               +---------------+----------------+
               |                                |
               v                                v
   +-----------------------+        +-----------------------+
   | Flask Deployment      |        | Jupyter Deployment    |
   | LoadBalancer Service  |        | LoadBalancer Service  |
   +-----------------------+        +-----------------------+
   | Public URL (5000)     |        | Public URL (8888/lab) |
   +-----------------------+        +-----------------------+
```

---

# 🎉 **Conclusion (Updated)**

This project now demonstrates **end‑to‑end DevOps engineering**, including:

- Local development  
- Docker + Docker Compose  
- Docker Hub publishing  
- GitHub Actions CI/CD  
- Kubernetes (Minikube + AWS EKS)  
- AWS LoadBalancer exposure  
- Automated deployments for Flask + Jupyter  
- Clean workflow separation  
- Professional architecture documentation  
