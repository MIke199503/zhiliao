__name__  =  "AscillImage.py"
__doc__ = """
该模块中：用于生成字符画
    get_ascill_image(pth,opt)
    |---pth:需要被转换的图片路径
    |---opt:字符画保存的路径,以name.txt为结尾。

Examples:
    get_ascill_image("/Users/MikeImac/Desktop/image.png","/Users/MikeImac/Desktop/test.txt")
            """


from PIL import Image # 导入Image模块

def get_ascill_image(pth,opt):
    """将图片转换字符画，该函数接受两个参数：
            pth:需要被转换的图片路径
            opt:字符画保存的路径,以name.txt为结尾。
    """
    img = Image.open(pth) #读取文件
    out_img = img.convert('L')  # 图片转换为灰度模式
    w, h = out_img.size  #返回原始图片大小
    n=600/max(w,h) #图像缩小倍数，不然图片转换后会很大

    if n<1:
        out_img = out_img.resize((int(w * n), int(h * n * 0.5)))  # 因字符的宽度一般大于2倍的高度，所以重新设置图片的大小。
    else:
        out_img = out_img.resize((int(w), int(h)))

    w, h = out_img.size #获取变化之后的图片大小
    #asciis='$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^\ '  #字符集，不执行，选择其中的字符做填充。
    asciis = "@%#*+=-:. "  # 灰度表
    texts = '' #存储字符数据

    for row in range(h): #遍历列
        for col in range(w): #遍历行
            gray = out_img.getpixel((col, row)) #获取对应点的灰度值
            texts += asciis[int(gray / 255 * (len(asciis) - 1))]  # 根据灰度值选择不同复杂度的 ASCII 字符
        texts += '\n' #完成一行就换行，

    with open(opt, "w") as file:
        file.write(texts)
        file.close()


if __name__ == "__main__":
    print("运行完成")
    
    