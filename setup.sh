#!/bin/bash

echo "🚀 Starting Setup..."

# 1️⃣ Start Minikube
echo "🟢 Starting Minikube..."
minikube start

# 2️⃣ Build Docker Images
echo "🐳 Building Docker Images..."
docker build -t fastapi-backend -f backend/app/Dockerfile .
docker build -t celery-worker -f backend/app/Dockerfile.celery .
docker build -t my-frontend-image -f Dockerfile.frontend .

# 3️⃣ Load Images into Minikube
echo "📦 Loading Images into Minikube..."
minikube image load fastapi-backend
minikube image load celery-worker
minikube image load my-frontend-image

# 4️⃣ Deploy Kubernetes Resources
echo "🚀 Deploying to Kubernetes..."
kubectl apply -f k8s/

echo "✅ Deployment Complete!"

# 5️⃣ Wait for Pods to Be Ready
echo "⏳ Waiting for Pods to be ready..."
kubectl wait --for=condition=available --timeout=90s deployment/fastapi
kubectl wait --for=condition=available --timeout=90s deployment/frontend

# 6️⃣ Expose Services & Get URLs
echo "🌍 Getting URLs for FastAPI & Frontend..."
FRONTEND_URL=$(minikube service frontend-service --url)
FASTAPI_URL=$(minikube service fastapi --url)

echo "🖥️ FastAPI is running at: $FASTAPI_URL"
echo "🌍 Frontend is running at: $FRONTEND_URL"

echo "🎉 Setup Complete! Open the frontend in your browser: $FRONTEND_URL"
