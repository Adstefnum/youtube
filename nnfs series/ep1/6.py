
from manimlib.imports import *
import os
import sys


module_directory = os.path.abspath(os.path.dirname(__file__))
sys.path.append(module_directory)

from neural_network_manim import NeuralNetworkMobject

class Net6(Scene):
    def construct(self):
        net = NeuralNetworkMobject([3, 4, 4, 3])
        net.label_inputs("x")
        net.label_outputs("y")
        net.label_hidden_layers("h")
        # net.label_outputs_text(["sunny", "snowy", "rainy"])

        net.scale(2)
        self.play(Write(net), run_time=3)

        surRect = SurroundingRectangle(net.layers[3], color = YELLOW, buff=0.15)
        self.play(ShowCreation(surRect))
        self.wait(7)


