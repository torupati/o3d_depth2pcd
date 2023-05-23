"""
Check file read methods.
"""

import open3d as o3d
import numpy as np
import cv2
infile_test = '../../../open3d_data/extract/SampleRedwoodRGBDImages/depth/00002.png'


def test_read_depth(infile:str = infile_test):
    depth_o3d = o3d.io.read_image(infile)
    print(type(depth_o3d))
    print(f'dtype=', np.asarray(depth_o3d).dtype, ' shape=', np.asarray(depth_o3d).shape)
    print(f'max=', np.asarray(depth_o3d).max(), ' min=', np.asarray(depth_o3d).min())
    print('')
    
    depth_cv2= cv2.imread(infile, cv2.IMREAD_ANYDEPTH )
    #depth_cv2_u= cv2.imread( path, cv2.IMREAD_UNCHANGED )
    print('-----------------------------------------------')
    print(type(depth_cv2))
    print(f'dtype=', depth_cv2.dtype, ' shape=', depth_cv2.shape)
    print(f'max=', np.asarray(depth_cv2).max(), ' min=', np.asarray(depth_cv2).min())
    print('')
    depth_o3d_2 = o3d.geometry.Image(depth_cv2)
    print(type(depth_o3d_2))
    print(f'dtype=', np.asarray(depth_o3d_2).dtype, ' shape=', np.asarray(depth_o3d_2).shape)
    print(f'max=', np.asarray(depth_o3d_2).max(), ' min=', np.asarray(depth_o3d_2).min())
    print('')
    
    w, h = depth_cv2.shape
    print(w,h)
    for i in range(w):
        for j in range(h):
            assert np.asarray(depth_o3d)[i][j] == np.asarray(depth_o3d_2)[i][j]
            assert np.asarray(depth_o3d)[i][j] == depth_cv2[i][j]
    
