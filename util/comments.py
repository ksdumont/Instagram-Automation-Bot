potential_comments = []


def comment_checker(comments):
    print(f"{len(comments)} comments...")
    if len(comments) == len(set(comments)):
        return True
    else:
        return False


def find_duplicates(comments):
    seen = {}
    duplicates = []
    for comment in comments:
        if comment not in seen:
            seen[comment] = 1
        else:
            duplicates.append(comment)
    return duplicates


# print(find_duplicates(potential_comments))
# print(comment_checker(potential_comments))
