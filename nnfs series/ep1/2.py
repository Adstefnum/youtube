from manimlib.imports import *
import os
import sys


module_directory = os.path.abspath(os.path.dirname(__file__))
sys.path.append(module_directory)

from neural_network_manim import NeuralNetworkMobject

class NeuralNet(Scene):
    def construct(self):
        net = NeuralNetworkMobject([3, 4, 4, 3])
        net.label_inputs("x")
        net.label_outputs("y")
        net.label_hidden_layers("h")
        # net.label_outputs_text(["sunny", "snowy", "rainy"])

        net.scale(2)
        self.play(Write(net), run_time=3)
        # Add the text
        text = Text("Data").scale(0.8)
        text.move_to(net.get_left() + 2 * LEFT)  # Adjust the position as needed

        # Add the arrow
        arrow = Arrow(text.get_right(), net.get_left(), color=WHITE)

        # Add the text and arrow to the scene
        self.add(text, arrow)
        self.play(ShowCreation(text), ShowCreation(arrow))
