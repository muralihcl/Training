# This is a sample script
import os
import sys
a = 10
b = 20
print ("Sum of {0} and {1} is {2}".format(a,b,a+b))
var1 = os.getcwd()
var2 = os.path.dirname(sys.executable)
print ("Value of variable var1 is: %s" % var1)
print ("Value of variable var2 is: {0}".format(var2))
name = 'Muralidhara K'
print ('Hello Muralidhara K')
var3 = '1'
var4 = 1
type(var3)
type(var4)
print (var3 * 3)
print (var4 * 3)
print ('Hello ',var4)
print ('Hello '+ var4)
print ('Hello %s' % name)

name = input("Enter your name: ")
provider = input("Enter the provider: ")
print(name,provider,sep='@')
import seaborn as sns
import numpy as np
import pandas as pd

letter = input("Enter the alphabet :")
def check_letter(val):
    if val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u':
        print("Entered letter {0} is a vovel".format(val))
    else:
        print("Entered letter {0} is a consonent".format(val))
check_letter(letter)

ds = sns.load_dataset('flights')
ds.head()
sns.distplot(a=ds['passengers'])
sns.distplot(a=ds['passengers'],kde=False,bins=25)

from scipy import stats
sns.distplot(a=ds['passengers'],rug=True,color='b',fit=stats.norm,
             hist_kws={"linewidth": 1,
                       "alpha": 0.5, "color": "g", "label": "Hist"},
             kde_kws={"color": "r", "lw": 2, "label": "KDE"}
             )

sns.kdeplot(data=ds['passengers'],shade=True)
sns.kdeplot(data=ds['passengers'],shade=True,cumulative=True)
y = np.random.randn(144)+200
ds=ds.assign(passengers_new=y)
sns.jointplot(x="passengers",y="passengers_new",data=ds,kind="reg")
corr = ds.corr()
sns.heatmap(corr)
sns.heatmap(corr,annot=True)
p = [1,2,3,4,5,6,7,8,9,10]
p
np.random.choice(p, size=5)
np.random.seed(10)
np.random.choice(p, size=5)
np.random.seed(10)
np.random.choice(p, size=5, replace=False)
