data = [
    ["Symbol", "How to type this into a Python string"],
    ['"', '\\"'],  # Escape double quote with a backlash
    ["'", "\\'"],  # Escape single quote with a backlash
    ["\\", "\\\\"],  # Escape backlash with another backlash
]

for row in data:
    print("\t".join(row))  # tabs for column separtion
