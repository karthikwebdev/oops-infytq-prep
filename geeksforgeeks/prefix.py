num = int(input())
for i in range(num):
    n = int(input())
    li = list(input().split())
    for letter in range(len(min(li))):
        for word in li:
            if(min(li)[letter] != word[letter]):
                if(letter > 0):
                    print(len(word[:letter])+1)
                    break
                else:
                    print(-1)
                    break
        else:
            continue
        break
