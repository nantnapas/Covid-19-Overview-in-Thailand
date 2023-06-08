import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import requests

#อ่านข้อมูลจาก API all cases
url= "https://covid19.th-stat.com/api/open/cases"
cr = requests.get(url)

date = cr.json()
date = date["UpdateDate"]
print("Update Date=",date)

case = cr.json()
case = case["Data"]
case_df = pd.DataFrame(case)
case_df.tail()

#นำ column ที่ไม่ได้ใช้ออก
case_df = case_df.drop(["ConfirmDate","No","Gender","Nation","Province","ProvinceId","District","Detail"],axis=1)
print("Update Date=",date)
case_df.head()

#ลบ row ที่มี missing value
case_df = case_df.dropna(axis=0)
print("Update Date=",date)
case_df.head()

#เลือกข้อมูลสัญชาติมาแสดงผล
print("Update Date=",date)
set_nation=set(case_df["NationEn"])
nationlist=list(case_df["NationEn"])
count_set_nation=len(set_nation)
print("Number of nations : ", count_set_nation)

nations={}
for nation in nationlist:
    if nation in nations:
        nations[nation]+=1
    else:
        nations[nation]=1
print(nations)

#เลือกข้อมูลเพศมาแสดงผล
print("Update Date=",date)
set_gender=set(case_df["GenderEn"])
genderlist=list(case_df["GenderEn"])
count_set_gender=len(set_gender)
print("Number of gender : ", count_set_gender)

genders={}
for gender in genderlist:
    if gender in genders:
        genders[gender]+=1
    else:
        genders[gender]=1
print(genders)

#แสดง bar chart เพศ
plt.figure(figsize=[2,5])
x = np.arange(1,3) 
y = [genders['Male'],genders['Female']]  
gender = ['Male','Female']

ax = plt.gca(xticks=x)
ax.set_xticklabels(gender)
bara = plt.bar(x,y,align='center',width=0.3,color='red')
plt.title('Population of each gender')
plt.show()

print("Update Date=",date)

#อ่านข้อมูลจาก API update cases
url="https://covid19.th-stat.com/api/open/timeline"
ur = requests.get(url)

update = ur.json()
date = update["UpdateDate"]
print("Update Date=",date)

update = ur.json()
update = update["Data"]
update_df = pd.DataFrame(update)
update_df.tail()

#นำ column ที่ไม่ได้ใช้ออก
print("Update Date=",date)
update_df = update_df.drop(["NewRecovered","NewHospitalized","NewDeaths"],axis=1)
update_df.tail()

#อัตราพบผู้ป่วยใหม่
fig, ax1 = plt.subplots(figsize=(20,7))
sns.lineplot(data=update_df[-30:], y="NewConfirmed", ax=ax1, x="Date", color="blue")

ax1.set_xlabel("Date")
ax1.set_ylabel("New confirmed cases")

plt.title("Rate of new confirmed cases")
plt.show()

print("Update Date=",date)

#แสดงกราฟ overview
fig, ax1 = plt.subplots(figsize=(30,10))
sns.lineplot(data=update_df[-30:], y="Confirmed", ax=ax1, x="Date", label="Total Confirmed", color="red")
sns.lineplot(data=update_df[-30:], y="Recovered", ax=ax1, x="Date", label="Total Recovered", color="green")
sns.lineplot(data=update_df[-30:], y="Hospitalized", ax=ax1, x="Date", label="Total Hospitalized", color="blue")
sns.lineplot(data=update_df[-30:], y="Deaths", ax=ax1, x="Date", label="Deaths", color="black")

ax1.set_xlabel("Date")
ax1.set_ylabel("Population")

plt.title("Total cases")
plt.show()

print("Update Date=",date)