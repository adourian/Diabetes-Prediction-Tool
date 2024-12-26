# Diabetes Prediction Tool

This repository is my attempt to toy around with **Streamlit** and explore building simple interactive applications for machine learning models. The project focuses on predicting the probability of diabetes based on user inputs. It's nothing fancy, just a small side project to learn and have fun!

---

## Background

The tool uses data from the `diabetes.csv` dataset to predict the likelihood of diabetes. The underlying models include an ensemble of **XGBoost**, **LightGBM**, and **Logistic Regression**, which have been trained and optimized using various techniques like feature engineering, clustering, and hyperparameter tuning. The focus is on providing interpretable and actionable predictions.

---

## Features

- **Interactive Interface**: A user-friendly Streamlit app for predicting diabetes probability.
- **Ensemble Model**: Combines XGBoost, LightGBM, and Logistic Regression for robust predictions.
- **Real-time Inputs**: Accepts user inputs and instantly displays results.

---

## How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/adourian-Diabetes-Prediction-Tool.git
   cd adourian-Diabetes-Prediction-Tool
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run src/main.py
   ```

4. **Access the app**:
   Open your browser and navigate to `http://localhost:8501`.

---

## Folder Structure

```plaintext
adourian-Diabetes-Prediction-Tool/
├── images/                # Placeholder for app screenshots
├── data/                  # Dataset used for training
│   └── diabetes.csv
├── models/                # Saved models and preprocessing artifacts
├── requirements.txt       # Python dependencies
├── LICENSE                # License information
├── README.md              # This file
├── notebook.ipynb         # Jupyter notebook for EDA and modeling
└── src/                   # Source code for the app
    ├── main.py            # Streamlit app code
    ├── make_predictions.py  # Functions for model predictions
    ├── helpers.py         # Helper functions
    └── preprocessing_data.py  # Data preprocessing steps
```

---

## App Preview

![App Screenshot](images/app_screenshot.png)

---

## Models Used

1. **XGBoost**:
   - Handles non-linear relationships well.
   - Optimized using `xgb_params.pkl`.

2. **LightGBM**:
   - Fast and efficient gradient boosting framework.
   - Feature set stored in `lgb_features.pkl`.

3. **Logistic Regression**:
   - Provides interpretable baseline predictions.
   - Preprocessed data scaled using `scaler.pkl`.

The ensemble combines predictions using weights stored in `ensemble_weights.pkl`.

---

## Next Steps

- Experiment with additional datasets to generalize predictions.
- Improve app aesthetics and user experience.
- Add model interpretability features like SHAP visualizations.

---

## License

This project is licensed under the [MIT License](LICENSE).
