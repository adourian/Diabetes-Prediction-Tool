# Diabetes Prediction Tool

I recently came across Streamlit, a tool designed for building interactive web apps with minimal code. I wanted to try it out, so I took on a small project to test how it could be used to create simple end-to-end solutions with low-code. I was curious to see how easy it would be to go from an idea to something functional without spending hours on setup or front-end work.

I decided to build an interactive tool to predict the probability of diabetes based on user inputs. It felt like a practical and relatable use case—perfect for exploring Streamlit's capabilities while creating something functional and user-friendly.

The project involved taking a simple dataset, experimenting with feature engineering and clustering, and building an ensemble model combining XGBoost, LightGBM, and Logistic Regression. The result is a Streamlit app that allows users to input their data and instantly see predictions, making inference very easy.

This project is by no means a polished product; it's a fun experiment, a tinkering session to learn and explore.

---

## Background

The tool uses data from the Pima Indians dataset (`diabetes.csv`) to predict the likelihood of diabetes. The underlying models include an ensemble of **XGBoost**, **LightGBM**, and **Logistic Regression**, which have been trained and optimized using various techniques like feature engineering, clustering, and hyperparameter tuning. The focus is on providing interpretable and actionable predictions.

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

![App Screenshot](images/app_screenshot.PNG)

---

## Models Used

This project just uses a few plain, good old-fashioned machine learning models combined in an ensemble to provide predictions. Simple often does the job. A bit of clustering-based feature engineering was also thrown in to improve performance. The actual ML work was done in the `notebook.ipynb` file.

- **XGBoost**:
  - Handles non-linear relationships effectively.
  - Optuna to tune parameters, saved in `xgb_params.pkl`.

- **LightGBM**:
  - A fast and efficient gradient boosting framework.
  - Optuna to tune parameters, saved in `lgb_params.pkl`.

- **Logistic Regression**:
  - Serves as an interpretable baseline model.
  - Input data is scaled using a pre-fitted scaler saved in `scaler.pkl`.

In addition, a k-means clustering approach was used during feature engineering to create positive and negative diabetes indicators based on cluster centroids. The ensemble model combines predictions from all three models, using weights optimized and stored in `ensemble_weights.pkl`.

Recall was prioritized as a metric to avoid false negatives.

---

## License

This project is licensed under the [MIT License](LICENSE).
