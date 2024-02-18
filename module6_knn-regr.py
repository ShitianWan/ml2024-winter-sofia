import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        distances = np.sqrt(np.sum((self.X_train - X_test)**2, axis=1))
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_neighbors = self.y_train[nearest_indices]
        return np.mean(nearest_neighbors)

def main():
    N = int(input("Enter the number of points: "))
    k = int(input("Enter the value of k for k-NN Regression: "))

    if k > N:
        print("Error: k should <= N")
        return

    X_train = []
    y_train = []
    print("Enter the coordinates for each point (x, y):")
    for i in range(N):
        x = float(input("Enter x coordinate for point {}: ".format(i+1)))
        y = float(input("Enter y coordinate for point {}: ".format(i+1)))
        X_train.append([x, y])
        y_train.append(y)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    knn_regressor = KNNRegression(k)
    knn_regressor.fit(X_train, y_train)

    X_test = np.array([[float(input("Enter the value of for prediction: ")), 0]])
    prediction = knn_regressor.predict(X_test)

    print("Predicted value using k-NN Regression:", prediction)

if __name__ == "__main__":
    main()