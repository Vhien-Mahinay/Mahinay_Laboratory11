Word_count = 0
Listofwords = []
Matched_words = []

while Word_count < 10:
    Word_input = input("Enter a word of your choice:")
    Listofwords.append(Word_input)
    Word_count += 1
num = int(input("Enter a number to determine the words that match the count of letters:"))
for i in Listofwords:
    if len(i) >= num:
        Matched_words.append(i)
print(Matched_words)


    