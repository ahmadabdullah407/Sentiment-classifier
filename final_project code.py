def strip_punctuation(str1):
    str2 = ''
    for ch in str1:
        if ch not in punctuation_chars:
            str2 = str2 + ch
    return str2


def get_pos(str1):
    str2 = strip_punctuation(str1)
    lower_str1 = str2.lower()
    words = lower_str1.split()
    count = 0
    for word in words:
        if word in positive_words:
            count = count + 1
    return count


def get_neg(str1):
    str2 = strip_punctuation(str1)
    lower_str1 = str2.lower()
    words = lower_str1.split()
    count = 0
    for word in words:
        if word in negative_words:
            count = count + 1
    return count


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
vals = []
with open("project_twitter_data.csv") as tweets:
    lines = tweets.readlines()
    header = lines[0]
    for row in lines[1:]:
        vals.append(row.strip().split(','))
with open("resulting_data.csv", "w") as outfile:
    outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    outfile.write('\n')
    for val in vals:
        pos = get_pos(val[0])
        neg = get_neg(val[0])
        net = pos - neg
        row_string = "{},{},{},{},{}".format(val[1], val[2], pos, neg, net)
        outfile.write(row_string)
        outfile.write('\n')



