from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd

def cat2num(table):
	dd = {}
	for c in table.columns:
		dd.update({c: [0]*table.shape[0]})
	num_table = pd.DataFrame(dd)
	for col in table.columns:
		feat_set = table[col].unique()
		for i in range(table.shape[0]):
			for j in range(feat_set.shape[0]):
				if table[col][i] == feat_set[j]:
					num_table[col][i] = j
					break
	return num_table

def c2(feat1, feat2, tab):
	feat1_set = tab[feat1].unique()
	feat2_set = tab[feat2].unique()
	count_table = np.zeros([feat1_set.shape[0],feat2_set.shape[0]])
	for i in tab.index:
		for m in range(feat1_set.shape[0]):
			if tab[feat1][i] == feat1_set[m]:
				for n in range(feat2_set.shape[0]):
					if tab[feat2][i] == feat2_set[n]:
						count_table[m,n] += 1
						break
				break
	# freq_table = count_table / count_table.sum()
	chi2_value, p_value, dof, expected = chi2_contingency(count_table)
	return (chi2_value, p_value)
