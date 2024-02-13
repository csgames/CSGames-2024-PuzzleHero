# Censored 3

## Write-up

The third flag is censored with:

```python
def censor3(flag):
    out = ""
    for i in range(randint(1, 5)):
        out += chr(randint(33, 126))
    for c in flag:
        out += c
        for i in range(randint(1, 5)):
            out += chr(randint(33, 126))
    return out
```

This adds and random amount of random garbage between the letters of
the flag.

There are various ways to solve this, this is my solution:

```python
data = [censor(flag) for i in range(30)] # Get a few censored flags

def get_first_letter(flags):
    out = dict()
    def add_to_count(letters):
        for l in letters:
            out[l] = out[l] + 1 if l in out else 1

    subsets = [''.join(set(f[:6])) for f in flags]

    for subset in subsets[1:]:
        add_to_count(subset)

    return sorted(out.items(), key=lambda f: -f[1])[0][0]

def trim_first_letter(letter, flags):
    out_flags = []

    for flag in flags:
        idx = flag.index(letter[:6])
        out_flags.append(flag[idx+1:])

    return out_flags

for i in range(len(flag)):
    l = get_first_letter(data)
    print(l, end='')
    data = trim_first_letter(l, data)

print()
```

## Flag

`FLAG{jis98(289iojf0j09A)*&65s7?*UJvjmampxo92g5}`
