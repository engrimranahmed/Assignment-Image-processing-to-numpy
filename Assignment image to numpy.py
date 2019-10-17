from PIL import Image
import numpy as np
import os
import matplotlib.pylab as plt
from os.path import join

pics_list = []
a = int(input('Enter picture number to resize\n'))
              
def path_finder():
    #dir = '.'
    #dir = '/Users/ABC/picture'
    dir = '/picture'
    for dirpath, dirnames, filenames in os.walk(dir):
    #for dirpath, dirnames, filenames in os.walk('/Users/ABC/OneDrive/Desktop/Pil picture/'):
        # if os.path.isdir(dirpath):
        print('currentpath exists', dirpath)
        print('directories', dirnames)
        print('files', filenames)
        for filename in filenames:
            try:
                if filename is not None:
                #if os.stat(filename).st_size > 0:
                    # print('Files:',filename)
                    path = join(dirpath, filename)
                    #print('complete path:' ,path)
                    try:
                        if os.path.exists(path):
                            #pics_list.append(filename)
                            #print('path exist')
                            # if os.path.isfile(filename):
                            isFile_exist(path)
                    except:
                        #path does not exist
                        print("path is not Found")

            except FileNotFoundError:
                print("file not found")

def isFile_exist(path):
    # Check if given path exists and it is a file
    #try:
        # if os.path.exists(filename) or os.path.isfile(filename):
    #print('file is:', path)
    pics_list.append(path)
    #except:
        #print("filname ", filename, " does not exists")
        #raise Exception("File doesn't exist")
    # else:
    # print('file is not found')
    # raise Exception("File doesn't exist")

'''except Exception as e:
    print(" Error " + str(e))'''

def original_pic(a,count):
    #a = int(input('Enter picture number to resize:'))

    if a <=count:
        #print(pics_list[a])
        im1 = plt.imread(pics_list[a])
        plt.imshow(im1, interpolation="None")#, **kwargs)
        plt.legend('Orginal pic')
        im=Image.open(pics_list[a])
        im.show()
        print('Pil Image')
        print('Matplotlib Image')

        print(type(im1))
        print('Original pic shape:', im1.shape)
        print('Original pic size:' , im.size)
        print('Original pic color:', im.mode)
        print('Original pic format:', im.format)
        j = picResize(im)
        return j
#except Exception as e:
        #print(" Error " + str(e))'''


def picResize(im):
    im = im
    im_resize = im.resize((200, 200))
    im_resize.show()
    print(im_resize.format)
    print(im_resize.mode)
    print('Resize pic size:', im_resize.size)
    i = np.asarray(im_resize)
    print('Resize pic shape:', i.shape)
    print('Resize pic ndim:', i.ndim)
    print(type(i))
    print(i)
    return i

def count_file(pics_list):
    fileCount = len(pics_list)
    print('files Count :', fileCount)
    return fileCount

def imagedata_to_numpy(a,resizePicData):
    picData = resizePicData
    b=a
    num = np.zeros([20, 200, 200, 3])
    #b = original_pic(a,count)
    d = num[:b,:,:,:]
    num = d + resizePicData
    print("Resize data save into numpy array(20,200,200,3):\n" ,num)
    print("resize:", num.shape)
    return num

def savedata(imgToNum):
    pic_numpydata_file = imgToNum
    numpydata = str(input('Do you want to save picture numpy data yes or no ?'))
    if numpydata == 'yes':
        #pic_numpydata_file = imagedata_to_numpy(a)
        pic_numpydata = np.save('Image to numpy Data Files' , pic_numpydata_file)
    #else:
        #imagedata_to_numpy(a)


def main():
    #a = int(input('Enter picture number to resize:'))
    path_finder()
    count = count_file(pics_list)
    print(count)
    if count!=0:
        resizePicData = original_pic(a,count)
        imgToNum = imagedata_to_numpy(a,resizePicData)
        savedata(imgToNum)
    else:
        print('file is empty')


if __name__ == "__main__":
    # execute only if run as a script
    main()
