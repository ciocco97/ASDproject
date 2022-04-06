import logging

import matplotlib.pyplot as plt


class OurPlotter:
    SOLVER_TIME = 0
    PRE_PROC_TIME = 1
    MIN_MHS_SIZE = 2
    MAX_MHS_SIZE = 3
    NUM_DATA_TYPES = 4

    def __init__(self):
        self.data = None
        self.reset_data()

    def reset_data(self):
        self.data = []
        for i in range(0, self.NUM_DATA_TYPES):
            self.data.insert(i, {})

    def reset_data_type(self, data_type: int):
        self.data[data_type] = {}

    def add_data(self, data_name: str, data, data_type: int):
        if data_name in self.data[data_type]:
            self.data[data_type][data_name].append(data)
        else:
            self.data[data_type][data_name] = []
            self.data[data_type][data_name].append(data)

    def plot_data_to_compare(self, data_type, data_name1, data_name2, abscissa_name=None):
        fig, axs = plt.subplots(2)
        y1 = self.data[data_type][data_name1]
        y2 = self.data[data_type][data_name2]
        while len(y1) > len(y2):
            logging.warning("La lunghezza dei dati che si vogliono plottare e' diversa")
            del self.data[data_type][data_name1][-1]
        while len(y1) < len(y2):
            logging.warning("La lunghezza dei dati che si vogliono plottare e' diversa")
            del self.data[data_type][data_name2][-1]
        if abscissa_name:
            x = self.data[data_type][abscissa_name]
        else:
            x = range(0, max(len(y1), len(y2)))

        axs[0].set_title("Both graphs")
        # axs[0].xlabel("Problem n°")
        # axs[0].ylabel("Seconds")
        # axs[0].grid()
        axs[0].plot(x, y1, label=data_name1)
        axs[0].plot(x, y2, label=data_name2)
        # axs[0].legend()

        axs[0].set_title("Difference graph")
        # axs[1].xlabel("Problem n°")
        # axs[1].ylabel("Seconds")
        # axs[1].grid()
        axs[1].plot(x, [((y2[i] - y1[i])/y2[i] * 100 if y2[i] != 0 and y2[i] - y1[i] > 0 else 0) for i in x], label="y2 - y1")
        # axs[1].legend()

        plt.pause(0.5)
        plt.savefig("last_plot_experience.png")
