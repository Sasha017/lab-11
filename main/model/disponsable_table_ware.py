from main.model.matherial_type import MaterialType


class DisponsableTableWare:

    def __init__(self, manufacture="Ukraine", price=35, fire_resistance=0,
                 date_of_manufacture=3, mathetial=MaterialType):
        self.manufacture = manufacture
        self.price = price
        self.fire_resistance = fire_resistance
        self.date_of_manufacture = date_of_manufacture
        self.mathetial = mathetial

    def __str__(self):
        return "manufacture is {} \t price is {} \t fire_resistance {} \t" \
               "date_of_manufacture {} \t mathetial {}" \
            .format(self.manufacture, self.price, self.fire_resistance, self.date_of_manufacture,
                    self.mathetial)
