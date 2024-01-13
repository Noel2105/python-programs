import re
phpat=re.compile(r'\+\d{12}')
mailpat=re.compile(r'[A-Za-z0-9._]+@[A-Za-z]+\.[A-Z|a-z]{2,}')
with open('example','r') as f:
    for line in f:
        matches=phpat.findall(line)
        for match in matches:
            print(match)
        matches=mailpat.findall(line)
        for match in matches:
            print(match)