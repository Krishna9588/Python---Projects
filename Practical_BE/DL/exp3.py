# -----------------------------------------------------------
# Image Classification Model (Convolutional Neural Network - CNN)
# Stages: Data Prep, Architecture, Training, Performance
# Dataset: MNIST
# -----------------------------------------------------------

# a. Loading and preprocessing the image data
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt
import numpy as np

# --- 1. CONFIGURATION ---
NUM_CLASSES = 10
EPOCHS = 10
BATCH_SIZE = 128

print("--- Starting CNN Image Classification ---")

# a. Loading and preprocessing the image data
print("\n[Stage A] Loading and preprocessing image data...")

# Load MNIST data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocessing Step 1: Reshape data for CNN input
# Images must be 4D: (samples, height, width, channels). Grayscale = 1 channel.
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

# Preprocessing Step 2: Normalize pixel values (0-255 -> 0.0-1.0)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print(f"Input shape: {input_shape}")


# b. Defining the model’s architecture
print("\n[Stage B] Defining the model's architecture (CNN)...")
model = Sequential([
    # 1. Convolutional Block 1
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D(pool_size=(2, 2)),

    # 2. Convolutional Block 2
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    # 3. Classification Head
    Flatten(), # Prepare output for Dense layers
    Dense(128, activation='relu'),
    Dense(NUM_CLASSES, activation='softmax') # Output layer
])

model.summary()


# c. Training the model
print("\n[Stage C] Compiling and training the model...")

# Compile the model using a popular optimizer and loss function
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy', # Used for integer labels (0-9)
    metrics=['accuracy']
)

# Fit the model to the training data
H = model.fit(
    x_train, y_train,
    validation_data=(x_test, y_test),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=1
)
print("Model training complete.")


# d. Estimating the model’s performance
print("\n[Stage D] Estimating the model's performance...")

# Evaluate model on the test dataset
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Final Test Loss: {test_loss:.4f}")
print(f"Final Test Accuracy: {test_accuracy*100:.2f}%")

# Plotting the Training History
plt.style.use("ggplot")
plt.figure(figsize=(12, 5))

# Plot Loss
plt.subplot(1, 2, 1)
plt.plot(np.arange(0, EPOCHS), H.history["loss"], label="Train Loss")
plt.plot(np.arange(0, EPOCHS), H.history["val_loss"], label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend()

# Plot Accuracy
plt.subplot(1, 2, 2)
plt.plot(np.arange(0, EPOCHS), H.history["accuracy"], label="Train Accuracy")
plt.plot(np.arange(0, EPOCHS), H.history["val_accuracy"], label="Validation Accuracy")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.legend()

plt.tight_layout()
plt.show()

# Example Prediction
random_index = np.random.randint(0, len(x_test))
sample_image = x_test[random_index]
true_label = y_test[random_index]

# Predict requires a batch, so we add a dimension (1, 28, 28, 1)
sample_image_batch = np.expand_dims(sample_image, axis=0)
prediction = model.predict(sample_image_batch, verbose=0)
predicted_label = np.argmax(prediction[0])

print(f"\nExample Prediction on Test Image:")
print(f"True Label: {true_label}")
print(f"Predicted Label: {predicted_label}")
