from config import path_model_h5
from keras.models import load_model
import numpy

obj = [
    {'id': 0, 'name': 'cone'},
    {'id': 1, 'name': 'sphere'},
    {'id': 2, 'name': 'torus'}
]


class CNN3D:
    def __int__(self):
        self.model = load_model(path_model_h5)

    def pred(self, data):
        result = self.model.predict(data)
        result = numpy.argmax(result, axis=1)
        return [j['name'] for i in result for j in obj if j['id'] == i]
