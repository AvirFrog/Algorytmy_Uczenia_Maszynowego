import json
import regex as re

with open('wulgaryzmy.json', 'r', encoding='utf-8') as fh:
    wulgarki = json.load(fh)

while True:
    wulgaryzm = input("Podaj wulgaryzm: ")

    if wulgaryzm != 'Koniec !@#$%^&':

        regex = re.compile('|'.join(re.escape(x) for x in wulgarki))

        cenzura = re.sub(regex, '!@#$%^&', wulgaryzm)

        ocenzurowane = re.sub(r'\p{L}*[-]+\p{L}+', '---', cenzura)
        print(ocenzurowane)
    else:
        break

