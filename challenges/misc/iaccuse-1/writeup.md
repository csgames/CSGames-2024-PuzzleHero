# I accuse!, part 1

## Write-up

The more detailed solution of many puzzles, including this one, can be found at [https://github.com/desharnc27/incoming-csg-2024-python](https://github.com/desharnc27/incoming-csg-2024-python).

On ne peut donc pas tout détailler ici, mais en gros, on utilise la programmation dynamique.

On définit P(i;j) comme la probabilité que si le joueur courant et l'adversaire n'ont pas encore vu respectivement i et j cartes non-coupables, le joueur courant remporte la partie.

Joueur courant = celui dont c'est le tour de jouer.

Si i=0, on accuse, car on sait, mais ce cas n'arrive pas car l'adversaire nous laissera pas jouer notre tour s'il sait qu'on sait. Si j=0, l'adversaire sait, alors on accuse avant qu'il joue: nos chances de réussite sont 1/C(2,i+2) car il reste encore 2 parmi i+2 paires de cartes coupables possibles.

Ça se complique lorsque i>0 et j>0. L'équation de récurrence  est la suivante (explication dans le pdf du repo):
```
\begin{align*}
P_{i,j}=& \frac{Ni -N P_{j,i-1} + j(N-i) P_{i,j-1}}{(Ni+Nj-ij)}
\end{align*}
```
où N est le nombre de cartes dans la main de notre adversaire avant de piger dedans, soit 6.

Vous pouvez utiliser [ce petit compilateur latex](https://quicklatex.com) pour mieux visualiser.

La réponse qu'on cherche est $P_{N,N-1}$, car $(N,N-1)$ est l'état initial du jeu. La manière la plus efficace de de calculer est de remplir un tableau 2D contenant tous les $P_{i,j}$ 

```
answer->6557099/13634544
Flag--->FLAG{6557099/13634544}
```


## Flag

FLAG{6557099/13634544}