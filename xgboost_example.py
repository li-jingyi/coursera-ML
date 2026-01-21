#!/usr/bin/env python3
"""
XGBoost Sample Program
This program demonstrates how to use XGBoost for classification tasks
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import xgboost as xgb


def main():
    print("=" * 60)
    print("XGBoost Classification Example")
    print("=" * 60)

    # Load the Iris dataset
    print("\n1. Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target
    print(f"   Dataset shape: {X.shape}")
    print(f"   Number of classes: {len(np.unique(y))}")
    print(f"   Feature names: {iris.feature_names}")

    # Split the data into training and testing sets
    print("\n2. Splitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"   Training samples: {len(X_train)}")
    print(f"   Testing samples: {len(X_test)}")

    # Create and train XGBoost classifier
    print("\n3. Training XGBoost classifier...")
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        objective='multi:softmax',
        num_class=3,
        random_state=42,
        eval_metric='mlogloss'
    )

    # Fit the model
    model.fit(X_train, y_train)
    print("   Training complete!")

    # Make predictions
    print("\n4. Making predictions on test set...")
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("\n5. Model Evaluation:")
    accuracy = accuracy_score(y_test, y_pred)
    print(f"   Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

    print("\n   Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    print("\n   Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    # Feature importance
    print("\n6. Feature Importance:")
    feature_importance = model.feature_importances_
    for i, (feature, importance) in enumerate(zip(iris.feature_names, feature_importance)):
        print(f"   {feature}: {importance:.4f}")

    # Demonstrate prediction on a single sample
    print("\n7. Single Sample Prediction:")
    sample = X_test[0].reshape(1, -1)
    prediction = model.predict(sample)
    prediction_proba = model.predict_proba(sample)
    print(f"   Sample features: {sample[0]}")
    print(f"   Predicted class: {iris.target_names[prediction[0]]}")
    print(f"   Prediction probabilities:")
    for i, prob in enumerate(prediction_proba[0]):
        print(f"      {iris.target_names[i]}: {prob:.4f}")
    print(f"   Actual class: {iris.target_names[y_test[0]]}")

    print("\n" + "=" * 60)
    print("XGBoost example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
