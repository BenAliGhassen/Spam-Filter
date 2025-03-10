import string

punct = string.punctuation ='؟'


def count_punc(text) :
    count = sum([1 for char in text if char in punct])
    return round (count / (len(text) - text.count(' ')),3 )*100





def count_cap(text) :
    count = sum([1 for char in text if char.isupper()])
    return round (count / (len(text) - text.count(' ')),3 )*100

def length(text) :
    counter = 0
    for i in range(len(text)) : 
        if(text[i] == " "):    
            counter += 1
    return len(text) - counter