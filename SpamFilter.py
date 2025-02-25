from langdetect import detect


text = "Bonjour, comment ça va ?"  
language = detect(text)  
print(language)

text2 = "مرحبًا، هل لديك أخبار عن خالد؟"
language = detect(text2)
print(language)

text3 = "Hello Word"
language = detect(text3)
print(language)

TextIn = input('Tapez un message : ')
language =detect(TextIn) 
print(language)

if(language == 'fr') : 
    print("Model 2")
elif(language =='en'):
    print('model 1')
elif(language == 'ar'):
    print('model 3')
else : 
    print('language not supported')       