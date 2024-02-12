# Here

## Write-up

I wanted to make a challenge that punished people who don't use
adblockers :v)

This web page tries to load 1500 scripts, all of which look like:

```javascript
edit_flag[523] = function(f, g) { return [(f ^ 0x1a25a98f), (g ^ 0x220b847)]}; finish();
```

Each time a script is loaded, all those `edit_flag` functions are
applied to the same two values.

Once all scripts have been loaded, there are two ways this can go:

- When all 1500 scripts are loaded, only the right half of the flag is
  correct
- If only the right 1497 scripts are loaded, only the left half is
  correct

This is hinted with:

```javascript
if(Object.keys(edit_flag).length == 1497)
    document.querySelector('#disclaimer1').style.display = 'block';
else if(Object.keys(edit_flag).length == 1500)
    document.querySelector('#disclaimer2').style.display = 'block';
```

People who have an adblocker installed wont be able to load those
three scripts:

- ad-scroll.js
- ane-popup.js
- expads-blocked.js

If you have an adblocker installed, you'll see something is fishy with
the total number of scripts. Disabling your adblocker (or using
another browser) will show you the other correct half of the flag.

If you don't use one, though luck :^)

## Flag

`FLAG{60bc331b5487b726}`
