# Floating

Le message était caché dans la partie exposant de chacun des flotant. Lorsque l'on représente un float en binaire (avec la norme IEEE754, la partie exposant est écrit su un octet). En prenant cet octet pour chaque flotant et en convertisant avec son caractère ASCII, on retrouve le flag.

```cpp
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

union float_bits {
    float value;
    uint32_t bits;

    explicit float_bits(float value) : value(value) {}
};

void print_char(float val) {
    float_bits f(val);
    unsigned char c = 0;

    for (int i = 30; i > 22; --i) {
        c <<= 1;
        c |= ((f.bits >> i) & 1);
    }

    std::cout << c;
}

int main(void) {
    std::ifstream file("message.txt");
    std::string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        float f;
        iss >> f;
        print_char(f);
    }

    return 0;
}
```

## Flag

`flag{TrU5t_m3_1m_@n_3nG1n33r}`