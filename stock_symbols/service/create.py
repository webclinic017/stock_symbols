from abc import ABC, abstractmethod

import pandas as pd

from stock_symbols.global_constants import SYMBOL_COL, DB_PREF_STOCK_KW, ST_PREF_STOCK_KW, STOCK_LIST_COL, \
    IB_PREF_STOCK_KW

pd.set_option('mode.chained_assignment', None)


class Creator(ABC):
    
    @abstractmethod
    def create(self, data: pd.DataFrame):
        pass


class ListCreator(Creator):
    
    def __init__(self):
        self.stock_lists = None
    
    def create(self, stock_data: pd.DataFrame):
        self._get_symbols(stock_data)
        self._convert_symbols()
        
        return self.stock_lists
    
    def _get_symbols(self, stock_data):
        self.stock_lists = stock_data[[STOCK_LIST_COL, SYMBOL_COL]]
    
    @abstractmethod
    def _convert_symbols(self):
        pass


class SterlingTraderListCreator(ListCreator):
    
    def _convert_symbols(self):
        self.stock_lists[SYMBOL_COL] = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW, ST_PREF_STOCK_KW)


class InteractiveBrokersListCreator(ListCreator):
    IB_STOCK_LIST_DES_COL = "destination"
    IB_STOCK_LIST_DES_COL_VAL = "DES"
    IB_STOCK_LIST_TYPE_COL = "stock_type"
    IB_STOCK_LIST_TYPE_COL_VAL = "STK"
    IB_STOCK_LIST_EXCHANGE_COL = "exchange"
    IB_STOCK_LIST_EXCHANGE_COL_VAL = "SMART/NYSE"
    IB_SOCK_LIST_FIRST_ROW_VAL_1 = "COLUMN"
    IB_SOCK_LIST_FIRST_ROW_VAL_2 = 0
    ib_stock_list_first_row = pd.DataFrame([[None, IB_SOCK_LIST_FIRST_ROW_VAL_1, IB_SOCK_LIST_FIRST_ROW_VAL_2]],
                                           columns=[STOCK_LIST_COL, IB_STOCK_LIST_DES_COL, SYMBOL_COL])
    
    def create(self, stock_data: pd.DataFrame):
        self.stock_lists = super().create(stock_data)
        self._create_ib_watchlists()
        
        return self.stock_lists
    
    def _convert_symbols(self):
        self.stock_lists.loc[:, SYMBOL_COL] = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW,
                                                                                       IB_PREF_STOCK_KW)
    
    def _create_ib_watchlists(self):
        self._add_feature_cols()
        self._reorder_cols()
        self._add_watchlists_header_rows()
    
    def _add_feature_cols(self):
        self.stock_lists.loc[:, self.IB_STOCK_LIST_DES_COL] = self.IB_STOCK_LIST_DES_COL_VAL
        self.stock_lists.loc[:, self.IB_STOCK_LIST_TYPE_COL] = self.IB_STOCK_LIST_TYPE_COL_VAL
        self.stock_lists.loc[:, self.IB_STOCK_LIST_EXCHANGE_COL] = self.IB_STOCK_LIST_EXCHANGE_COL_VAL
    
    def _reorder_cols(self):
        self.stock_lists = self.stock_lists[
            [STOCK_LIST_COL, self.IB_STOCK_LIST_DES_COL, SYMBOL_COL, self.IB_STOCK_LIST_TYPE_COL,
             self.IB_STOCK_LIST_EXCHANGE_COL]]
    
    def _add_watchlists_header_rows(self):
        self.stock_lists = self.stock_lists \
            .groupby(STOCK_LIST_COL) \
            .apply(self._add_watchlist_header_row) \
            .reset_index(drop=True)
    
    def _add_watchlist_header_row(self, df):
        stock_list_name = df[STOCK_LIST_COL].iloc[0]
        self.ib_stock_list_first_row[STOCK_LIST_COL] = stock_list_name
        df = self.ib_stock_list_first_row.append(df).reset_index(drop=True)
        
        return df
