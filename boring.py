from skimage import io,data,img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

def lsb(x):
    lsb_list=[]
    for i in range(0, 8):
        lsb_list.append(x % (2**(i+1)))
        #print(lsb_list)
    for j in range(7, 0, -1):
        lsb_list[j] = lsb_list[j] - lsb_list[j-1]
        if lsb_list[j] != 0:
            if (lsb_list[j] % 2) ==0:
                lsb_list[j] = 1
            else:
                lsb_list[j] = 0
# print("lsb(%s) -> %s" % (j, lsb_list[j]))
# print("lsb(%s) -> %s" % (0, lsb_list[0]))
    return lsb_list
#lsb(254)
# img=data.chelsea()
img=io.imread('0413.jpg')
rows,cols,dims=img.shape
plt.figure(figsize=(16,16))
img_gray = img_as_ubyte(img.copy())
img_sample = img[:,:,0].copy()
for i in range(0,rows):
    for j in range(0,cols):
        sum = 0.0
        for k in range(0,3): #dims=3
            sum = sum + img[i,j,k]
# print(sum)
        img_gray[i,j] = sum/3 #dims=3

        img_sample[i,j] = sum/3 #dims=2

        lsb_list = lsb(img_sample[i,j])
        if lsb_list[6] == 1:
            img_sample[i,j] = 255
        else:
            img_sample[i,j] = 0

plt.subplot(3,1,1)
plt.title('origin image')
plt.imshow(img)
plt.subplot(3,1,2)
plt.title('gray image')
plt.imshow(img_gray)
plt.subplot(3,1,3)
plt.title('LSB6')
io.imshow(img_sample)
plt.show()