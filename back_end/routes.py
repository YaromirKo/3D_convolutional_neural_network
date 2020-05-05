from flask import jsonify, request
from app import *
from Data import Data


if PRODUCTION:
    @app.route('/get_3d_info_cnn', methods=['GET', 'POST'])
    def get_3d_info_cnn():
        if request.method == 'POST':
            data = request.files.getlist('file')
            D = Data(data)
            data = D.get_voxel_grid_vector()
            recognized = cnn3d.pred(data)
            points = D.get_points()
            voxel = D.get_n_voxels()
            structure = D.get_structure()
            vector = D.get_vector()

            return jsonify(recognized=recognized,
                           points=points,
                           voxel=voxel,
                           structure=structure,
                           vector=vector)

if DEV:
    @app.route('/test')
    def get_3d_info_cnn():
        D = Data(["./cone_2.ply"])
        data = D.get_voxel_grid_vector()
        recognized = cnn3d.pred(data)
        points = D.get_points()
        voxel = D.get_n_voxels()
        structure = D.get_structure()
        vector = D.get_vector()

        return jsonify(recognized=recognized,
                       points=points,
                       voxel=voxel,
                       structure=structure,
                       vector=vector)
