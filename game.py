import numpy as np
import string
import re


words_data = []
with open("words.txt", "r") as fr:
    for line in fr.readlines():
        line = line.strip()
        words_data.append(line)

data = []
with open("data.txt", "r") as fr:
    for line in fr.readlines():
        line = line.strip().split(",")
        data.append(line)
    data = np.array(data)
    m, n = data.shape
    if m != 11 | n != 11:
        print "have error in input"

letters = list("pianeee")

amazing = len(filter(lambda x: x == "0", letters))
letters = filter(lambda x: x != "0", letters)
answer = []


def transform(letter_list, int_amazing, mode):
    if int_amazing <= 0:
        return letter_list
    else:
        for x in list(string.lowercase):
            letter_list_copy = letter_list[:]
            letter_list_copy.append(x)
            int_amazing_copy = int_amazing - 1
            last_letter_list = transform(letter_list_copy, int_amazing_copy, mode)
            if last_letter_list != None:
                last_letter_list.extend(list(re.sub(r'0', '', word)))
                ind = 0
                for index, ans_letter in enumerate(ans_letters):
                    if ans_letter in last_letter_list:
                        del (last_letter_list[last_letter_list.index(ans_letter)])
                        ind = index
                    else:
                        break
                if ind == len(ans_letters) - 1:
                    if mode == "row":
                        print i + 1, j + 1, mode, ans.group(0)
                        answer.append([i + 1, j + 1, mode, ans.group(0)])
                    else:
                        print j + 1, i + 1, mode, ans.group(0)
                        answer.append([j + 1, i + 1, mode, ans.group(0)])


# read line by row
for i in range(m):
    for j in range(0, m-1):
        for k in range(1, m+1):
            if j+k >= m:
                break
            word = data[i, j:j+k+1]
            if j+k+1 <= 10:
                if re.match(r"[A-Za-z]", data[i, j+k+1]):
                    continue
            if j > 0:
                if re.match(r"[A-Za-z]", data[i, j-1]):
                    continue
            if sum(map(lambda x:x!="0", word)) == 0:
                continue
            word = "".join(word)
            re_word = re.sub(r'0', '\w', word)
            for wor in words_data:
                ans = re.match(re_word+"$", wor)
                if ans:
                    ans_letters = list(ans.group(0))
                    letters_copy = letters[:]
                    if amazing > 0:
                        transform(letters_copy, amazing, "row")
                    else:
                        ind = 0
                        letters_copy = letters[:]
                        for index, ans_letter in enumerate(ans_letters):
                            if ans_letter in letters_copy:
                                del (letters_copy[letters_copy.index(ans_letter)])
                                ind = index
                            else:
                                break
                        if ind == len(ans_letters) - 1:
                            print i + 1, j + 1, "row", ans.group(0)
                            answer.append([i + 1, j + 1, "row", ans.group(0)])


data = data.T
for i in range(m):
    for j in range(0, m-1):
        for k in range(1, m+1):
            if j+k >= m:
                break
            word = data[i, j:j+k+1]
            if j+k+1 <= 10:
                if re.match(r"[A-Za-z]", data[i, j+k+1]):
                    continue
            if j > 0:
                if re.match(r"[A-Za-z]", data[i, j-1]):
                    continue
            if sum(map(lambda x:x!="0", word)) == 0:
                continue
            word = "".join(word)
            re_word = re.sub(r'0', '\w', word)
            for wor in words_data:
                ans = re.match(re_word+"$", wor)
                if ans:
                    ans_letters = list(ans.group(0))
                    letters_copy = letters[:]
                    if amazing > 0:
                        transform(letters_copy, amazing, "column")
                    else:
                        ind = 0
                        letters_copy = letters[:]
                        for index, ans_letter in enumerate(ans_letters):
                            if ans_letter in letters_copy:
                                del (letters_copy[letters_copy.index(ans_letter)])
                                ind = index
                            else:
                                break
                        if ind == len(ans_letters) - 1:
                            print j + 1, i + 1, "column", ans.group(0)
                            answer.append([j + 1, i + 1, "column", ans.group(0)])
data = data.T





