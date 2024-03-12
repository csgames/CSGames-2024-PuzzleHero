# Rules 2

En inspectant le code [html](./dist/index.html), on voit que certaine lettre son en italique et ont des attributs `data-piece` et `data-id`. On sait qu'il y avait un nombre de morceaux, on peut donc supposé que `data-piece` fait référence au morceau et `data-id` à l'id dans le morceau. Cela peut être confirmé en regardant que pour chaque `data-piece` il y a toujours deux `data-id` ce qui valide le fait que chaque morceau est de même taille.

Après il est possible de faire un programme allant reformer les différents morceaux:

```js
Array.from(document.querySelectorAll('i[data-piece][data-id]'))
  .reduce((acc, el) => {
    const piece = el.getAttribute('data-piece');
    const id = parseInt(el.getAttribute('data-id'), 10);
    acc[piece] = [...(acc[piece] || [])]
      .reduce((str, c, idx) => {
          return idx === id ?
            str + el.textContent + c :
            str + c;
      }, '') + (id >= (acc[piece] || []).length ? el.textContent : '');
    return acc;
  }, {});
```

On obtient ceci:

```
| id | valeur |
| :-- | :--: |
| 0 | -L |
| 1 | fl |
| 2 | ov |
| 3 | {I |
| 4 | ag |
| 5 | le |
| 6 | 5} |
| 7 | e- |
| 8 | ru |
```

Il est dit par contre qu'en tombant les morceaux se sont mélanger. On doit donc retrouver l'ordre d'origine.

Une méthode naïve consite à tester les 9! permutations possible des ces blocs pour trouver le flag. Sinon il est possible par de réduire le nombre de permutation à tester. On sait que le flag est de format `flag{}`. On saif donc que le flag commençera par le bloc #1 suivi du bloc #4 suivi du bloc #3. On sait aussi que le flag termine par le bloc #6.

Pour l'instant nous avons donc:

```
+----+----+----+----+----+----+----+----+----+
| fl | ag | {I |    |    |    |    |    | 5} |
+----+----+----+----+----+----+----+----+----+
  #1   #4   #3   #?   #?   #?   #?   #?   #6
```

il reste donc 120 permutations possible avec les blocs #0, #2, #5, #7 et #8. Un algorithme de permutations vous permet de trouver un combinaison formant une phrase.

```
+----+----+----+----+----+----+----+----+----+
| fl | ag | {I | -L | ov | e- | ru | le | 5} |
+----+----+----+----+----+----+----+----+----+
  #1   #4   #3   #0   #2   #7   #8   #5   #6
```

## Flag
flag{I-Love-rule5}