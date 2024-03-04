import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))
    if N < 1:
        print("Error: N must be positive.")
        return

    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    for i in range(N):
        x = int(input(f"Enter x value for point {i + 1}: "))
        y = int(input(f"Enter y value for point {i + 1}: "))

        if x not in [0, 1] or y not in [0, 1]:
            print("Error: Both x and y values must be 0 or 1.")
            return

        X[i] = x
        Y[i] = y

    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()