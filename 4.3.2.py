def remove_word(Str,word):
    Str= Str.replace(word,' ')

    return Str
Str="hello  good good hello morning "
Str2=remove_word(Str,"hello")
print(Str2)



