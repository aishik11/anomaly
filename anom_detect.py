import csv
import numpy as np
from scipy.stats import multivariate_normal
from operator import mul
from functools import reduce

def assigh(arg):
   
   try:
       t=float(arg)
   except:
       t=0
       
   #print('%.08f \n'%t)
   return t

def prod(arg):
    x=1
    for j in arg:
        j=assigh(j)
        if j!=0:
            x=x*j
        
    return x
def alpha_deci(arg):
   arr_key=[]
   new_list=[]
   x=0
   arr_key.append("")
   #print(len(arg))
   #print(arg[3])
   for j in range(0,len(arg)):
      #if arg[j]=='':
      #  new_list.append(arr_key[0])
      if arg[j] in arr_key:
         new_list.append((arr_key.index(arg[j]))/1000)
        # print("%f %f" %(j,(arr_key.index(arg[j]))/1000))
      else:
         arr_key.append(arg[j])
         new_list.append((arr_key.index(arg[j]))/1000)
         #print("%f %f" %(j ,(arr_key.index(arg[j]))/1000))
      x=x+1
      
   return new_list
         
   

#with open('train_anom_half.csv', 'r') as f:
with open('train_anom_half.csv', 'r') as f:
  reader = csv.DictReader(f)
  he=reader.fieldnames
  list1=list(reader)
  x=0
  transaction_id_list=[]
  num_var_1_list=[]
  num_var_2_list=[]
  num_var_3_list=[]
  num_var_4_list=[]
  num_var_5_list=[]
  num_var_6_list=[]
  num_var_7_list=[]
  cat_var_1_list=[]
  cat_var_2_list=[]
  cat_var_3_list=[]
  cat_var_4_list=[]
  cat_var_5_list=[]
  cat_var_6_list=[]
  cat_var_7_list=[]
  cat_var_8_list=[]
  cat_var_9_list=[]
  cat_var_10_list=[]
  cat_var_11_list=[]
  cat_var_12_list=[]
  cat_var_13_list=[]
  cat_var_14_list=[]
  cat_var_15_list=[]
  cat_var_16_list=[]
  cat_var_17_list=[]
  cat_var_18_list=[]
  cat_var_19_list=[]
  cat_var_20_list=[]
  cat_var_21_list=[]
  cat_var_22_list=[]
  cat_var_23_list=[]
  cat_var_24_list=[]
  cat_var_25_list=[]
  cat_var_26_list=[]
  cat_var_27_list=[]
  cat_var_28_list=[]
  cat_var_29_list=[]
  cat_var_30_list=[]
  cat_var_31_list=[]
  cat_var_32_list=[]
  cat_var_33_list=[]
  cat_var_34_list=[]
  cat_var_35_list=[]
  cat_var_36_list=[]
  cat_var_37_list=[]
  cat_var_38_list=[]
  cat_var_39_list=[]
  cat_var_40_list=[]
  cat_var_41_list=[]
  cat_var_42_list=[]
  target_list=[]
  target_list.append(0)
  #target_list.append(0)
  
  
  
  
  
 
  
