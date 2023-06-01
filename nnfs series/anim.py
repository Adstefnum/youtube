from manimlib.imports import Scene
from neural_network_manim import NeuralNetworkMobject

class NeuralNet(Scene):
    def construct(self):
        net = NeuralNetworkMobject([2, 3, 4, 5, 2])