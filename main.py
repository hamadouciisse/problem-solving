geese = ["ali", "mona", "sara", "nada", "marva", "halima", "majed"]


def goose_filter(birds):
    filtered_birds = []
    for word in geese:
        if word >= birds:
            filtered_birds.append(word)
    return filtered_birds


print(goose_filter(["ali", "mona", "sara"]))