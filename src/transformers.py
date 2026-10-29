
import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import rbf_kernel


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_add=None):
        self.features_to_add = features_to_add

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        if "bed_room" in (self.features_to_add or []):
            X["bed_room"] = (
                X["AveBedrms"] /
                X["AveRooms"].replace(0, np.nan)
            )

        if "room_per_person" in (self.features_to_add or []):
            X["room_per_person"] = (
                X["AveRooms"] /
                X["AveOccup"].replace(0, np.nan)
            )

        if "incpop_ratio" in (self.features_to_add or []):
            X["incpop_ratio"] = (
                X["MedInc"] /
                X["Population"].replace(0, np.nan)
            )

        if "lat_long" in (self.features_to_add or []):
            X["lat_long"] = X["Latitude"] + X["Longitude"]

        if "latlong_ratio" in (self.features_to_add or []):
            X["latlong_ratio"] = (
                X["Latitude"] /
                X["Longitude"].replace(0, np.nan)
            )

        return X


class ClusterSimilarity(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        n_clusters=10,
        gamma=1.0,
        random_state=42
    ):
        self.n_clusters = n_clusters
        self.gamma = gamma
        self.random_state = random_state

    def fit(self, X, y=None):
        self.kmeans_ = KMeans(
            n_clusters=self.n_clusters,
            random_state=self.random_state,
            n_init=10
        )
        self.kmeans_.fit(X)
        self.kmeans_cluster_centers_ = (
            self.kmeans_.cluster_centers_
        )
        return self

    def transform(self, X):
        return rbf_kernel(
            X,
            self.kmeans_cluster_centers_,
            gamma=self.gamma
        )

    def get_feature_names_out(self, input_features=None):
        return [
            f"Cluster {i} similarity"
            for i in range(self.n_clusters)
        ]
