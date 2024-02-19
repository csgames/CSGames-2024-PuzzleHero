# Don't blink 2

## Write-up

This is the same challenge as the previous one, but with a much larger
number of steps before the columns can display "FLAG-{...}" in sync.

The number of steps is 124821358521.

This must be solved mathematically using the chineese remainder
theorem:


```
zyFM{@cXubp__
  ^
}Q[[L@rUGOPW|e^|_wcnTDG@`FBqS[IvCqoPZ_{sCyEPklKn[XxiVMn[Arx\Bv_hT__
    ^
|lyBpxOBelZA|LJUmI@pYjKahOuMjag~|ab__
           ^
fcStP^GQzIKtQ{e\P__
      ^
ydazzsFgryL~wK~q_}]HLkulLvcxC_Dsfcj-aNWndlHZIOunoUx[wuonYqXj?dQ}QAcoFV_^JqwqUMwetwWzS~]__
                                   ^
z`tR`mnaB~lqjH[@}ellAuhDdiml^`am|sebt~Vt[`[z?jGZeDymzo|OnSQMYOmz`ISIwb\RnzWvDoo^EjoVCfozZ\l[xgOOz@OhwqMiOQIxj?FhFqjZvJDgjGiUaIh@oyW]o`}ZdCQOSJWzWwQa^gApyDc{aEICe[TpshqH@MD__
                                                                                                                                                           ^
...

OyS}xDaFdYV_i[{__
   ^
```

We get the system:

```
F:  col1: nb_steps % 13 == 2
L:  col2: nb_steps % 67 == 4
A:  col3: nb_steps % 37 == 11
G:  col4: nb_steps % 19 == 6
-:  col5: nb_steps % 89 == 35
{:  col6: nb_steps % 173 == 155
}:  last col: nb_steps % 17 == 3
```

The smallest nb_steps that satisfies all these is 124821358521. If we
look at the 124821358521-th iteration, the correct flag will show

## Flag

`FLAG-{de-delicieux-restes-chinois-pour-le-diner-de-demain}`
