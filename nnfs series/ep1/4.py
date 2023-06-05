from manimlib.imports import *
import os
import sys


module_directory = os.path.abspath(os.path.dirname(__file__))
sys.path.append(module_directory)

from neural_network_manim import NeuralNetworkMobject

class Net4(Scene):
    def construct(self):
        net = NeuralNetworkMobject([3, 4, 4, 3])
        net.label_inputs("x")
        net.label_outputs("y")
        net.label_hidden_layers("h")
        # net.label_outputs_text(["sunny", "snowy", "rainy"])

        net.scale(2)
        self.play(Write(net), run_time=3)
        # Add the text
        text = Text("Hidden Layer").scale(0.8)
        text.move_to(net.get_bottom() + 2)  # Adjust the position as needed
        
        surRect = SurroundingRectangle(net.layers[1:3], color = YELLOW, buff=0.3)
        self.play(ShowCreation(surRect))
        self.wait()
       

        self.play(ShowCreation(text))
        self.wait(12)
