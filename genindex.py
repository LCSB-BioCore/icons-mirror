#!/usr/bin/env python3

import os
import unicodedata

def get_codes():
    for file in os.listdir("assets/svg"):
        if file[-4:] != '.svg': break
        yield file[:-4].split('-')

print("""<!doctype html>
<html>
<head><title>Twemoji browsable listing</title></head>
<body>
<h1> Twemoji browsable listing </h1>
<p><strong>How-to</strong>: use Ctrl+F to find your favorite emoji by name.</p>
<p>All data on this page is generated from Twitter Twemoji, subject to the <a href="https://github.com/twitter/twemoji">corresponding license terms</a>.</p>
<table>
""")

def safename(x):
    try:
        return unicodedata.name(x)
    except:
        return 'UNKNOWN'

for codes in sorted(get_codes()):
    codestr='-'.join(codes)
    print('<tr><td><div style="width: 72px; height: 72px; background-image: url(\'assets/72x72/'+codestr+'.png\')"></div></td><td>'+codestr+'</td>')
    print('<td>'+''.join(map(lambda x: chr(int(x, 16)), codes))+'</td>')
    print('<td>'+'→'.join(map(lambda x: safename(chr(int(x, 16))), codes))+'</td>')
    print('<td><a href="assets/svg/'+codestr+'.svg">svg</a></td><td><a href="assets/72x72/'+codestr+'.png">72x72 png</a></td></tr>')

print("</table></body></html>")
