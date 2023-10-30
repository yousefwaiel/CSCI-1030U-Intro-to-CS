
sentence = 'ahmed runs quickly'

words = sentence.split(' ')

reverse_words = []

for n in range(len(words) - 1, -1, -1):
    reverse_words.append(words[n])

reverse_sentence = ''
for word in reverse_words:
    reverse_sentence += word + ' '

print(reverse_sentence)
