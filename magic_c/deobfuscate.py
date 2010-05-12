""" Small utility to deobfuscate the code from 
http://groups.google.com/group/comp.lang.c/msg/e105e5d339edec01?pli=1

Hint: pipe the output of this to GNU's `indent' utility to get more 
comprehensible code.
"""

import re
import sys

def main():
    if len(sys.argv) <> 2:
        print "Usage: python deobfuscate.py <name_of_magic_file.c>"
        sys.exit(1)

    f = file(sys.argv[1])

    token_dict = {}
    token_define_re = re.compile(r'^#define\s+([^ ]+)\s+([^ ].*)$')

    for line in f:
        re_obj = token_define_re.match(line)
        if re_obj:
            token_dict[re_obj.groups()[0]] = re_obj.groups()[1]
        else:
            deobfuscate(line, token_dict)

def deobfuscate(line, token_dict):
    tokens = line.strip().split()
    token_translation = []

    for token in tokens:
        translation = token_dict.get(token, token)
        token_translation.append(translation)

    print ' '.join(token_translation)

if __name__ == '__main__':
    main()
