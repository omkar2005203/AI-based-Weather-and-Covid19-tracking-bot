import re 

def numext(chat):
    numbers = re.findall('\d+',chat)

    return numbers