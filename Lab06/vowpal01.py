# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:49:09 2022

@author: AvirFrog
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import re
import subprocess

#stworzenie dataframe z pliku csv
mails = pd.read_csv('spam_ham_dataset.csv')

#naprawa csv tak by działało w wabbice
mails = mails[["text", "label_num"]]
all_cols = list(mails)
mails[all_cols] = mails[all_cols].astype('str')
mails["label_num"] = mails["label_num"].astype(int)
mails["label_num"] = mails["label_num"].replace(0, -1)
mails["text"] = mails["text"].apply(lambda x: re.sub(r'\r\n', ' ', x))
mails["text"] = mails["text"].apply(lambda x: re.sub(r'Subject:', '', x))
mails["text"] = mails["text"].apply(lambda x: re.sub(r':', '', x))

#podzielenie dataframe na dwa zbiory, uczący i testowy
mail_train, mail_test = train_test_split(mails, test_size=0.1)

#zapis data frame  do csv
mail_train.to_csv("spam_ham_train.csv", header=True, index=False)
mail_test.to_csv("spam_ham_test.csv", header=True, index=False)

#zmienne z nazwami 
spam_ham_train = "spam_ham_train_vowpal.txt"
spam_ham_test = "spam_ham_test_vowpal.txt"
spam_ham_model = "spam_ham_model_vowpal.vw"
spam_ham_preds = "spam_ham_preds_vowpal.txt"

#odpalanie komend subprocesem
with open(spam_ham_train, 'w') as fh:
    subprocess.run('python3 csv2vw.py spam_ham_train.csv --label label_num'.split(), stdout=fh)
with open(spam_ham_test, 'w') as fh:
    subprocess.run('python3 csv2vw.py spam_ham_test.csv --label label_num'.split(), stdout=fh)
subprocess.run(f"vw -d {spam_ham_train} -f {spam_ham_model}".split())
subprocess.run(f"vw -d {spam_ham_test} -i {spam_ham_model} -p {spam_ham_preds} --binary".split())

#ewaluacja
values = pd.read_csv("spam_ham_test.csv")["label_num"].astype(int).to_numpy()
values[values == 0] = -1
with open(spam_ham_preds, 'r') as fh:
    prediction = np.array([int(val.strip()) for val in fh])

true_positive = ((values == 1) & (prediction == 1)).sum()
true_negative = ((values == -1) & (prediction == -1)).sum()
false_positive = ((values == -1) & (prediction == 1)).sum()
false_negative = ((values == 1) & (prediction == -1)).sum()

print("\n" * 3)
print("Ewaluacja: ")
print(f"Accuracy = {(values == prediction).sum() / len(prediction)}")
print(f"Precision = {true_positive / (true_positive + false_positive)}")
print(f"Recall = {true_positive/ (true_positive + false_negative)}")

