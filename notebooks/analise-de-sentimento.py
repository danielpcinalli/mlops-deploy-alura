from textblob import TextBlob

frase = "Python é ótimo para Machine Learning"

tb = TextBlob(frase)
tb_en = tb.translate(to='en')

print(tb_en.sentiment.polarity)