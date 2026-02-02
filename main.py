geese = [10.5, 20.6, 30.7, 40.8, 50.9, 60.9, 70.9, 80.6, 90.4, 100.10]


def goose_filter(birds):
    filtered_birds = []
    for word in geese:
        if word >= birds:
            filtered_birds.append(word)
    return filtered_birds


print(goose_filter([10.7, 9.8, 8.9, 30.4]))