from scipy.spatial.distance import cdist
from scipy.stats import mode
import numpy as np
from um6p_CC_learn.base.base import ClassifierMixin, BaseEstimator

class KNeighborsClassifier(ClassifierMixin, BaseEstimator):
    def __init__(self, n_neighbors=5, metric='euclidean'):
        self.n_neighbors = n_neighbors
        self.metric = metric

    def fit(self, X, y):
        self._fit_X = X
        self._fit_y = y
        self.classes_, self._y = np.unique(y, return_inverse=True)
        self._is_fitted = True
        return self

    def predict(self, X):
        dist_mat = cdist(X, self._fit_X, metric=self.metric)
        neigh_ind = np.argsort(dist_mat, axis=1)[:, :self.n_neighbors]
        neigh_labels = self._y[neigh_ind]
        most_common = mode(neigh_labels, axis=1)[0]
        return self.classes_[most_common.ravel()]

    def predict_proba(self, X):
        dist_mat = cdist(X, self._fit_X, metric=self.metric)
        neigh_ind = np.argsort(dist_mat, axis=1)[:, :self.n_neighbors]
        proba = np.zeros((X.shape[0], len(self.classes_)))
        for i, indices in enumerate(neigh_ind):
            counts = np.bincount(self._y[indices], minlength=len(self.classes_))
            proba[i, :] = counts / self.n_neighbors
        return proba
