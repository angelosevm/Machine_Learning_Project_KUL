import ternary
from egtplot import *
import time


class TernaryLearningCurves:

    @staticmethod
    def plot_curves(curves, name="learning", colors=['b', 'r', 'k']):
        figure, tax = ternary.figure(scale=1.0)
        tax.boundary()
        tax.gridlines(multiple=0.2, color="blue")
        tax.left_corner_label("S", fontsize=16)
        tax.right_corner_label("R", fontsize=16)
        tax.top_corner_label("P", fontsize=16)
        for i, points in enumerate(curves):
            tax.plot(points, linewidth=2.0, label="Curve", color=colors[i])
        # tax.ticks(axis='lbr', multiple=0.2, linewidth=1, tick_formats="%.1f")
        tax.get_axes().axis('off')
        tax.clear_matplotlib_ticks()
        tax.get_axes().set_aspect(1)
        tax.savefig("Graphs/" + str(time.time()) + "-" + name + ".jpg")

    @staticmethod
    def plot_theoretical_trajectory(labels=['S', 'R', 'P'], payoff_matrix=[[0], [-1], [1], [1], [0], [-1], [-1], [1], [0]]):
        plot_static(payoff_entries=payoff_matrix, vert_labels=labels, display_parameters=False)
        plt.savefig("Graphs/theory.jpg")
