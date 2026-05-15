from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)



model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.summary()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
my_callbacks = [
    callbacks.TensorBoard(log_dir='logs', update_freq=100),
    callbacks.ModelCheckpoint(filepath='best_model.h5', monitor='val_accuracy', 
                              mode='max', save_best_only=True)


history = model.fit(
    x_train_s, y_train_s,
    epochs=10,            
    batch_size=64,
    validation_split=0.1,
    callbacks=my_callbacks
)
best_model = keras.models.load_model('best_model.h5')

train_pred = best_model.predict(x_train_s)
test_pred = best_model.predict(x_test_s)

train_labels_pred = np.argmax(train_pred, axis=1)
test_labels_pred = np.argmax(test_pred, axis=1)

train_accuracy = accuracy_score(y_train, train_labels_pred)
test_accuracy = accuracy_score(y_test, test_labels_pred)

print(f'Točnost na skupu za učenje: {train_accuracy*100:.2f}%')
print(f'Točnost na testnom skupu: {test_accuracy*100:.2f}%')
print("Matrica zabune na testnom skupu:")
cm = confusion_matrix(y_test, test_labels_pred)
print(cm)