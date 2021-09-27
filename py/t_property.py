

class Test():
    _order_id = 1

    @property
    def order_id(self):
        self._order_id += 1
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    

    def run(self):
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        self.order_id = 50
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        self.order_id = 5
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)
        print(self.order_id)


if __name__ == "__main__":
    t = Test()
    t.run()
