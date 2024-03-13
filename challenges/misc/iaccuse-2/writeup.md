# I accuse!, part 2

## Write-up

The more detailed solution of many puzzles, including this one, can be found at [https://github.com/desharnc27/incoming-csg-2024-python](https://github.com/desharnc27/incoming-csg-2024-python).

On ne peut donc pas tout détailler ici, mais en gros, on utilise la programmation dynamique comme au premier défi.

On définit P(k;i;j) comme la probabilité que si le joueur courant et l'adversaire n'ont pas encore vu respectivement i et j cartes non-coupables, il reste exactement k piges avant que quelqu'un accuse.

Si i=0 ou j=0, il faut accuser immédiatement, alors il n'y aura pas d'autres piges, dans ce cas:
    P(k;i;j) = 1 si k =0,
    P(k;i;j) = 0 sinon



Pour i>0 et j>j, l'équation de récurrence est la suivante:
```
\begin{align*}
P_{k,i,j}=& \frac{i}{N} P_{k-1,j,i-1} + \frac{N-i}{N} P_{k-1,j,i}
\end{align*}
```

où N est le nombre de cartes dans la main de notre adversaire avant de piger dedans, soit 12.

Vous pouvez utiliser [ce petit compilateur latex](https://quicklatex.com) pour mieux visualiser.

On calcule ensuite:
```
$1 - \sum_{k=0}^{49}P_{k,N,N-1}$
```

C'est la réponse, soit la probabilité que la partie atteigne 50 piges.

```
answer->1897575782773925539190703878422815958489/2835207499940367381525377228038276644864
Flag--->FLAG{1897575782773925539190703878422815958489/2835207499940367381525377228038276644864}
```


## Flag

FLAG{1897575782773925539190703878422815958489/2835207499940367381525377228038276644864}