import sys

if sys.argv[1] == "reverse" and len(sys.argv) == 4:
    with open(sys.argv[2], 'r') as f:
        contents = f.readlines()
    with open(sys.argv[3], 'w') as f:

        contents.reverse()
        for s in contents:
            f.write(s[::-1])

elif sys.argv[1] == 'copy' and len(sys.argv) == 4:
    contents = ''
    with open(sys.argv[2], 'r') as f:
        contents = f.read()

    with open(sys.argv[3], 'w') as f:
        f.write(contents)

elif sys.argv[1] == 'duplicate-contents' and len(sys.argv) == 4:
    with open(sys.argv[2], 'r') as f:
        contents = f.read()

    with open(sys.argv[2], 'a') as f:
        for i in range(int(sys.argv[3])):
             f.write(contents)

elif sys.argv[1] == "replace-string" and len(sys.argv) == 5:
    with open(sys.argv[2], 'r') as f:
        contents = f.readlines()
    with open(sys.argv[2], 'w') as f:
        for s in contents:
            if sys.argv[3] in s:
                s = s.replace(sys.argv[3], sys.argv[4])
            f.write(s)