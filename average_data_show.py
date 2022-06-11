import matplotlib.pyplot as plt
from main import chengdu_weathers as cd
from main import changsha_weathers as cs
import  numpy as np
# 数据处理部分
def count_month_average(weather=[]):
    month_averages = []
    for i in range(0, 12):
        sum = 0
        for j in weather[i]:  # 记住这里是列表中元素不是列表下标
            sum = sum + float(j['平均气温'])
        month_averages.append(round(sum / len(weather[i]), 2))
    return month_averages


changsha_month_averages = []
chengdu_month_averages = []

changsha_month_averages = count_month_average(cs)
chengdu_month_averages = count_month_average(cd)

print("长沙每月平均气温分别为：")
for i in range(0, 12):
    print(changsha_month_averages[i], end=',')

print('\n')
print("成都每月平均气温分别为：")
for i in range(0, 12):
    print(chengdu_month_averages[i], end=',')

# 可视化部分
month = np.arange(len(changsha_month_averages))

# 设置绘图风格
plt.style.use('seaborn-notebook')
# 处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 坐标轴负号的处理
plt.rcParams['axes.unicode_minus'] = False

# 绘制折线图
plt.plot(month, changsha_month_averages, color='red', label='长沙', linestyle='-', marker='+', linewidth=1)
plt.plot(month, chengdu_month_averages, color='blue', label='成都', linestyle='-', marker='+', linewidth=1)
# 设置数字标签
for a in range(0, 12):
    plt.text(month[a], changsha_month_averages[a], str(changsha_month_averages[a]), ha='center', va='bottom',
             fontsize=9, )
    plt.text(month[a], chengdu_month_averages[a], str(chengdu_month_averages[a]), ha='center', va='bottom',
             fontsize=9, )
# 显示图例
plt.legend()
# 修改x轴和y轴标签
plt.xlabel('月份')
plt.ylabel('气温/℃')
# 添加图形标题
plt.title('2019年度长沙&成都每月平均气温')
# 调整比例
ax = plt.gca()
ax.set_aspect(0.25)
# 显示图形
plt.show()
