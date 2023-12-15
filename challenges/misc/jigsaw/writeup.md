# Jigsaw

## Write-up

See `instructions.png` and come up with an algorithm :-)

The only caveat is that 700x700 patches might be too large for a naive
O(N^2) algorithm.

## More infos, in case anyone asks

- The pieces are not rotated
- The colors are unique vertically and horizontally but can be reused
  between the two

These infos should be fairly easy to figure out, either by trying a
simple algorithm first, or by analyzing the colors and figuring out
that the number of unique colors in each direction is the same (those
are the border pieces)

## Flag

`FLAG-HERO-OF-THE-PUZZLE-OF-THE-PUZZLE-HERO`
