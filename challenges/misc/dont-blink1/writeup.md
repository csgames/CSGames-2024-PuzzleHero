# Don't blink 1

## Write-up

As stated in the HTML comments:

```html
    <!-- XXX: I just found out <marquee> is considered obsolete :(((
         It seems that different browsers will show different things...
         Unless you like to waste your time, you should look at this challenge using Firefox.
    -->
```

In Firefox, each `<marquee>` tag shows its letter in the order :

1. First letter
2. Second letter
3. ...
N-1. Blank space
N. Blank space

So for instance, the first column:

```html
<pre><marquee direction="up" scrolldelay="1000" truespeed height="90" scrollamount="90">F</marquee></pre>
```

will show:

1. F
2. blank
3. blank

The second column will show:

```html
<pre><marquee direction="up" scrolldelay="1000" truespeed height="90" scrollamount="90">x<br>\<br>L</marquee></pre>
```

1. x
2. \
3. L
4. blank
5. blank

Third column will show:

```
<pre><marquee direction="up" scrolldelay="1000" truespeed height="90" scrollamount="90">q<br>A<br>E<br>u<br>w</marquee></pre>
```

1. q
2. A
3. E
4. u
5. w
6. blank
7. blank

etc

As stated in the page, the flag follows the format
`FLAG-{...something...}`. The key is to seek the number of steps
required to display "FLAG-{" in the first 6 columns and "}" in the
last. For this first challenge, 1643307 steps are required. This can
be bruteforced with a small script that simulates all marquee steps
and looks for `FLAG-{ ... }`.

## Flag

`FLAG-{l_element_de_fronton}`
