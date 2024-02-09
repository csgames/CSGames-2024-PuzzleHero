# Tab supremacy

## Write-up

The provided file was composed of exclusively tabs and spaces. If you transformed tabs into ones and spaces into zeros (you had to guess which one was which but since tabs are superior, that gave you a hint that tabs = 1), you got an ASCII text as binary.

```python
def binary_to_ascii(binary_str):
    bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

    ascii_text = ''.join([chr(int(byte, 2)) for byte in bytes_list])

    return ascii_text

def main():
    with open('tab_supremacy.txt', 'r') as file:
        binary_data = ''.join(['1' if c == '\t' else '0' if c == ' ' else '' for c in file.read()])

    ascii_text = binary_to_ascii(binary_data)

    print("Texte ASCII résultant :")
    print(ascii_text)

if __name__ == "__main__":
    main()
```

## Flag

`flag{Em1li0IsRrighttab5-are-ind33dSuperiorTOSpaces}`