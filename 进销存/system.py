from goods import Good


# 导入判断数据的模块

class Wms(object):
    # [1]程序的准备工作，创建列表，输出程序功能框，将程序可以实现的功能展示给用户
    def __init__(self):
        self.good_data = []

    def sendout(self):
        print("=================================================")
        print("---------------阿里巴巴·进销存系统------------------")
        print("------------------1.录入货物----------------------")
        print("------------------2.添加货物----------------------")
        print("------------------3.修改货物----------------------")
        print("------------------4.取出货物----------------------")
        print("------------------5.移除货物----------------------")
        print("------------------6.查看货物----------------------")
        print("------------------7.退出系统----------------------")

    # aaa,bbb,ccc 完成了录入货物 [bbb,ccc为aaa的判断条件]
    def aaa_good(self):
        good_id = input("请输入货物编号：")
        while (not self.ccc_good(good_id, isint=True) or self.bbb_good(good_id)):
            if self.bbb_good(good_id):
                print("该编号已占用")
            good_id = input("请输入货物编号：")
        good_name = input("请输入货物名称：")
        good_pirce = input("请输入货物单价：")
        while not self.ccc_good(good_pirce):
            good_pirce = input("请输入货物单价：")
        good_count = input("请输入货物数量：")
        while not self.ccc_good(good_count):
            good_count = input("请输入货物数量：")
        good_unit = input("请输入货物计量单位：")
        good_type = input("请输入货物类型：")
        good = Good(good_id, good_name, float(good_pirce), int(good_count), good_unit, good_type)
        self.good_data.append(good)
        print("添加货物成功！")

    # 判断条件，判断数据库中有没有你要添加ID
    def bbb_good(self, id):
        for item in self.good_data:
            if item.id == id:
                return True
            else:
                return False

    # 判断条件，判断输入的格式是否正确
    def ccc_good(self, str, isint=False):
        if isint:
            try:
                res = int(str)
            except:
                print("输入数据格式有误请从新输入")
                return False
            else:
                return True
        else:
            try:
                res = float(str)
            except:
                print("输入数据格式有误请从新输入")
                return False
            else:
                return True

    # 实现添加功能
    def ddd_good(self):
        while True:
            good_id = input("请输入货物编号：")
            for item in self.good_data:
                if item.id == good_id:
                    aa = float(input("请输入添加的数量："))
                    item.count += aa
                    print("添加成功")
                    print(item.count)
                    return
                else:
                    pass

    # 实现修改功能
    def eee_good(self):
        while True:
            good_id = input("请输入货物编号：")
            for item in self.good_data:
                if item.id == good_id:
                    good_name = input("请输入货物名称：")
                    item.name = good_name
                    good_pirce = input("请输入货物单价：")
                    while not self.ccc_good(good_pirce):
                        good_pirce = input("请输入货物单价：")
                    item.price = good_pirce
                    good_count = input("请输入货物数量：")
                    while not self.ccc_good(good_count):
                        good_count = input("请输入货物数量：")
                    item.count = good_count
                    good_unit = input("请输入货物计量单位：")
                    item.unit = good_unit
                    good_type = input("请输入货物类型：")
                    item.type = good_type

                    print("添加成功")
                    return
                else:
                    pass

    # 实现取出功能
    def fff_good(self):
        while True:
            good_id = input("请输入货物编号：")
            for item in self.good_data:
                if item.id == good_id:
                    aa = float(input("请输入取出货物的数量："))
                    item.count -= aa
                    print("取出成功")
                    print(item.count)
                    return
                else:
                    pass

    # 实现移除功能
    def ggg_good(self):
        while True:
            good_id = input("请输入货物编号")
            for item in self.good_data:
                if item.id == good_id:
                    self.good_data.remove(item)
                    print("移除成功")
                    return
                else:
                    pass

    # 查看货物
    def hhh_good(self):
        print("----货物信息如下---")
        for item in self.good_data:
            print(f"编号{item.id}  名称{item.name}    数量{item.count}    单价{item.price}    单位 {item.unit}    种类{item.type}")

    # 主循环【主程序】
    def run(self):
        while True:
            self.sendout()
            index = input("$$请输入操作指令$$：")
            if index == "1":
                self.aaa_good()
            elif index == "2":
                self.ddd_good()
            elif index == "3":
                self.eee_good()
            elif index == "4":
                self.fff_good()
            elif index == "5":
                self.ggg_good()
            elif index == "6":
                self.hhh_good()
            elif index == "7":
                print("拜拜了您嘞奥里给")
                return
            else:
                print("你输的啥鬼玩意，再来一遍")
