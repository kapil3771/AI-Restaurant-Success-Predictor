# 🍽️ AI-Powered Restaurant Success Predictor

This is an end-to-end **Data Science & Machine Learning** project that predicts whether a restaurant will be successful or not and also estimates using its expected rating using both classification and regression models.

---

## ✨ Features

* ✅ Cleaned and preprocessed real-world dataset (Zomato)
* ✅ Exploratory Data Analysis (EDA) with visualizations
* ✅ Feature Engineering & Encoding
* ✅ Model Building:

  * Classification (Success/Failure)
  * Regression (Rating Prediction)
* ✅ Model Evaluation (Accuracy, Confusion Matrix, MAE, RMSE)
* ✅ Trained and saved models as `.pkl` files
* ✅ `app.py` Streamlit app to load and predict locally

---

## 📁 Project Structure

```
AI-Restaurant-Predictor/
├── app.py                     # Streamlit app to run predictions
├── rf_classifier.pkl          # Trained classifier model (Random Forest)
├── rf_regressor.pkl           # Trained regression model (Random Forest)
├── zomato.csv                 # Dataset used
├── requirements.txt           # Cleaned dependencies
├── LICENSE                    # MIT License
└── README.md                  # This file
```

---

## 🛠 Setup Instructions

## 📥 Download Dataset

Due to GitHub file size limits, the dataset is not included in the repo.

To download:

```bash
bash dataset_download.sh
This will fetch zomato-eda.zip from Kaggle and save it to ~/Downloads.
➡️ Unzip it and copy zomato.csv into the project root before running the app.

1️⃣ **Clone the repo**

```bash
git clone https://github.com/<your-username>/AI-Restaurant-Predictor.git
cd AI-Restaurant-Predictor
```

2️⃣ **Create virtual environment**

```bash
python3 -m venv ml_env
source ml_env/bin/activate  # or .\ml_env\Scripts\activate on Windows
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the app**

```bash
streamlit run app.py
```

---

## 📊 Dataset Info

* Source: Zomato Restaurant Dataset
* Includes features like:

  * Online Order, Book Table, Location, Cuisines, Votes, Rating, etc.

---

## 🧠 Machine Learning Models

* ✅ **Classification:**

  * Model: RandomForestClassifier
  * Target: Whether restaurant is successful (rating > 3.5)
* ✅ **Regression:**

  * Model: RandomForestRegressor
  * Target: Predict the exact rating

---

## ⚖ License

This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

**Kapil Pravin Marathe**
GitHub: [kapil3771](https://github.com/kapil3771)

---

## 🙏 Credits

* Zomato Dataset Source
* Scikit-learn, Pandas, Matplotlib, Seaborn
* Streamlit / CLI Python
