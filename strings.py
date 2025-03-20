#strings
sentence="the quick brown fox jumps over the lazy dog"
#builtin functionality
#functoins
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.count("fox"))
print(sentence.isspace())

sentence=""

if sentence.isspace() or sentence.isdigit() or sentence.isnumeric():
    print("incorrect name")
else:
    print(" correct name")