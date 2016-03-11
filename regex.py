import re
while True:
    string = raw_input('string > ')
    print re.search(raw_input('search >'),string)
    if raw_input('Continue >') == 'No':
        break
    
        