from secrets import randbelow

from services.wordlist import words as wordlist

wordlist_length = 10000

def generate_password(titlecase=False, separators=False, length=4, numbers=2) -> str:
    pp = ""
    words = []
    
    for i in range(length):
        if titlecase:
            words.append(wordlist[randbelow(wordlist_length)].title())
        else:
            words.append(wordlist[randbelow(wordlist_length)])
    pp = words[0]
    for word in words[1:]:
        sep = "!@#$%^&*"[randbelow(8)] if separators else " "
        pp += sep + word
    for i in range(numbers):
        pp += str(randbelow(10))

    return(pp)