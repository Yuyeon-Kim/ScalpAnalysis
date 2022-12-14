# from: https://github.com/aparico/pca-color-augment

from numpy import asarray
import argparse
import fancy_pca
from PIL import Image
import os
import glob

# Construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True,
#	help = "Path to the image")
#args = vars(ap.parse_args())

# Load multiple images
image_list = []
fname_list = []
path = 'F:/DGU/Codes/ScalpAnalysis/ScalpAnalysis/ColorPreprocessing/test_images' # path of the original dataset folder
alpha = 0.3

base = os.listdir(path)
for f in base:
    # Extract the names of the files and put them in a list (fname_list)
    fname = os.path.splitext(f)
    fname_list.append(fname[0])
    print(len(image_list)," image name has saved.")

    # Load images and put them in a list (image_list)
    im = Image.open(os.path.join(path, f))
    image_list.append(im)
    print("Inage", f, "has loaded.")

# Load one image and show it
# i = Image.open('test.jpg')
# i.show(title="Original image")

# Convert images to numpy arrays
array_list =[]
n=1
for i in image_list:
    i_a = asarray(i)
    array_list.append(i_a)
    print("Image", n, ": Conversion successful.")
    n+=1
print("Array of original image: ", i_a) #To see the array

print("Conversion successful")
print(type(i_a), i_a.shape)

# Perform the PCA color augmentation
n=1
aug_list=[]
for a in array_list:
    augmented = fancy_pca.fancy_pca(a, alpha)
    aug_list.append(augmented)
    print("Array",n, ":Augmentation successful")
    n += 1
print("Array of PCA augmented image: ", augmented) #To see the array

# Convert Fancy PCA result back to PIL image
path3 = "F:/DGU/Codes/ScalpAnalysis/ScalpAnalysis/PcaColorAugmentation/res_images/" #path of the destination folder
idx=0
for aug in aug_list:
    i2 = Image.fromarray(aug)
    # print(fname_list)
    while idx<= len(fname_list):
        print(str(fname_list[idx])+"_1.jpg")
        i2.save(path3+(str(fname_list[idx])+"_1.jpg"))
        break
    idx+=1
    print("Augmented image", idx, "saved.")