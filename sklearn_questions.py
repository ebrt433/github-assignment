"""Assignment - making a sklearn estimator.

The goal of this assignment is to implement by yourself a scikit-learn
estimator for the OneNearestNeighbor and check that it is working properly.

The nearest neighbor classifier predicts for a point X_i the target y_k of
the training sample X_k which is the closest to X_i. We measure proximity with
the Euclidean distance. The model will be evaluated with the accuracy (average
number of samples corectly classified). You need to implement the `fit`,
`predict` and `score` methods for this class. The code you write should pass
the test we implemented. You can run the tests by calling at the root of the
repo `pytest test_sklearn_questions.py`.

We also ask to respect the pep8 convention: https://pep8.org. This will be
enforced with `flake8`. You can check that there is no flake8 errors by
calling `flake8` at the root of the repo.

Finally, you need to write docstring similar to the one in `numpy_questions`
for the methods you code and for the class. The docstring will be checked using
`pydocstyle` that you can also call at the root of the repo.
"""
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import check_classification_targets


class OneNearestNeighbor(BaseEstimator, ClassifierMixin):
    """OneNearestNeighbor classifier."""

    def __init__(self):
        """Initialize the OneNearestNeighbor classifier."""
        pass

    def fit(self, X, y):
        """
        Fit the model using X as training data and y as target values.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data.
        y : array-like of shape (n_samples,)
            Target values.

        Returns
        -------
        self : object
            Returns self.
        """
        X, y = check_X_y(X, y)
        check_classification_targets(y)
        self.X_ = X
        self.y_ = y
        return self

    def predict(self, X):
        """
        Predict the class labels for the provided data.

        Parameters
        ----------
        X : array-like of shape (n_queries, n_features)
            Test samples.

        Returns
        -------
        y_pred : array of shape (n_queries,)
            Class labels for each data sample.
        """
        # This line also needs to be indented to be part of the predict method
        check_is_fitted(self, ['X_', 'y_'])
        X = check_array(X)

        y_pred = []
        for x in X:
            distances = np.sqrt(np.sum((self.X_ - x) ** 2, axis=1))
            nearest_neighbor = np.argmin(distances)
            y_pred.append(self.y_[nearest_neighbor])

        return np.array(y_pred)

    def score(self, X, y):
        """
        Return the mean accuracy on the given test data and labels.

        Parameters
        ----------
        X : array-like of shape (n_queries, n_features)
            Test samples.
        y : array-like of shape (n_queries,)
            True labels for X.

        Returns
        -------
        score : float
            Mean accuracy of self.predict(X) wrt. y.
        """
        # This line also needs to be indented to be part of the score method
        X, y = check_X_y(X, y)
        y_pred = self.predict(X)
        return np.mean(y_pred == y)
