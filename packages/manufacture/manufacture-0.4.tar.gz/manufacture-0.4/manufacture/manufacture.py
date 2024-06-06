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


def main():
    if len(sys.argv) < 3:
        print("Usage: manufacture create <filename> [--content=<content>] | change <oldname> <newname> [--backup] | permissions <filename> <permissions> | ownership <filename> <owner> <group> | directory <dirname> | info <filename> | compress <directory> --output=<output>")
        sys.exit(1)

    command = sys.argv[1]
    if command == "create":
        filename = sys.argv[2]
        content = ""
        if "--content" in sys.argv:
            content_index = sys.argv.index("--content")
            content = sys.argv[content_index + 1]
        create_file(filename, content)
    elif command == "change":
        if len(sys.argv) < 4:
            print("Usage: manufacture change <oldname> <newname> [--backup]")
            sys.exit(1)
        oldname = sys.argv[2]
        newname = sys.argv[3]
        backup = "--backup" in sys.argv
        change_file(oldname, newname, backup)
    elif command == "permissions":
        if len(sys.argv) != 4:
            print("Usage: manufacture permissions <filename> <permissions>")
            sys.exit(1)
        filename = sys.argv[2]
        permissions = int(sys.argv[3], 8)
        modify_permissions(filename, permissions)
    elif command == "ownership":
        if len(sys.argv) != 5:
            print("Usage: manufacture ownership <filename> <owner> <group>")
            sys.exit(1)
        filename = sys.argv[2]
        owner = sys.argv[3]
        group = sys.argv[4]
        modify_ownership(filename, owner, group)
    elif command == "directory":
        directory = sys.argv[2]
        create_directory(directory)
    elif command == "info":
        filename = sys.argv[2]
        display_metadata(filename)
    elif command == "compress":
        if "--output" not in sys.argv:
            print("Usage: manufacture compress <directory> --output=<output>")
            sys.exit(1)
        directory = sys.argv[2]
        output_index = sys.argv.index("--output")
        output = sys.argv[output_index + 1]
        compress_directory(directory, output)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
