import json
from difflib import get_close_matches
with open('data.json') as myfile:
    data=myfile.read()
obj = json.loads(data)
while True:
    word = input("Enter word:")
    word=word.lower()
    if word in obj:
        definitions = obj[word]
        r = len(definitions)
        if r > 1:
            for i in range(r):
                print(" -->>" + str(definitions[i]))
        elif r == 1:
            print("-->>" + str(definitions[0]))
    elif word not in obj:
        matches = get_close_matches(word,obj)
        if len(matches)>=1:
            closematches = ",".join(matches)
            word_match = input("Did you mean one of following words: " + closematches + "?")
            if word_match in obj:
                definition_match = obj[word_match]
                r = len(definition_match)
                if r > 1:
                    for i in range(r):
                        print(" -->>" + str(definition_match[i]))
                elif r == 1:
                    print("-->>" + str(definition_match[0]))
            else:
                print("Please double check!There is not definition of the word you entered.")
        else:
            print("There is not definition of the word you entered.")
