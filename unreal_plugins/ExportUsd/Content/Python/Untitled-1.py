






if "__name__" == "__main__":
    s = "egg"
    t = "add"

    print(zip(s, t))
    zipped = set(zip(s, t))
    print(len(zipped) == len(set(s)) == len(set(t)))