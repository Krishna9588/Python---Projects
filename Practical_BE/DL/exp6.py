# -----------------------------------------------------------------
# Object Detection using Transfer Learning (VGG16 + Custom Classifier)
# Task: Image Classification on a small dataset (e.g., CIFAR-10 subset)
# -----------------------------------------------------------------

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import cifar10
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration ---
IMG_SIZE = 32  # CIFAR-10 images are 32x32
INPUT_SHAPE = (IMG_SIZE, IMG_SIZE, 3)
VGG_INPUT_SIZE = 224 # VGG16 requires 224x224 input
NUM_CLASSES = 10
# Reduced BATCH_SIZE to alleviate memory pressure during fine-tuning (was 32)
BATCH_SIZE = 16 
EPOCHS_CLASSIFIER = 2      # <-- EDITED: Reduced from 5 to 2 for speed
EPOCHS_FINETUNE = 2        # <-- EDITED: Reduced from 5 to 2 for speed

print("--- Starting Transfer Learning Implementation (VGG16 on CIFAR-10) ---")

# Data preparation
print("\n[Stage A - Data Preparation] Loading and preprocessing data...")

# Load CIFAR-10 dataset (32x32 color images)
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Convert labels to one-hot encoding
y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)


# a. Load in a pre-trained CNN model trained on a large dataset
print("\n[Stage A - Base Model] Loading VGG16 (ImageNet weights)...")

# Instantiate VGG16, excluding the top (classification) layers.
base_model = VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(VGG_INPUT_SIZE, VGG_INPUT_SIZE, 3) # Specify VGG's expected input shape here
)

# b. Freeze parameters (weights) in the model’s lower convolutional layers
print("[Stage B] Freezing VGG16 layers...")
base_model.trainable = False # Freeze all layers in the base model


# c. Add a custom classifier with several layers of trainable parameters
print("[Stage C] Adding custom trainable classifier head...")

# Define the overall model input for our small dataset (32x32x3)
inputs = Input(shape=INPUT_SHAPE) 

# 1. Add resizing layer to meet VGG16's expected input size (224x224)
resize_layer = tf.keras.layers.Resizing(VGG_INPUT_SIZE, VGG_INPUT_SIZE, interpolation="bilinear", name='resizing_layer')
x = resize_layer(inputs)

# 2. Pass resized input through the frozen VGG base model
x = base_model(x, training=False) 

# 3. Add new classification layers (head)
x = Flatten()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(128, activation='relu')(x)
outputs = Dense(NUM_CLASSES, activation='softmax')(x)

# Create the final model
model = Model(inputs, outputs)

# Compile the model for initial training (only the new layers are trainable)
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()


# d. Train classifier layers on training data available for the task
print(f"\n[Stage D] Training only the custom classifier head (Epochs: {EPOCHS_CLASSIFIER})...")

# Initial training phase (only new layers train)
history_initial = model.fit(
    x_train, y_train,
    epochs=EPOCHS_CLASSIFIER,
    # Use the reduced BATCH_SIZE here
    batch_size=BATCH_SIZE, 
    validation_data=(x_test, y_test),
    verbose=1
)


# e. Fine-tune hyperparameters and unfreeze more layers as needed
print(f"\n[Stage E] Fine-tuning: Conservatively unfreezing high-level feature blocks (Block 4 & 5)...")

# 1. Unfreeze the base model
base_model.trainable = True

# 2. Select specific layers/blocks to unfreeze (Memory Optimization: Keep more layers frozen)
# Freeze the first three blocks (Block 1, Block 2, Block 3)
for layer in base_model.layers:
    # We only want to train block4 and block5 to save memory
    if layer.name.startswith('block1') or layer.name.startswith('block2') or layer.name.startswith('block3'):
        layer.trainable = False
    else:
        # Unfreeze all layers from block 4 onwards.
        layer.trainable = True

# 3. Recompile the model with a much lower learning rate for fine-tuning
model.compile(
    optimizer=Adam(learning_rate=0.00001), # CRITICAL: Very low LR prevents catastrophic forgetting
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 4. Continue training (Fine-tuning phase)
print(f"\nFine-tuning entire model (Epochs: {EPOCHS_FINETUNE})...")
history_finetune = model.fit(
    x_train, y_train,
    epochs=EPOCHS_FINETUNE,
    # Use the reduced BATCH_SIZE here
    batch_size=BATCH_SIZE,
    validation_data=(x_test, y_test),
    verbose=1
)

# Final Evaluation
print("\n--- Final Model Performance Estimation ---")
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Loss after Fine-tuning: {loss:.4f}")
print(f"Test Accuracy after Fine-tuning: {accuracy*100:.2f}%")