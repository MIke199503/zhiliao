import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
def parse_url(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return etree.HTML(response.content)
    return False

def get_date(response):
    start_date = ".join(response.xpath('//input[@name = 'date_start_type']/@value')[0].split('-'))"
    end_date = ".join(response.xpath('//input[@name = 'date_end_type']/@value')[0].split('-'))"
    code = response.xpath('//h1[@class= "name"]/span/a/text()')[0]
    return code,start_date,end_date

def download(code,start_date,end_date):
    download_url="http://quotes.money.163.com/service/chddata.html?code=0"+code+"&start="+start_date+"&den="+end_date+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VATURNOVER;VATURNOVER;TCAP;MCAP"
    print(download_url)
    data=requests.get(download_url,headers=headers)
    f = open(code + '.csv','wb')
    for chunk in data.iter_content(chunk_size=10000):
        if chunk:
            f.write(chunk)
    print("股票---",code,'历史数据正在下载')

ulr="http://quotes.money.163.com/trade/lsjysj_600893.html"
response= parse_url(ulr)
code,start_date,end_date=get_date(response)
download(code,start_date,end_date)


import pandas as pd
import  numpy as np
stock =pd.read_csv(code+'.csv',usecols=[0,1,2,3,4,5,6],encoding='gbk')
stock.head()
stock_new=stock.iloc[:180,:]
stock_new_sorted = stock_new.sort_values('日期',ascending=True)
stock_new_sorted.head()




from pyecharts.charts import Kline
from pyecharts import options as opts

stock_code=stock_new_sorted['股票代码'][0]
stock_name=stock_new_sorted['名称'][0]
index = stock_new_sorted['日期']

index1 = np.array(index)
index2 = index1.tolist()
stock_tclose=stock_new_sorted.loc[:,['开盘价','收盘价','最低价','最高价']]
stock_tclose1=np.array(stock_tclose)
stock_tclose2= stock_tclose1.tolist()


kline = (
    Kline()
         .add_xaxis(xaxis_data=index2)
         .add_yaxis(series_name=stock_code+stock_name,y_axis=stock_tclose2))
kline.render('hangdadongli.html')
