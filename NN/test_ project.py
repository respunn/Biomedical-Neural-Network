import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load data from CSV
df = pd.read_csv(".\\Datasets\\ilovescience\\trainLabels_cropped.csv")

image_height = 1024
image_width = 1024
num_channels = 1

# Assuming the last column is the label and the rest are pixel values
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Reshape X to [num_samples, image_height, image_width, num_channels]
# For grayscale images, num_channels would be 1
X = X.reshape(-1, image_height, image_width, num_channels)

# Normalize pixel values
X = X / 255.0

# Convert labels to categorical format
y = to_categorical(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(image_height, image_width, num_channels)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_accuracy * 100:.2f}%')
