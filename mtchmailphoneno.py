import re
ph_regexp=re.compile(r'\+\d{12}')
email_regexp=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{2,}')
with open('trial.txt','r') as f:
    for line in f:
        matches=ph_regexp.findall(line)
        for match in matches:
            print(match)
        matches=email_regexp.findall(line)
        for match in matches:
            print(match)