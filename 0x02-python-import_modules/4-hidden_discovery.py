#!/usr/bin/python3


def print_hidden(names):
    for i, name in enumerate(names):
        if name[:2] == '__':
            continue
        print('{:s}'.format(name))

if __name__ == '__main__':
    import hidden_4
    print_hidden(dir(hidden_4))
