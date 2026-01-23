import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv("data/learning_logs.csv")
X = data[[
    "last_studied_days",
    "revision_count",
    "study_duration"
]]

y = data["quiz_score"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
def predict_memory(days, revisions, duration):
    score = model.predict([[days, revisions, duration]])[0]
    score = max(0, min(score, 100))  # clamp
    return score / 100  # normalize (0–1)
def next_revision_day(memory_strength):
    if memory_strength > 0.8:
        return 5
    elif memory_strength > 0.6:
        return 3
    elif memory_strength > 0.4:
        return 1
    else:
        return 0  # revise today
