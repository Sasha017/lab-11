from main.model.disponsable_table_ware import DisponsableTableWare
from main.model.sort_type import SortType


class DisponsableTableWareManagerUtils:

    @staticmethod
    def sort_by_date(table_ware_list, sort_type):
        """
        Sorting by date
        >>> new_created_list = [DisponsableTableWare("none", 35, 0, 23, 1), \
        DisponsableTableWare("none", 35, 1, 7, 2), DisponsableTableWare("none", 23, 1, 14, 3)]
        >>> DisponsableTableWareManagerUtils.sort_by_date(new_created_list, SortType(1))
        >>> print(new_created_list[0].date_of_manufacture)
        25
        >>> print(new_created_list[1].date_of_manufacture)
        30
        >>> print(new_created_list[2].date_of_manufacture)
        40
        """
        if sort_type == SortType( 1 ):
            table_ware_list.sort( key=lambda table_ware:table_ware.date_of_manufacture )
        elif sort_type == SortType( 2 ):
            table_ware_list.sort( key=lambda table_ware:table_ware.date_of_manufacture,
                                  reverse=True )
        else:
            print( "Oh no,cant sort" )

    @staticmethod
    def sort_by_price(table_ware_list, sort_type):
        """
        Sorting by price
        >>> new_created_list = [DisponsableTableWare("none", 35, 0, 23, 1), \
        DisponsableTableWare("none", 35, 1, 7, 2), DisponsableTableWare("none", 23, 1, 14, 3)]
        >>> DisponsableTableWareManagerUtils.sort_by_price(new_created_list, SortType(1))
        >>> print(new_created_list[0].price)
        25
        >>> print(new_created_list[1].price)
        30
        >>> print(new_created_list[2].price)
        40
        """
        if sort_type == SortType( 1 ):
            table_ware_list.sort( key=lambda table_ware:table_ware.price )
        elif sort_type == SortType( 2 ):
            table_ware_list.sort( key=lambda table_ware:table_ware.price_per_hour,
                                  reverse=True )
        else:
            print( "Can't sort" )


if __name__ == '__main__':
    import doctest

    doctest.testmod( verbose=True )
