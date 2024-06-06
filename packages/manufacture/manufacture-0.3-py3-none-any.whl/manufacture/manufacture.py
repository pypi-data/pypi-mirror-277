import os
import sys
import shutil


def create_file(filename):
    with open(filename, 'w') as f:
        pass


def change_file(oldname, newname):
    if os.path.exists(oldname):
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


def main():
    if len(sys.argv) < 3:
        print("Usage: manufacture create <filename> | change <oldname> <newname> | permissions <filename> <permissions> | ownership <filename> <owner> <group>")
        sys.exit(1)

    command = sys.argv[1]
    if command == "create":
        filename = sys.argv[2]
        create_file(filename)
    elif command == "change":
        if len(sys.argv) != 4:
            print("Usage: manufacture change <oldname> <newname>")
            sys.exit(1)
        oldname = sys.argv[2]
        newname = sys.argv[3]
        change_file(oldname, newname)
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
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
