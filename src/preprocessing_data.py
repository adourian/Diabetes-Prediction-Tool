import joblib
from helpers import create_cluster_indicators, create_interaction_features

def preprocess(data):
    """
    Preprocess the input data by applying scaling, creating interaction features, and generating cluster indicators.

    Parameters:
    - data: pandas DataFrame with the features to preprocess.

    Returns:
    - pandas DataFrame with all preprocessing steps applied.
    """
    # Load saved preprocessing objects
    scaler = joblib.load('models/scaler.pkl')
    centroids = joblib.load('models/cluster_centroids.pkl')
    fitted_kmeans = joblib.load('models/fitted_kmeans.pkl')

    # Define feature sets for cluster indicators
    feature_sets = [
        (['Glucose', 'DiabetesPedigreeFunction'], [8], [2, 6]),
        (['Glucose', 'SkinThickness'], [3], [5, 9]),
        (['Glucose', 'Pregnancies'], [7], [2, 8]),
        (['Glucose', 'BloodPressure'], [], [1, 8]),
        (['Glucose', 'BMI'], [9], [1]),
        (['Glucose', 'Age'], [6], [2, 7]),
        (['Pregnancies', 'BMI'], [6], []),
        (['Pregnancies', 'SkinThickness'], [9], []),
        (['BloodPressure', 'SkinThickness'], [2], []),
        (['BloodPressure', 'BMI'], [7], []),
        (['SkinThickness', 'DiabetesPedigreeFunction'], [8], []),
        (['SkinThickness', 'BMI'], [6], []),
        (['SkinThickness', 'Age'], [2], []),
        (['BMI', 'Age'], [3], []),
    ]

    # Step 1: Scale features
    columns_to_scale = data.columns.difference(['Outcome'])
    data[columns_to_scale] = scaler.transform(data[columns_to_scale])

    print("Step 1: Scaling applied.")

    # Step 2: Create cluster indicators
    data = create_cluster_indicators(data, centroids, fitted_kmeans, feature_sets)
    print("Step 2: Cluster indicators created.")

    # Step 3: Create interaction features
    interaction_columns = ['Glucose', 'DiabetesPedigreeFunction', 'BMI']
    data = create_interaction_features(data, interaction_columns)
    print("Step 3: Interaction features created.")

    

    return data