for row in list1:
      #portfolio_id_list.append(row["portfolio_id"])
      transaction_id_list.append(row["transaction_id"])
      num_var_1_list.append(assigh(row["num_var_1"]))
      num_var_2_list.append(assigh(row["num_var_2"]))
      num_var_3_list.append(assigh(row["num_var_3"]))
      num_var_4_list.append(assigh(row["num_var_4"]))
      num_var_5_list.append(assigh(row["num_var_5"]))
      num_var_6_list.append(assigh(row["num_var_6"]))
      num_var_7_list.append(assigh(row["num_var_7"]))
      cat_var_1_list.append(row["cat_var_1"])
      cat_var_2_list.append(row["cat_var_2"])
      cat_var_3_list.append(row["cat_var_3"])
      cat_var_4_list.append(row["cat_var_4"])
      cat_var_5_list.append(row["cat_var_5"])
      cat_var_6_list.append(row["cat_var_6"])
      cat_var_7_list.append(row["cat_var_7"])
      cat_var_8_list.append(row["cat_var_8"])
      cat_var_9_list.append(row["cat_var_9"])
      cat_var_10_list.append(row["cat_var_10"])
      cat_var_11_list.append(row["cat_var_11"])
      cat_var_12_list.append(row["cat_var_12"])
      cat_var_13_list.append(row["cat_var_13"])
      cat_var_14_list.append(row["cat_var_14"])
      cat_var_15_list.append(row["cat_var_15"])
      cat_var_16_list.append(row["cat_var_16"])
      cat_var_17_list.append(row["cat_var_17"])
      cat_var_18_list.append(row["cat_var_18"])
      cat_var_19_list.append(assigh(row["cat_var_19"]))
      cat_var_20_list.append(assigh(row["cat_var_20"]))
      cat_var_21_list.append(assigh(row["cat_var_21"]))
      cat_var_22_list.append(assigh(row["cat_var_22"]))
      cat_var_23_list.append(assigh(row["cat_var_23"]))
      cat_var_24_list.append(assigh(row["cat_var_24"]))
      cat_var_25_list.append(assigh(row["cat_var_25"]))
      cat_var_26_list.append(assigh(row["cat_var_26"]))
      cat_var_27_list.append(assigh(row["cat_var_27"]))
      cat_var_28_list.append(assigh(row["cat_var_28"]))
      cat_var_29_list.append(assigh(row["cat_var_29"]))
      cat_var_30_list.append(assigh(row["cat_var_30"]))
      cat_var_31_list.append(assigh(row["cat_var_31"]))
      cat_var_32_list.append(assigh(row["cat_var_32"]))
      cat_var_33_list.append(assigh(row["cat_var_33"]))
      cat_var_34_list.append(assigh(row["cat_var_34"]))
      cat_var_35_list.append(assigh(row["cat_var_35"]))
      cat_var_36_list.append(assigh(row["cat_var_36"]))
      cat_var_37_list.append(assigh(row["cat_var_37"]))
      cat_var_38_list.append(assigh(row["cat_var_38"]))
      cat_var_39_list.append(assigh(row["cat_var_39"]))
      cat_var_40_list.append(assigh(row["cat_var_40"]))
      cat_var_41_list.append(assigh(row["cat_var_41"]))
      cat_var_42_list.append(assigh(row["cat_var_42"]))
      target_list.append(assigh(row["target"]))

         
      

#cat_var_1_list=alpha_deci(cat_var_1_list)
#num_var_1_list=norm(num_var_1_list)


    
def norm(lis):
    range_list=max(lis)-min(lis)
    mean=sum(lis)/len(lis)
    lisn=[]

    for i,h in enumerate(lis):
        #print(h)
        #print(" with mean ")
        #print(mean)
        #print(" with range ")
        #print(range_list)
        #print(" norm = ")
       try:
         h=(h-mean)/range_list
       except:
         h=0
         
       lisn.append(h)
        #print(h)
        #print("\n")
    
    return lisn

#cat_var_1_list=alpha_deci(cat_var_1_list)
#cat_var_2_list=alpha_deci(cat_var_2_list)
#cat_var_3_list=alpha_deci(cat_var_3_list)
#cat_var_4_list=alpha_deci(cat_var_4_list)
#cat_var_5_list=alpha_deci(cat_var_5_list)
#cat_var_6_list=alpha_deci(cat_var_6_list)
#cat_var_7_list=alpha_deci(cat_var_7_list)
#cat_var_8_list=alpha_deci(cat_var_8_list)
#cat_var_9_list=alpha_deci(cat_var_9_list)
#cat_var_10_list=alpha_deci(cat_var_10_list)
#cat_var_11_list=alpha_deci(cat_var_11_list)
#cat_var_12_list=alpha_deci(cat_var_12_list)
#cat_var_13_list=alpha_deci(cat_var_13_list)
#cat_var_14_list=alpha_deci(cat_var_14_list)
#cat_var_15_list=alpha_deci(cat_var_15_list)
#cat_var_16_list=alpha_deci(cat_var_16_list)
#cat_var_17_list=alpha_deci(cat_var_17_list)
#cat_var_18_list=alpha_deci(cat_var_18_list)

