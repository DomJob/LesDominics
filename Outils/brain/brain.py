from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import RPropMinusTrainer
import pickle

class Brain:
    def __init__(self, nbOutputs):
        self.net = buildNetwork(256, 10, nbOutputs+1)
        self.ds = SupervisedDataSet(256, nbOutputs+1)

    def load(self, file):
        try:
            f = open(file, 'rb')
            self.net = pickle.load(f)
            f.close()
        except:
            print("No brain file found")
            pass

    def save(self, file):
        f = open(file, 'wb')
        pickle.dump(self.net, f)
        f.close()

    def addToDataSet(self, pixelString, outputs):
        inputs = tuple([float(p) for p in pixelString])
        outputs = tuple(outputs)

        self.ds.addSample(inputs, outputs)

    def loadTrainer(self):
        self.trainer = RPropMinusTrainer(self.net, learningrate=5, momentum=1, verbose=True)

    def train(self):
        self.trainer.trainOnDataset(self.ds)


    def activate(self, pixelString):
        inputs = [float(p) for p in pixelString]
        outputs = self.net.activate(inputs)

        return outputs