word = input()
if(word == word[::-1]):
    while(word):
        word = word[:len(word)-1]
        if(word == word[::-1]):
            pass
        else:
            break
    print(len(word))
else:
    print(len(word))
