import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import pandas as pd

# Load the datasets
with open('X_train.pkl', 'rb') as f:
    X_train_full = pickle.load(f)

with open('y_train.pkl', 'rb') as f:
    Y_train_full = pickle.load(f)

X_train_full = X_train_full[:100000]
Y_train_full = Y_train_full[:100000]

print("Number of total rows ", len(Y_train_full))

#Convert string to to alphanum and lowercase
for i in range(len(X_train_full)):
    X_train_full[i] = ''.join(filter(lambda char: char.isalnum() or char.isspace(), X_train_full[i]))


#Tokenize String
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train_full)
X_train_full = tokenizer.texts_to_sequences(X_train_full)


#Convert jagged array to square
maxLen = 0
for i in X_train_full:
    maxLen = max(maxLen, len(i))

X_train_full = pad_sequences(X_train_full, maxlen=maxLen)

print("Max length ", maxLen)

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

#Get number of tokens
wordCount = 1

for word, count in tokenizer.word_counts.items():
    # print(word)
    wordCount += 1
# wordCount = sum([x for _,x in tokenizer.word_counts.items()])

#Divide data
end_of_train = int(len(X_train_full) * 0.8) #Train is 80% of data
end_of_test = int(len(X_train_full) * 0.9) #Test and validate is 10% and 10%

X_train, y_train = X_train_full[:end_of_train], Y_train_full[:end_of_train]
X_test, y_test = X_train_full[end_of_train:end_of_test], Y_train_full[end_of_train:end_of_test]
X_valid, y_valid = X_train_full[end_of_test:], Y_train_full[end_of_test:]

#Convert to numpy
X_train = np.array(X_train, dtype=float)
X_test = np.array(X_test, dtype=float)
X_valid = np.array(X_valid, dtype=float)

y_train = np.array(y_train, dtype=float)
y_test = np.array(y_test, dtype=float)
y_valid = np.array(y_valid, dtype=float)

print(X_train.shape)
print(y_train.shape)

#Build model
model = keras.Sequential()
# model.add(layers.Embedding(input_dim=wordCount, output_dim=512))
# model.add(layers.SimpleRNN(units=256, return_sequences=True))
# model.add(layers.Dense(units=1, activation='sigmoid'))

model.add(layers.Embedding(input_dim=wordCount, output_dim=512))
model.add(keras.layers.GRU(256, return_sequences=True))
model.add(keras.layers.GRU(128))
model.add(layers.Dense(units=1, activation='sigmoid'))

model.summary()

model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])


#Train model
model.fit(X_train, y_train, epochs=1,batch_size=32,
                    validation_data=(X_valid, y_valid))


#Evaluate model
model.evaluate(X_test, y_test)


#Save model
model.save('./GRUModel')
# model = keras.models.load_model('path/to/location')
