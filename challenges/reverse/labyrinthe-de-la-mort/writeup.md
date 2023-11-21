# Le Labyrinthe de la MORT

## Write-up

The template arguments have requirements that must be satisfied in
order for the code to compile. These are constraints that can be
satisfied by searching through by hand, or by using a fancy
backtracker.

For instance :

```c++
    (par % 2 == 0) and
    (par % 6 == 4) and
    ...
    (par % 19 == 0) and
```

`par` is the second template argument, which is printed as a char
later. With those constraints in bind, the only possible value is
`76`.

This value can be reused to guess other values :

```c++
    (Conçu * par * l_esprit == 345800) and
    (Conçu % par == 70) and
```

`Conçu` is thus `70` and `l_esprit` is `65`.

The full answer is :

```c++
    Flag<70,  76,  65,  71,  45,  101, 115,  84, 109, 112, 108, 97, 77, 83, 114, 115, 101, 110, 80, 108, 117,  81, 117, 105, 110,  97, 117, 116, 111, 114> f;
```

which successfully compiles the code and allows to print the flag :

```bash
$ g++ --std=c++20 labyrinthe.cpp -o labyrinthe
$ ./labyrinthe
FLAG-LesTemplatesMeStressentPlusQueLeMinotaure
```

## Flag

`FLAG-LesTemplatesMeStressentPlusQueLeMinotaure`
