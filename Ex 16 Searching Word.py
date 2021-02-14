"""Enter the search string will match the word to giving string  """


def MatchWord(sen1, sen2):
    """match the word and give match count"""
    match = 0
    words1 = sen1.strip().split(" ")
    words2 = sen2.strip().split(" ")
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                match += 1
    return match


if __name__ == '__main__':

    lst = ["Python is good", "Python is not Python snack", "i am trying to write good python program", "all write"]
    search_string = input("Enter the search string")
    match_found = [MatchWord(search_string, lst_sen) for lst_sen in lst]
    score_string = [sentance for sentance in sorted(zip(match_found, lst), reverse=True) if sentance[0] != 0]

    print(f"\t{len(score_string)} result found!\n")
    for score, item in score_string:
        print(f"String:\"{item}\" {score} word found from search string")
