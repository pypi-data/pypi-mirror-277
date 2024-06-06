import os
import sys
import shutil
import time
from pathlib import Path


def create_file(filename, content=""):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created file {filename}")


def change_file(oldname, newname, backup=False):
    if os.path.exists(oldname):
        if backup:
            backup_name = f"{oldname}.bak"
            shutil.copy2(oldname, backup_name)
            print(f"Backup created: {backup_name}")
        os.rename(oldname, newname)
        print(f"Renamed {oldname} to {newname}")
    else:
        print(f"Error: {oldname} does not exist")


def modify_permissions(filename, permissions):
    if os.path.exists(filename):
        os.chmod(filename, permissions)
        print(f"Permissions of {filename} changed to {oct(permissions)}")
    else:
        print(f"Error: {filename} does not exist")


def modify_ownership(filename, owner, group):
    if os.path.exists(filename):
        shutil.chown(filename, user=owner, group=group)
        print(f"Ownership of {filename} changed to {owner}:{group}")
    else:
        print(f"Error: {filename} does not exist")


def create_directory(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"Created directory {directory}")


def display_metadata(filename):
    if os.path.exists(filename):
        stats = os.stat(filename)
        print(f"Metadata for {filename}:")
        print(f"Size: {stats.st_size} bytes")
        print(f"Created: {time.ctime(stats.st_ctime)}")
        print(f"Modified: {time.ctime(stats.st_mtime)}")
        print(f"Permissions: {oct(stats.st_mode & 0o777)}")
        print(f"Owner: {stats.st_uid}, Group: {stats.st_gid}")
    else:
        print(f"Error: {filename} does not exist")


def compress_directory(directory, output):
    shutil.make_archive(output, 'zip', directory)
    print(f"Compressed {directory} to {output}.zip")


def parse_args(args):
    parsed_args = {}
    skip_next = False
    for i, arg in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if arg.startswith("--"):
            key = arg.lstrip('-')
            if "=" in key:
                key, value = key.split("=", 1)
                parsed_args[key] = value
            else:
                parsed_args[key] = args[i + 1] if i + 1 < len(args) else None
                skip_next = True
        else:
            parsed_args[f"arg{i}"] = arg
    return parsed_args


def main():
    if len(sys.argv) < 3:
        print("Usage: manufacture create <filename> [--content=<content>] | change <oldname> <newname> [--backup] | permissions <filename> <permissions> | ownership <filename> <owner> <group> | directory <dirname> | info <filename> | compress <directory> --output=<output>")
        sys.exit(1)

    command = sys.argv[1]
    args = parse_args(sys.argv[2:])

    if command == "create":
        filename = args.get("arg0")
        content = args.get('content', "")
        create_file(filename, content)
    elif command == "change":
        oldname = args.get("arg0")
        newname = args.get("arg1")
        backup = 'backup' in args
        change_file(oldname, newname, backup)
    elif command == "permissions":
        filename = args.get("arg0")
        permissions = int(args.get("arg1"), 8)
        modify_permissions(filename, permissions)
    elif command == "ownership":
        filename = args.get("arg0")
        owner = args.get("arg1")
        group = args.get("arg2")
        modify_ownership(filename, owner, group)
    elif command == "directory":
        directory = args.get("arg0")
        create_directory(directory)
    elif command == "info":
        filename = args.get("arg0")
        display_metadata(filename)
    elif command == "compress":
        directory = args.get("arg0")
        output = args.get('output')
        if not output:
            print("Usage: manufacture compress <directory> --output=<output>")
            sys.exit(1)
        compress_directory(directory, output)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
