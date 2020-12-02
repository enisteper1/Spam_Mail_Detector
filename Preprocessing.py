import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np
import pandas as pd
import re
from pathlib import Path


def data_preprocessing(csv="data/spam.csv"):
    # Check if data is created before
    if Path("data/x.npy").exists() and Path("data/y.npy").exists():
        print("Loading data...")
        # Load numpy arrays
        x, y = np.load("data/x.npy", allow_pickle=True), np.load("data/y.npy", allow_pickle=True)
    else:
        print("Creating data...")
        word_dict = {}
        word_index = 0
        nltk.download("stopwords")
        stop_word_list = stopwords.words("english")
        # Read csv
        data = pd.read_csv(csv, encoding="latin1").to_numpy()
        # First column is output and second column is input
        _x, _y = data[:, 1], data[:, 0]
        # if mail is ham assign 1 otherwise 0
        y = np.array(list(map(lambda word: 1 if str(word) == "ham" else 0, _y)))
        # PorterStemmer is used to get roots of all words in sentences
        porter_stemmer = PorterStemmer()
        mail_list = list()
        # Process Each mail
        for row in _x:
            # Only take characters and lower the words then split to list
            mail = re.sub("[^a-zA-Z]", " ", row).lower().split()
            # Get roots of all words and ignore if the word is stop word
            mail = [porter_stemmer.stem(word) for word in mail if word not in stop_word_list]
            for word in mail:
                if word not in word_dict:
                    word_dict[word] = word_index
                    word_index += 1
            mail_list.append(mail)
        with open("data/word_dictionary", "w") as f:
            f.write(str(word_dict))
        # Reshaping the x and y
        x = np.empty((_x.shape[0], len(word_dict)))
        for i, mail in enumerate(mail_list):
            for word in mail:
                x[i, word_dict[word]] += 1
        # Save inputs and outputs
        np.save("data/x.npy", x, allow_pickle=True)
        np.save("data/y.npy", y, allow_pickle=True)

    return x, y