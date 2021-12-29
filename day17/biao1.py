import xlrd
from xlutils.copy import copy
class rwsj:

    def dq(self):
        f=[]
        wd=xlrd.open_workbook(filename=r"D:\python\day17【自动化测试框架】\代码\表1.xls",encoding_override=True)
        st=wd.sheet_by_index(0)
        cols=st.ncols
        rows=st.nrows
        for i in range(1, rows):  # 第一行属于表头数据，肯定不要，从第二行开始读取数据
            l = []
            for j in range(0, cols-4):
                l.append(st.cell_value(i, j))
            f.append(l)

        for i in range(len(f)):
            for y in range(len(f[i])):
                if type(f[i][y]) == float:
                    a = f[i][y]
                    f[i].remove(f[i][y])
                    f[i].insert(y, int(a))
        return f
    def writeData(self,row, col, data):
        new_wb = copy(xlrd.open_workbook(filename=r"D:\python\day17【自动化测试框架】\代码\表1.xls", encoding_override=True))
        new_wb.get_sheet(0).write(row, col, data)  # 测试结果
        new_wb.save(r"D:\python\day17【自动化测试框架】\代码\表1.xls")