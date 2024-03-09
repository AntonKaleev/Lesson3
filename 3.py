class Human:
    default_name = ' jek'
    default_age = 12
    def __init__(self, money ,house, name = default_name ,age = default_age):
        self.name = name
        self.age = age
        self.__money= money
        self.__house= house
    def info(self):
        print(str(self.name)+' '+str(self.age)+' '+str(self.__house)+' '+str(self.__money))
    def default_info() :
        default_name = ' jek'
        default_age = 12
        print(str(default_name)+' '+str(default_age))
    def earn_money(self,sum):
        self.__money=self.__money+sum
    def __make_deal(self,price,ss_house):
        self.__money=self.__money-price
        self.__house=ss_house
        print('вы купили дом')
    def buy_house(self,price, num):
        if price<=self.__money:
            print('достаточно средств')
            self.__make_deal(price , num)
        else:
            print('не достаточно средств')
class House:
    def __init__(self,price,area):
        self.price = price
        self.__area = area
    def final_price(self,sale):
        self.__price= self.__price*(sale/100)
class SmallHouse(House):
    def __init(self,price,area=40):
        self.__area = area
        self.__price = price
buyer = Human(1200,None, 'sd',18)
buyer.info()
Human.default_info()
smal = SmallHouse(2,500)
buyer.buy_house(smal._SmallHouse__price,smal)
buyer.info()
buyer.earn_money(2131)
buyer.info()
