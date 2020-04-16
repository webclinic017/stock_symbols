from abc import ABC, abstractmethod

import pandas as pd

from stock_symbols.global_constants import STOCK_LIST_COL


class Sorter(ABC):
    
    @abstractmethod
    def sort(self, data: pd.DataFrame):
        pass


class StockDataSorter(Sorter):
    
    def __init__(self, sort_by: list = None, ascending: tuple = None):
        self.sort_by = sort_by
        self.ascending = ascending
    
    def sort(self, stock_data: pd.DataFrame) -> pd.DataFrame:
        copy = stock_data.copy()
        copy = copy.sort_values(self.sort_by, ascending=self.ascending).reset_index(drop=True)
        
        return copy


class StockGroupsSorter(StockDataSorter):
    
    def __init__(self, sort_by: list = None, ascending: tuple = None,
                 stock_list_col=STOCK_LIST_COL, groupby=None, criteria=None, reverse=True):
        super().__init__(sort_by, ascending)
        self.stock_list_col = stock_list_col
        self.groupby = groupby
        self.criteria = criteria
        self.reverse = reverse
    
    def _sort_groups_by_criteria(self, stock_data: pd.DataFrame) -> pd.DataFrame:
        groups = stock_data.groupby(self.groupby)
        sorted_groups = sorted(groups, key=self.criteria, reverse=self.reverse)
        sorted_groups = [kvp[1] for kvp in sorted_groups]
        stock_data = pd.concat(sorted_groups)
        
        return stock_data
    
    def sort(self, stock_data: pd.DataFrame) -> pd.DataFrame:
        copy = stock_data.copy()
        copy = super().sort(copy)
        copy = copy. \
            groupby(self.stock_list_col). \
            apply(lambda df: self._sort_groups_by_criteria(df)). \
            reset_index(drop=True)
        
        return copy
