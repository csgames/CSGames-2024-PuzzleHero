# Patience

## Write-up

This is the write-up for the whole track.

The challenge is structured as:

- The client sends a request
- The server waits for a few minutes and answers with something that
  hints that the HTTP request has to change in order to move forward

Each request takes more and more time to get an answer (+5min each
time), so you can't really start this challenge late on sunday and
expect to finish it :P


A `curl` configuration that satisfies all steps would be:

```
# If you accept the terms and conditions
url = "http:// <URL and PORT here> /?status=accept"
# Using the right browser
user-agent = "Firefox/114.0"
# Are you ready
cookie = "READY=YESSIR"
# Simple auth
user = admin:secret
# You should ask not to be tracked
header = "DNT: 1"
# You should accept at least "de" if you speak german
header = "Accept-Language: fr,de,en"
# Changed their mind about the browser
user-agent = "Windows Phone"
# gzip compression
compressed
# You always GET, you should PUT
request = PUT
# Go to perdu.com and go back
referer = "http://perdu.com/"
```

## Flags

`flag{this-book-is-about-MS-Azure-right?-https://hubertreeves.info/livres/patience.html}`
`flag{waiting-for-godot}`
`flag{puzzle-heros-are-idle-games-now}`
