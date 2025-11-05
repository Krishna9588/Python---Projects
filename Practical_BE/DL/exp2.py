# a. Import the necessary packages
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

# --- Configuration ---
NUM_CLASSES = 10
INPUT_SHAPE = (28, 28)
BATCH_SIZE = 128
EPOCHS = 10
LEARNING_RATE = 0.01

# b. Load the training and testing data (MNIST)
print("[INFO] Loading and preprocessing data...")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocessing: Normalize the pixel values from 0-255 to 0-1
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# The data is now (60000, 28, 28) and (10000, 28, 28).

# c. Define the network architecture using Keras (Sequential API)
# The Sequential model is a linear stack of layers
print("[INFO] Defining network architecture...")
model = Sequential([
    # The Flatten layer converts the 2D (28x28) image into a 1D vector (784)
    Flatten(input_shape=INPUT_SHAPE),
    # First Hidden Layer: 256 neurons with ReLU activation
    Dense(256, activation='relu'),
    # Second Hidden Layer: 128 neurons with ReLU activation
    Dense(128, activation='relu'),
    # Output Layer: 10 neurons (one for each digit) with Softmax for probability distribution
    Dense(NUM_CLASSES, activation='softmax')
])

# Display the model structure
model.summary()

# d. Train the model using SGD
# 1. Compile the model
# The loss function is 'sparse_categorical_crossentropy' because the labels (y_train) are integers (0-9)
# The optimizer is Stochastic Gradient Descent (SGD)
print("[INFO] Compiling model with SGD optimizer...")
sgd_optimizer = SGD(learning_rate=LEARNING_RATE)
model.compile(
    optimizer=sgd_optimizer,
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 2. Fit the model to the training data
print("[INFO] Training network...")
H = model.fit(
    x_train, y_train,
    validation_data=(x_test, y_test),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=1 # Show progress bar
)

# e. Evaluate the network
print("[INFO] Evaluating network...")
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy*100:.2f}%")

# f. Plot the training loss and accuracy
print("[INFO] Plotting training loss and accuracy...")
plt.style.use("ggplot")
plt.figure(figsize=(12, 4))

# Plot Training Loss vs. Validation Loss
plt.subplot(1, 2, 1)
plt.plot(np.arange(0, EPOCHS), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, EPOCHS), H.history["val_loss"], label="val_loss")
plt.title("Training Loss and Validation Loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend()

# Plot Training Accuracy vs. Validation Accuracy
plt.subplot(1, 2, 2)
plt.plot(np.arange(0, EPOCHS), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, EPOCHS), H.history["val_accuracy"], label="val_acc")
plt.title("Training Accuracy and Validation Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.legend()

plt.tight_layout()
plt.show()

# Example Prediction
# Get a random image from the test set
random_index = np.random.randint(0, len(x_test))
sample_image = x_test[random_index]
true_label = y_test[random_index]

# Keras expects a batch of inputs, so we add a dimension
sample_image_batch = np.expand_dims(sample_image, axis=0)
prediction = model.predict(sample_image_batch)
predicted_label = np.argmax(prediction[0])

print(f"\nExample Prediction:")
print(f"True Label: {true_label}")
print(f"Predicted Label: {predicted_label}")
print(f"Confidence: {prediction[0][predicted_label]*100:.2f}%")

plt.imshow(sample_image, cmap='gray')
plt.title(f"True: {true_label}, Predicted: {predicted_label}")
plt.axis('off')
plt.show()