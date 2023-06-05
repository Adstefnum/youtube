from manimlib.imports import *
    
module_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(module_directory)

from neural_network_manim import NeuralNetworkMobject
class Net1(Scene):
    def construct(self):
        # Create a single neuron
        neuron = Circle(radius=1, fill_opacity=1, color=BLUE)
        neuron_label = Text("Neuron").next_to(neuron, DOWN)

        # Create the neural network
        net = NeuralNetworkMobject([3, 4, 4, 3])
        network_label = Text("Neural Network").next_to(net, DOWN)

        # Add animations
        self.play(Write(neuron), Write(neuron_label))
        self.wait(2)
        self.play(Transform(neuron, net), Transform(neuron_label, network_label))
        self.wait(1)
        self.play(
            LaggedStartMap(GrowFromCenter, net, run_time=1),
            Write(network_label)
        )
        self.wait(1)
