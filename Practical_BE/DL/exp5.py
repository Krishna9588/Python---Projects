# -----------------------------------------------------------------
# Continuous Bag of Words (CBOW) Model for Word Embeddings
# Implemented using Keras/TensorFlow.
# -----------------------------------------------------------------

# a. Data preparation
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Lambda, Reshape
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import backend as K

# --- Configuration ---
CONTEXT_WINDOW_SIZE = 2  # Two words before and two words after
EMBEDDING_DIM = 50       # Dimensionality of the word vectors
HIDDEN_DIM = 128
BATCH_SIZE = 32          # <-- FIX: Added missing BATCH_SIZE definition
EPOCHS = 100
LEARNING_RATE = 0.001

def create_lookup_tables(text_data):
    """Tokenizes text and creates word-to-index and index-to-word mappings."""
    # Simple tokenization: lowercasing and splitting by space
    tokens = [word.lower() for sentence in text_data for word in sentence.split()]
    
    # Vocabulary creation
    vocab = sorted(list(set(tokens)))
    word_to_idx = {word: i for i, word in enumerate(vocab)}
    idx_to_word = {i: word for i, word in enumerate(vocab)}
    
    # Vocabulary size
    vocab_size = len(vocab)
    
    return tokens, vocab_size, word_to_idx, idx_to_word

# Sample Corpus
text_data = [
    "The quick brown fox jumps over the lazy dog",
    "Word embeddings are useful for natural language processing",
    "CBOW predicts the word from context"
]

print("--- Starting CBOW Implementation ---")
print("\n[Stage A] Data Preparation...")

tokens, VOCAB_SIZE, word_to_idx, idx_to_word = create_lookup_tables(text_data)
print(f"Vocabulary Size: {VOCAB_SIZE}")
print(f"Total Tokens: {len(tokens)}")

# b. Generate training data
print("\n[Stage B] Generating training data (Context-Target pairs)...")

X_context = []  # Input: Sum of one-hot vectors of context words
Y_target = []   # Output: One-hot vector of the target word

for i, target_word in enumerate(tokens):
    # Determine context window boundaries
    start_index = max(0, i - CONTEXT_WINDOW_SIZE)
    end_index = min(len(tokens), i + CONTEXT_WINDOW_SIZE + 1)
    
    context_words = tokens[start_index:i] + tokens[i+1:end_index]
    
    if not context_words:
        continue

    # Convert context words to indices
    context_indices = [word_to_idx[w] for w in context_words]
    
    # 1. Input (Context Summation) - We will handle the averaging/summation in the model architecture
    # For now, prepare the input as a list of context word indices
    # (The Embedding layer will handle the lookup)
    X_context.append(context_indices)
    
    # 2. Output (Target Word)
    target_index = word_to_idx[target_word]
    Y_target.append(target_index)

# Convert lists to NumPy arrays
# X_context must be padded so all input sequences have the same length (4)
MAX_CONTEXT_LEN = 2 * CONTEXT_WINDOW_SIZE 
X_context = tf.keras.preprocessing.sequence.pad_sequences(
    X_context, maxlen=MAX_CONTEXT_LEN, padding='post', value=VOCAB_SIZE
)
Y_target = np.array(Y_target)

# Convert target labels to one-hot encoding
Y_target_one_hot = to_categorical(Y_target, num_classes=VOCAB_SIZE)

print(f"Shape of X_context (Input): {X_context.shape}")
print(f"Shape of Y_target (Output): {Y_target_one_hot.shape}")
print(f"Max Context Length (Input Size): {MAX_CONTEXT_LEN}")


# Model Architecture (CBOW is inherently a shallow neural network)
# The CBOW skip-gram structure is often implemented by summing the embeddings of the context words.
print("\n[Stage C - Part 1] Defining Model Architecture...")

# 1. Input layer: Takes padded context indices (e.g., [1, 5, 20, 0])
input_context = Input(shape=(MAX_CONTEXT_LEN,), name='context_input')

# 2. Embedding layer: Converts indices to dense vectors
# mask_zero=True allows the model to ignore the padding value (VOCAB_SIZE used for padding)
embedding_layer = Embedding(
    input_dim=VOCAB_SIZE + 1,  # +1 for the padding mask value
    output_dim=EMBEDDING_DIM,
    mask_zero=True,
    name='word_embedding'
)(input_context)

# 3. Summation layer (CBOW magic): Sums the embeddings of the context words
# The Lambda layer applies a custom function (summation over the time/sequence axis)
summed_embeddings = Lambda(lambda x: K.sum(x, axis=1), output_shape=(EMBEDDING_DIM,))(embedding_layer)

# 4. Hidden Layer (Projection layer - Optional but often used)
projection = Dense(HIDDEN_DIM, activation='relu', name='projection_layer')(summed_embeddings)

# 5. Output layer: Predicts the target word (size = Vocabulary Size)
output_word = Dense(VOCAB_SIZE, activation='softmax', name='output_softmax')(projection)

cbow_model = Model(inputs=input_context, outputs=output_word, name='CBOW_Model')
cbow_model.summary()

# c. Train model
print("\n[Stage C - Part 2] Training Model...")

cbow_model.compile(
    optimizer=Adam(learning_rate=LEARNING_RATE),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = cbow_model.fit(
    X_context, 
    Y_target_one_hot,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=0 # Suppress output during actual training
)
print(f"Training finished after {EPOCHS} epochs.")


# d. Output
print("\n[Stage D] Outputting Word Embeddings and Sample Prediction...")

# Extract the trained Embedding layer weights
# The weights are the word vectors!
word_vectors = cbow_model.get_layer('word_embedding').get_weights()[0]

print(f"\nExtracted Word Vector Shape: {word_vectors.shape}")
print(f"First 5 dimensions of 'fox': {word_vectors[word_to_idx['fox']][:5]}")
print(f"First 5 dimensions of 'dog': {word_vectors[word_to_idx['dog']][:5]}")


# Example Prediction (Find the most likely word for a context)
sample_context_words = ["the", "quick", "jumps", "over"]
sample_indices = [word_to_idx.get(w, 0) for w in sample_context_words]

# Pad and reshape the input for the model (batch size of 1)
input_data = tf.keras.preprocessing.sequence.pad_sequences(
    [sample_indices], maxlen=MAX_CONTEXT_LEN, padding='post', value=VOCAB_SIZE
)

prediction_probabilities = cbow_model.predict(input_data, verbose=0)[0]
predicted_index = np.argmax(prediction_probabilities)
predicted_word = idx_to_word[predicted_index]

print(f"\nContext: {sample_context_words}")
print(f"Predicted Word (Highest Probability): {predicted_word}")