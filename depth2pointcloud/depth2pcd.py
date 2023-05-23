import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt


def func(rgb_filepath: str, depth_filepath: str):
    print(rgb_filepath)
    print(depth_filepath)
    color_raw = o3d.io.read_image(rgb_filepath)
    depth_raw = o3d.io.read_image(depth_filepath)

    print(f'color: {type(color_raw)} type={color_raw.get_geometry_type()} dim={color_raw.dimension()}')
    print(f'depth: {type(depth_raw)} type={depth_raw.get_geometry_type()} dim={depth_raw.dimension()}')

    print(np.asarray(color_raw).shape, np.asarray(color_raw).dtype)
    print(np.asarray(depth_raw).shape, np.asarray(depth_raw).dtype)

    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw)
    print(rgbd_image)
    print('---')

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    print(type(pcd))
    #o3d.visualization.draw_geometries([pcd], zoom=0.5)

    o3d.io.write_point_cloud("test.pcd", pcd)

def test_rgb_depth_to_pcd():
    print("Read Redwood dataset")
    redwood_rgbd = o3d.data.SampleRedwoodRGBDImages()

    data_index=0
    print(f'Redwood Dataset {len(redwood_rgbd.color_paths)}')
    rgb_filepath = redwood_rgbd.color_paths[data_index]
    depth_filepath = redwood_rgbd.depth_paths[data_index]
    func(rgb_filepath, depth_filepath)

test_rgb_depth_to_pcd()

