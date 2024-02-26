# Tab Supremacy

## Write-up

The provided `tab_supremacy.txt` file was composed of only three characters: tabs, spaces and one LF at the end. These characters were a binary representation of an ASCII text. You could either assign tabs to 0 or 1, but the challenge's title gave you an hint (it was 1). The result was the flag.

### Possible solution script

```python
def binary_to_ascii(binary_str):
    bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

    ascii_text = ''.join([chr(int(byte, 2)) for byte in bytes_list])

    return ascii_text

def main():
    with open('./tab_supremacy.txt', 'r') as file:
        binary_data = ''.join(['1' if c == '\t' else '0' if c == ' ' else '' for c in file.read()])

    ascii_text = binary_to_ascii(binary_data)

    print("Texte ASCII résultant :")
    print(ascii_text)

if __name__ == "__main__":
    main()
```

## Flag

`flag{Em1li0IsRrighttab5-are-ind33dSuperiorTOSpaces}`