#!/usr/bin/python

# htmlc (HTML Creator)
# Author: Jake Wilson
# Date: 1/17/2015

# The purpose of this program is to generate a blank html file with all the
# tags filled in, since they are a pain in the ass to add every time I create a 
# new html file.

import sys
import re
#import argparse

# if a file name isn't provided, call this file 'file'
if len(sys.argv) >= 2:
    file = sys.argv[1]
else:
    file = 'file'

match = re.search('\.html$', file)

# add html extension if there isn't one
if match == None:
    file += '.html'
else:
    print 'No match'

# the 'w+' says open a file for write, and create it if it doesn't exist
f = open(file, 'w+')
tab = '    ' # four spaces

f.write('<!DOCTYPE html>\n')
f.write('<html>\n')
f.write(tab + '<head>\n')
f.write(tab + tab + '<title></title>\n')
f.write(tab + '</head>\n')
f.write(tab + '<body>\n')
f.write(tab + '</body>\n')
f.write('</html>\n')
f.close()
