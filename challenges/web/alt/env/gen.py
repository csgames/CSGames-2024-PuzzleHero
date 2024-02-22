#!/usr/bin/env python3

from random import shuffle, randint, random, seed, choice
import string

seed(32897)
NB_STYLESHEETS = 10_000

good_stylesheet = 6431 #randint(0, NB_STYLESHEETS - 1)

flag = 'FLAG-ILoveCSSSoMuch-IReallyReallyLikeToUseTheImportantKeywordEverywhereAndAlsoPutingTheZIndexAt99999999ItsJustSoConvenientAsALanguage'

divs = []
ids = []

all_generated_ids = set()
all_generated_ids.add('')

def gen_id(length):
    id = ''
    while id in all_generated_ids:
        id = ''.join(choice(string.ascii_letters) for i in range(length))
    all_generated_ids.add(id)
    return id


for i, letter in enumerate(flag):
    id = gen_id(2)
    ids.append(id)
    divs.append(f'''<div id="{id}">{letter}</div>''')

shuffle(divs)

assert len(set(ids)) == len(ids), f"Nooo! Some ids are not unique in the divs: {len(set(ids))} != {len(ids)}"

min_x = 19 * 0 + 0 * 5 - 2.5
max_x = 19 * (len(flag) -1) + 1 * 5 - 2.5

min_y = 13.7 * 0 + 0 * 4 - 2
max_y = 13.7 * (len(flag) -1) + 1 * 4 - 2

for i in range(NB_STYLESHEETS):

    with open(f's/a{i}.css', 'w') as f:
        lines = []
        if i == good_stylesheet:
            # Follow a straight diagonal line
            for i, id in enumerate(ids):
                x = 19 * i + random() * 5 - 2.5
                y = 13.7 * i + random() * 4 - 2
                lines.append('#' + str(id) + '{position:absolute;left:' + str(x) + 'px;top:' + str(y) + 'px;}')
        else:
            # Random positions
            for i, id in enumerate(ids):
                x = random() * (max_x - min_x) + min_x
                y = random() * (max_y - min_y) + min_y
                lines.append('#' + str(id) + '{position:absolute;left:' + str(x) + 'px;top:' + str(y) + 'px;}')
        shuffle(lines)
        f.write(''.join(lines))


print('''
<!doctype html>
<html>
    <head>
        <title></title>
        <meta charset="utf-8" />
'''.strip())

stylesheets_ids = []

for i in range(NB_STYLESHEETS):
    id = gen_id(3)

    if i == min(NB_STYLESHEETS - 1, 10):
        print('''<!--
===============
/!\ WARNING /!\\
===============

Alt stylesheets are really cool, but the dumb browser manufacturers
won't optimize their browser enough to allow me to use all the alt
stylesheets I need

They say it can ***CRASH*** your browser if you force it to load all
of them at once... I have a bug report opened for that but the
bastards won't fix it''')

    rel = "stylesheet alternate" if i > 0 else "stylesheet"
    print(f'''<link rel="{rel}" type="text/css" href="s/a{i}.css" title="{id}"/>''')

    stylesheets_ids.append(id)

assert len(set(stylesheets_ids)) == len(stylesheets_ids), "Nooo! Some ids are not unique in the stylesheets"

print('''
-->
    </head>
    <body>
''')

for div in divs:
    print(div)

print('''
    </body>
</html>
''')