d=[
   transaction_id_list,
   norm(num_var_1_list),
   norm(num_var_2_list),
   norm(num_var_3_list),
   norm(num_var_4_list),
   norm(num_var_5_list),
   norm(num_var_6_list),
   norm(num_var_7_list),
   alpha_deci(cat_var_1_list),
   alpha_deci(cat_var_2_list),
   alpha_deci(cat_var_3_list),
   alpha_deci(cat_var_4_list),
   alpha_deci(cat_var_5_list),
   alpha_deci(cat_var_6_list),
   alpha_deci(cat_var_7_list),
   alpha_deci(cat_var_8_list),
   alpha_deci(cat_var_9_list),
   alpha_deci(cat_var_10_list),
   alpha_deci(cat_var_11_list),
   alpha_deci(cat_var_12_list),
   alpha_deci(cat_var_13_list),
   alpha_deci(cat_var_14_list),
   alpha_deci(cat_var_15_list),
   alpha_deci(cat_var_16_list),
   alpha_deci(cat_var_17_list),
   alpha_deci(cat_var_18_list),
   cat_var_19_list,
   cat_var_20_list,
   cat_var_21_list,
   cat_var_22_list,
   cat_var_23_list,
   cat_var_24_list,
   cat_var_25_list,
   cat_var_26_list,
   cat_var_27_list,
   cat_var_28_list,
   cat_var_29_list,
   cat_var_30_list,
   cat_var_31_list,
   cat_var_32_list,
   cat_var_33_list,
   cat_var_34_list,
   cat_var_35_list,
   cat_var_36_list,
   cat_var_37_list,
   cat_var_38_list,
   cat_var_39_list,
   cat_var_40_list,
   cat_var_41_list,
   cat_var_42_list,
   target_list
  ]

d2=[
   
   norm(num_var_1_list),
   norm(num_var_2_list),
   norm(num_var_3_list),
   norm(num_var_4_list),
   norm(num_var_5_list),
   norm(num_var_6_list),
   norm(num_var_7_list),
   alpha_deci(cat_var_1_list),
   alpha_deci(cat_var_2_list),
   alpha_deci(cat_var_3_list),
   alpha_deci(cat_var_4_list),
   alpha_deci(cat_var_5_list),
   alpha_deci(cat_var_6_list),
   alpha_deci(cat_var_7_list),
   alpha_deci(cat_var_8_list),
   alpha_deci(cat_var_9_list),
   alpha_deci(cat_var_10_list),
   alpha_deci(cat_var_11_list),
   alpha_deci(cat_var_12_list),
   alpha_deci(cat_var_13_list),
   alpha_deci(cat_var_14_list),
   alpha_deci(cat_var_15_list),
   alpha_deci(cat_var_16_list),
   alpha_deci(cat_var_17_list),
   alpha_deci(cat_var_18_list),
   cat_var_19_list,
   cat_var_20_list,
   cat_var_21_list,
   cat_var_22_list,
   cat_var_23_list,
   cat_var_24_list,
   cat_var_25_list,
   cat_var_26_list,
   cat_var_27_list,
   cat_var_28_list,
   cat_var_29_list,
   cat_var_30_list,
   cat_var_31_list,
   cat_var_32_list,
   cat_var_33_list,
   cat_var_34_list,
   cat_var_35_list,
   cat_var_36_list,
   cat_var_37_list,
   cat_var_38_list,
   cat_var_39_list,
   cat_var_40_list,
   cat_var_41_list,
   cat_var_42_list,
   
  ]
