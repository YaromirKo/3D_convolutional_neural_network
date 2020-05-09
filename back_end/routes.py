from flask import jsonify, request
import os
from app import *
from Data import Data
import json



# @app.route('/get_3d_info_cnn', methods=['GET', 'POST'])
# def get_3d_info_cnn():
#     if request.method == 'POST':
#         datas = request.files.getlist('file')
#         path_files = []
#         for file in datas:
#             ply_file = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(ply_file)
#             path_files.append(ply_file)
#         D = Data(path_files)
#         data = D.get_voxel_grid_vector()
#         recognized = cnn3d.pred(data)
#         obj_s = D.get_voxel_grid()
#         for file in datas:
#             ply_file = os.path.join(UPLOAD_FOLDER, file.filename)
#             os.remove(ply_file)
#         return jsonify(recognized=recognized, obj_s=obj_s)


@app.route('/some')
def get_3d_info_cnn():
    D = Data(["./cone_2.ply"])
    data = D.get_voxel_grid_vector()
    # recognized = cnn3d.pred(data)
    # # points = D.get_points()
    # # voxel = D.get_n_voxels()
    # # structure = D.get_structure()
    # # vector = D.get_vector()
    obj_s = D.get_plot_points()
    with open('data.json', 'w') as f:
        json.dump(obj_s, f)
    return 0
