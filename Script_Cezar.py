message = input("Введите сообщение: ") #Hello world H=72
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ch>="A" and ch<="Z":
         pos = ord(ch) - ord('A')
         pos = (pos + offset) % 26
         new_char = chr(pos + ord("A"))
         encoded_message+=new_char
    elif ch>="a" and ch<="z":
         pos = ord(ch) - ord('a')
         pos = (pos + offset) % 26
         new_char = chr(pos + ord("a"))
         encoded_message+=new_char
    else:
         encoded_message+=ch

print(encoded_message)