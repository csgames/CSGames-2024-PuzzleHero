# Alt

## Write-up

The web page contains HTML `<div>` blocks showing one letter each:


```html
<div id="pm">l</div>
<div id="dY">A</div>
<div id="LY">i</div>
<div id="we">y</div>
<div id="sg">g</div>
<div id="QC">v</div>
<div id="cF">o</div>
<div id="AI">r</div>
<div id="on">E</div>
<div id="ET">A</div>
<div id="lw">I</div>
<div id="RI">o</div>
<div id="YU">t</div>
```

The blocks are in a random order.

The web page has 10 000 possible alternate stylesheets. To avoid
crashing the browser, most of them are commented out in the HTML. The
different stylesheets change the position of the `<div>` blocks in the
page:

```css
#AQ{left:84.62831753899864px;top:1728.9018478601545px;}#Et{left:284.931007199969px;top:789.7886184887133px;}...
```

Those are absolute positions. 9 999 of the 10 000 stylesheets yield
random positions, and one of them uses positions that put the flag in
a diagonal line.

The first step is to gather all stylesheets:

```bash
$ for i in {0..9999} ; do wget $WEBSITE/s/a$i.css ; done
```

Next, parse the stylesheets, fit a line $y = mx + c$ in the list of
positions and dump the error for all files:

```python
#!/usr/bin/env python3

import numpy as np
import re

for i in range(10_000):
    with open(f'public/s/a{i}.css') as f:
        lines = f.readlines()[0].split('#')
        lines = [l for l in lines if l]

        positions = np.zeros((len(lines), 2))

        for pos, line in enumerate(lines):
            div_id, x, y = re.match(r'(..)\{left:(.+)px;top:(.+)px;\}', line).groups()
            positions[pos] = (x, y)

        # Fit a line in the points, see
        # https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        x = positions[:, 0]
        y = positions[:, 1]
        A = np.vstack([x, np.ones(len(x))]).T

        m, c = np.linalg.lstsq(A, y, rcond=None)[0]

        # Residual sum of squares
        print(i, ((y - (m * x + c)) ** 2).sum())
```

Check which CSS file yields the smallest error with

```bash
$ ./solve.py | sort --numeric-sort -k 2 | sed 5q

6431 281.8534038069672
2971 25240439.561322838
8441 26826947.53689649
6304 26896452.6950183
4442 27096489.21625124
```

The stylesheet `a6431.css` is the answer. Use this stylesheet in
`index.html` to read the flag.


## Flag

`FLAG-ILoveCSSSoMuch-IReallyReallyLikeToUseTheImportantKeywordEverywhereAndAlsoPutingTheZIndexAt99999999ItsJustSoConvenientAsALanguage`
