# -----------------------------------------------------------------
# Autoencoder for Anomaly Detection (using MNIST)
# Stages: Data Prep, Encoder, Decoder, Compile/Train/Evaluate
# -----------------------------------------------------------------

# a. Import required libraries
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
import numpy as np
import matplotlib.pyplot as plt

# Define constants
ANOMALY_DIGIT = 9  # Digit 9 will be treated as the anomaly
IMAGE_SIZE = 28 * 28
LATENT_DIM = 32    # The size of the compressed bottleneck layer
EPOCHS = 20
BATCH_SIZE = 128

print("--- Starting Autoencoder Anomaly Detection ---")

# b. Upload/access the dataset
print("\n[Stage A] Accessing and preprocessing dataset...")

# Load MNIST data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize and Flatten the image data (28x28 -> 784 features)
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape((len(x_train), IMAGE_SIZE))
x_test = x_test.reshape((len(x_test), IMAGE_SIZE))

# Prepare 'Normal' data (digits 0-8) and 'Anomaly' data (digit 9)
x_train_normal = x_train[y_train != ANOMALY_DIGIT]
x_test_normal = x_test[y_test != ANOMALY_DIGIT]
x_test_anomaly = x_test[y_test == ANOMALY_DIGIT]

# Create a balanced test subset for final evaluation and visualization
x_test_subset = np.concatenate([x_test_normal[:100], x_test_anomaly[:100]])
y_test_subset = np.concatenate([y_test[y_test != ANOMALY_DIGIT][:100], y_test[y_test == ANOMALY_DIGIT][:100]])


# c. The encoder converts it into a latent representation
print("\n[Stage B] Defining Encoder Network...")
input_layer = Input(shape=(IMAGE_SIZE,))

# Encoder Architecture (compression)
encoder = Dense(128, activation='relu')(input_layer)
encoder = Dense(64, activation='relu')(encoder)
# Latent representation (bottleneck)
latent_view = Dense(LATENT_DIM, activation='relu', name='latent_space')(encoder)


# d. Decoder networks convert it back to the original input
print("[Stage C] Defining Decoder Network...")

# Decoder Architecture (reconstruction)
decoder = Dense(64, activation='relu')(latent_view)
decoder = Dense(128, activation='relu')(decoder)
# Output layer (must reconstruct the original 784 pixels, using sigmoid for 0-1 range)
output_layer = Dense(IMAGE_SIZE, activation='sigmoid')(decoder)

# Combine Encoder and Decoder into the Autoencoder Model
autoencoder = Model(inputs=input_layer, outputs=output_layer, name='Autoencoder')
autoencoder.summary()


# e. Compile the models with Optimizer, Loss, and Evaluation Metrics
print("\n[Stage D] Compiling and training the Autoencoder...")

# Compile the model
autoencoder.compile(
    optimizer=Adam(learning_rate=0.001),
    loss=MeanSquaredError() # Standard loss for reconstruction
)

# Train ONLY on 'normal' data (digits 0-8)
history = autoencoder.fit(
    x_train_normal, x_train_normal, # Input == Target (unsupervised)
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    shuffle=True,
    validation_data=(x_test_normal, x_test_normal),
    verbose=1
)

print("\n--- Anomaly Detection Evaluation ---")

# --- Performance Estimation: Calculating Reconstruction Error ---
# 1. Predict reconstruction for the test subset
predictions = autoencoder.predict(x_test_subset, verbose=0)

# 2. Calculate the Mean Squared Error (Reconstruction Error) for each sample
mse = np.mean(np.power(x_test_subset - predictions, 2), axis=1)

# 3. Find a threshold: Use the 95th percentile of the MSE on the normal test set.
mse_normal_test = np.mean(np.power(x_test_normal - autoencoder.predict(x_test_normal, verbose=0), 2), axis=1)
threshold = np.percentile(mse_normal_test, 95) 

# 4. Classify anomalies
is_anomaly = mse > threshold

# 5. Display detection stats
print(f"Reconstruction Error Threshold (95th percentile of normal data): {threshold:.5f}")
print(f"Total test samples evaluated: {len(x_test_subset)}")
print(f"True Anomaly (Digit {ANOMALY_DIGIT}) count: {np.sum(y_test_subset == ANOMALY_DIGIT)}")
print(f"Detected Anomaly count (MSE > Threshold): {np.sum(is_anomaly)}")


# 6. Visualize results (with safe indexing)
# Get indices for correctly detected anomalies (True Anomaly & Error > Threshold)
anomaly_indices = np.where(np.logical_and(is_anomaly, y_test_subset == ANOMALY_DIGIT))[0]
# Get indices for correctly classified normal samples (True Normal & Error < Threshold)
normal_indices = np.where(np.logical_and(~is_anomaly, y_test_subset != ANOMALY_DIGIT))[0]

# Determine the number of plots possible (max 5)
num_plots = min(5, len(anomaly_indices), len(normal_indices))

if num_plots > 0:
    fig, axes = plt.subplots(2, num_plots, figsize=(3 * num_plots, 6))
    
    # Check if axes is a 1D array (only possible if num_plots=1, but safe indexing handles this)
    is_single_plot = num_plots == 1
    
    for i in range(num_plots):
        idx_anomaly = anomaly_indices[i]
        idx_normal = normal_indices[i]
        
        # Determine correct axis handles
        ax0 = axes[0] if is_single_plot else axes[0, i]
        ax1 = axes[1] if is_single_plot else axes[1, i]

        # Plot Anomaly (Digit 9)
        ax0.imshow(x_test_subset[idx_anomaly].reshape(28, 28), cmap='gray')
        ax0.set_title(f"Anomaly (9)\nError: {mse[idx_anomaly]:.4f}")
        ax0.axis('off')

        # Plot Normal (Digit 0-8)
        ax1.imshow(x_test_subset[idx_normal].reshape(28, 28), cmap='gray')
        ax1.set_title(f"Normal\nError: {mse[idx_normal]:.4f}")
        ax1.axis('off')

    plt.suptitle(f"Anomaly Detection using Autoencoder (Trained on 0-8, Anomaly is 9)\nThreshold: {threshold:.5f}")
    plt.tight_layout()
    plt.show()
else:
    print("\nNot enough correctly classified anomaly/normal samples to generate plot.")
