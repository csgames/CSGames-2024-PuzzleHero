# Lily Bernard at Learngame-HC College

## Write-up

The more detailed solution of many puzzles, including this one, can be found at [https://github.com/desharnc27/incoming-csg-2024-python](https://github.com/desharnc27/incoming-csg-2024-python).

On ne détaillera donc pas tout ici. Mais en résumé:

Ce qui est difficile ici, c'est qu'il faut améliorer la cote z de Lily sans baisser les notes des autres.

La clé est de faire baisser l'écart-type le plus possible sans trop monter la moyenne. Il est possible de prouver (explications dans le lien) que la manière optimale d'y arriver est de choisir un certain seuil S, de majorer à S les notes qui lui sont inférieures et de ne pas toucher aux autres notes.

Il fallait coder un algo qui essaie plein de valeurs de S distinctes, en convergeant vers la valeur optimale. Pour notre ensemble de données en particulier, 84.11% était le seuil S optimal.

Ensuite, on modifie les pourcentages dans le string de data.txt et la réponse est le string modifié.

```
answer------->Jayvon Acosta:97.66%,Quinn Andersen:84.11%,Blake Ashley:84.11%,Tristen Baxter:84.11%,Lily Bernard:94.27%,Kash Blackburn:84.11%,Deandre Blackwell:85.71%,Alfredo Bradley:84.11%,Kamari Branch:91.00%,Mohammad Burns:86.53%,Anaya Bush:84.11%,Jett Calhoun:84.11%,Adalyn Campos:94.49%,Kyan Carrillo:84.11%,Kathryn Castillo:94.63%,Laurel Chandler:84.11%,Solomon Cohen:84.11%,Lance Collins:84.11%,Terrence Cox:84.11%,Davian Curtis:84.11%,Kameron Donaldson:84.11%,Natalya Dougherty:84.11%,Abbie Dyer:84.11%,Nyasia Elliott:84.11%,Angelica Finley:84.11%,Noelle Fisher:84.11%,Shaun Flores:84.11%,Seamus Frazier:85.24%,Anastasia Fuller:99.34%,Haven Gallagher:87.50%,Caitlyn Garrison:86.94%,Rhys Gay:92.58%,Niko Golden:84.11%,Juan Gomez:97.42%,Linda Gomez:95.38%,Rebecca Hale:98.05%,Jeremiah Haley:84.11%,Abbey Haney:84.11%,Rose Hardy:92.49%,Harley Hardy:84.11%,Piper Holder:84.11%,Josue Horn:90.12%,Ciara Howard:84.11%,Ayden James:88.65%,Hassan Kaufman:84.11%,Adriel Kirby:89.85%,Lucas Le:84.11%,Gianna Leblanc:90.71%,Jamie Logan:93.71%,Summer Malone:84.11%,Titus Maynard:84.11%,Parker Mccall:84.27%,Iliana Mcconnell:84.11%,Alisa Mccormick:84.11%,Kayden Mcgrath:84.11%,Riya Mcmahon:96.74%,Anna Mcneil:84.11%,Shea Meyer:84.11%,Haven Munoz:84.11%,Kaiya Obrien:84.11%,Jade Ochoa:84.11%,Jaylene Oconnell:87.19%,Haylie Oneill:84.11%,Hugh Owens:84.11%,Clinton Peterson:84.11%,Zoe Pratt:84.11%,Stanley Reid:84.11%,Allan Roach:84.11%,Lucille Roman:94.56%,Asa Salinas:84.11%,Cullen Sandoval:84.11%,Henry Schneider:87.58%,Madison Schultz:84.11%,Lorelei Shannon:94.62%,Perla Shelton:84.11%,Ingrid Skinner:84.11%,Urijah Stanton:84.11%,Malaki Stanton:84.11%,Lukas Suarez:87.56%,Erika Swanson:84.11%,Wesley Swanson:84.11%,Sawyer Thornton:89.88%,Howard Valencia:92.79%,Jordon Valentine:96.49%,Kamren Villa:84.11%,Jabari Vincent:85.58%,Karina Wang:84.11%,Casey Watson:84.11%,Hana Watson:84.11%,Kyra Weaver:84.11%,Wilson Weber:84.11%,Lesly Whitaker:84.11%,Ruben Willis:84.11%,Cecilia Woodard:84.11%,Kendrick Woods:88.26%,Leanna Yates:84.39%,Haylee Yates:84.11%,Braydon Yoder:84.11%,Jamir Yu:99.91%,Arielle Zavala:84.11%
sha1(answer)->70dd5eb985dca345fae297712542e61bf0ee7cfa
Flag--------->FLAG{70dd5eb985dca345fae297712542e61bf0ee7cfa}
```


## Flag

FLAG{70dd5eb985dca345fae297712542e61bf0ee7cfa}