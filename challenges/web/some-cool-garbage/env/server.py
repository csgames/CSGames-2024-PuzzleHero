"""
Dirty edit of https://github.com/danvk/RangeHTTPServer/
"""
from random import randint, seed
import os
import re
import datetime

import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('port', type=int)

args = arg_parser.parse_args()


garbage_prefix = b"""<!DOCTYPE html>
<html><body><h1>Welcome to the FLAG!!</h1><p>I'm going to give you the flag :-)</p>
<p>But first, here is some cool garbage I found laying around, I hope you enjoy it!</p>
<pre>"""
flag = b"</pre><p>FLAG{4e57a63b0829ccfec385109a23d2f28d}</p>"
garbage_length = 1_000_000_000_000_000_000_000_000_000 - len(flag) - len(garbage_prefix)
total_length = len(garbage_prefix) + garbage_length + len(flag)

# garbage_prefix = b"""abc"""
# garbage_length = 3
# flag = b"abc"
# total_length = len(garbage_prefix) + garbage_length + len(flag)


try:
    # Python3
    from http.server import SimpleHTTPRequestHandler
    from http import server as SimpleHTTPServer
except ImportError:
    # Python 2
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    import SimpleHTTPServer


def copy_byte_range(infile, outfile, start=None, stop=None, bufsize=16*1024):
    """Like shutil.copyfileobj, but only copy a range of the streams.

    Both start and stop are inclusive.
    """
    if start is not None: infile.seek(start)
    while 1:
        to_read = min(bufsize, stop + 1 - infile.tell() if stop else bufsize)
        buf = infile.read(to_read)
        if not buf:
            break
        outfile.write(buf)


BYTE_RANGE_RE = re.compile(r'bytes=(\d+)-(\d+)?$')
def parse_byte_range(byte_range):
    """Returns the two numbers in 'bytes=123-456' or throws ValueError.

    The last number or both numbers may be None.
    """
    if byte_range.strip() == '':
        return None, None

    m = BYTE_RANGE_RE.match(byte_range)
    if not m:
        raise ValueError('Invalid byte range %s' % byte_range)

    first, last = [x and int(x) for x in m.groups()]
    if last is not None and last < first:
        raise ValueError('Invalid byte range %s' % byte_range)
    return first, last


class RangeRequestHandler(SimpleHTTPRequestHandler):
    """Adds support for HTTP 'Range' requests to SimpleHTTPRequestHandler

    The approach is to:
    - Override send_head to look for 'Range' and respond appropriately.
    - Override copyfile to only transmit a range when requested.
    """

    def send_head(self):

        if 'Range' not in self.headers:
            print('NO RANGE')
            self.range = None
            first, last = 0, total_length

        else:
            try:
                self.range = parse_byte_range(self.headers['Range'])
                first, last = self.range
            except ValueError as e:
                self.send_error(400, 'Invalid byte range')
                return None

        # Mirroring SimpleHTTPServer.py here
        # path = self.translate_path(self.path)
        # f = None
        # ctype = self.guess_type(path)
        # try:
        #     f = open(path, 'rb')
        # except IOError:
        #     self.send_error(404, 'File not found')
        #     return None

        # fs = os.fstat(f.fileno())
        # file_len = fs[6]

        if first >= total_length:
            self.send_error(416, 'Requested Range Not Satisfiable')
            return None

        if last is None or last >= total_length:
            last = total_length - 1
        response_length = last - first + 1

        if self.range is not None:
            self.range = (first, last)

            self.send_response(206)

            self.send_header('Content-Range',
                             'bytes %s-%s/%s' % (first, last, total_length))
            self.send_header('Content-Length', str(response_length))
        else:
            self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.send_header('Last-Modified', datetime.datetime.now())
        self.end_headers()

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        return SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        self.send_head()

        if self.range is None:
            self.wfile.write(garbage_prefix)
            for i in range(garbage_length):
                seed(i)
                c = chr(randint(33, 125))
                b = bytearray(c, "utf-8")
                self.wfile.write(b)
            self.wfile.write(flag)
        else:
            start, stop = self.range
            # Dans un range, stop est inclus, dans les slices/range()
            # en python, stop est exclus
            stop = stop+1

            print("===================")
            print(start, stop)

            if start < len(garbage_prefix):
                subprefix = garbage_prefix[start:stop]
                assert len(subprefix) != 0
                print('Sending prefix')
                self.wfile.write(subprefix)

            start -= len(garbage_prefix)
            stop -= len(garbage_prefix)

            print('After prefix =>', start, stop)

            if start < 0:
                start = 0
            if stop <= 0:
                return

            print('*** keep going with:')
            print(start, stop)

            start_range = start
            stop_range = min(garbage_length, stop)
            print('Sending garbage?')

            total_range = stop_range - start_range

            for i in range(start_range, stop_range):
                seed(i)
                c = chr(randint(33, 125))
                b = bytearray(c, "utf-8")
                self.wfile.write(b)

            if total_range > 0:
                print('Yep, actually. len(garbage)=', total_range)
            else:
                print('Nopes, no garbage')

            start -= garbage_length
            stop -= garbage_length

            print('After garbage', start, stop)

            if start < 0:
                start = 0
            if stop < 0:
                return

            print('***** Keeeeeep going with flag:')
            print(start, stop)

            out = flag[start:stop]
            print('Length:', len(out), 'len(flag):', len(flag))
            if len(out):
                print('Sending', out)
                self.wfile.write(out)

SimpleHTTPServer.test(HandlerClass=RangeRequestHandler, port=args.port)
