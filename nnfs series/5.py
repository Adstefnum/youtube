from manimlib.imports import *
import os
import sys


module_directory = os.path.abspath(os.path.dirname(__file__))
sys.path.append(module_directory)

from neural_network_manim import NeuralNetworkMobject

class Net5(Scene):
    def construct(self):
        net = NeuralNetworkMobject([1])
       

        net.scale(4)
        self.play(Write(net), run_time=2)

        text = Text("Weights").scale(0.8)
        text.move_to(net.get_left() + 4.5 * LEFT)  # Adjust the position as needed

        text2 = Text("Biases").scale(0.8)
        text2.move_to(net.get_right() + 5 * RIGHT)  # Adjust the position as needed

        # Add the arrow
        arrow = Arrow(text.get_right(), net.get_left(), color=BLUE)
        arrow2 = Arrow(text2.get_right(), net.get_right(), color=ORANGE)

        self.play(ShowCreation(text), ShowCreation(arrow))
        self.play(ShowCreation(text2), ShowCreation(arrow2))

        text = Text("Parameters").scale(0.8)
        text.move_to(2 * UP)  # Adjust the position as needed
        self.play(Write(text))
        self.wait(1)