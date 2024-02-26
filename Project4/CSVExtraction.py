"""
This file parses the csv dataset.
Strips the necessary data and stores it into the X and y training sets.
Stores the sets locally using pickle.
"""
import csv
import pickle


with open('rotten_tomatoes_critic_reviews.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    X_train = []
    y_train = []

    for row in reader:
        if (row[0] == 'rotten_tomatoes_link'):      # Skip first line
            continue

        isRotten = row[4]

        # Loop through the row until the rating is found
        for x in row:
            if (isRotten == 'Fresh' or isRotten == 'Certified-Fresh'):
                X_train.append(row[7])      # Movie description
                y_train.append(1)
                break
            elif (isRotten == 'Rotten'):
                X_train.append(row[7])      # Movie description
                y_train.append(0)
                break



with open('X_train.pkl', 'wb') as f:
    pickle.dump(X_train, f)


with open('y_train.pkl', 'wb') as f:
    pickle.dump(y_train, f)
