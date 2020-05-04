from config import path_model_h5
from keras.models import load_model
import numpy as np
from matplotlib.pyplot import cm

obj = [
    {'id': 0, 'name': 'cone'},
    {'id': 1, 'name': 'sphere'},
    {'id': 2, 'name': 'torus'}
]


class CNN3D:
    def __int__(self):
        self.model = load_model(path_model_h5)

    def prep_data(self, data):
        # Introduce the channel dimention in the input dataset
        _data = np.ndarray((data.shape[0], 4096, 3))

        # iterate in train and test, add the rgb dimention
        def add_rgb_dimention(array):
            scaler_map = cm.ScalarMappable(cmap="Oranges")
            array = scaler_map.to_rgba(array)[:, : -1]
            return array

        for i in range(_data.shape[0]):
            _data[i] = add_rgb_dimention(_data[i])
        # convert to 1 + 4D space (1st argument represents number of rows in the dataset)
        return _data.reshape(_data.shape[0], 16, 16, 16, 3)

    def pred(self, data):
        result = self.model.predict(self.prep_data(data))
        result = np.argmax(result, axis=1)
        return [j['name'] for i in result for j in obj if j['id'] == i]
