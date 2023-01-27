import nltk
import numpy as np
import random
import string
f = open('Poem.txt','r', errors = 'ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)



sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]
remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))  

greet_inputs = ('hello', 'hi','whassup','how are you?')
greet_responses = ('hi','Hey', 'Hey There!', 'There there!!')
def greet(sentence):
  for word in sentence.split():
    if word.lower() in greet_inputs:
      return random.choice(greet_responses)
  
  
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  


def response(user_response):
  global robo1_response
  robo1_response = ''
  TfidVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
  tfidf = TfidVec.fit_transform(sentence_tokens)
  vals = cosine_similarity(tfidf[-1],tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf= flat[-2]
  if(req_tfidf ==0):
    robo1_response = robo1_response + "I am sorry. Unable to Understand You!"
    return robo1_response 
  else:
    robo1_response = robo1_response + sentence_tokens[idx]
    return robo1_response


flag = True
print("Hello! I am the Retrieval Learning Bot, whats your Query, For ending convo type bye!" )
while(flag == True):
  user_response = input()

  user_response = user_response.lower()
  if(user_response != 'bye'):
    if(user_response == ' Thank you' or user_response == " thanks"):
      flag = False
      print('Bot! you are very welcome')
     
    
    else:
      if(greet(user_response)!=None):
        print('Bot' + greet(user_response))
      else:
        sentence_tokens.append(user_response)
        word_tokens = word_tokens + nltk.word_tokenize(user_response)
        final_words = list(set(word_tokens))
        print('Bot: ' , end = '')
        print(response(user_response))
        sentence_tokens.remove(user_response)
        
  else:
    flag = False
    print("Bot: GoodBye!")

      
      
      