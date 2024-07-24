""" Tests for translate.py """

from subprocess import getstatusoutput
import os
import re
import string
import random

PRG = './translate.py'
DNA = 'gaactacaccgttctcctggt'
RNA = 'UGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAA'


# --------------------------------------------------
def random_filename():
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# --------------------------------------------------
def run(input_seq, codons, expected):
    """ Run """

    random_file = random_filename()
    try:
        flip = random.randint(0, 1)
        out_file, out_arg = (random_file,
                             '-o ' + random_file) if flip == 1 else ('out.txt',
                                                                     '')
        print(f'{PRG} -c {codons} {out_arg} {input_seq}')
        rv, output = getstatusoutput(
            f'{PRG} -c {codons} {out_arg} {input_seq}')

        assert rv == 0
        assert output.rstrip() == f'Output written to "{out_file}".'
        assert os.path.isfile(out_file)
        with open(out_file, encoding='utf-8') as fh:
            assert fh.read().strip() == expected
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
