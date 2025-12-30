#  AI‑Powered Restaurant Success Predictor (ML + DevOps Project)

A **production‑style Machine Learning application** that predicts:
1. Whether a restaurant is likely to succeed  
2. Estimated cost for two people  

The project demonstrates **end‑to‑end ML DevOps practices** using **Docker, Jenkins, Kubernetes (Minikube), and HPA autoscaling**.

This repository is intentionally structured to reflect **real‑world ML engineering workflows**, not just academic ML notebooks.

---

## 🧠 What This Project Demonstrates (Big Picture)

✔ ML model packaging & inference  
✔ Docker as the deployable artifact (not GitHub)  
✔ CI with Jenkins  
✔ CD to Kubernetes  
✔ Health probes, resource limits, autoscaling  
✔ GitHub as *source of truth*, Docker Registry as *artifact store*  

This is **how ML systems are actually deployed**, scaled, and validated in practice.

---

## 🚀 Quick Start (Recommended: Docker)

### Prerequisite
- Docker installed

### Run Application
```bash
docker pull kapil9123/restaurant-predictor:1.0.0

docker run -d   -p 8501:8501   --name restaurant_app   kapil9123/restaurant-predictor:1.0.0
```

Open:
```
http://localhost:8501
```

### Stop & Cleanup
```bash
docker stop restaurant_app
docker rm restaurant_app
```

---

## 🧠 Machine Learning Models

| Model | Purpose |
|------|--------|
| RandomForestClassifier | Predict restaurant success |
| RandomForestRegressor | Estimate cost for two |

📦 **Model artifacts (`.pkl`) are NOT stored in GitHub**  
They are baked into the Docker image (industry best practice).

---

## 🗂️ Project Structure

```
AI-Restaurant-Success-Predictor/
├── app.py                     # Streamlit ML inference app
├── Dockerfile                 # Image definition
├── docker-compose.yml         # Local multi‑container setup
├── Jenkinsfile                # CI/CD pipeline
├── k8s/
│   ├── deployment.yaml        # Deployment + probes + resources
│   ├── service.yaml           # NodePort service
│   └── hpa.yaml               # Horizontal Pod Autoscaler
├── docs/                      # Assignment proofs & screenshots
├── requirements.txt
├── run.sh
├── README.md
└── LICENSE
```

---

## ⚙️ CI/CD Pipeline (Jenkins)

The Jenkins pipeline performs:

1. Pulls versioned Docker image
2. Deploys to Kubernetes
3. Verifies rollout status
4. Confirms service exposure

### Jenkinsfile 
```groovy
pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                git 'https://github.com/kapil3771/AI-Restaurant-Success-Predictor.git'
            }
        }

        stage('Pull Docker Image') {
            steps {
                sh 'docker pull kapil9123/restaurant-predictor:1.0.0'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl rollout status deployment/restaurant-app
                kubectl get pods
                kubectl get services
                '''
            }
        }
    }
}
```

---

## ☸️ Kubernetes Architecture

### Deployment Features
✔ Rolling updates  
✔ CPU & memory requests/limits (ML‑aware)  
✔ Liveness probe  
✔ Readiness probe  

### Service
- NodePort (Minikube compatible)

### Autoscaling (HPA)
```yaml
minReplicas: 1
maxReplicas: 5
targetCPUUtilizationPercentage: 60
```

The app **automatically scales under CPU load** and scales back down when idle.

---

## 📈 Autoscaling Demo (What Was Proven)

- Artificial CPU load injected into pod
- HPA detected CPU > 60%
- Replica count increased automatically
- Pods terminated once load stopped


---

## 📌 Why Models & Dataset Are NOT in GitHub

This is **intentional and correct**:

- GitHub ≠ artifact store
- ML models are runtime assets
- Docker image is the immutable deployable unit

**This matches real production ML systems.**

---

## 🧪 Local Development (Optional)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Requires trained model files locally.

---

## 👤 Author

**Kapil Pravin Marathe**  
GitHub: https://github.com/kapil3771

---

## ⚖ License
MIT License
