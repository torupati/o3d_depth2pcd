import open3d as o3d
import matplotlib.pyplot as plt

print("Read Redwood dataset")
redwood_rgbd = o3d.data.SampleRedwoodRGBDImages()

print(f'Redwood Dataset {len(redwood_rgbd.color_paths)}')
rgb_filepath = redwood_rgbd.color_paths[0]
depth_filepath = redwood_rgbd.depth_paths[0]
print(rgb_filepath)
print(depth_filepath)
color_raw = o3d.io.read_image(rgb_filepath)
depth_raw = o3d.io.read_image(depth_filepath)

print(f'color: {type(color_raw)} type={color_raw.get_geometry_type()} dim={color_raw.dimension()}')
print(f'depth: {type(depth_raw)} type={depth_raw.get_geometry_type()} dim={depth_raw.dimension()}')

rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_raw, depth_raw)
print(rgbd_image)
print('---')
#plt.subplot(1, 2, 1)
#plt.title('Redwood grayscale image')
#plt.imshow(rgbd_image.color)
#plt.subplot(1, 2, 2)
#plt.title('Redwood depth image')
#plt.imshow(rgbd_image.depth)
#plt.savefig('out.png')
#plt.close()
#plt.show()

pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# Flip it, otherwise the pointcloud will be upside down
#pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
print(type(pcd))
#o3d.visualization.draw_geometries([pcd], zoom=0.5)

o3d.io.write_point_cloud("test.pcd", pcd)

input('qqq')

