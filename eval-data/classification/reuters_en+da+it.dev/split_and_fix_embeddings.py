#!/home/gmulcaire/anaconda/bin/python

import sys
import re
import codecs
import io
import IPython as ipy

def split(filename, new_filename_base):
    language_files = {}
    d = None
    #outfile = io.open(new_filename_base, encoding='utf-8', mode='w')
    with io.open(filename, encoding='utf-8', mode='r') as f:
        for i, line in enumerate(f):
            if len(line.split()) < 5:
                continue
            lang, l = line[:2], line[3:] #remove language prefix from word
            nl = l.split()
            if d is None:
                d = len(nl)
            if len(nl) != d:
                print "Line has wrong length", d, len(nl), "first word is", line.split()[0]
                continue
            nl.insert(1, ':')
            if lang not in language_files:
                language_files[lang] = io.open(new_filename_base+'.'+lang, encoding='utf-8', mode='w')
            outline = u' '.join(nl)+u'\n'
            language_files[lang].write(outline)
            #outfile.write(outline)


if __name__=="__main__":
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        new_filename_base = sys.argv[2]
        split(filename, new_filename_base)
    else:
        for filename in sys.argv[1:]:
            new_filename_base = filename.split('.')[0]
            print filename, '-->', new_filename_base
            split(filename, new_filename_base)
