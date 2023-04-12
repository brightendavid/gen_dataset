import random
import os
# 生成train.txt和val.txt
random.seed(2020)
xml_dir = r'C:\Users\brighten\Desktop\MyDataset\Annotations'
img_dir = r'C:\Users\brighten\Desktop\MyDataset\JPEGImage'
path_list = list()
for img in os.listdir(img_dir):
    img_path = os.path.join(img_dir,img)
    xml_path = os.path.join(xml_dir,img.replace('jpg', 'xml'))
    path_list.append((img_path, xml_path))
random.shuffle(path_list)
ratio = 0.9
train_f = open('./train.txt', 'w')
val_f = open('./val.txt', 'w')
for i ,content in enumerate(path_list):
    img, xml = content
    text = img + ' ' + xml + '\n'
    if i < len(path_list) * ratio:
        train_f.write(text)
    else:
        val_f.write(text)
train_f.close()
val_f.close()
# 根据自己数据类别生成标签文档
label = ['Over_railingw']
with open(r'C:\Users\brighten\Desktop\MyDataset\label_list.txt', 'w') as f:
    for text in label:
        f.write(text + '\n')