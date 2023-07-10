import pandas as pd

# df = pd.read_csv("output.csv",dtype={'related':'str', 'title':'str', 'asin':'str', 'price':'str', 'brand':'str',
#                                      'imUrl':'str', 'categories':'str', 'salesRank':'str', 'description':'str'})
#
# df.to_csv("output2.csv",index=False)

df = pd.read_csv("output.csv",delimiter="\t")

