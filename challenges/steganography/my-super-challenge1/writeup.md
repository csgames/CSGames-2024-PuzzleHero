# My Super Challenge 1

## Write-up

The zip file contains a git repository with a branch named
`testodf`. In that branch, each commit contains a new version of the
`instructions.odt` document.

Each "draft challenge" changes a specific letter in the
instructions. By looking at that letter in every commit in order, a
message forms.

An easy way of doing this quickly is by using `pandoc`, but looking at
the `xml` contained in the ODT file is another simple way of doing it.

```bash
git log|grep '^commit '|awk '{print $2}'|tac>/tmp/commits
for line in $(cat /tmp/commits)
do 
  git checkout $line 2>/dev/null
  pandoc instructions.odt -t markdown -o - | grep -Eo '`.`'
done | 
    tr -d '`' | tr -d '\n' | 
    tr '_' ' ' | tr '[:upper:]' '[:lower:]'
```

Part of the message reads:

> okay so here is how you can get the flag: you'll have to put the two
> words darth and plagueis in lowercase separated by a space into a
> tool that can compute the md5 sum of a string, and then put all of
> that inside curly brackets and then prepend the word galf backwards
> in lowercase and all of this put together is the thing that you
> should submit.

```bash
$ echo -n 'darth plagueis' | md5sum
84742722baccc4b5a53062008914bf47  -
```

## Flag

`flag{84742722baccc4b5a53062008914bf47}`
