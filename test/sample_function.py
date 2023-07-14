import argparse


def set_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int)
    parser.add_argument("--b", type=int)
    args = parser.parse_args()
    return args


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    args = set_args()
    c = add(args.a, args.b)
    print(f"{args.a} + {args.b} = {c}")


if __name__ == "__main__":
    main()
