# Import required libraries
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
df = pd.read_csv("student_study_data.csv")
# df = pd.read_csv("student")
print("Dataset Loaded Successfully!\n")
print(df.head())

# Step 2: Split input and output
X = df[['Hours_Studied', 'Attendance']]
y = df['Marks']

# Step 3: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Step 4: Scale input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Convert to torch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
y_test = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

# Step 6: Define a simple neural network model
class StudentModel(nn.Module):
    def __init__(self):
        super(StudentModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 8),   # Input layer (2 features)
            nn.ReLU(),
            nn.Linear(8, 4),
            nn.ReLU(),
            nn.Linear(4, 1)    # Output layer (Marks)
        )

    def forward(self, x):
        return self.net(x)

model = StudentModel()

# Step 7: Define loss function and optimizer
criterion = nn.MSELoss()             # Mean Squared Error loss
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Step 8: Train the model
epochs = 300
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Step 9: Evaluate model on test data
model.eval()
with torch.no_grad():
    predictions = model(X_test)
    test_loss = criterion(predictions, y_test).item()

print("\nModel Evaluation Completed!")
print("Mean Squared Error (Test Loss):", round(test_loss, 4))

# Step 10: Show actual vs predicted marks
comparison = pd.DataFrame({
    "Actual Marks": y_test.flatten().numpy(),
    "Predicted Marks": predictions.flatten().numpy().round(2)
})
print("\nPrediction Comparison:\n")
print(comparison)
