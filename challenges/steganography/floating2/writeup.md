# Floating 2

Même principe que le premier Floating, mais la payload est cachée dans
le signe + les 23 bits de mantisse d'un gros paquet de NaN


```c++
#include <iostream>
#include <cassert>
#include <array>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <fstream>
#include <istream>

using namespace std;

int main() {

    ifstream infile("challenge.dat");

    unsigned int c = infile.get();

    do {
        unsigned int b1 = c;
        unsigned int b2 = infile.get();
        unsigned int b3 = infile.get();
        unsigned int b4 = infile.get();

        assert(b1 == (b1 & 0xFF));
        assert(b2 == (b2 & 0xFF));
        assert(b3 == (b3 & 0xFF));
        assert(b4 == (b4 & 0xFF));

        unsigned int data = 0;

        data |= b4;
        data <<= 8;
        data |= b3;
        data <<= 8;
        data |= b2;
        data <<= 8;
        data |= b1;

        c = infile.get();

        float f = *reinterpret_cast<float*>(&data);

        if(f != f) {
            printf("%p\n", data);
        }

    } while(c != -1);

    return 0;
}
```


Avec les valeurs obtenues :

    0x7fe66c61
    0x7fe77b63
    0x7fe1726c
    0x7ff92d72
    0x7fe1652d
    0x7fea6570
    0x7ff36967
    0x7fee6564
    0x7fad696e
    0x7ff46567
    0x7fe5727d

On peut extraite le bit de signe + les 23 derniers bits de mantisse :

```python
values = [
    0x7fe66c61,
    0x7fe77b63,
    0x7fe1726c,
    0x7ff92d72,
    0x7fe1652d,
    0x7fea6570,
    0x7ff36967,
    0x7fee6564,
    0x7fad696e,
    0x7ff46567,
    0x7fe5727d,
]

def extract_bits(val):
    binary = bin(val)[2:].zfill(32)

    return binary[0] + binary[9:]

toute = ""

for val in values:
    toute += extract_bits(val)

for pos in range(0, len(toute), 8):
    print(chr(int(toute[pos:pos+8], 2)), end='')
print()
```

## Flag

`flag{carly-rae-jepsigned-integer}`
