# FastAPI + Celery + Vue + Kubernetes (Minikube)

This project is a **full-stack** application using:

- **FastAPI** (Python backend)
- **Celery** (Task queue for CPU-intensive jobs)
- **Redis** (Broker for Celery)
- **Vue.js** (Frontend)
- **Kubernetes + Minikube** (Container orchestration)

## Prerequisites

Before running, ensure you have installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## Quick Start Guide

### 1⃣ **Clone the Repository**

```sh
git clone https://github.com/bahareeskandari/backend-case.git
cd BACKEND-CASE
```

### 2⃣ **Start Minikube**

```sh
minikube start
```

### 3⃣ **Run the Setup Script**

This builds the project, loads images, and deploys everything automatically.

```sh
make setup
```

### 4⃣ **Get Service URLs**

After deployment, Minikube will provide URLs for your services:

```sh
minikube service frontend-service --url
minikube service fastapi --url
```

Copy and paste these into your browser to access the **frontend** and **API**.
