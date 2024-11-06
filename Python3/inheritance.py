class Fruit:
    def __init__(self, ripe):
        if not  isinstance(ripe, bool):
            raise ValueError("The 'ripe' attribute must be a boolean value (True or False).")
        self.ripe = ripe
        #print(f"Fruit is {'ripe' if self.ripe else 'not ripe'}.")
        print(f"Fruit is {'ripe' if self.ripe else 'not ripe'}")

class Apple(Fruit):
    def __init__(self):
        super().__init__(False)
        print("This is Apple")

fruit =Apple()
                