import argparse
import sys
from pathlib import Path


def main(args):
    parser = argparse.ArgumentParser(description='Returns Sum_1-01/Minus_1-0A1 of two arguments')
    parser.add_argument("--Arg1_1-1", type=float, required=True)
    parser.add_argument("--Arg2_2-1", type=float, required=True)
    parser.add_argument("--Sum_1-01", type=str, required=True)
    parser.add_argument("--Minus_1-0A1", type=str, required=True)
    args = parser.parse_args(args)

    Path(args.Sum_1-01).parent.mkdir(parents=True, exist_ok=True)
    with open(args.Sum_1-01, 'w') as Sum_1-01_path:
        Sum_1-01_path.write('{}'.format(args.Arg1_1-1 + args.Arg2_2-1))
        
    Path(args.Minus_1-0A1).parent.mkdir(parents=True, exist_ok=True)
    with open(args.Minus_1-0A1, 'w') as Minus_1-0A1_path:
        Minus_1-0A1_path.write('{}'.format(args.Arg1_1-1 - args.Arg2_2-1))


if __name__ == '__main__':
    main(sys.argv[1:])