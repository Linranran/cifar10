from scipy.misc import imsave
import numpy as np
import os
from PIL import Image



def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

traindir="train"
if os.path.exists(traindir) == False:
    os.mkdir(traindir)
for j in range(1, 6):
    dataName = "cifar-10-batches-py\\data_batch_" + str(j)
    Xtr = unpickle(dataName)
    print dataName + " is loading..."

    for i in range(0, 10000):
        img = np.reshape(Xtr['data'][i], (3, 32, 32))
        img0 = img[0]
        img1 = img[1]
        img2 = img[2]
        i0 = Image.fromarray(img0)
        i1 = Image.fromarray(img1)
        i2 = Image.fromarray(img2)
        img = Image.merge("RGB", (i2, i1, i0))
        picName = 'train/' + str(Xtr['labels'][i]) + '_' + str(i + (j - 1)*10000) + '.jpg'
        imsave(picName, img)
    print dataName + " loaded."


testdir="test"
if os.path.exists(testdir) == False:
    os.mkdir(testdir)
testXtr = unpickle("cifar-10-batches-py\\test_batch")
for i in range(0, 10000):
    img = np.reshape(testXtr['data'][i], (3, 32, 32))
    img0 = img[0]
    img1 = img[1]
    img2 = img[2]
    i0 = Image.fromarray(img0)
    i1 = Image.fromarray(img1)
    i2 = Image.fromarray(img2)
    img = Image.merge("RGB", (i2, i1, i0))
    picName = 'test/' + str(testXtr['labels'][i]) + '_' + str(i) + '.jpg'
    imsave(picName, img)

root=os.getcwd()
traindir="train"
testdir="test"
train_imgs=os.listdir(traindir)
test_imgs=os.listdir(testdir)
f = open('train_lable_1.txt','w')
for i in train_imgs:
    train_img=i
    train_lab=i.split("_")[0]
    f.write(root+'\\'+traindir+'\\'+train_img+' '+train_lab+'\n')
print ("genarate train lable")
f = open('test_lable.txt','w')
for i in test_imgs:
    test_img=i
    test_lab=i.split("_")[0]
    f.write(root+'\\'+testdir+'\\'+test_img+' '+test_lab+'\n')
print ("genarate test lable")