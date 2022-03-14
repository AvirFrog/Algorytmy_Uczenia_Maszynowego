import regex as re

with open("strona.txt", 'r', encoding='utf-8') as fh:
    fh = fh.read()
    emails= re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", fh)
    emails = set(emails)
    for email in emails:
        print(email)


fh.close()


