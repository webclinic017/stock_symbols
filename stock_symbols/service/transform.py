from abc import ABC, abstractmethod

import pandas as pd

from stock_symbols.common.utils import invert_dict
from stock_symbols.global_constants import STOCK_LIST_COL


class Transformer(ABC):
    
    @abstractmethod
    def transform(self, data: pd.DataFrame):
        pass


class StockDataTransformer(Transformer):
    
    def __init__(self, list_cols: list = None):
        self.list_cols = list_cols
    
    def transform(self, stock_data: pd.DataFrame):
        copy = stock_data.copy()
        copy = copy[self.list_cols]
        
        return copy


class ListNamesTransformer(StockDataTransformer):
    
    def __init__(self, list_cols: list, stock_list_map, stock_list_col=STOCK_LIST_COL, map_col=None):
        super(ListNamesTransformer, self).__init__(list_cols)
        self.stock_list_map = stock_list_map
        self.stock_list_col = stock_list_col
        self.map_col = map_col
    
    def _create_stock_list_name_col(self, stock_data: pd.DataFrame) -> pd.DataFrame:
        inverted_list_map = invert_dict(self.stock_list_map)
        stock_data[self.stock_list_col] = stock_data[self.map_col].map(inverted_list_map)
        
        return stock_data
    
    def transform(self, stock_data: pd.DataFrame) -> pd.DataFrame:
        copy = stock_data.copy()
        copy = super().transform(copy)
        copy = self._create_stock_list_name_col(copy)
        
        return copy
