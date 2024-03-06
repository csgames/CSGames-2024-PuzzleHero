# Badge (1/2)

## Write-up

On each persons badge there is a QR code. If you scan this QR code there is a tiny url that redirects to the csgames 2024 website. In this url there in an added get parameter called secret.
Here is it's value:
```
2a&oU9O^53?V3"E?UdC:5%6910RQJHF[KPG5;c84
```
If you paste it in the famous tool [cyberchef](https://gchq.github.io/CyberChef/) it will immediately suggest you that it's base85.
Now we have:
```
7=28Lb?y_J0J_FC0>b2=0|J0uC`b?5PN
```
Based on the fact that it's a bit of an uncommun encoding, we should probably try classic yet unusual ways to decode this. It can't be a ROT13, there's not enough letters, but we can try its cousin, ROT47, and bam we got the flag!


## Flag

```
flag{3nJ0y_y0ur_m3al_My_Fr13nd!}
```
