str = input().upper()
str_list = list(set(str))
count_list = []
print(str_list)
for c in str_list:
    count = str.count(c)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
elif count_list.count(max(count_list)) == 1:
    max_index = count_list.index(max(count_list))
    print(str_list[max_index])