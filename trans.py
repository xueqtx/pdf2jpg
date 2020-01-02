import fitz
import os
from create import createFiles





def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

#  打开PDF文件，生成一个对象
def trans():
    desktop = GetDesktopPath()
    dirs = str(desktop)+"\\发票报销"
    os.chdir(dirs)
    os.listdir(dirs)
    if not os.path.exists("png"):
        os.mkdir("png")
    files = os.listdir(dirs)
    for fileName in files:
        file_name, extension_name = os.path.splitext(fileName)
        if extension_name=='.pdf':
            doc = fitz.open(fileName)
            for pg in range(doc.pageCount):
                page = doc[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
                zoom_x = 0.8
                zoom_y = 0.8
                trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
                pm = page.getPixmap(matrix=trans, alpha=False)
                pm.writePNG(str(fileName)[0:-4]+'.png')
        else:
            continue

    createFiles(dirs)

    print("success!")