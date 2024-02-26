from tensorflow import keras
from keras.preprocessing.text import Tokenizer
import pickle
import numpy as np
from GUI import GUI

review = ["this movie is good"]

#Tokenize String
tokenizer = Tokenizer()

with open('tokenizer.pickle', 'rb') as handle:
	tokenizer = pickle.load(handle)

	def predict(review):
		tokenizer.fit_on_texts(review)
		review = tokenizer.texts_to_sequences(review)

		for i in range(len(review[0])):
			if review[0][i] >= 63490:
				review[0].remove(review[0][i])
		
		review = np.array(review, dtype=float)

		model = keras.models.load_model('./GRUModel')

		predictValue = model.predict(review)

		if predictValue[0][0] <= 0.25:
			return "Rotten"
		elif predictValue[0][0] >= 0.75:
			return "Fresh"
		elif predictValue[0][0] <= 0.45:
			return "Likely Rotten"
		elif predictValue[0][0] >= 0.55:
			return "Likely Fresh"
		elif predictValue[0][0] < 0.5:
			return "Possibly Rotten"
		elif predictValue[0][0] > 0.5:
			return "Possibly Fresh"
		else:
			return "Unknown"

	GUI(predict)