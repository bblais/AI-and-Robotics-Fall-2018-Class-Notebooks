import os
import numpy as np
from numpy import s_
from pylab import imread

def read_image(fname,crop=None):  # crop=s_[30:260,45:310]
    if crop is None:
        raise ValueError('Crop info not given.  Call like read_image("blah.jpg",s_[30:260,45:310])')

    arr=imread(fname)
    print("Min and Max",arr.min(),arr.max())    
    
    if np.any(arr>1):  # if the image is read in as uint8, it's not 0-1 but 0-255, so scale it down
        print("Min and Max",arr.min(),arr.max())
        print("Scaling it down....")
        arr=arr/255
        print("Min and Max",arr.min(),arr.max())    
        
    if len(arr.shape)>2 and arr.shape[2]>3:  # alpha channel
        print("arr shape",arr.shape)
        print("Removing alpha channel")
        arr=arr[:,:,:3]
        print("new arr shape",arr.shape)
        
        
    arr=arr[crop]  # change this for your image
    
    return arr


def get_square(arr,Nr,Nc,r,c,percent=100):
    image_rows,image_cols=arr.shape[:2]
    square_row=int(image_rows/Nr)
    square_col=int(image_cols/Nc)
    
    start_row=int(r*square_row)
    end_row=int((r+1)*square_row)

    start_col=int(c*square_col)
    end_col=int((c+1)*square_col)
    
    if percent==100:
        square=arr[start_row:end_row,start_col:end_col]
        
    else:
        dc=int((end_col-start_col)*(100-percent)/2.0/100.0)
        dr=int((end_row-start_row)*(100-percent)/2.0/100.0)

        square=arr[start_row+dr:end_row-dr,start_col+dc:end_col-dc]
        
        
    return square

def get_square_size(arr,Nr,Nc,r,c,size=None):
    image_rows,image_cols=arr.shape[:2]
    square_row=int(image_rows/Nr)
    square_col=int(image_cols/Nc)

    start_row=int(r*square_row)
    end_row=int((r+1)*square_row)

    start_col=int(c*square_col)
    end_col=int((c+1)*square_col)

    if size is None:
        square=arr[start_row:end_row,start_col:end_col]
    else:
        start_row=int(start_row+(end_row-start_row)/2.0-size[0]/2.0)
        start_col=int(start_col+(end_col-start_col)/2.0-size[1]/2.0)

        square=arr[start_row:start_row+size[0],start_col:start_col+size[1]]


    return square

from Game import Board
from imageio import imwrite
import os
from glob import glob

from classy import *

def images_to_vectors(im,verbose=True):
    data_all=image.images_to_vectors(im,verbose=verbose)
    if np.any(data_all.vectors>1):
        if verbose:
            print("\nScaling down...")

        data_all.vectors/=255.0
        if verbose:
            summary(data_all)

    return data_all

def array_to_image_struct(arr):
    if isinstance(arr,list):
        N=len(arr)
        data=Struct()
        data.DESCR="Images"
        data.files=[None]*N
        data.data=arr
        data.targets=[0]*N
        data.target_names=['None']*N
        
        
    else:
        data=Struct()
        data.DESCR="Images"
        data.files=[None]
        data.data=[arr]
        data.targets=[0]
        data.target_names=['None']

    return data

