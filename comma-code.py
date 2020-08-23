#! python 3
# comma-code.py - put a comma in between items and an 'and' before the last item

def list(listothings) :
    for i in range (len(listothings)-1):
        print(listothings[i] + ',' , end= ' ')
        
spam = ['apples','bananas','tofu','cats']

list(spam)

print('and ' + spam[-1])

