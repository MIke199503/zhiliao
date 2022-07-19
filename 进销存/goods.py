class Good(object):
    def __init__(self, id, name, count, price, unit, type):
        # id：编号     name：名称     count：数量    price：单价    unit：单位     type：种类
        self.id = id
        self.name = name
        self.count = 0
        self.price = 0
        self.unit = unit
        self.type = type
        self.set_count(count)
        self.set_price(price)

    # 数量的限制，如果输入小于0，则返回0
    def set_count(self, count):
        if count > 0:
            self.count = count
        else:
            self.count = 0

    def get_count(self):
        return self.count

    ##单价的限制，如果输入小于0，则返回0
    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            self.price = 0

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.count},{self.unit},{self.type}"
