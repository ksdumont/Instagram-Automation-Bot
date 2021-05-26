primary_yoga_tags = []


def tag_checker(tags):
    print(f"{len(tags)} tags...")
    if len(tags) == len(set(tags)):
        return True
    else:
        return False


def find_duplicates(tags):
    seen = {}
    duplicates = []
    for tag in tags:
        if tag not in seen:
            seen[tag] = 1
        else:
            duplicates.append(tag)
    return duplicates


def tag_searcher(tag, tags):
    if tag in tags:
        idx = tags.index(tag)
        return idx
    else:
        print(f"{tag} not in list")


# print(find_duplicates(primary_yoga_tags))
# print(tag_checker(primary_yoga_tags))
# print(tag_searcher("yogafun", primary_yoga_tags))
