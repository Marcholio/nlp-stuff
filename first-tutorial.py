# https://www.youtube.com/watch?v=FLZvOKSCkxY&t=11s

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = """
  Hello there Mr. Smith, how are you doing today?
  Python is great.
  Sky is pinkish blue.
  Don't eat cardboard ples
  """

print(sent_tokenize(example_text))
print(word_tokenize(example_text))
