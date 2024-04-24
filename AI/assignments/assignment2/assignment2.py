import numpy as np
import re
import nltk
from sklearn.datasets import load_files
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from nltk.tokenize import  word_tokenize

#function
def preprocess_text(text, exclude_regex=False):
    # remove esape character
    text = text.replace("\n", " ").replace("\r", " ")
    #lowercase
    text = text.lower()
    #remove case reernces and citaions- Jan Purchase Regex
    if exclude_regex:
        pattern = r"(([A-Z] [A-Za-z\s]*\v.\ [A-Za-z]+(\s[A-Za-z]+)*,)?\s[0-9]*\s(U\.\sS\.|Wall\.|Rev\.)|[Ii]d\.)(\s?[0-9]*)|(,\s(at\s)?[0-9\-]+)" 
        clean_text =re.sub(pattern,"",text, flags = re.IGNORECASE)
        clean_text = re.sub(r'\W', ' ', clean_text)
        text = clean_text
    #tokenize
    tokens = word_tokenize(text)
    #remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    print(tokens)
    return tokens

nltk.download("stopwords")
stemmer = WordNetLemmatizer()
comment_data = load_files(
    r"D:\repository\python_example\AI\assignments\assignment2\data")
x, y = comment_data.data, comment_data.target
documents = []
plt.scatter(x, y)

for sen in range(0, len(x)):
#     # remove all the special characters
    document = re.sub(r'\W', ' ', str(x[sen]))
#     # remove all single chatacters
#     document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
#     # Remove single character from the start
#     document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
#     # Substituting multiple spaces with single space
#     document = re.sub(r'\s+', ' ', document, flags=re.I)
#     # removing prefixed 'b'
   
#     documnet = re.sub(r'^b+', '', document, flags=re.I)
#     print("----",documnet)
#    # print("====", document)
#     #documnet = remove_b(document)
#     #print('----------------')
    
#     # Convert to lowercase
#     document = document.lower()
#     # Lemmatization
#     document = document.split()
#     print('after ->', documnet)
#     document = [stemmer.lemmatize(word) for word in document if word != 'b' ]
#     print("->", document)
#     print('----------------')
#     document = ' '.join(document)
    document = preprocess_text(document,True)
    documents.append(document)

tfidfconverter = TfidfVectorizer(
    max_features=8, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(documents).toarray()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
clf = KNeighborsClassifier().fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(y_pred)

print("======= Report =======")
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
