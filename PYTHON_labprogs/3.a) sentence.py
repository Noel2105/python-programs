try:
    sent = input("Enter a sentence")
    prev = sent[0]
    up = low = dig = sym = 0
    w = 1
    for i in sent:
        if i == " " and prev == " ":
            continue
        elif i.isupper():
            up += 1
        elif i.islower():
            low += 1
        elif i.isdigit():
            dig += 1
        elif i == " ":
            w += 1
        else:
            sym += 1
        prev = i
    print("The sentence has ", up, "uppercase,", low, "lowercase,", dig, "digits", sym, "symbols and", w, "words")
except(Exception):
    print("Enter a valid sentence")