demo=[
   norm(num_var_1_list),
   norm(num_var_2_list),
   
   norm(num_var_4_list),
   norm(num_var_5_list),
   norm(num_var_6_list),
   norm(num_var_7_list),
   cat_var_19_list,
   cat_var_20_list,
   cat_var_21_list,
   cat_var_22_list,
      cat_var_23_list,
   cat_var_24_list,
   cat_var_25_list,
   cat_var_26_list,
   cat_var_27_list,
   cat_var_28_list,
   cat_var_29_list,
   cat_var_30_list,
   cat_var_31_list,
   cat_var_32_list,
   cat_var_33_list,
   cat_var_34_list,
   cat_var_35_list,
   cat_var_36_list,
   cat_var_37_list,
   cat_var_38_list,
   cat_var_39_list,
   cat_var_40_list,
   cat_var_41_list,
   cat_var_42_list
   




    ]
d1=zip(*d)
D=zip(*d2)
X_arr=[]
for k in D:
    X_arr.append(k)
    
#X=np.array(d1)
#X=d2
#print(X_arr)
#C=np.cov(np.array(X_arr).astype(np.float))
C=np.cov(d2)
#print(d2)
#M=np.mean(np.array(X_arr).astype(np.float))
M=np.mean(d2)
f=cat_var_24_list
C1=np.cov(f)
M1=np.mean(f)
M1=np.array(M1)
C1=np.array(C1)

y1=multivariate_normal.pdf(f,M1,C1,1)
#print(y1)
pred=[]
u=[]
for k in demo:
    k_m=np.mean(k)
    k_c=np.cov(k)
    #print("%f %f"%(k_m,k_c))
    y=multivariate_normal.pdf(k,k_m,k_c,1)
    for k in y:
        u.append(assigh(k))
    pred.append(norm(u))
    #print(y)
#print(pred)

n_z=zip(*pred)

pred_1=[]
for j in n_z:
    pred_1.append(prod(j))
                  
    #print(pred_1)
ix=0
out=[target_list,pred_1]
iy=0
for o in zip(*out):
    print ("%f %f %0.30f"%(iy,o[0],o[1]))
    iy=iy+1

for k in out:
        #print(target_list[k])
        if o[0]==1:
            print("%f %f"%k)
        ix=ix+1

for j in pred_1:
    #print("%f %f"%(ix,j))
    ix=ix+1
#Y=X_arr,mean=M,cov=np.array(C))
#Y=multivariate_normal.pdf(X_arr)

#dif=list(set(creation_date_list)-set(start_date_list))

#rows=zip(start_date_norm,sold_norm,euribor_rate_norm,libor_rate_norm,bought_norm,creation_date_norm)
#rows1=[start_date_norm,sold_norm,euribor_rate_norm,libor_rate_norm,bought_norm,creation_date_norm]


#creation_date_norm=norm(creation_date_list)
#dif=norm(cus_lis)
#euribor_rate_norm=norm(euribor_rate_list)
#print(start_date_norm)
                                 
#with open('test_new.csv', "w",newline='') as f:
with open('test_new.csv', "w",newline='') as f:   
        writer = csv.writer(f,delimiter=',')
        writer.writerow(he)
        #writer.writerow(["portfolio_id","desk_id","office_id","pf_category","start_date","sold","country_code","euribor_rate","currency","libor_rate","bought","creation_date","indicator_code","sell_date","type","hedge_value","status"])
        #for i in range(len(transaction_id_list)):
           # if len(target_list)>0:
                #a=[portfolio_id_list[i],desk_id_list[i],office_id_list[i],pf_category_list[i],start_date_norm[i],sold_norm[i],country_code_list[i],euribor_rate_norm[i],currency_list[i],libor_rate_norm[i],bought_norm[i],creation_date_norm[i],indicator_code_list[i],sell_date_norm[i],type_list[i],hedge_value_list[i],status_list[i],return_list[i]]
              #  writer.writerow(d)
           # else:
                #a=[portfolio_id_list[i],desk_id_list[i],office_id_list[i],pf_category_list[i],start_date_norm[i],sold_norm[i],country_code_list[i],euribor_rate_norm[i],currency_list[i],libor_rate_norm[i],bought_norm[i],creation_date_norm[i],indicator_code_list[i],sell_date_norm[i],type_list[i],hedge_value_list[i],status_list[i]]
               # writer.writerow(d)
#print('%.08f \n'%euribor_rate_list)
        for i in d1:
            writer.writerow(i)

  #print(sold_list)

