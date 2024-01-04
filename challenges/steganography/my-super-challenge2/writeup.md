# My Super Challenge 2

## Write-up

See the writeup for *My Super Challenge 1* for the basic structure.

The ODT files all have the same image, except for one of them.

You can extract the images from an ODT file with `binwalk`, or simply
by renaming it as `.zip` and extracting everything. Once all images
have been extracted, the interesting image can quickly be identified
through the md5sum (everthing is the same except for one).

## Flag

`flag-{b20f43d3e9fa753cec69dbd9ae8b0d93}`
