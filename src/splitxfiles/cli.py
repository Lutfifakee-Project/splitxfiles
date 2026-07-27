import argparse
import sys
from splitxfiles import split_by_lines, split_by_size


def main():
    parser = argparse.ArgumentParser(
        description='Split files into smaller parts based on line count or file size',
        prog='splitxfiles'
    )

    parser.add_argument('input', help='Path to input file')
    parser.add_argument('-o', '--output', default=None,
                        help='Output folder (default: {input_name}_split)')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--lines', type=int,
                       help='Number of lines per file')
    group.add_argument('-s', '--size', type=int,
                       help='Size per file in bytes')

    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Run without progress output')

    args = parser.parse_args()

    if args.lines:
        success = split_by_lines(
            args.input,
            args.output,
            args.lines,
            verbose=not args.quiet
        )
    else:
        success = split_by_size(
            args.input,
            args.output,
            args.size,
            verbose=not args.quiet
        )

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
