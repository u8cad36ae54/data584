"""Quick helpers."""

def flatten(xs):
    return [y for x in xs for y in x]

if __name__ == "__main__":
    print(clamp(11, 0, 10))

# see notes
