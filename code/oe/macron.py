strings = ["ond","and","on","þonne","wið","to","þæt","þe","ne","ic","me","heo","him","he","swa","þis","mid","þu","ofer","his","þriwa","seo","hit","se","þas","cweð","þæs","in","sy","ða","ðy","ær","ðonne","næfre","þone","ge","ðas","þære","þam","is","of","gif","þæm","nu","under","wiþ","geond","æfter","ðis","do","hwæt","her","þurh","þus","lytel","æt","ðin","willian","cume","þeos","þara","are","cuman","com","ænig","þon","for","us","ac","bot","ende","wæs","wǣre","wes","wǣron","wǣren","wesað","ic","wit","wē","mīn","uncer","ūser","ūre","mē","unc","ūs","mec","uncit","ūsic","ðū","git","gē","ðīn","incer","ēower","ēowre","ðē","inc","ēow","ðec","incit","ēowic","hē","hēo","hīe","hit","hyt","hī","hȳ","hire","hira","heora","hiera","heom","hine","nǣr","nǣfre","nǣnig","nolde","noldon","be","beforan","betweox","for","from","fram","mid","tō","geond","oð","þurh","ofer","under","bēo","bist","biþ","bēoþ","bēon","ēom","sīe","eart","sī","is","sēo","sindon","sint","nēom","neart","nis","sīo","ðæt","tæt","ðæs","ðǣre","ðǣm","ðām","ðone","ðā","ðȳ","ðē","ðon","ðāra","ðǣra","ðes","ðēos","ðisse","ðeosse","ðises","ðisses","ðisum","ðissum","ðisne","ðās","ðīs","ðȳs","ðissa","ðeossa","ðeosum","ðeossum","twēgen","twā","tū","twēgra","twǣm","þrīe","þrēo","þrēora","þrīm","endlefan","twelf","twēntig","þrēotīene","þrītig","fēower","fēowertīene","fēowertig","fīf","fīftīene","fīftig","siex","siextīene","siextig","seofon","seofontīene","seofontig","eahta","eahtatīene","eahtatig","nigon","nigontīene","nigontig","tīen","hund","gā","gǣst","gǣð","gāð","gān","gānde","gangende","gegān","ēode","ēodest","ēodon","ēoden","ic","mīn","mē","mec","wit","uncer","unc","uncit","wē","ūser", "ūre","ūs","ūsic","ðū","ðīn","ðē","ðec","git","incer","inc ","incit","gē","ēower","ēowre","ēow","ēowic","hē","his","him","hine","hēo","hīe","hire","hit","hyt","hī","hȳ","hira","heora","hiera","heom","nǣre","nolde","noldon"]

# Define a dictionary that maps macrons to acute diacritics
diacritic_map = {'ā': 'á', 'ē': 'é', 'ī': 'í', 'ō': 'ó', 'ū': 'ú', 'ǣ': 'ǽ'}

# Define the output file name
output_file = "macron.txt"

# Iterate over each string in the list and replace macrons with acute diacritics
for i, s in enumerate(strings):
    for macron, acute in diacritic_map.items():
        s = s.replace(macron, acute)
    strings[i] = s

# Write the modified strings to the output file
with open(output_file, "w", encoding = "UTF-8") as f:
    for s in strings:
        f.write(s + "\n")

# Print a message to indicate that the file has been written
print(f"The modified strings have been written to {output_file}.")

