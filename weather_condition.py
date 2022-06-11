import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# 读取数据
df = pd.read_csv('长沙市.csv', encoding='UTF-8')
df1 = pd.read_csv('成都市.csv', encoding='UTF-8')

# 以上提取的日期为object中的字符串类型，我们要使用pandas数据处理装换为datatime类型
df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))
df1['日期'] = df1['日期'].apply(lambda x: pd.to_datetime(x))

# 使用groupby聚合类对象将df中的内容按天气状况计数
df_agg = df.groupby(['天气状况']).size().reset_index()
df_agg.columns = ['天气状况', '天数']
df_agg1 = df1.groupby(['天气状况']).size().reset_index()
df_agg1.columns = ['天气状况', '天数']
print(df_agg)

changsha_data = df_agg[['天气状况', '天数']].values.tolist()
chengdu_data = df_agg1[['天气状况', '天数']].values.tolist()
changsha_data.sort(reverse=True, key=lambda x: x[1])
chengdu_data.sort(reverse=True, key=lambda x: x[1])

print(changsha_data,end='\n')
result_cs = dict(changsha_data)
result_cd = dict(chengdu_data)

ltcs = []
ltcd = []


#由于两个城市可能,有些天气互相没有，故要添加缺少的天气键值并赋值为0
for i in result_cs.keys():
    if i not in result_cd:
        result_cd[i] = 0
for i in result_cd.keys():
    if i not in result_cs:
        result_cs[i] = 0

# 统计天气状况,并将天气状况放入到对应的列表当中。包含雨的天气统一视为雨天
lt = [ltcs, ltcd, result_cs, result_cd]
for i in range(0, 2):
    lt[i].append(lt[i + 2]['晴'])
    lt[i].append(lt[i + 2]['多云'])
    lt[i].append(lt[i + 2]['阴'])
    lt[i].append(
        lt[i + 2]['小雨'] + lt[i + 2]['多云转雨'] + lt[i + 2]['阴转雨'] + lt[i + 2]['小雨转雨'] + lt[i + 2]['小雨到中雨'] + lt[i + 2][
            '大雨转雨'] + lt[i + 2]['中雨转雨'] + lt[i + 2]['小雨转多云'] + lt[i + 2]['小雨转阴'] + lt[i + 2]['小雨到暴雨'] + lt[i + 2][
            '中雨到大雨'] + lt[i + 2]['晴转雨']  + lt[i + 2]['小雨到大雨'])
    lt[i].append(lt[i + 2]['霾'])
    lt[i].append(lt[i + 2]['晴转多云'])
    lt[i].append(lt[i + 2]['多云转阴'])
    lt[i].append(lt[i + 2]['多云转晴'])
    lt[i].append(lt[i + 2]['阴转多云'])
    lt[i].append(lt[i + 2]['霾转多云'])


print('长沙天气状况种类为：{}种,成都天气状况种类为：{}种'.format(len(result_cs),len(result_cd)))

print(ltcs, end='\n')
print(ltcd, end='\n')

# 设置绘图风格
plt.style.use('bmh')
# 处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
weather_conditions = ['晴', '多云', '阴', '雨', '霾', '晴转多云', '多云转阴', '多云转晴', '阴转多云', '霾转多云']

# 创建分组柱状图，需要自己控制x轴坐标
xticks = np.arange(len(weather_conditions))

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(xticks, ltcs, width=0.25, label="长沙市天气状况", color="#FF6600")
ax.bar(xticks + 0.25, ltcd, width=0.25, label="成都市天气状况", color="#FFFF00")

ax.set_title("2019年长沙&成都天气总体状况", fontsize=15)
ax.set_xlabel("天气")
ax.set_ylabel("天数/天")
ax.legend()
# 最后调整x轴标签的位置
ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(weather_conditions)
plt.show()
