# girilen string her kelime kaç kez tekrarlandı?

print("bi seyler yaz")
text = input()

text = text.lower()
words = text.split()

# kelimeleri say
wordCount = {}
for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

# sonucu yazdır
print(wordCount)

# --------------------------------------------------------


