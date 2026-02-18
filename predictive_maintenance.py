import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# Step 1: In a real scenario, download 'ai4i2020.csv' from Kaggle
# For now, let's assume the friend has the data.
# This script trains a model to predict machine failure.

def train_slb_model(data_path):
    """
    Train a Random Forest model for predictive maintenance.
    
    Args:
        data_path: Path to the AI4I 2020 dataset CSV file
        
    Returns:
        model: Trained RandomForestClassifier model, or None if failed
    """
    try:
        df = pd.read_csv(data_path)
        
        # Features: Air temperature, Process temperature, Rotational speed, Torque, Tool wear
        features = ['Air temperature [K]', 'Process temperature [K]', 
                    'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
        
        # Validate that required columns exist
        if not all(col in df.columns for col in features):
            missing_cols = [col for col in features if col not in df.columns]
            print(f"Error: Missing columns in dataset: {missing_cols}")
            return None
            
        X = df[features]
        y = df['Machine failure']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions, average='weighted')
        
        print(f"Model Accuracy: {accuracy * 100:.2f}%")
        print(f"F1-Score: {f1:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, predictions))
        
        # Feature importance
        print("\nFeature Importance:")
        for feature, importance in zip(features, model.feature_importances_):
            print(f"  {feature}: {importance:.4f}")
        
        return model
    except FileNotFoundError:
        print(f"Error: Dataset file '{data_path}' not found.")
        print("Please provide the AI4I 2020 dataset CSV file from Kaggle.")
        return None
    except KeyError as e:
        print(f"Error: Required column not found in dataset: {e}")
        return None
    except Exception as e:
        print(f"Error during model training: {e}")
        return None


if __name__ == "__main__":
    # To run: uncomment the line below and ensure 'ai4i2020.csv' is in the working directory
    # model = train_slb_model('ai4i2020.csv')
    print("Predictive Maintenance Model Ready.")
    print("To train the model, uncomment the train_slb_model() call and provide the AI4I 2020 dataset.")