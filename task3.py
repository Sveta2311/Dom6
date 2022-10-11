# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# data = open(r"text.txt", "r", encoding="UTF-8")
# text = data.read()
# text = text.split(" ")
# data.close()
# print(text)
# new_text = ""

# for i in range(len(text)-1):
#     if (text[i].lower().find("абв") == -1):
#             new_text+= text[i]+" "

# data = open (r"text1.txt", "w", encoding="UTF-8")
# data.write(new_text)
# data.close()

# enumerate

with open(r"text.txt", "r", encoding="UTF-8") as data:
    text = data.read()
text = text.lower().split(" ")
new_txt = ''

for i, el in enumerate(text):
    if "абв" in el:
            text.pop(i)
for el in text:
    new_txt += el + ' '
        
with open (r"text1.txt", "w", encoding="UTF-8") as data:
    data.write(new_txt)
