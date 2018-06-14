import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        # similarity
        match = get_close_matches(w, data.keys())[0] 
        choose =  input("did you mean %s instead? enter Y if yes, or N if no: " %match)
        if choose == "Y":
            return data[match]
        elif choose == "N":
            return "the word doesn't exist, check it again"
        else:
            return "we didn't understand your query"
    else:
        return "the word doesn't exist, check it again"
    
word = input("enter a word : ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
