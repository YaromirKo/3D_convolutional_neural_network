from pyntcloud import PyntCloud
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from VoxelGrid import VoxelGrid


class Data(object):
    def __init__(self, data):
        self.data = data
        self.VG = []
        self.points = []

    def get_voxel_grid_vector(self):
        vox = []
        for ply_file in self.data:
            points = PyntCloud.from_file(ply_file)
            cloud_points = points.get_sample("mesh_random", n=10000, as_PyntCloud=True)
            new_format_voxel = pd.DataFrame({"x": cloud_points.points['x'], "y": cloud_points.points['y'],
                                             "z": cloud_points.points['z']}).to_numpy()
            self.points.append(new_format_voxel)
            voxel_grid = VoxelGrid(new_format_voxel, x_y_z=[16, 16, 16])
            self.VG.append(voxel_grid)
            _vector = np.reshape(voxel_grid.vector, (4096))
            vox.append(_vector)
        return np.array(vox)

    # def get_points(self):
    #     return [item.points.tolist() for item in self.VG][0]
    #
    # def get_n_voxels(self):
    #     return [item.n_voxels for item in self.VG]
    #
    # def get_structure(self):
    #     return [item.structure.tolist() for item in self.VG][0]
    #
    # def get_vector(self):
    #     return [item.vector.tolist() for item in self.VG][0]

    def get_voxel_grid(self):
        cmap = "Oranges"
        axis = False
        arr_obj = []

        for v_g in self.VG:
            scaled_shape = v_g.shape / min(v_g.shape)

            # coordinates returned from argwhere are inversed so use [:, ::-1]
            points = np.argwhere(v_g.vector)[:, ::-1] * scaled_shape

            s_m = plt.cm.ScalarMappable(cmap=cmap)
            rgb = s_m.to_rgba(v_g.vector.reshape(-1)[v_g.vector.reshape(-1) > 0])[:, :-1]

            camera_position = points.max(0) + abs(points.max(0))
            look = points.mean(0)

            if axis:
                axis_size = points.ptp() * 1.5
            else:
                axis_size = 0

            arr_obj.append({
                "camera_x": str(camera_position[0]),
                "camera_y": str(camera_position[1]),
                "camera_z": str(camera_position[2]),
                "look_x": str(look[0]),
                "look_y": str(look[1]),
                "look_z": str(look[2]),
                "X": str(points[:, 0].tolist()),
                "Y": str(points[:, 1].tolist()),
                "Z": str(points[:, 2].tolist()),
                "R": str(rgb[:, 0].tolist()),
                "G": str(rgb[:, 1].tolist()),
                "B": str(rgb[:, 2].tolist()),
                "S_x": str(scaled_shape[0]),
                "S_y": str(scaled_shape[2]),
                "S_z": str(scaled_shape[1]),
                "n_voxels": str(sum(v_g.vector.reshape(-1) > 0)),
                "axis_size": str(axis_size)})

        return arr_obj

    def get_plot_points(self):

        colors = None
        size = 0.1
        axis = False
        arr_obj = []

        for model_xyz in self.points:

            xyz = model_xyz
            positions = xyz.reshape(-1).tolist()
            camera_position = xyz.max(0) + abs(xyz.max(0))
            look = xyz.mean(0)
            if colors is None:
                colors = [1, 0.5, 0] * len(positions)
            elif len(colors.shape) > 1:
                colors = colors.reshape(-1).tolist()
            if axis:
                axis_size = xyz.ptp() * 1.5
            else:
                axis_size = 0

            arr_obj.append({
                "camera_x": str(camera_position[0]),
                "camera_y": str(camera_position[1]),
                "camera_z": str(camera_position[2]),
                "look_x": str(look[0]),
                "look_y": str(look[1]),
                "look_z": str(look[2]),
                "positions": str(positions),
                "colors": str(colors),
                "points_size": str(size),
                "axis_size": str(axis_size)})

        return arr_obj
