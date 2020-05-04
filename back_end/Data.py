from pyntcloud import PyntCloud
import pandas as pd
import numpy as np
from VoxelGrid import VoxelGrid


class Data(object):
    def __init__(self, data):
        self.data = data
        self.VG = []

    def get_voxel_grid_vector(self):
        vox = []
        for ply_file in self.data:
            points = PyntCloud.from_file(ply_file)
            cloud_points = points.get_sample("mesh_random", n=10000, as_PyntCloud=True)
            new_format_voxel = pd.DataFrame({"x": cloud_points.points['x'], "y": cloud_points.points['y'], "z": cloud_points.points['z']}).to_numpy()
            voxel_grid = VoxelGrid(new_format_voxel, x_y_z=[16, 16, 16])
            self.VG.append(voxel_grid)
            _vector = np.reshape(voxel_grid.vector, (4096))
            vox.append(_vector)
        return np.array(vox)

    def get_points(self):
        return [item.points.tolist() for item in self.VG][0]

    def get_n_voxels(self):
        return [item.n_voxels for item in self.VG]

    def get_structure(self):
        return [item.structure.tolist() for item in self.VG][0]

    def get_vector(self):
        return [item.vector.tolist() for item in self.VG][0]

