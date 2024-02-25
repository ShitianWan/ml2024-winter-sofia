import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def knn_regression(X_train, y_train, X_test, k):
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)
    y_pred = knn_regressor.predict(X_test)
    return y_pred

def main():
    N = int(input("Enter the number of points: "))
    k = int(input("Enter the value of k for k-NN Regression: "))

    if k > N:
        print("Error: k should <= N")
        return

    train = []
    print("Enter the coordinates for each point (x, y):")
    for i in range(N):
        x = float(input("Enter x coordinate for point {}: ".format(i+1)))
        y = float(input("Enter y coordinate for point {}: ".format(i+1)))
        train.append([x, y])

    train = np.array(train)

    X_train = train[:, 0].reshape(-1, 1)
    y_train = train[:, 1]

    X_test = np.array([[float(input("Enter the value of for prediction: "))]])
    y_pred = knn_regression(X_train, y_train, X_test, k)

    print("Predicted value using k-NN Regression:", y_pred[0])

    r2 = r2_score(y_train, knn_regression(X_train, y_train, X_train, k))
    print(f"Coefficient of Determination (R^2): {r2}")

if __name__ == "__main__":
    main()