
class Good_item:
    """
    商品
    """
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

class Store:
    """
    一个简单的类
    """

    # 自执行初始化函数
    def __init__(self, name):
        # 设置商店名称
        self.name = name
        # 设置商店的货物
        self.goods = []
        self.total_goods = 0
        self.total_price = 0

    def add_item(self, name="新商品", price=0, num=1):
        good_item = Good_item(name, price, num)
        # 向商店添加货物
        self.goods.append(good_item)
        self.total_goods += 1
        self.update_total_price()

    def update_total_price(self):
        for good in self.goods:
            self.total_price += good.price * good.num

    # 定义自定义对象打印信息
    def __repr__(self):
        return f'<Store {self.name}>'


my_store = Store('my store')

my_store.add_item('apple', 5)
my_store.add_item('banana', 10)
# my_store.add_item('orange', 15)

print(my_store.total_goods)
print(my_store.total_price)
print(my_store)