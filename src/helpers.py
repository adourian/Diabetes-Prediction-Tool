import pandas as pd

def create_cluster_indicators(data, centroids, fitted_kmeans, feature_sets):
    """
    Create binary indicators for cluster memberships based on predefined cluster sets for each pair of features.
    Also creates global summary indicators for positive and negative clusters across all feature pairs.

    Parameters:
    - data: pandas DataFrame with the feature columns used for clustering.
    - centroids: dict mapping (feature1, feature2) tuples to cluster centroids.
    - fitted_kmeans: dict mapping (feature1, feature2) tuples to fitted KMeans instances.
    - feature_sets: list of tuples where each tuple contains:
        - A list of two features.
        - A list of negative cluster indices.
        - A list of positive cluster indices.

    Returns:
    - pandas DataFrame with the original data plus the new cluster indicator features and global summary indicators.
    """
    new_features = pd.DataFrame(index=data.index)
    pos_indicator_cols = []
    neg_indicator_cols = []

    for feature_pair, negative_clusters, positive_clusters in feature_sets:
        feature_pair_key = tuple(feature_pair)
        if feature_pair_key not in centroids or feature_pair_key not in fitted_kmeans:
            continue

        centroids_pair = centroids[feature_pair_key]
        kmeans = fitted_kmeans[feature_pair_key]

        # Extract and scale feature data
        feature_data = data[feature_pair]

        # Predict cluster labels using the fitted KMeans model
        cluster_labels = kmeans.predict(feature_data)

        # Create binary indicators for positive and negative clusters
        if positive_clusters:
            for cluster_idx in positive_clusters:
                col_name = f"Pos_Cluster_{'_'.join(feature_pair)}_{cluster_idx}"
                new_features[col_name] = (cluster_labels == cluster_idx).astype(int)
                pos_indicator_cols.append(col_name)

        if negative_clusters:
            for cluster_idx in negative_clusters:
                col_name = f"Neg_Cluster_{'_'.join(feature_pair)}_{cluster_idx}"
                new_features[col_name] = (cluster_labels == cluster_idx).astype(int)
                neg_indicator_cols.append(col_name)

    # Create global summary indicators
    if pos_indicator_cols:
        new_features["Sum_Pos_2D_Indicators"] = new_features[pos_indicator_cols].sum(axis=1)

    if neg_indicator_cols:
        new_features["Sum_Neg_2D_Indicators"] = new_features[neg_indicator_cols].sum(axis=1)

    return pd.concat([data, new_features], axis=1)


def create_interaction_features(df, features):
    for i in range(len(features)):
        for j in range(i+1, len(features)):
            df[f'{features[i]}_x_{features[j]}'] = df[features[i]] * df[features[j]]
    return df

