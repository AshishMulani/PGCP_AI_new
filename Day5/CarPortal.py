class Car:
    count = 0

    def __init__(self, make, model, price, segment='Economy'):
        self._make = make
        self._model = model
        self._price = price
        self._segment = segment

    @property
    def make(self):
        return self._make

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            return ValueError('Price should be positive')
        else:
            self._price = value

    def __calculate_premium(self, tenure):
        if self._segment == 'Economy':
            return self._price * tenure * 0.05
        else:
            return self._price * tenure * 0.1

        # print(__calculate_premium(self,40000))

    @classmethod
    def from_string(cls,data):
        make,model,price=data.split(',')
        return cls(make,model,int(price))

    def __str__ (self):
        return (f'Car Data: {self._make},{self._model}'
                f'{self._price},{self._segment}')