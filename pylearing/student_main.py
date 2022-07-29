from student_tools import new_student,show_all_student,search_student

# 通过死循环控制整个业务主体运行
while True:
    # 编写系统欢迎界面，并显示功能菜单
    print("*" * 20)
    print("欢迎使用【学生管理系统】1.0\n\n1. 新增学生\n2. 显示全部学生\n3. 查询学生\n0. 退出系统")
    print("*" * 20)
    # 提供用户输入选项
    option = input("请选择操作功能：")

    # 对输入选项进行输出
    print("您选择的操作是：%s" % option)

    # 根据用户输入决定后续的操作
    if option in ["1", "2", "3"]:
        if option == "1":
            new_student()
        elif option == "2":
            show_all_student()
        elif option == "3":
            search_student()
    elif option == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误，请重新输入")