import requests  # 替代浏览器进行数据请求的模块
from lxml import etree  # 进行数据项处理
import csv  # 写入csv文件
# URL规律 ../年份/月份.html得到指定年份数据
def getweather(url):
    weather_info = []  # 新建一个空列表，存放本月的每一天天气数据
    # 请求头,User-Agent相当于浏览器签名，如果不正确，那数据库肯定认为是爬虫
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }
    # 发起请求
    resp = requests.get(url, headers=headers)
    # 数据预处理 xpath,通过使用etree的HTML方法将网站每一天的信息转换为html格式
    resp_html = etree.HTML(resp.text)
    # xpath提取当月所有数据
    resp_list = resp_html.xpath("//ul[@class='thrui']/li")  # xpath语法,这里当时少打了//
    # for循环迭代遍历每日数据
    for li in resp_list:
        day_weather_info = {}  # 建立一个字典，每天的数据放入字典
        # 日期 {'日期':'2019-9-01',} 例如2019-9-01 星期日 变为 2019-9-01
        day_weather_info['日期'] = li.xpath('./div[1]/text()')[0].split(' ')[
            0]  # xpath得到的数据会存放在列表当中，第一个[0]是取出第0项数据，也就是日期,第二个是分割只取出日期，不取星期几
        high = li.xpath("./div[2]/text()")[0]  # 最高气温，定义一个high，得到第0项
        day_weather_info['最高气温'] = high[:high.find('℃')]  # 字符串切割，根据索引切割，切到对应的℃前面，只需要前面数字部分
        low = li.xpath("./div[3]/text()")[0]
        day_weather_info['最低气温'] = low[:low.find('℃')]
        day_weather_info['天气状况'] = li.xpath('./div[4]/text()')[0]
        day_weather_info['风向'] = li.xpath('./div[5]/text()')[0]
        average = (int(day_weather_info['最高气温']) + int(day_weather_info['最低气温'])) / 2
        day_weather_info['平均气温'] = str(average)
        weather_info.append(day_weather_info)  # 列表添加每一天的数据字典
    # 返回数据
    return weather_info

changsha_weathers = []  # 定义一个全年的天气数据列表
chengdu_weathers = []
for month in range(1, 13):
    # 某年莫月天气信息
    # 判断月份是否小于10，如果小于10就得在个位前面添加上0
    weather_time = '2019' + ('0' + str(month) if month < 10 else str(month))  # 三目运算符方法
    url = f'https://lishi.tianqi.com/changsha/{weather_time}.html'
    url1 = f'https://lishi.tianqi.com/chengdu/{weather_time}.html'

    # 爬虫获取每个月天气数据
    weather = getweather(url)  # 每月的天气数据
    weather1 = getweather(url1)
    changsha_weathers.append(weather)  # 将每月的天气数据添加到一年的列表当中
    chengdu_weathers.append(weather1)

print(changsha_weathers)
print(chengdu_weathers)

# 数据写入，打开直接写入一次
lt = ['长沙市.csv', '成都市.csv']
lt1 = [changsha_weathers, chengdu_weathers]

for i in range(0, 2):
    with open(lt[i], 'w', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入列名:colums_name
        writer.writerow(['日期', '最高气温', '最低气温', '天气状况', '风向', '平均温度'])
        list_year = []
        for month_weather in lt1[i]:  # 循环年列表里的月列表
            for day_weather_dict in month_weather:  # 循环月列表里的每一天的字典
                list_year.append(list(day_weather_dict.values()))  # 字典里面的值拿出来转换为列表
        writer.writerows(list_year)  # 将列表写入文件中

