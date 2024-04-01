import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.probability import FreqDist

text = "I think Amazon is making a great effort in adding engaging content but I can’t get past the ugly interface. It’s not as intuitive as other competing streaming services and if it weren’t lumped in with my Prime membership, I wouldn’t pay for the stand-alone service."
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filter_tokens = [token for token in tokens if token.lower() not in stop_words]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_tokens = [stemmer.stem(token) for token in filter_tokens]
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filter_tokens]
freq_dist = FreqDist(lemmatized_tokens)
print(freq_dist.most_common(5)) 

