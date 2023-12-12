# The Safe

## Write-up

The challenge gives us a PNG file. It's a safe so we can assume that there is a hidden file inside the PNG file.
We can use `binwalk` to extract the hidden file.

```bash
binwalk the-safe.png // to see what the tool can find

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1024 x 1024, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, default compression
1324473       0x1435B9        PNG image, 1024 x 1024, 8-bit/color RGB, non-interlaced
1324548       0x143604        Zlib compressed data, default compression
```
We can see that there is a PNG image at 0x1435B9.

We can extract it with the -D option and its type

```bash
binwalk the-safe.png -D png
```

The extracted file is a PNG file. We can open it and see a flag near a safe. If you look closely, you can see that the flag is written in the flag's pole.

## Flag

```
FLAG-4N_3@$Y_54F3_T0_BR34K_1NT0
```
