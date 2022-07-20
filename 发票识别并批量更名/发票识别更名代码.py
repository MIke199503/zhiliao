# encoding:utf-8
# 导入相关库
import os
import requests
import base64
from pathlib import Path

'''
定额发票识别
'''


# 识别发票中想要的数据
def recg_bill(img_path, new_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"
    p = Path(img_path)
    # 得到所有文件夹下 .png 图片
    img_dir = p.glob('**/*.png')
    abs_path = []
    for file_path in img_dir:
        # 二进制方式打开图片文件
        f = open(file_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        access_token = '你的access_token码'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            result = response.json()
            words_result = result['words_result']
            Invoice_number = words_result['InvoiceNum']
            Billing_date = words_result['InvoiceDate']
            Amount = words_result['AmountInFiguers']
            img_name = Invoice_number + '-' + Billing_date + '-' + Amount
            absp = new_path + '\\' + img_name + '.png'
        else:
            absp = new_path + '\\' + '识别失败' + '.png'
        f.close()
        os.rename(file_path, absp)


if __name__ == '__main__':
    img_path = r'你的图片文件夹路径'
    new_path = r'图片另存的文件夹路径'
    recg_bill(img_path, new_path)


