
def latest(scores):
    return scores[-1]
    # pass


def personal_best(scores):
    return max(scores)
    # pass


def personal_top_three(scores):

    sorted_scores = ordered_list(scores)
    count = 3

    if len(scores) < 3:
        count = len(scores)
    
    return sorted_scores[0:count]
    # lists = []
    # largest = max(scores)
    # scores.remove(largest)
    # lists.append(largest)

    # if len(scores) >= 1:
    #     second_largest = max(scores)
    #     scores.remove(second_largest)
    #     lists.append(second_largest)

    # if len(scores) >= 1:
    #     third_largest = max(scores)
    #     lists.append(third_largest)

    # return lists
        
  
def ordered_list(scores):
    return sorted(scores, reverse=True)


