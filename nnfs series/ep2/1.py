from manim import *
    
class Net1(Scene):
    def construct(self):
        # Create a single neuron
        neuron = Circle(radius=1, fill_opacity=1, color=BLUE)
        neuron_label = Tex("Neuron").next_to(neuron, DOWN)

        # Create the neural network
        network = VGroup()
        for _ in range(3):
            network.add(Circle(radius=1, fill_opacity=1, color=BLUE))
        network.arrange(RIGHT, buff=2)
        network_label = Tex("Neural Network").next_to(network, DOWN)

        # Add animations
        self.play(Create(neuron), Write(neuron_label))
        self.wait(1)
        self.play(Transform(neuron, network[0]), Transform(neuron_label, network_label))
        self.play(
            LaggedStartMap(GrowFromCenter, network[1:], run_time=1),
            Write(network_label)
        )
        self.wait(1)
