def check(sen):
    sen=sen.lower()
    vow=set("aeiou")
    s=set({})
    for char in sen:
        if char in vow:
            s.add(char)
        else:
            pass
    if len(s)==len(vow):
        print("consists of all vowels")
    else:
        print("does not consists of all vowels")
sen=input("enter a word:")
check(sen)