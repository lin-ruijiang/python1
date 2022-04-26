import os
import re

filename = 'student.txt'


def menu():
    print('==========================学生管理系统=========================')
    print('---------------------------功能菜单---------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.按照成绩排序')
    print('\t\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t\t7.显示学生信息')
    print('\t\t\t\t\t\t0.退出当前系统')
    print('-------------------------------------------------------------')


def main():
    while True:
        menu()
        choice = int(input('请输入你的选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('你确定要退出系统吗?y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢你的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def insert():
    student_list = []
    while True:
        id = input('请输入学生ID:')
        if not id:
            break

        name = input('请输入学生姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            java = int(input('请输入java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加?y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完成！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        if os.path.exists(filename):
            with  open(filename, 'r', encoding='utf-8')as file:
                student = file.readlines()
                if student:
                    mode = input('按ID查找请输入1，按姓名查找请输入2：')
                    if mode == '1':
                        student_id = input('请输入要查找的学生ID:')
                        if id != '':
                            for item in student:
                                d = dict(eval(item))
                                if d['id'] == student_id:
                                    student_query.append(d)
                        else:
                            print('输入为空，请重新输入')
                            continue
                    elif mode == '2':
                        name = input('请输入要查找的学生姓名:')
                        if name != '':
                            for item in student:
                                d = dict(eval(item))
                                if d['name'] == name:
                                    student_query.append(d)
                        else:
                            print('输入为空，请重新输入')
                            continue
                    else:
                        print('输入有误，请重新输入')
                        search()
                else:
                    print('无学生信息')
                    break
                show_student(student_query)
                student_query.clear()
                answer = input('是否继续查询?y/n')
                if answer == 'y' or answer == 'Y':
                    continue
                else:
                    break
        else:
            student_query = []
            print('无学生信息')
            break


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


def delete():
    while True:
        if os.path.exists(filename):
            with  open(filename, 'r', encoding='utf-8')as file:
                student_old = file.readlines()
        else:
            student_old = []
            print('无学生信息')
            break
        flag = False
        if student_old:
            student_id = input('请输入要删除的学生ID:')
            if student_id != '':
                with  open(filename, 'w', encoding='utf-8')as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('输入为空，请重新输入')
                continue
            show()
        else:
            print('无学生信息')
            break
        answer = input('是否继续删除?y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def modify():
    while True:
        show()
        if os.path.exists(filename):
            with  open(filename, 'r', encoding='utf-8')as file:
                student_old = file.readlines()
        else:
            student_old = []
            print('无学生信息')
            break
        flag = False
        if student_old:
            student_id = input('请输入要修改的学生ID:')
            if student_id != '':
                with  open(filename, 'w', encoding='utf-8')as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                            print('找到学生信息，可以进行修改操作')
                            while True:
                                try:
                                    d['name'] = input('请输入姓名：')
                                    d['english'] = input('请输入英语成绩：')
                                    d['python'] = input('请输入python成绩：')
                                    d['java'] = input('请输入java成绩：')
                                except:
                                    print('你的输入有误,请重新输入!!!')
                                else:
                                    break
                            wfile.write(str(d) + '\n')

                    if flag:
                        print(f'id为{student_id}的学生信息已被修改')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('输入为空，请重新输入')
                continue

        else:
            print('无学生信息')
            break
        answer = input('是否继续修改?y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
            student_new = []
            for item in student_list:
                d = dict(eval(item))
                student_new.append(d)
    else:
        print('无学生信息')
        return
    asc_or_desc = input('请选择（0.升序 1.降序）：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式（1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序')
    if mode == "1":
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == "2":
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == "3":
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == "0":
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            studentdata = rfile.readlines()
            if studentdata:
                print(f'一共有{len(studentdata)}名学生')
    else:
        print('暂未保存任何数据信息')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            studentdata = rfile.readlines()
            for item in studentdata:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            else:
                print('暂未保存任何数据信息')
                return
    else:
        print('暂未保存任何数据信息')
        return


if __name__ == '__main__':
    main()
