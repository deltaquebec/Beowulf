from nltk.stem import WordNetLemmatizer
import ety

lemmatizer = WordNetLemmatizer()

word = 'kings'
lemma = lemmatizer.lemmatize(word, pos='n')
print(lemma)  # 'dog'

def classify_language_family(word):
    origins = ety.origins(word)
    germanic_languages = ['ang', 'enm', 'eng', 'non', 'goh', 'gmh', 'osx', 'got']
    romance_languages = ['lat', 'fro', 'frm', 'fra', 'ita', 'spa', 'por', 'ron']
    
    for origin in origins:
        if origin.language.iso in germanic_languages:
            return 'Germ.'
        if origin.language.iso in romance_languages:
            return 'Lat.'
    
    return None

word = 'god'
language_family = classify_language_family(word)

if language_family:
    print(f"Etymology for '{word}':\n{language_family}")
else:
    print(f"No Germanic or Romance etymology found for '{word}'.")
