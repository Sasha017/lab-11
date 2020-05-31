from main.model.disponsable_table_ware import DisponsableTableWare


class Glass( DisponsableTableWare ):
    def _init_(self, temperature_resistance=40, water_capacity_gal=2):
        super( DisponsableTableWare, self )
        self.temperature_resistance = temperature_resistance
        self.water_capacity_gal = water_capacity_gal

    def _str_(self):
        return super()._str_() + ", temperature_resistance %s" % self.temperature_resistance + \
               ", water_capacity_gal %s" % self.water_capacity_gal
