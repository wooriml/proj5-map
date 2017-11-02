
def process(raw):
    """
    """
    entry = {}
    cooked = []
    for line in raw:
        line = line.strip()
        if len(line) == 0 or line[0] == "#":
            print("Skipping")
            continue
        parts = line.split(':')

        #print(parts)

        if len(parts) == 2:
            field = parts[0]
            content = parts[1]

        else:
            raise ValueError("Trouble with line: '{}'\n".format(line) +"Split into |{}|".format("|".join(parts)))

        if field == 'location':
            continue

        elif field == 'name' or field == 'address':
            entry[field] = content


        else:
            raise ValueError("Syntax error in line: {}".format(line))

        if entry:
            cooked.append(entry)

    return cooked


def main():

    f = open("data/eugene.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()
            
    
