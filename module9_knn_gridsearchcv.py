import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


def main():
    def read_pairs(num_pairs):
        pairs = []
        for _ in range(num_pairs):
            x = float(input("Enter x value: "))
            y = int(input("Enter y value: "))
            pairs.append((x, y))
        return pairs

    N = int(input("Enter the number of pairs in the training set: "))
    train_set = np.array(read_pairs(N))

    M = int(input("Enter the number of pairs in the test set: "))
    test_set = np.array(read_pairs(M))

    X_train = train_set[:, 0].reshape(-1, 1)
    y_train = train_set[:, 1]

    X_test = test_set[:, 0].reshape(-1, 1)
    y_test = test_set[:, 1]

    param_grid = {'n_neighbors': list(range(1, 11))}
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_k = grid_search.best_params_['n_neighbors']

    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Best k for kNN Classification:", best_k)
    print("Corresponding test accuracy:", accuracy)


if __name__ == "__main__":
    main()
