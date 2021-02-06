import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

vien_pack_lifespans = familiar.lifespans('vein')
artery_pack_lifespans = familiar.lifespans('artery')
vien_pack_test = ttest_1samp(vien_pack_lifespans,71)
print vien_pack_test.pvalue
if (vien_pack_test.pvalue<0.05):
  print 'The Vien Pack is proven to make you live you long!'
else:
  print 'The Vien Pack is probably good for you somehow'
  
package_comparison_results = ttest_ind(vien_pack_lifespans, artery_pack_lifespans).pvalue  
if package_comparison_results<0.05:
  print 'the Artery Package guarantees even stronger results'
else :
  print 'the Artery Package is also a great product!'
  
iron_contingency_table = familiar.iron_counts_for_package()
iron_pvalue = chi2_contingency(iron_contingency_table)[1]
if iron_pvalue<0.05:
  print "The Artery Package Is Proven To Make You Healthier!"
else:
  print 'Artery Pack is also nice'