import argparse
import sys
from pathlib import Path
import time


def main(args):
    parser = argparse.ArgumentParser(description='Returns sum of two arguments')
    parser.add_argument("--a", type=float, required=True) #入参a，自定义算子类型：number
    parser.add_argument("--b", type=float, required=True) #入参b，自定义算子类型：number
    parser.add_argument("--sum", type=str, required=True) #出参sum，自定义算子类型：string
    args = parser.parse_args(args)

    Path(args.a).parent.mkdir(parents=True, exist_ok=True)
    with open(args.a, 'w') as sum_path:
        time.sleep(60)
        sum_path.write('{}'.format(args.a))


if __name__ == '__main__':
    main(sys.argv[1:])
