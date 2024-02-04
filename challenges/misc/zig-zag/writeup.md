# Zig Zag

## Write-up

Le défi montre une chaîne de caractère écrit en utilisant le `rail fense cipher` aussi connu sous le nom de `zigzag cipher`.
Cette informations pouvait être déduite en lisant le message et en regardant l'image. Dans cette algorithme, nous avons besoin du nombre de `rails` ici représenté dans l'image par la version de ruby on rails (7).

Une fois ces informations, il est possible de retrouver le code d'origine:

```go
package main

import (
	"fmt"
	"strings"
    "os"
)

func rf_cipher(els int, n int) []int {
	var rails [][]int
	rail, d := 0, 1

	for i := 0; i < els; i++ {
		if rail <= n {
			rails = append(rails, []int{})
		}
		rails[rail] = append(rails[rail], i)
		if (rail+d) < 0 || n <= (rail+d) {
			d *= -1
		}
		rail += d
	}
	result := []int{}
	for _, slice := range rails {
		result = append(result, slice...)
	}
	return result
}

func decode(s string, n int) string {
	text := make([]string, len(s))
	for start, end := range rf_cipher(len(s), n) {
		text[end] = string(s[start])
	}
	return strings.Join(text, "")
}

func main() {
    b, _ := os.ReadFile("message.txt")
    message := string(b)

    fmt.Println(decode(message, 7))
}
```

Cela nous donne le code en ruby suivant:

```rb
word.each_char.map.with_index { |c, i| (c.ord + 1 ^ 'potato'[i % 6].ord).chr }.join # \x17\x02\x16\t\b4B\a/\x03\x1C]\x1F!\x0E(@.\x15\x11
```

il est donc possible de faire le comportement inverse

```rb
word = "\x17\x02\x16\t\b4B\a/\x03\x1C]\x1F!\x0E(@.\x15\x11"
p word.each_char.map.with_index { |c, i| ((c.ord ^ 'potato'[i % 6].ord) - 1).chr }.join
```

## Flag

`flag{Z1gZag1nMyH3@d}`