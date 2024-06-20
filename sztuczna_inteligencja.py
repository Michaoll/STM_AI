import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Function to read and parse the data file
def read_processed_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def parse_lines(lines):
    adc_values = []
    gestures = []

    current_adc = []
    for line in lines:
        line = line.strip()
        try:
            value = float(line)
            current_adc.append(value)
            if len(current_adc) == 128:
                # Read next line for gesture state
                gesture_state = int(lines[lines.index(line) + 1].strip())
                adc_values.append(current_adc)
                gestures.append(gesture_state)
                current_adc = []
        except ValueError:
            continue

    return np.array(adc_values), np.array(gestures)

# Load data from file
file_name = 'obrobiony_nowy_test.txt'
lines = read_processed_file(file_name)
adc_values, gestures = parse_lines(lines)

# Normalize the data
adc_values_normalized = adc_values / 4096.0

# Split data into training and test sets (80% train, 20% test)
split_index = int(0.8 * len(adc_values_normalized))
x_train, x_test = adc_values_normalized[:split_index], adc_values_normalized[split_index:]
y_train, y_test = gestures[:split_index], gestures[split_index:]

# Define the neural network model
model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(128,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Print the model summary
print("Model Summary before training:")
model.summary()

# Train the model
history = model.fit(x_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy}")

# Save the model to file
model.save('gesture_detection_model_normalized.h5')
print("Model saved to disk.")

# Make predictions
predictions = model.predict(x_test)

# Plot the actual vs predicted gesture values
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual Gestures', color='blue')
plt.plot(predictions, label='Predicted Gestures', color='red', linestyle='--')
plt.title('Actual vs Predicted Gesture Values')
plt.xlabel('Sample Index')
plt.ylabel('Gesture Value')
plt.legend()
plt.grid(True)
plt.show()
