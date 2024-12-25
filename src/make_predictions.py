import joblib
import pandas as pd
from preprocessing_data import preprocess

def load_models():
    """
    Load the trained models, weights, and feature names from disk.

    Returns:
    - models: dict containing the loaded models.
    - ensemble_weights: dict containing the weights for the weighted average ensemble.
    - model_features: dict mapping each model to its required features.
    """
    print("Loading models, weights, and feature names...")
    xgb_model = joblib.load('models/xgb_model.pkl')
    lgb_model = joblib.load('models/lgb_model.pkl')
    lr_model = joblib.load('models/lr_model.pkl')
    ensemble_weights = joblib.load('models/ensemble_weights.pkl')

    # Load feature names for each model
    xgb_features = joblib.load('models/xgb_features.pkl')
    lgb_features = joblib.load('models/lgb_features.pkl')
    lr_features = joblib.load('models/lr_features.pkl')

    models = {
        'xgb': xgb_model,
        'lgb': lgb_model,
        'lr': lr_model
    }

    model_features = {
        'xgb': xgb_features,
        'lgb': lgb_features,
        'lr': lr_features
    }

    return models, ensemble_weights, model_features


def make_prediction(input_data):
    """
    Preprocess the input data and make predictions using the ensemble model.

    Parameters:
    - input_data: pandas DataFrame containing the input features.

    Returns:
    - prediction: The final binary prediction (0 or 1).
    - probability: The final predicted probability for the positive class.
    """
    # Step 1: Preprocess the input data
    print("Preprocessing input data...")
    preprocessed_data = preprocess(input_data)

    # Step 2: Load models, weights, and model-specific features
    models, ensemble_weights, model_features = load_models()

    # Step 3: Extract and align features for each model
    print("Aligning features for each model...")
    X_xgb = preprocessed_data.reindex(columns=model_features['xgb'], fill_value=0)
    X_lgb = preprocessed_data.reindex(columns=model_features['lgb'], fill_value=0)
    X_lr = preprocessed_data.reindex(columns=model_features['lr'], fill_value=0)

    # Step 4: Get predictions from individual models
    print("Getting predictions from individual models...")
    preds_xgb = models['xgb'].predict_proba(X_xgb)[:, 1]
    preds_lgb = models['lgb'].predict_proba(X_lgb)[:, 1]
    preds_lr = models['lr'].predict_proba(X_lr)[:, 1]

    # Step 5: Compute weighted average of probabilities
    total_weight = sum(ensemble_weights.values())
    final_probability = (
        ensemble_weights['weight_xgb'] / total_weight * preds_xgb +
        ensemble_weights['weight_lgb'] / total_weight * preds_lgb +
        ensemble_weights['weight_lr'] / total_weight * preds_lr
    )

    # Step 6: Convert probability to binary prediction
    final_prediction = (final_probability > 0.5).astype(int)

    return final_prediction, final_probability