from flask import jsonify, request
from app import *


@app.route('/get_3d_info_cnn', methods=['GET', 'POST'])
def get_3d_info_cnn():

    if request.method == 'POST':
        data = request.files.getlist('file')
        D = Data(data)
        data = D.data_preparation()
        recognized = CNN3D.pred(data)
        points = D.get_points()
        voxels = D.get_voxels()

        return jsonify()

