# Aoe2 civs and techs, part 1

## Write-up

The more detailed solution of many puzzles, including this one, can be found at [https://github.com/desharnc27/incoming-csg-2024-python](https://github.com/desharnc27/incoming-csg-2024-python).

Warning for this puzzle: if you see python in the above automatically generated link, change it to java.

Website https://ageofempires.fandom.com/wiki/ contains the desired data. It's literally the first link you'd get in Google search.

By browsing //ageofempires.fandom.com/wiki/[Any technology] you get all civs that do, and all civs that don't get this technology.

Get the information you need, then place everything in the correct order. The git repo at the top contains an algorithm to find the correct order, but honestly, it's faster to do it all by hand.

```
answer------->Japanese,Slavs,Ethiopians,Spanish,Sicilians,Crop_Rotation,Bombard_Cannon,Gold_Shaft_Mining,Blast_Furnace,Bloodlines,Heated_Shot
sha1(answer)->4e0d18448c7a6cd1aa8c6af049fb897fb73f6fe8
Flag--------->FLAG{4e0d18448c7a6cd1aa8c6af049fb897fb73f6fe8}

```


## Flag

FLAG{4e0d18448c7a6cd1aa8c6af049fb897fb73f6fe8}