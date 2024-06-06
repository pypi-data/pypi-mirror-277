import os
import sys
import shutil
import time
from pathlib import Path


def create_file(filename):
    with open(filename, 'w') as f:
        pass
    print(f"Created file {filename}")


def add_content(filename, content):
    if os.path.exists(filename):
        with open(filename, 'a') as f:
            f.write(content)
        print(f"Added content to {filename}")
    else:
        print(f"Error: {filename} does not exist")


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
    parsed_args = {'command': None, 'filename': None, 'content': None}
    if len(args) >= 2:
        parsed_args['command'] = args[0]
        parsed_args['filename'] = args[1]
        if len(args) > 2:
            parsed_args['content'] = ' '.join(args[2:])
    else:
        print("Usage: manufacture <command> <filename> [content]")
        sys.exit(1)
    return parsed_args

def main():
    if len(sys.argv) < 2:
        print(
            "Usage: manufacture create <filename> | change <oldname> <newname> [--backup] | permissions <filename> <permissions> | ownership <filename> <owner> <group> | directory <dirname> | info <filename> | compress <directory> --output=<output>")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "create":
        if len(args) != 1:
            print("Usage: manufacture create <filename>")
            sys.exit(1)
        filename = args[0]
        create_file(filename)
    elif command == "add":
        if len(args) < 1:
            print("Usage: manufacture add <filename> <content>")
            sys.exit(1)
        filename = args[0]
        content = ' '.join(args[1:])
        add_content(filename, content)
    elif command == "change":
        if len(args) < 2:
            print("Usage: manufacture change <oldname> <newname> [--backup]")
            sys.exit(1)
        oldname = args[0]
        newname = args[1]
        backup = '--backup' in args
        change_file(oldname, newname, backup)
    elif command == "permissions":
        if len(args) != 2:
            print("Usage: manufacture permissions <filename> <permissions>")
            sys.exit(1)
        filename, permissions = args
        modify_permissions(filename, int(permissions, 8))
    elif command == "ownership":
        if len(args) != 3:
            print("Usage: manufacture ownership <filename> <owner> <group>")
            sys.exit(1)
        filename, owner, group = args
        modify_ownership(filename, owner, group)
    elif command == "directory":
        if len(args) != 1:
            print("Usage: manufacture directory <dirname>")
            sys.exit(1)
        directory = args[0]
        create_directory(directory)
    elif command == "info":
        if len(args) != 1:
            print("Usage: manufacture info <filename>")
            sys.exit(1)
        filename = args[0]
        display_metadata(filename)
    elif command == "compress":
        if len(args) != 2 or not args[1].startswith("--output="):
            print("Usage: manufacture compress <directory> --output=<output>")
            sys.exit(1)
        directory = args[0]
        output = args[1][len("--output="):]
        compress_directory(directory, output)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)



if __name__ == "__main__":
    main()
