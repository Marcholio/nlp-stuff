# https://www.youtube.com/watch?v=FLZvOKSCkxY&t=11s
# https://www.youtube.com/watch?v=w36-U-ccajM&t=2s
# https://www.youtube.com/watch?annotation_id=annotation_2104835535&feature=iv&index=3&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&src_vid=w36-U-ccajM&v=yGKTphqxR9Q
# https://www.youtube.com/watch?annotation_id=annotation_4217019901&feature=iv&index=4&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&src_vid=yGKTphqxR9Q&v=6j6M2MtEqi8

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer

# === TUTORIAL 1 ===
example_text = """
  Hello there Mr. Smith, how are you doing today?
  Python is great.
  Sky is pinkish blue.
  Don't eat cardboard ples
  """

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

# === TUTORIAL 2 ===

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_text)

filtered = [w for w in words if not w in stop_words]

print(filtered)

# === TUTORIAL 3 ===
ps = PorterStemmer()

example_sentence = """It's really important to be pythonly while you're pythoning with python.
All pythoners have pythoned poorly at least once."""

words = word_tokenize(example_sentence)

for w in words:
  print(ps.stem(w))
  
# === TUTORIAL 4 ===

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
  try:
    for i in tokenized:
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)
      
      # print(tagged)
  except Exception as e:
    print(str(e))
    
process_content()