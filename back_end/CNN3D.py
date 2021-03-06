from tensorflow import keras
import numpy as np
from matplotlib.pyplot import cm
import tensorflow as tf

path_model_h5 = 'figure_w.h5'

obj = [
    {'id': 0, 'name': 'cone'},
    {'id': 1, 'name': 'sphere'},
    {'id': 2, 'name': 'torus'}
]


class CNN3D:
    def __init__(self):
        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                # Currently, memory growth needs to be the same across GPUs
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
                logical_gpus = tf.config.experimental.list_logical_devices('GPU')
                print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
            except RuntimeError as e:
                # Memory growth must be set before GPUs have been initialized
                print(e)

        self.model = keras.models.load_model(path_model_h5)

    def prep_data(self, data):
        pred = np.ndarray((data.shape[0], 4096, 3))

        # iterate in train and test, add the rgb dimention
        def add_rgb_dimention(array):
            scaler_map = cm.ScalarMappable(cmap="Oranges")
            array = scaler_map.to_rgba(array)[:, : -1]
            return array

        for i in range(data.shape[0]):
            pred[i] = add_rgb_dimention(data[i])

        # convert to 1 + 4D space (1st argument represents number of rows in the dataset)
        return pred.reshape(data.shape[0], 16, 16, 16, 3)

    def pred(self, data):
        result = self.model.predict(self.prep_data(data))
        result = np.argmax(result, axis=1)
        return [j['name'] for i in result for j in obj if j['id'] == i]
