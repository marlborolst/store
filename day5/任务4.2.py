fruits={"苹果":12.3,"草莓":4.5,"香蕉":6.3,"葡萄":5.8,"橘子":6.4,"樱桃":5.8}
info={
      '小明':{'fruits':{'苹果':4,'草莓':13,'香蕉':10},'m1':0},
      '小刚':{'fruits':{'葡萄':19,'橘子':12,'樱桃':30},'m2':0}
      }
money1=0
money2=0
for a, x in info['小明']['fruits'].items():
      m1 = fruits[a] * x
      money1 = m1 + money1
      info['小明']['m1'] = money1
      print("小明", a, m1)
for b, y in info['小刚']['fruits'].items():
      m2 = fruits[b] * y
      money2 = m2 + money2
      info['小刚']['m2'] = money2
      print("小刚", b, m2)
print(info)
