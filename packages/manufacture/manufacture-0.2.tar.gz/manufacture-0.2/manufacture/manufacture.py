import os
import argparse


def create_file(filename):
    """Create an empty file."""
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")
    else:
        print(f"File '{filename}' already exists.")


def main():
    parser = argparse.ArgumentParser(
        description="Create a file with the specified name and type.")
    parser.add_argument(
        "filename", help="The name of the file to create, including the extension.")
    args = parser.parse_args()

    create_file(args.filename)


if __name__ == "__main__":
    main()
