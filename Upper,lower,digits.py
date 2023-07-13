sentence = input("Enter a sentence\n")
wordlist = sentence.split(" ")
print("The sentence has ", len(wordlist), " words")
digcnt = upcnt = locnt = 0
for ch in sentence:
    if ch.isdigit():
        digcnt += 1
    elif ch.isupper():
        upcnt += 1
    elif ch.islower():
        locnt += 1
print("This sentence has", digcnt, "digits", upcnt, "upper case letters", locnt, "lower case letters.")
