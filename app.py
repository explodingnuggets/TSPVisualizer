import tkinter as tk

import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


import tsp

class GraphApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.title('Traveling Salesman Problem - Examples')

        self.step_counter = 0
        self.step_total = 0
        self.callback = None

        self.tsp = tsp.TSP()

        self.figure = Figure(figsize=(7, 5), dpi=100, tight_layout=True)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_axis_off()

        self.create_widgets()

        self.randomize()

    def create_widgets(self):
        # Widget: Canvas Frame widget
        self.canvas_frame = tk.Frame(self, bg='white')
        self.canvas_frame.pack()

        # Widget: Menu Frame
        self.menu_frame = tk.Frame(self, pady=5)
        self.menu_frame.pack()

        # Widget: Matplotlib Canvas
        self.plt_canvas = FigureCanvasTkAgg(self.figure, self.canvas_frame)
        self.plt_canvas.show()
        self.plt_canvas.get_tk_widget().pack(side='bottom', expand=True)

        # Widget: Botões
        self.step_button = tk.Button(self.menu_frame, text='Step', command=self.step)
        self.step_button.pack(side='left')

        self.run_button = tk.Button(self.menu_frame, text='Run', command=self.run)
        self.run_button.pack(side='left')

        self.reset_button = tk.Button(self.menu_frame, text='Reset', command=self.reset)
        self.reset_button.pack(side='left')

        self.randomize_button = tk.Button(self.menu_frame, text='Randomize', command=self.randomize)
        self.randomize_button.pack(side='left')

        # Widget: Texto
        self.counter_nodes_var = tk.StringVar()
        self.counter_nodes = tk.Label(self.menu_frame, textvariable=self.counter_nodes_var, padx=10)
        self.counter_nodes.pack(side='right')

        self.distance_var = tk.StringVar()
        self.distance = tk.Label(self.menu_frame, textvariable=self.distance_var, padx=10)
        self.distance.pack(side='right')

    def step(self):
        self.tsp.step_bruteforce()
        self.step_counter += 1
        self.draw()

    def run(self):
        step = self.tsp.step_bruteforce()
        if step:
            self.step_counter += 1
            self.callback = self.master.after(10, self.run)
            self.run_button.configure(text='Stop', command=self.stop)
        else:
            self.run_button.configure(text='Run', command=self.run)
        self.draw()

    def stop(self):
        if self.callback is not None:
            self.master.after_cancel(self.callback)
            self.run_button.configure(text='Run', command=self.run)

    def reset(self):
        self.tsp.reset()
        self.step_counter = 0
        self.draw()

    def randomize(self):
        self.tsp.random_graph()
        self.step_counter = 0
        self.step_total = len(self.tsp.paths)
        self.draw()
        self.stop()

    def draw(self):
        self.counter_nodes_var.set('{}/{}'.format(self.step_counter, self.step_total))
        self.distance_var.set('Distance: {}'.format(self.tsp.distance))
        self.axes.cla()
        self.axes.set_axis_off()
        nx.draw_networkx_nodes(self.tsp.graph, pos=self.tsp.pos, ax=self.axes)
        nx.draw_networkx_labels(self.tsp.graph, pos=self.tsp.pos, ax=self.axes)
        nx.draw_networkx_edge_labels(self.tsp.graph, pos=self.tsp.pos, ax=self.axes, edge_labels=nx.get_edge_attributes(self.tsp.graph, 'weight'), label_pos=0.3)
        if self.tsp.path is not None:
            colors = [self.tsp.graph[u][v]['color'] for (u, v) in self.tsp.graph.edges()]
            nx.draw_networkx_edges(self.tsp.graph, pos=self.tsp.pos, ax=self.axes, width=1.8, edge_color=colors)
        else:
            nx.draw_networkx_edges(self.tsp.graph, pos=self.tsp.pos, ax=self.axes, width=1.8)
        self.plt_canvas.show()
