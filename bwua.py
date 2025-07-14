import sys

if len(sys.argv) >= 2:
    username = sys.argv[1]
else:
    exit()

print(f"Hello {username}!")
