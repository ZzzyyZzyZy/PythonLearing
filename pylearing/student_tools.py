student_list = []

def new_student():
    """新建名片"""
    print("-" * 50)
    print("功能:新建学生")
    #提示用户输入学生信息
    name = input("请输入姓名：")
    gender = input("请输入性别：")
    age = input("请输入年龄：")
    team = input("请输入班级：")
    # 将学生信息保存到一个字典
    student_dict = {"name": name,
                    "gender": gender,
                    "age": age,
                    "team": team}
    # 将学生字典添加到学生列表
    student_list.append(student_dict)

def show_all_student():
    """显示全部学生"""
    # 显示全部学生模块信息提示
    print("-" * 50)
    print("功能：显示全部学生")

    # 遍历列表显示全部学生信息
    for name in ["姓名", "性别", "年龄", "班级"]:
        print(name, end="\t\t")
    print("")
    # 打印分隔线
    print("=" * 50)
    # 格式化输出信息
    for student_dict in student_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (student_dict["name"],
                                        student_dict["gender"],
                                        student_dict["age"],
                                        student_dict["team"]))


def search_student():
    """查询学生信息"""
    # 查询学生信息模块信息提示
    print("-" * 50)
    print("功能：搜索名片")
    # 提示用户输入搜索学生的姓名
    find_name = input("请输入要查询的学生姓名：")
    # 遍历字典进行查询
    for student_dict in student_list:
        if student_dict["name"] == find_name:
            print("姓名\t\t\t性别\t\t\t年龄\t\t\t班级")
            print("-" * 40)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (
                student_dict["name"],
                student_dict["gender"],
                student_dict["age"],
                student_dict["team"]))
            print("-" * 40)
            # 找到后进行后续操作：修改/删除
            # 提示用户输入修改学生的相关信息
            options = input("请选择要执行的操作[1] 修改 [2] 删除 [0] 返回上级菜单")
            if options == "1":
                student_dict["name"] = input("请输入姓名：")
                student_dict["gender"] = input("请输入性别：")
                student_dict["age"] = input("请输入年龄：")
                student_dict["team"] = input("请输入班级：")
                # 提示修改成功信息
                print("学生：'%s'的信息修改成功" % student_dict["name"])
            elif options == "2":
                student_list.remove(student_dict)
                # 提示删除成功信息

                print("学生：'%s'的信息删除成功" % student_dict["name"])
            break
    else:
        # 没有找到输出提示信息
        print("没有找到 %s" % find_name)
