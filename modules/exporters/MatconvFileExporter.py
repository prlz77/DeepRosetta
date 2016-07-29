from core.BaseExporter import BaseExporter
from scipy.io import savemat
import numpy as np


class CaffeExporter(BaseExporter):
    """ Class modeling a Caffe exporter

    """
    def __init__(self):
        pass

    def save(self, file_path, model):
        layers = model['layers']
        weights = model['parameters']
        output = {'layers':{}, 'meta':np.array([], dtype=object)}
        oLayers = None
        begin = ''
        for l in layers:
            if layers[l]['bottom'] is None:
                begin = layers[l]
                break

        if begin is not None:
            e = Exception('No initial layer found (pointing to None)')
            raise e

