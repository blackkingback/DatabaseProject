import pandas as pd

df = pd.read_csv("categories2.tsv",sep="\t")
df = df[['asin','category1','category2','category3']]
f = open("category_for_display.tsv","w")
f.write("category1"+"\t"+"category1_count"+"\t"+"category2"+"\t"+"category2_count"+"\t"+"category3"+"\t"+"category3_count"+"\n")
for name1, group1 in df.groupby(['category1']):
    for name2,group2 in group1.groupby(['category2']):
        for name3,group3 in group2.groupby(['category3']):
            if name2 == "End_of_Category":
                continue
            if name3 == "End_of_Category":
                continue
            target_string = name1+"\t"+str(len(group1))+"\t"+name2+"\t"+str(len(group2))+"\t"+name3+"\t"+str(len(group3))
            f.write(target_string+"\n")
f.close()