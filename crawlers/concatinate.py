import pandas as pd
import pandas as p
from more_itertools import unique_everseen

csv_list=['chkarGilgit.csv', 'chkarGojal.csv','chkarHunza.csv','chkarmurree.csv','chkarskardu.csv']
list1= []
for itw in csv_list:
    df = p.read_csv(itw, index_col=None, header=0)
    list1.append(df)
    print(list1)
    import pdb;pdb.set_trace()
frame = pd.concat(list1, axis=0, ignore_index=True)
print(frame)
frame.to_csv('conat.csv', mode='a')


with open('conat.csv','r') as f, open('chkar.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))