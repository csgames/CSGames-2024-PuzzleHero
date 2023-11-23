# wat

## Write-up

I wanted to make a reverse engineering challenge in a less common
"language" :^)

The intermediate representation is in the Gimple family
https://gcc.gnu.org/wiki/GIMPLE

As the challenge description suggests, the file `wat.c` does some
weird pointer things:

```c
  void* waaaaaaaat[26];
  void** wow_la = waaaaaaaat + 26;
  void* wat0();
  void* wat1();
  void* wat2();
  void* wat3();
```

We can already see :

- `waaaaaaaat` is an array of 26 untyped (`void*`) pointers. Because
  of how C arrays work, this is basically a `void**`
- `wow_la` is a pointer to the end of `waaaaaaaat`

This means that :

```c
wow_la == &waaaaaaaat[26]
*wow_la == waaaaaaaat[26]
*(wow_la - 1) == waaaaaaaat[25]
*(wow_la - 26) == waaaaaaaat[0]
```

We can use `wow_la` to access the same things as `waaaaaaaat`.

The functions

```c
  void* wat0();
  void* wat1();
  void* wat2();
  ...
```

all return untyped pointers. We can look at the provided Gimple IR:

```
wat0 ()
{
  void * D.2943;

  putchar (76);
  wow_la.0_1 = wow_la;
  D.2943 = MEM[(void * *)wow_la.0_1 + -168B];
  return D.2943;
}
```

All `wat...()` functions return a pointer that looks like an entry
from `wow_la` at a negative offset.

The start of the Gimple main() looks like this :

```
  wow_la.26_1 = wow_la;
  _2 = wow_la.26_1 + 18446744073709551408;
  *_2 = wat0;

  wow_la.27_3 = wow_la;
  _4 = wow_la.27_3 + 18446744073709551416;
  *_4 = wat1;

  wow_la.28_5 = wow_la;
  _6 = wow_la.28_5 + 18446744073709551424;
  *_6 = wat2;

  ...
```

The large numbers such as:

```
_2 = wow_la.26_1 + 18446744073709551408;
```

