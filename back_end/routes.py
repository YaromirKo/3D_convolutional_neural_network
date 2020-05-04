from flask import jsonify, request
from app import *
from Data import Data


# @app.route('/get_3d_info_cnn', methods=['GET', 'POST'])
# def get_3d_info_cnn():
#     if request.method == 'POST':
#         data = request.files.getlist('file')
#         D = Data(data)
#         data = D.get_voxel_grid_vector()
#         recognized = CNN3D.pred(data)
#         points = D.get_points()
#         voxel = D.get_n_voxel()
#         structure = D.get_structure()
#         vector = D.get_vector()
#
#         return jsonify(recognized=recognized,
#                        points=points,
#                        voxel=voxel,
#                        structure=structure,
#                        vector=vector)


@app.route('/test')
def get_3d_info_cnn():
    D = Data(["./sphere_0.ply"])
    data = D.get_voxel_grid_vector()
    # recognized = CNN3D.pred(data)
    points = D.get_points()
    n_voxels = D.get_n_voxels()
    structure = D.get_structure()
    vector = D.get_vector()

    return jsonify(points=points,
                   n_voxels=n_voxels,
                   structure=structure,
                   vector=vector)
