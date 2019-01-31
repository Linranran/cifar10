#encoding:utf-8
#author：guohuifeng
#email：309884616@qq.com
from scipy.misc import imsave
import numpy as np
import os

# 解压缩，返回解压后的字典
def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

# 生成训练集图片，如果需要png格式，只需要改图片后缀名即可。
traindir="train"
if os.path.exists(traindir) == False:
    os.mkdir(traindir)
for j in range(1, 6):
    dataName = "cifar-10-batches-py\\data_batch_" + str(j)  # 读取当前目录下的data_batch12345文件，dataName其实也是data_batch文件的路径，本文和脚本文件在同一目录下。
    Xtr = unpickle(dataName)
    print dataName + " is loading..."

    for i in range(0, 10000):
        img = np.reshape(Xtr['data'][i], (3, 32, 32))  # Xtr['data']为图片二进制数据
        img = img.transpose(1, 2, 0)  # 读取image
        picName = 'train/' + str(Xtr['labels'][i]) + '_' + str(i + (j - 1)*10000) + '.jpg'  # Xtr['labels']为图片的标签，值范围0-9，本文中，train文件夹需要存在，并与脚本文件在同一目录下。
        imsave(picName, img)
    print dataName + " loaded."

print "test_batch is loading..."

# 生成测试集图片
testdir="test"
if os.path.exists(testdir) == False:
    os.mkdir(testdir)
testXtr = unpickle("cifar-10-batches-py\\test_batch")
for i in range(0, 10000):
    img = np.reshape(testXtr['data'][i], (3, 32, 32))
    img = img.transpose(1, 2, 0)
    picName = 'test/' + str(testXtr['labels'][i]) + '_' + str(i) + '.jpg'
    imsave(picName, img)
print "test_batch loaded."

traindir="train"
testdir="test"
train_imgs=os.listdir(traindir)
test_imgs=os.listdir(testdir)
f = open('train_lable.txt','w')
for i in train_imgs:
    train_img=i
    train_lab=i.split("_")[0]
    f.write(train_img+' '+train_lab+'\n')
print "genarate train lable"
f = open('text_lable.txt','w')
for i in test_imgs:
    test_img=i
    test_lab=i.split("_")[0]
    f.write(test_img+' '+test_lab+'\n')
print "genarate test lable"