import argparse
import sys
from pathlib import Path


def main(args):
    parser = argparse.ArgumentParser(description='Returns Sum_1-01/Minus_1-0A1 of two arguments')
    parser.add_argument("--arg1_11", type=float, required=True)
    parser.add_argument("--arg2_21", type=float, required=True)
    parser.add_argument("--sum_101", type=str, required=True)
    parser.add_argument("--minus_101", type=str, required=True)
    args = parser.parse_args(args)

    Path(args.sum_101).parent.mkdir(parents=True, exist_ok=True)
    with open(args.sum_101, 'w') as sum_101_path:
        sum_101_path.write('{}'.format(args.arg1_11 + args.arg2_21))
        
    Path(args.minus_101).parent.mkdir(parents=True, exist_ok=True)
    with open(args.minus_101, 'w') as minus_101_path:
        minus_101_path.write('{}'.format(args.arg1_11 - args.arg2_21))


if __name__ == '__main__':
    main(sys.argv[1:])