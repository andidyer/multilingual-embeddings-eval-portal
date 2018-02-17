#!/home/gmulcaire/anaconda/bin/python

import sys
import re
import codecs
import io

def fix(filename, new_filename):
    outfile = io.open(new_filename, encoding='utf-8', mode='w')
    with io.open(filename, encoding='utf-8', mode='r') as f:
        for i, line in enumerate(f):
            if len(line.split()) < 5:
                continue
            nl = line.strip().split()
            nl.insert(1, ':')
            outline = u' '.join(nl)+u'\n'
            outfile.write(outline)


if __name__=="__main__":
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        new_filename = sys.argv[2]
        fix(filename, new_filename)
    else:
        for filename in sys.argv[1:]:
            new_filename = filename+'fixed'
            print filename, '-->', new_filename
            split(filename, new_filename)
