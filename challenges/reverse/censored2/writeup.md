# Censored 2

## Write-up

The second flag is censored with:

```python
def censor2(flag):
    out = ""
    for c in flag:
        if random() < 0.5:
            out += c
    if len(out) > 0.75 * len(flag):
        return censor1(flag)
    return out
```

Which means every time you get a flag, at least 75% of the letters
have been deleted

Since all letters are independently checked, the probability for a
letter to appear first reduces with position:

```
F L A G - B L A B L A
. . .
50% chances of being the first
  . .
  25% chances of being the first
    .
    (50%)^3 chances of being the first
```

Let's say the flag is FLAG-ABCDEFGHI

We can analyze a lot of different answers, sort them and get our first
letter :


    FLA-ABDE
    LABCH
    FLAG-DEFHI
    LGBCGHI
    FAEH
    AG-ABFGI
    FABDEGI
    AGACDEFG
    FLGAFGHI
    FA-DFG
    L-BCDG

The most common letter will be the first: F

If we trim that F from the start of every flag that contains it, we
can reuse those results to find the second letter

    LA-ABDE
    LABCH
    LAG-DEFHI
    LGBCGHI
    AEH
    AG-ABFGI
    ABDEGI
    AGACDEFG
    LGAFGHI
    A-DFG
    L-BCDG

The most common second letter is: L


We can trim the L from every flag that starts with that and repeat the
process to deduce the rest of the flag

## Flag

`FLAG{iasudY*YHUnr0fewq78ydgbu2i098haxjcjmi}`
