# 🏦 Bank Churn Prediction App

This is a simple **Bank Churn Prediction Web App** built using **Streamlit** and a pre-trained **Gradient Boosting Classifier**. It predicts whether a bank customer is likely to churn (exit) based on user-input data.

## 🚀 Features

- Predicts customer churn using input features like Credit Score, Age, Balance, etc.
- Interactive UI built with Streamlit.
- Loads a serialized machine learning model (`model.pkl`) for prediction.
- Handles categorical variables (Gender, Geography) with mapping.
- Easy-to-use sliders and dropdowns for data input.

## 📊 Input Features

- Credit Score
- Age
- Gender (Male/Female)
- Tenure (Years with the bank)
- Balance
- Number of Products
- Has Credit Card (0 or 1)
- Is Active Member (0 or 1)
- Estimated Salary
- Geography (France, Germany, Spain)

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/bank-churn-prediction-app.git
cd bank-churn-prediction-app
pip install -r requirements.txt
```

Make sure the following files are present:
- `model.pkl` : Trained GradientBoostingClassifier model.
- `X.csv` : A CSV file containing training feature columns (used for aligning input columns).

## 📦 Run the App

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501`.

## 📁 Project Structure

```
bank-churn-prediction-app/
│
├── app.py                # Main Streamlit app
├── model.pkl             # Trained model file
├── X.csv                 # CSV with feature columns
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 💡 Example Output

- ✅ **Not Exited** — The customer is predicted to stay.
- ❌ **Exited** — The customer is predicted to churn.

## ✨ Requirements

- Python 3.7+
- Streamlit
- scikit-learn
- pandas

## 📬 Contact

For any questions, feel free to reach out via adarshai5770@gmail.com] or open an issue in the repository.

---

**Enjoy predicting churns! 🎉**
```
