
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pickle

stop_words = set(stopwords.words('english')) 
tokenize = word_tokenize

doc_frequency_dict_path = 'models/doc_frequency_dict.pkl'
with open(doc_frequency_dict_path, 'rb') as f:
    doc_frequency = pickle.load(f)



def tokenizer(s):
    
    """Wrapper tokenizer function
    
    Inputs
    ------
    
    s : str
    
    Returns
    -------
    
    tokens : list [str, ]
    """

    tokens =  tokenize(s.lower()) # apply the nltk tokenizer
    tokens = [t for t in tokens if doc_frequency[t]>5 and t not in stop_words]# and doc_frequency[t]<3000]
    
    return tokens


