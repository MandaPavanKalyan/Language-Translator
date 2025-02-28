from langdetect import detect
import googletrans

sentence=input(str("enter the sentence:" ))
print(detect(sentence))

#print(googletrans.LANGCODES)

language=input("Type the translation language code:").lower()

translator=googletrans.Translator()
translation=translator.translate(text=sentence,dest=language)
print("Translation: ",translation.text)
print(detect(translation.text))
