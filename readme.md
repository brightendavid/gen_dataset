# 数据集生成方式
* gen_img.py 通过视频截取帧图像
* nothing.py  删除多余的负样本，xml未标注的多出的图像
* voc2coco.py voc格式数据集转换为coco数据集格式
* 通过labelimg工具标注获得原始的voc数据集格式自建数据集


# 这是目标检测数据集生成方式
具体实现如下
* 基于lableimg实现
* 主要是不同格式的转换
