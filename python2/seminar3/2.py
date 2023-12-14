text = 'Hello world. Hello python. Hello again. a a a a a a a a a a b b b b b c c c c d d d e e e f f f g h i j'
signs = '.,/[]{}`~!@#$%^&*()-_+=\\":;<>?\''
#print(text, signs)

for s in signs:
    text = text.replace(s,'')
#print(text)

text = text.lower()
words = text.split()
#print(words)

freq = {}
for word in words:
    freq[word]=freq.get(word,0) + 1
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
backpack = sorted_freq[0:10]
print(backpack)
