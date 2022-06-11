import matplotlib.pyplot as plt

ltcs = []
# 将.csv中文件读出来
with open('长沙市.csv', 'r', encoding='UTF-8') as fid:
    for line in fid:
        line = line.replace('\n', '')
        ltcs1 = line.split(',')
        ltcs.append(ltcs1)
ltcd = []
with open('成都市.csv', 'r', encoding='UTF-8') as fid:
    for line in fid:
        line = line.replace('\n', '')
        ltcd1 = line.split(',')
        ltcd.append(ltcd1)

print(ltcs,end='\n')
changsha_at = []
chengdu_at = []
changsha_wind = 0
chengdu_wind = 0

for i in range(1, 366):
    changsha_at.append(float(ltcs[i][5]))
    temp = int(ltcs[i][4][-2])  # 取出每一天风力等级
    if (temp < 5) and ((float(ltcs[i][5]) >= 10) and (float(ltcs[i][5]) <= 25)):
        changsha_wind = changsha_wind + 1
    chengdu_at.append(float(ltcd[i][5]))
    temp = int(ltcd[i][4][-2])  # 取出每一天风力等级
    if (temp < 5) and ((float(ltcd[i][5]) >= 10) and (float(ltcd[i][5]) <= 25)):
        chengdu_wind = chengdu_wind + 1

str = "2019年，长沙温度为10~25摄氏度，风力等级小于5的天数为:" + str(changsha_wind) + ",成都为" + str(chengdu_wind) + '，故最适合旅游城市为成都'
# print(str)
day = list(range(1, 366))
# 设置绘图风格
plt.style.use('seaborn')
# 处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 坐标轴负号的处理
plt.rcParams['axes.unicode_minus'] = True
# 绘制折线图
plt.plot(day, changsha_at, color='red', label='长沙', linewidth=1)
plt.plot(day, chengdu_at, color='blue', label='成都', linewidth=1)
# 显示图例
plt.legend()
# 修改x轴和y轴标签
plt.xlabel('平均气温走势')
plt.ylabel('气温/℃')
# 添加图形标题
plt.title('2019年长沙&成都一年平均气温走势')
# 添加注释
plt.text(0, 0, str, fontdict=None)
# 调整比例
ax = plt.gca()
ax.set_aspect(6)
# 显示图形
plt.show()
