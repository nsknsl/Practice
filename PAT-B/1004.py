
n = int(input())

name_list = list()
num_list = list()
grade_list = list()

for i in range(n):
    seq = input()
    seq = seq.split(" ")

    name_list.append(seq[0])
    num_list.append(seq[1])
    grade_list.append(int(seq[2]))
max_idx = grade_list.index(max(grade_list))
min_idx = grade_list.index(min(grade_list))
print("{} {}".format(name_list[max_idx], num_list[max_idx]))
print("{} {}".format(name_list[min_idx], num_list[min_idx]))
