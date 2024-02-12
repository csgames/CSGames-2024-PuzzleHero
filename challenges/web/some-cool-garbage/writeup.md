# Some cool garbage

## Write-up

The website generates way too much information to be able to wait for
the end of it.

By inspecting the headers, we can see:

```bash
$ curl --head $website
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.10.12
Date: Mon, 12 Feb 2024 02:07:24 GMT
Content-type: text/html
Last-Modified: 2024-02-11 21:07:24.817315
Accept-Ranges: bytes  <=================
```

The key is to use an appropriate Range request to skip to the end.

Any range request will yield the total amount

```bash
$ curl --range 1-10 --head $website
HTTP/1.0 206 Partial Content
Server: SimpleHTTP/0.6 Python/3.10.12
Date: Mon, 12 Feb 2024 02:07:30 GMT
Content-Range: bytes 1-10/1000000000000000000000000000
Content-Length: 10
Content-type: text/html
Last-Modified: 2024-02-11 21:07:30.584135
Accept-Ranges: bytes
```

Using the right range request will yield the flag:

```bash
$ curl --range 999999999999999999999999900- $website
!mt7b}8%o5P3?UJHsi1<ZMlAP`'*|a!m%xVb4#'O7B/TZ-1Cy</pre><p>FLAG{4e57a63b0829ccfec385109a23d2f28d}</p>
```

## Flag

`FLAG{4e57a63b0829ccfec385109a23d2f28d}`
