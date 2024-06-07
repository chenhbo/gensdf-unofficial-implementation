import pandas as pd
import open3d as o3d
import numpy as np

# 读取CSV文件
df = pd.read_csv('data/vertebrae/Object_15_deleted/sdf_data.csv', names=['x', 'y', 'z', 'sdf'])

# 将点坐标转换为numpy数组
points = df[['x', 'y', 'z']].to_numpy()

# 根据SDF值设置颜色
colors = df['sdf'].apply(lambda x: [1, 0, 0] if x > 0 else ([0, 0, 1] if x < 0 else [0, 1, 0])).to_list()
colors = np.array(colors)
# 打印总共的点数
total_points = points.shape[0]
print(f"总共点数: {total_points}")

# # 筛选出SDF值小于0的点
# blue_points_df = df[df['sdf'] < 0]
# # 将点坐标转换为numpy数组
# points = blue_points_df[['x', 'y', 'z']].to_numpy()
# # 设置颜色为蓝色
# colors = np.array([[0, 0, 1]] * len(points))

# 创建Open3D点云对象
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
point_cloud.colors = o3d.utility.Vector3dVector(colors)

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])
