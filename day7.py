import xlrd
import xlwt
#import numpy as np
wb=xlrd.open_workbook(filename=r'C:/Users/dell/Desktop/python/day7/任务/百度合作单位-人员管理-二期 .xlsx',encoding_override=True)
st=wb.sheet_by_index(0)
row=st.nrows
col=st.ncols


#a)统计所有表格中有多少人
r=st.nrows-1
print('表格中人数:',r)



#统计办电信，联通，移动的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）
y=0
d=0
l=0
for i in st.col_values(5,1):
     if i>"13000000000"and i<"14000000000":
        y=y+1
     elif i>"15000000000"and i<"16000000000":
        l=l+1
     elif i > "14000000000" and i < "15000000000":
        d = d + 1
     elif i > "17000000000" and i < "18000000000":
        d = d + 1
print("办移动的用户数量:",y)
print("办联通的用户数量:",l)
print("办电信的用户数量:",d)


#总公司男女人数
g=0
m=0
for i in range(st.nrows):
     e=st.row_values(i)
     if e[8]=='男':
         g=g+1
     elif e[8]=='女':
         m+=1
print('男:', g, '女:', m)



#年龄超过45岁的老员工人数
a=0
for i in range(1,st.nrows):
    e=st.row_values(i)
    if e[7]>45:
        a=a+1
print('年龄超过45岁的老员工人数:',a)



#e)薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
h=0
j=0
for i in range(1,st.nrows):
     e=st.row_values(i)
     if e[11]>8000:
         h=h+1
     elif e[11]<3000:
         j=j+1
print("薪资高于8000元的高薪人员数量:",h,"薪资低于3000的底薪人员数量",j)

#统计去传媒公司的工作的人员数量
c=0
for i in st.col_values(13,1):
    if '传媒' in i:
        c=c+1
print('去传媒公司的工作的人员数量:',c)

#统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）
d=0
for i in st.col_values(9,1):
    if '黑龙江'in i or'北京'in i or'福建'in i or'四川'in i:
        d+=1
print('可能在疫情高危地区的人数:',d)


#将表格数据都存入到集团数据库中。
'''import xlwt
#import numpy as np
wb=xlrd.open_workbook(filename=r'C:/Users/dell/Desktop/python/day7/任务/百度合作单位-人员管理-二期 .xlsx',encoding_override=True)
st=wb.sheet_by_index(0)
row=st.nrows
col=st.ncols'''
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('百度人员管理')
for i in range(row):
    for y in range(col):
        worksheet.write(i,y,label=str(st.col_values(y,i)[0]))
        workbook.save('数据库.xls')
print("ok")