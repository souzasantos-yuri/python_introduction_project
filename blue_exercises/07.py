#Create a program that counts the ocurrences of the letter "a" on a word

word = input("Tell me any word: ")

qty = 0

for i in word:
    if i == "a":
        qty += 1

print(f"This word has {qty} ocurrences of 'a'")