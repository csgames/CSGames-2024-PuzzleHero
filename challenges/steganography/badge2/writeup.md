# Badge (2/2)

## Write-up

Based on the challenge's description we have two hints. The first one is that it's a steganography challenge so there must be something hidden. The second is the group of words 'not significant'. If you've learned a bit about steganography you learned that one of the most classic method to hide information in an image is called LSB(Least Significant Bit) so the hint if quite close.

Now we can try [an online tool](https://incoherency.co.uk/image-steganography/#unhide) to retrieve this information very easily, when we input the image we get the layer of the least significant bit and we can read the flag.

## Flag

```
FLAG{M4NY_S3CR3T5_@R3_R1GHT_1N_FR0NT_0F_Y0U}
```
