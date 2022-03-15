import open3d as o3d
import numpy as np
from octree import Octree, Node, Data
import thomsonpy.data_management.formatter as formatter
import thomsonpy.config.paths as paths

def vis_points_and_ne(i):
    points_filenames = ['points_1.obj', 'points_2.obj', 'points_3.obj', 'points_4.obj']
    pclouds = list()
    ne_filenames = ['ne_1.obj', 'ne_2.obj', 'ne_3.obj', 'ne_4.obj']
    ne_clouds = list()

    pcloud = formatter.load(paths.OCTREE_DATA_PATH + points_filenames[i])
    pclouds.append(pcloud)
    ne_cloud = formatter.load(paths.OCTREE_DATA_PATH + ne_filenames[i])
    ne_clouds.append(ne_cloud)
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)
    sphere.paint_uniform_color([0.8, 0.5, 0.0])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pclouds[0])
    colors = list()
    for ne_val in ne_clouds[0]:
        color = ne_val
        colors.append(np.array([color, color, color]))
    colors = np.array(colors)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    viewer = o3d.visualization.Visualizer()
    viewer.create_window()
    viewer.add_geometry(pcd)
    viewer.add_geometry(sphere)
    opt = viewer.get_render_option()
    opt.show_coordinate_frame = True
    opt.background_color = np.asarray([0.0, 0.2, 0.2])
    viewer.run()
    viewer.destroy_window()
    del pcloud
    del ne_cloud
    del pcd
    
def vis_octree(i):

    octrees_filenames = ["octree_1.oct", "octree_2.oct", "octree_3.oct", "octree_4.oct"]
    octree = Octree.load(paths.OCTREE_OBJECTS_PATH + octrees_filenames[i])
    octree_geom = octree.get_visual_octree()
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)
    sphere.paint_uniform_color([0.8, 0.5, 0.0])
    viewer = o3d.visualization.Visualizer()
    viewer.create_window()
    for i in octree_geom:
            viewer.add_geometry(i)
    viewer.add_geometry(sphere)
    opt = viewer.get_render_option()
    opt.show_coordinate_frame = True
    opt.background_color = np.asarray([0.0, 0.2, 0.2])
    viewer.run()
    viewer.destroy_window()

def vis_octree_data(i):
    points_filenames = ['points_1.obj', 'points_2.obj', 'points_3.obj', 'points_4.obj']
    pclouds = list()
    ne_filenames = ['ne_1.obj', 'ne_2.obj', 'ne_3.obj', 'ne_4.obj']
    ne_clouds = list()

    pcloud = formatter.load(paths.OCTREE_DATA_PATH + points_filenames[i])
    pclouds.append(pcloud)
    ne_cloud = formatter.load(paths.OCTREE_DATA_PATH + ne_filenames[i])
    ne_clouds.append(ne_cloud)
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)
    sphere.paint_uniform_color([0.8, 0.5, 0.0])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pclouds[0])
    colors = list()
    for ne_val in ne_clouds[0]:
        color = ne_val
        colors.append(np.array([color, color, color]))
    colors = np.array(colors)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    viewer = o3d.visualization.Visualizer()
    viewer.create_window()
    viewer.add_geometry(pcd)
    viewer.add_geometry(sphere)
    opt = viewer.get_render_option()
    opt.show_coordinate_frame = True
    opt.background_color = np.asarray([0.0, 0.2, 0.2])
    viewer.run()
    viewer.destroy_window()
    del pcloud
    del ne_cloud
    del pcd
    
vis_octree(3)