import random
import numpy as np

grade = np.random.normal(2.7, 0.6, [1, 90])
sabsents = np.random.normal(0.5, 0.15, [1, 90])
students = []
teachers = []
unlike_study = []


def sort_unwilling(arr, left, right):
    if len(arr) <= 1 or left > right:
        return
    temp = arr[left][3]
    i = left
    j = right
    while i < j:
        while arr[j][3] >= temp and i < j:
            j -= 1
        while arr[i][3] <= temp and i < j:
            i += 1
        if i < j:
            mTemp = arr[j][3]
            arr[j][3] = arr[i][3]
            arr[i][3] = mTemp
    arr[left][3] = arr[i][3]
    arr[i][3] = temp
    sort_unwilling(arr, left, j - 1)
    sort_unwilling(arr, j + 1, right)


def sort_sno(arr, left, right):
    if len(arr[1]) <= 1 or left > right:
        return
    temp = arr[left][0]
    i = left
    j = right
    while i < j:
        while arr[j][0] >= temp and i < j:
            j -= 1
        while arr[i][0] <= temp and i < j:
            i += 1
        if i < j:
            mTemp = arr[j][0]
            arr[j][0] = arr[i][0]
            arr[i][0] = mTemp
    arr[left][0] = arr[i][0]
    arr[i][0] = temp
    sort_sno(arr, left, j - 1)
    sort_sno(arr, j + 1, right)


def init_student_list(num):
    for p in range(num):
        students.append([320000001 + p, grade[0][p], sabsents[0][p], 0, 0, p + 1])


def init_teacher_list():
    for i in range(len(students)):
        teachers.append([students[i][0], students[i][1], 0, 0, 0, i + 1])


def write_student():
    # sort_sno(students,0,89)
    f = open("student_table.txt", "w")
    f.write(" 学号        绩点         兴趣度量    出勤意愿     是否出勤 " + "\n")
    for i in range(len(students)):
        f.write("%d   %f    %f   %f    %d\n" % (
            students[i][0], students[i][1], students[i][2], students[i][3], students[i][4]))
    f.close()


def write_teacher():
    # sort_sno(students, 0, 89)
    t = open("teacher_table.txt", "w")
    t.write("学号             绩点         不信任度         缺勤值度量     点名情况" + "\n")
    for j in range(len(students)):
        t.write("%d     %f      %f       %f         %d\n" % (
            teachers[j][0], teachers[j][1], teachers[j][2], teachers[j][3], teachers[j][4]))
    t.close()


def ran_num_project():
    rand = random.randint(5, 8)
    unlike_study.append(random.sample(students, rand))


def write_situation(day):
    sort_sno(students, 0, 89)
    s = open("situation.txt", 'a')
    s.write("第%d节课的记录\n" % day)
    day += 1
    s.write("学号       是否出勤     点名情况\n")
    for i in range(len(students)):
        s.write(str(students[i][0]) + "   " + str(students[i][4]) + "          " + str(teachers[i][4]) + '\n')
    s.close()
    return day


def attend():
    for i in range(len(students)):
        if students[i] in unlike_study[0]:
            rand = random.randint(1, 5)
            if rand <= 4:
                students[i][2] = -100
                students[i][4] = 1
    sort_unwilling(students, 0, len(students) - 1)
    rand = random.randint(0, 3)
    rand2 = random.randint(0, 5)
    for l in range(rand2):
        rand3 = random.randint(0, len(students) - 1)
        students[rand3][4] = 1
    for k in range(rand):
        students[-k][4] = 1
        students[-k][2] += 1
        students[-k][3] = students[-k][2] * 0.7 + students[-k][1] * 0.3
    for j in range(len(students)):
        students[i][3] = 0.7 * students[i][2] + 0.3 * students[i][1]


def init():
    init_student_list(90)
    init_teacher_list()
    ran_num_project()


def first_roll_call():
    for i in range(len(students)):
        if students[i][4] == 1:
            teachers[i][4] = 1
            teachers[i][2] += 1
            teachers[i][3] = teachers[i][2] * 0.7 + teachers[i][1] * 0.3


def roll_call():
    sort_unwilling(teachers, 0, len(students) - 1)
    for i in range(15):
        if students[i][4] == 1:
            teachers[students[-i][5]][4] = 1
            teachers[students[-i][5]][2] += 1
    for k in range(10):
        rand4 = random.randint(0, len(students) - 1)
        for h in range(rand4):
            if students[i][4] == 1:
                teachers[students[i][5]][4] = 1
                teachers[students[i][5]][2] += 1


def get_E():
    count = 0
    for i in range(len(teachers)):
        if teachers[i][4] == 1:
            count += 1
    print("本次点名的E值为：", count / 25)


def call(day):
    attend()
    roll_call()
    write_student()
    write_teacher()
    write_situation(day)
    get_E()


def main():
    init()
    attend()
    first_roll_call()
    for i in range(20):
        call(i+1)


if __name__ == "__main__":
    day = 1
    main()