Are actually negative numbers (2's complement) on 64 bits, in pointers
arithmetic.

Thus, `18446744073709551408` corresponds to :

```
    18446744073709551408

=>  1111111111111111111111111111111111111111111111111111111100110000
    |
  -2**63 + 111111111111111111111111111111111111111111111111111111100110000(bin)

=> -208
```

In a void*[], each slot in the array occupies 8 bytes. Thus, -208
corresponds to `-26` in pointers arithmetic.

From the first block:

```
  wow_la.26_1 = wow_la;
  _2 = wow_la.26_1 + 18446744073709551408;
  *_2 = wat0;
```

We get that:

```
  wow_la[-26] = wat0
```

or equivalently:

```
waaaaaaaat[0] == wat0
```

We can apply the same logic for the rest, and see that

```
waaaaaaaat[0] == wat0
waaaaaaaat[1] == wat1
waaaaaaaat[2] == wat2
...
```

Next we can see that the `wat...()` functions all follow the pattern :

```
wat0 ()
{
  void * D.2943;

  putchar (76);
  wow_la.0_1 = wow_la;
  D.2943 = MEM[(void * *)wow_la.0_1 + -168B];
  return D.2943;
}
```

Which is :

1. putchar() one character
2. Return something fetched from `wow_la` at a negative offset (again,
   with pointers arithmetic)

`wow_la` contains addresses of `wat...()` functions.

The end of the `main()`:

```
  beab2edb5fd1f1deee0ca6419ca2e8d2 = wat3;
  f92be48cfa44ab468cb386b86167c66b = wat12;
  goto <D.2941>;
  <D.2940>:
  f92be48cfa44ab468cb386b86167c66b.52_53 = (void * (*<T561>) (void)) f92be48cfa44ab468cb386b86167c66b;
  f92be48cfa44ab468cb386b86167c66b = f92be48cfa44ab468cb386b86167c66b.52_53 ();
  if (f92be48cfa44ab468cb386b86167c66b == beab2edb5fd1f1deee0ca6419ca2e8d2) goto <D.2995>; else goto <D.2996>;
  <D.2995>:
  goto <D.2939>;
  <D.2996>:
  beab2edb5fd1f1deee0ca6419ca2e8d2 = f92be48cfa44ab468cb386b86167c66b;
  <D.2941>:
  if (beab2edb5fd1f1deee0ca6419ca2e8d2 != 0B) goto <D.2940>; else goto <D.2939>;
  <D.2939>:
```

(cleaned up a bit for lisibility)

```
  aaaa = wat3;
  bbbb = wat12;
  goto LOOP_CONDITION;
  LOOP_BODY1:
  bbbb.52_53 = (void * (*<T561>) (void)) bbbb;
  bbbb = bbbb.52_53 ();
  if (bbbb == aaaa) goto BREAK; else goto LOOP_BODY2;
  BREAK:
  goto LOOP_END;
  LOOP_BODY2:
  aaaa = bbbb;
  LOOP_CONDITION:
  if (aaaa != 0B) goto LOOP_BODY1; else goto LOOP_END;
  LOOP_END:
```

can be decoded as something like:


```
  aaaa = wat3;
  bbbb = wat12;
  while(aaaa != 0) {

      bbbb.52_53 = (void * (*<T561>) (void)) bbbb;

      bbbb = bbbb.52_53 ();

      if (bbbb == aaaa)
          break;
      aaaa = bbbb;
  }
```

ie, while `aaaa` is non-zero, call one of the functions `wat...()`
(starting with wat12) and get another function in `bbbb`.

If `bbbb` is the same as `aaaa`, break.

On the next round, `bbbb` is stored in `aaaa`

This loop works similar to what a trampoline does. Each function
returns a pointer to the next function to call
https://en.wikipedia.org/wiki/Trampoline_(computing)

Thus, `bbbb` is the current function called and `aaaa` is the previous
one. If a function returns itself as the next to be called, the loop
stops.

From there, you can evaluate the different `wat...()` functions and
extrapolate the solution.

## Flag

`FLAG{Scott Michael Gimple}`


## Original `wat.c` source code

The original code looks like this :

```c
#include <stdlib.h>
#include <stdio.h>

void* waaaaaaaat[26];
void** wow_la = waaaaaaaat + 26;

void* wat0();
void* wat1();
void* wat2();
void* wat3();
void* wat4();
void* wat5();
void* wat6();
void* wat7();
void* wat8();
void* wat9();
void* wat10();
void* wat11();
void* wat12();
void* wat13();
void* wat14();
void* wat15();
void* wat16();
void* wat17();
void* wat18();
void* wat19();
void* wat20();
void* wat21();
void* wat22();
void* wat23();
void* wat24();
void* wat25();

void* wat0() {putchar('L');return wow_la[-21];}
void* wat1() {putchar('m');return wow_la[-7];}
void* wat2() {putchar('l');return wow_la[-12];}
void* wat3() {putchar('G');return wow_la[-4];}
void* wat4() {putchar('t');return wow_la[-15];}
void* wat5() {putchar('A');return wow_la[-23];}
void* wat6() {putchar('G');return wow_la[-8];}
void* wat7() {putchar('l');return wow_la[-16];}
void* wat8() {putchar('i');return wow_la[-2];}
void* wat9() {putchar('h');return wow_la[-3];}
void* wat10() {putchar('e');return wow_la[-5];}
void* wat11() {putchar('t');return wow_la[-11];}
void* wat12() {putchar('F');return wow_la[-26];}
void* wat13() {putchar('M');return wow_la[-18];}
void* wat14() {putchar(' ');return wow_la[-20];}
void* wat15() {putchar(' ');return wow_la[-13];}
void* wat16() {putchar('S');return wow_la[-1];}
void* wat17() {putchar('e');return wow_la[-24];}
void* wat18() {putchar('i');return wow_la[-25];}
void* wat19() {putchar('p');return wow_la[-19];}
void* wat20() {putchar('o');return wow_la[-22];}
void* wat21() {putchar('}');return wow_la[-5];}
void* wat22() {putchar('{');return wow_la[-10];}
void* wat23() {putchar('a');return wow_la[-9];}
void* wat24() {putchar('c');return wow_la[-17];}
void* wat25() {putchar('c');return wow_la[-6];}

void main() {
    wow_la[-26] = &wat0;
    wow_la[-25] = &wat1;
    wow_la[-24] = &wat2;
    wow_la[-23] = &wat3;
    wow_la[-22] = &wat4;
    wow_la[-21] = &wat5;
    wow_la[-20] = &wat6;
    wow_la[-19] = &wat7;
    wow_la[-18] = &wat8;
    wow_la[-17] = &wat9;
    wow_la[-16] = &wat10;
    wow_la[-15] = &wat11;
    wow_la[-14] = &wat12;
    wow_la[-13] = &wat13;
    wow_la[-12] = &wat14;
    wow_la[-11] = &wat15;
    wow_la[-10] = &wat16;
    wow_la[-9] = &wat17;
    wow_la[-8] = &wat18;
    wow_la[-7] = &wat19;
    wow_la[-6] = &wat20;
    wow_la[-5] = &wat21;
    wow_la[-4] = &wat22;
    wow_la[-3] = &wat23;
    wow_la[-2] = &wat24;
    wow_la[-1] = &wat25;

    void* beab2edb5fd1f1deee0ca6419ca2e8d2 = &wat3; // TODO: renommer en quelque chose de mêlant genre <D.2899>;
    void* f92be48cfa44ab468cb386b86167c66b = &wat12;
    while(beab2edb5fd1f1deee0ca6419ca2e8d2) {
        f92be48cfa44ab468cb386b86167c66b = ((void* (*)(void)) f92be48cfa44ab468cb386b86167c66b)();
        if(f92be48cfa44ab468cb386b86167c66b == beab2edb5fd1f1deee0ca6419ca2e8d2)
            break;
        beab2edb5fd1f1deee0ca6419ca2e8d2 = f92be48cfa44ab468cb386b86167c66b;
    }
    putchar(10);
}
```
