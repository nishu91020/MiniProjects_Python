import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, help="Directory to be organized.")
    args = parser.parse_args()
    sys.stdout.write(str(orga(args)))

def orga():
    return args.f

if __name__ == '__main__':
    main()
