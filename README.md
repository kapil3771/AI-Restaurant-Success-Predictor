# 🍽️ AI-Powered Restaurant Success Predictor

A production-ready **Machine Learning application** that predicts whether a restaurant is likely to succeed and estimates the approximate cost for two, based on location, cuisine, restaurant type, and user engagement data.

This project is **Dockerized** for easy execution on any machine without local Python or dependency setup.

---

## 🚀 Run with Docker (Recommended)

The easiest and recommended way to use this project is via Docker.

### Prerequisite
- Docker installed

### Run
```bash
docker pull kapil9123/restaurant-predictor:1.0.0

docker run -d \
  -p 8501:8501 \
  --name restaurant_app \
  kapil9123/restaurant-predictor:1.0.0
```

Open in browser:
http://localhost:8501

### Stop
```bash
docker stop restaurant_app
docker rm restaurant_app
```

---

## ✨ Features

- Real-world restaurant data (Zomato)
- Feature engineering & encoding
- Machine Learning models:
  - Classification (Success / Failure)
  - Regression (Cost estimation)
- Interactive Streamlit UI
- Visual analytics using Plotly & Altair
- Fully containerized & portable

---

## 🧠 Machine Learning Models

- Classifier: RandomForestClassifier  
  Predicts whether a restaurant is likely to succeed

- Regressor: RandomForestRegressor  
  Estimates approximate cost for two people

---

## 📦 Project Structure (GitHub)

```
AI-Restaurant-Success-Predictor/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.sh
├── README.md
├── LICENSE
└── .gitignore
```

Trained ML models and datasets are **not stored in this repository** due to size constraints.  
They are bundled securely inside the Docker image.

---

## ⚠️ Why Models & Dataset Are Not in GitHub

- GitHub has file size limits
- ML artifacts are runtime assets, not source code
- Docker image is the deployable artifact

---

## 🛠 Local Development (Optional)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Requires Python 3.10+ and trained models.

---

## ⚖ License

This project is licensed under the MIT License.

---

## 👤 Author

Kapil Pravin Marathe  
GitHub: https://github.com/kapil3771

---

## 🙏 Credits

Zomato Dataset  
Scikit-learn  
Pandas & NumPy  
Streamlit  
Plotly & Altair
