import nylo
import sys
import argparse


def main():
    if len(sys.argv) <= 1:
        sys.argv.append('-h')
    sys.argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description='A cool programming language')
    parser.add_argument('-f', '--file',
                        help='the file you want to evaluate')
    parser.add_argument('-v', '--version',
                        help='print current version',
                        action='version',
                        version='nylo 0.1.0')
    parser.add_argument('-i', '--inline',
                        help='inline command line',
                        action='store_true')
    args = parser.parse_args(sys.argv)

    if args.inline:
        previous_code = ''
        statement = False
        while True:
            try:
                if not statement:
                    code = input('>>> ')
                else:
                    code = input('... ')

                if code in ['exit', 'exit()']:
                    print('Bye!')
                    sys.exit(0)

                if not code:
                    code = previous_code
                    statement = False
                    previous_code = ''
                elif code[-1] == ':':
                    previous_code += code + '\n'
                    statement = True
                    continue
                elif statement:
                    previous_code += code + '\n'

                if not statement:
                    reader = nylo.Reader(code + '\n')
                    struct = nylo.Struct(reader).value
                    print(struct.calculate(nylo.nyglobals))
                del code
            except Exception as e:
                print(e0)

    if args.file is not None:
        with open(args.file, 'r') as codefile:
            code = codefile.read()

        reader = nylo.Reader(code)
        struct = nylo.Struct(reader).value
        try:
            print(struct.calculate(nylo.nyglobals))
        except Exception as e:
            print(e, struct)


if __name__ == '__main__':
    main()
