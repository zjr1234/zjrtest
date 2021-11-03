import argparse
import sys
from pathlib import Path
import time


def main(args):
    parser = argparse.ArgumentParser(description='Returns string arguments')
    parser.add_argument("--output1", type=str, required=True) #出参output1，自定义参数类型：string
    args = parser.parse_args(args)
    aa=[{"bucket":"mlflow","path":"MLmodel","destination":""},{"bucket":"mlflow","path":"92/model.pkl","destination":""},{"bucket":"mlflow","path":"model/conda.yaml","destination":""}]
    Path(args.output1).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output1, 'w') as f:
        f.write('{}'.format(aa))


if __name__ == '__main__':
    main(sys.argv[1:])
