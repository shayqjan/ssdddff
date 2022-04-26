from deep_translator import GoogleTranslator
text = input("inter numberv")
shayq = GoogleTranslator(source= "fa", target= "en").translate(text)
print (shayq)