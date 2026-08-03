import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Read CSV file
df = pd.read_csv("play_tennis_knn_dataset.csv")

# Features (X)
X_train = df[["Outlook", "Temp", "Humidity", "Windy"]].values

# Target (Y)
y_train = df["Play"].values

# Test Case
X_test = np.array([[85.00, 30.00, 60.00, 60.00]])

# KNN
for k in [1, 3, 5]:
    model = KNeighborsClassifier(
        n_neighbors=k,
        metric="euclidean"
    )

# Train model
    model.fit(X_train, y_train)

    # Predict
    prediction = model.predict(X_test)[0]

    # Find nearest neighbors
    distances, neighbor_indexes = model.kneighbors(X_test)
    print("=" * 60)
    print(f"k = {k}")
    print(f"Predicted class = {prediction}")

    print("\nNearest Neighbors")

    for rank, (distance, index) in enumerate(zip(distances[0],  neighbor_indexes[0]),  start=1):
        print(f"Rank {rank}"
              f" | Record No. {df.iloc[index]['No']}"
              f" | Outlook={df.iloc[index]['Outlook']}"
              f" | Temp={df.iloc[index]['Temp']}"
              f" | Humidity={df.iloc[index]['Humidity']}"
              f" | Windy={df.iloc[index]['Windy']}"
              f" | Play={df.iloc[index]['Play']}"
              f" | Distance={distance:.2f}"
              )
