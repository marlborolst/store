class person():
    age=""
    sex=""
    name=""

class G(person):
    def work(self,work):
        print(self.name,"正在",work)

class student(G):
    num=""
    def work(self,work):
        print(self.name,self.age,self.sex,self.num)
        super().work(work)

s=student()
s.name="molly"
s.age="16"
s.sex="girl"
s.num="1731010143"
s.work("学习，唱歌")
