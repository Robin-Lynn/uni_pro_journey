import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Training features
X_train = np.array([
    [90.00, 40.00, 80.00, 10.00],
    [95.00, 32.00, 85.00, 80.00],
    [50.00, 35.00, 90.00, 20.00],
    [10.00, 24.00, 80.00, 5.00],
    [15.00, 10.00, 50.00, 15.00],
    [20.00, 12.00, 55.00, 90.00],
    [55.00, 9.00, 45.00, 95.00],
    [85.00, 22.00, 95.00, 25.00],
    [95.00, 7.00, 50.00, 5.00],
    [5.00, 26.00, 45.00, 10.00],
    [80.00, 25.00, 40.00, 80.00],
    [45.00, 24.00, 85.00, 85.00],
    [40.00, 37.00, 60.00, 15.00],
    [25.00, 23.00, 90.00, 95.00],
])

# Training labels
y_train = np.array([
    "No", "No", "Yes", "Yes", "Yes", "No", "Yes",
    "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"
])

# Test case
X_test = np.array([[85.00, 30.00, 60.00, 60.00]])

for k in [1, 3, 5]:
    model = KNeighborsClassifier(
        n_neighbors=k,
        metric="euclidean"
    )

    model.fit(X_train, y_train)
    prediction = model.predict(X_test)[0]
    distances, neighbor_indexes = model.kneighbors(X_test)
    print("=" * 60)
    print(f"k = {k}")
    print(f"Predicted class: {prediction}")
    print("\nNearest neighbors:")

    for rank, (distance, index) in enumerate(zip(distances[0], neighbor_indexes[0]), start=1):
        print(
            f"Rank {rank}: "
            f"Record No. {index + 1}, "
            f"Class={y_train[index]}, "
            f"Distance={distance:.2f}"
        )
