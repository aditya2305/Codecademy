import numpy as np
import fetchmaker
import pandas as pd
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print rottweiler_tl, np.mean(rottweiler_tl), np.std(rottweiler_tl)

whippet_rescue = fetchmaker.get_is_rescue('whippet')
num = np.count_nonzero(whippet_rescue)

num_whippets = len(whippet_rescue)
pvalue = binom_test(num,num_whippets,0.08)

w = fetchmaker.get_weight('whippet')
p = fetchmaker.get_weight('pitbull')
t = fetchmaker.get_weight('terrier')

w_p_t_pvalue = f_oneway(w,p,t).pvalue

w_p_t =np.concatenate([w,p,t])
labels = ['whippet']*len(w)+['pitbull']*len(p)+['terriers']*len(t)
tukey_result = pairwise_tukeyhsd(w_p_t,labels,0.05)
print tukey_result


