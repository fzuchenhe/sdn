# 使用方法
进入文件夹后即可看见本次实验提交的材料，其中.py文件是本次实验的主要代码，txt文件为随机生成的学生数据

## 具体函数用法：
init_student_list和init_teacher_list方法用于生成随机学生数据
ran_num_project()用于生成随机（5，8）个缺席80%课程的同学fiirst
attend函数模拟学生出席的情况，roll_call函数模拟点名过程，其中，每次点名之前学生要先调用attend函数模拟学生出席
由于第一次点名为全点，采用first_roll_call函数进行第一次点名
attend函数负责模拟所有学生的出席情况


    write_student()
    write_teacher()
    write_situation(day）
    以上三个函数用于将学生表和教师表打印出来，write_situation负责打印点名情况
