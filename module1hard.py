students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
st_sorted = sorted(list(students))
grades_mean = []
st_dict = {}
for i in range(len(grades)):
    grades_mean.append(sum(grades[i])/len(grades[i]))
    st_dict[st_sorted[i]] = grades_mean[i]
print(st_dict)
