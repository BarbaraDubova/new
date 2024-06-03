def word_frequency(text):
    text = text.lower()
    words = text.split()

    slovar = {}
    
    for word in words:
        if word in slovar:
            slovar[word] += 1
        else:
            slovar[word] = 1
    
    return slovar

text = "world World hello Hello"
print(word_frequency(text))