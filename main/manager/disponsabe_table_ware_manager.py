from main.model.disponsable_table_ware import DisponsableTableWare


class DisponsableTableWareManager:

    def __init__(self):
        self.table_ware_list = []

    def add_table_wares(self, *all_table_wares: DisponsableTableWare):
        for table_ware in all_table_wares:
            self.table_ware_list.append( table_ware )

    def find_table_ware_by_price(self, needed_price: int):
        """
        >>> table_ware_first = DisponsableTableWare("Ukraine", 20, 20, 3, 1)
        >>> table_ware_second = DisponsableTableWare("USA", 65, 5, 3, 2)
        >>> table_ware_third = DisponsableTableWare("Canada", 30, 23, 14, 3)
        >>> disponsable_table_ware_manager = DisponsableTableWareManager()
        >>> disponsable_table_ware_manager.add_table_wares(table_ware_first, table_ware_second, table_ware_third)
        >>> founded_table_ware_list = disponsable_table_ware_manager.find_table_ware_by_price(20)
        >>> [table_ware.price for table_ware in founded_table_ware_list]
        [20]
        """
        founded_table_ware_list: list = []
        for table_ware in self.table_ware_list:
            if table_ware.price == needed_price:
                founded_table_ware_list.append(table_ware)
        return founded_table_ware_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, extraglobs={'disponsable_table_ware_manager': DisponsableTableWareManager()} )
