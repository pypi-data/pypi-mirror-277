# -*- coding: utf-8 -*-
"""
@Time : 2023/12/12 17:25 
@项目：crawler_exercise
@File : paddleocr_opetation.by
@PRODUCT_NAME :PyCharm
"""
import cv2
from paddleocr import PPStructure, save_structure_res, PaddleOCR


# is_exists = os.listdir("imgs")  # 读取图片文件位置
# print(is_exists)
# for index, i in enumerate(is_exists[:]):
#     print(index, i)
#     img_path = 'imgs/' + i
#     img = cv2.imread(img_path)
#     result = table_engine(img)
#     # print(result)
#     # print(','.join([i.get('text') for i in result[0].get("res")]))
#     for res in result:
#         print(type(res.get("res")), res.get("res"), )
#         print(res.get("res") and isinstance(res.get("res"), dict))
#         if res.get("res") and isinstance(res.get("res"), dict):
#             if res.get("res").get("html"):
#                 results = res.get("res").get("html")
#                 if '生师比' in results or '毕业生人数' in results or '接收国' in results or '校生人数' in results or '政拨款水平' in results:
#                     print("*" * 10, results)
#                     save_structure_res(result, 'where', 'ex02')  # 存放位置
#     break
class ImageOperations(object):
    def __init__(self):
        self.table_engine = PPStructure(show_log=True)

    def imgtable_to_excel(self, img_path):
        img = cv2.imread(img_path)
        result = self.table_engine(img)
        for res in result:
            print(type(res.get("res")), res.get("res"), )
            print(res.get("res") and isinstance(res.get("res"), dict))
            if res.get("res") and isinstance(res.get("res"), dict):
                if res.get("res").get("html"):
                    results = res.get("res").get("html")
                    # if '生师比' in results or '毕业生人数' in results or '接收国' in results or '校生人数' in results or '政拨款水平' in results:
                    save_structure_res(result, 'where', 'ex02')  # 存放位置

    def img_str(self, img_path):
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        # 要识别图片的路径：

        # 识别结果：
        result = ocr.ocr(img_path, cls=True)
        # 结果输出展示：
        for line in result[0]:
            print(line)


img_path = "imgs/image80_627.png"
