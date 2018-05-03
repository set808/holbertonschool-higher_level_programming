#!/usr/bin/python3


def text_indentation(text):
    special = {'.', '?', ':'}
    if type(text) is not str:
        raise TypeError('text must be a string')
    formatted = text.strip()
    for i, v in enumerate(formatted):
        if v in special:
            print('{:s}\n'.format(v))
        else:
            if (formatted[i - 1] in special or \
                (formatted[i] == ' ' and formatted[i - 1] == ' ')):
                continue;
            print('{:s}'.format(v), end='')
