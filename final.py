text = input("digite algo: ")

reversed = ""

for letter in text[::-1]:
    reversed += letter

print(reversed)
