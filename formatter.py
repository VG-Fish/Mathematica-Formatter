from argparse import ArgumentParser, Namespace
from os.path import exists
from pprint import pprint

def format(input: str, max_line_length: int = 80) -> None:
    pprint(input)
    bracket_counter: int

def main() -> None:
    parser: ArgumentParser = ArgumentParser(
        description="A CLI tool for converting natural language to Manim animations."
    )

    parser.add_argument(
        "-f",
        "--file",
        help="The input file.",
        required=True,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="The output file.",
        required=True,
    )

    args: Namespace = parser.parse_args()
    file: str = args.file
    if not exists(file):
        raise FileNotFoundError
    
    code: str = ""
    with open(file, "r") as f:
        code = f.read()
    
    format(code)

if __name__ == "__main__":
    main()