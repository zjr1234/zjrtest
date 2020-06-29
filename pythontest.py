import argparse
import sys
from pathlib import Path


def main(args):
    parser = argparse.ArgumentParser(description='Returns sum/minus of two arguments')
    parser.add_argument("--arg1", type=float, required=True)
    parser.add_argument("--arg2", type=float, required=True)
    parser.add_argument("--sum", type=str, required=True)
    parser.add_argument("--minus", type=str, required=True)
    args = parser.parse_args(args)

    Path(args.sum).parent.mkdir(parents=True, exist_ok=True)
    with open(args.sum, 'w') as sum_path:
        sum_path.write('{}'.format(args.arg1 + args.arg2))
        
    Path(args.minus).parent.mkdir(parents=True, exist_ok=True)
    with open(args.minus, 'w') as minus_path:
        minus_path.write('{}'.format(args.arg1 - args.arg2))


if __name__ == '__main__':
    main(sys.argv[1:])
