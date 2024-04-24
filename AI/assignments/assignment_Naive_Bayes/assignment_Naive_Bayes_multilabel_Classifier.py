from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np

categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(
    subset='train', categories=categories, shuffle=True, random_state=42)
print(twenty_train.target_names)
print(len(twenty_train.data))

twenty_train.target[:10]
for t in twenty_train.target[:10]:
    print(twenty_train.target_names[t])

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts)

tf_transfotm = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transfotm.transform(X_train_counts)
print(X_train_tf.shape)

tfidf_transfotm = TfidfTransformer()
X_train_tfidf = tf_transfotm.fit_transform(X_train_counts)
print(X_train_tfidf.shape)


nbClassifier = MultinomialNB()
nbClassifier.fit(X_train_tfidf, twenty_train.target)
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf',
                    TfidfTransformer()), ('nbClassifier', MultinomialNB())])
text_clf.fit(twenty_train.data, twenty_train.target)

twenty_test = fetch_20newsgroups(
    subset='test', categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
print(np.mean(predicted == twenty_test.target))
