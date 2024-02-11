# Puzzle Hero: The Musical 1

## Write-up

The challenge description has an important hint:


```
  This challenge should be fun!
  Here is a tip for having more fun with it:
  VHJ5IHRvIHBsYXkgdGhlIG5vdGVzIHVzaW5nIHRoaXM6IE1FUUdHMzNQTlFRSEEyTEJOWlhRPT09PQo=
```

This contains a base64 message, which says:

```
  Try to play the notes using this: MEQGG33PNQQHA2LBNZXQ====
```

Which itself contains a base32 message. This hints that baseX coding
are important here.


The challenge is a partition generated with ABC notation.

All notes are either A, B, C or D, which is enough to encode a message
in base4

The full message is :
BCBCBCDABCABBCBDBDCDBCCCBCBBACDCBCADBCDDBCDBBCDBBCBBBCDCBCADBCBBACDCBCDABCABACDCBCBDBDBBBCCBBDBABCABBDACBCBBBDDB


A quick search online did not yield decoders for base4, but the logic
is the same as base64 or base32: write down all 0's and 1's of your
data, and regroup them by packs of N bits (where 2^N is your baseX)

## Flag

`flag{je.commence.la.guitare}`
