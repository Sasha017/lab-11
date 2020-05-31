from main.model.disponsable_table_ware import DisponsableTableWare


class Fork( DisponsableTableWare ):
    def _init_(self, strenght=3, weight_capacity_kg=5):
        super( DisponsableTableWare, self )
        self.strenght = strenght
        self.weight_capacity_kg = weight_capacity_kg

    def _str_(self):
        return super()._str_() + ", strenght %s" % self.strenght + ", weight_capacity_kg %s" % self.weight_capacity_kg
