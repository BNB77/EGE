with open("24.txt", "r") as f:
    minNLine = min(f.readlines(), key=lambda x: x.count("N"))
    print(max(sorted(set(minNLine), reverse=True), key=minNLine.count))