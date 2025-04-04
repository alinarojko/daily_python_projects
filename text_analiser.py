from collections import Counter
import re
from functions import frequency

# Number of characters
user_input = str(input(("Enter a block of text for analysis: ")))
total_char = len(user_input)

# Number of words
words = user_input.split(" ")
total_words = len(words)

# Number of sentences
sentences = re.split(r'[.!?]', user_input)
total_sentences = len(sentences)

# Most common word
text = user_input.lower()
words = text.split()
word_counts = {}
for word in words:
    word = word.strip(',.!/?')
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_common_word = max(word_counts, key=word_counts.get)
frequency = word_counts[most_common_word]

# Average Word Length
av_word_len = float(total_char / total_words)

# Average Sentence Length
len_sentences = len(sentences)
av_sent_len = total_words / total_sentences

print("Text Analysis Result ")
print("_________________________")
print(f"Total Characters: {total_char}")
print(f"Total Words: {total_words}")
print(f"Total Sentences: {total_sentences}")
print(f"Most Frequent Word is : '{most_common_word}' (used {frequency} times)")
print(f"Average Word Length: {av_word_len}  characters")
print(f"Average Sentence Length: {av_sent_len}  words ")