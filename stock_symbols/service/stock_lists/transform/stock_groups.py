import pandas as pd


def order_groups_by_criteria(data, groupby=None, criteria=None, reverse=True):
	groups = data.groupby(groupby)
	ordered_groups = sorted(groups, key=criteria, reverse=reverse)
	ordered_groups = [kvp[1] for kvp in ordered_groups]
	
	return pd.concat(ordered_groups)
