import json
import copy
import csv

f = open("output.strict","r")
f2 = open("output.csv","w",newline='')
all_keys = ['title', 'asin', 'price', 'brand', 'imUrl', 'categories', 'salesRank', 'description',
            'also_bought','also_viewed','bought_together','buy_after_viewing']
csv_writer = csv.DictWriter(f2, sorted(all_keys), delimiter='\t')
csv_writer.writeheader()
line = f.readline()
# all_keys = ['related', 'title', 'asin', 'price', 'brand', 'imUrl', 'categories', 'salesRank', 'description',
#             'also_bought','also_viewed','bought_together','buy_after_viewing']

while line:

  line = line.strip("\n")
  line = json.loads(line)
  temp = copy.deepcopy(line)

  if "related" in temp.keys():

    if "also_bought" in temp["related"].keys():
      temp["also_bought"] = temp["related"]["also_bought"]
      temp["also_bought"] = ",".join(str(ele) for ele in temp["also_bought"])
    else:
      temp["also_bought"] = None

    if "also_viewed" in temp["related"].keys():
      temp["also_viewed"] = temp["related"]["also_viewed"]
      temp["also_viewed"] = ",".join(str(ele) for ele in temp["also_viewed"])
    else:
      temp["also_viewed"] = None

    if "bought_together" in temp["related"].keys():
      temp["bought_together"] = temp["related"]["bought_together"]
      temp["bought_together"] = ",".join(str(ele) for ele in temp["bought_together"])
    else:
      temp["bought_together"] = None

    if "buy_after_viewing" in temp["related"].keys():
      temp["buy_after_viewing"] = temp["related"]["buy_after_viewing"]
      temp["buy_after_viewing"] = ",".join(str(ele) for ele in temp["buy_after_viewing"])
    else:
      temp["buy_after_viewing"] = None

  ### fill all keys
  for key in all_keys:
    if key in temp.keys():
      pass
    else:
      temp[key] = None

  try:
    del temp['related']
  except Exception as e:
    pass

  csv_writer.writerow(temp)
  line = f.readline()

