import logging
from xml.dom import minidom

import matplotlib.pyplot as plt
import xml.etree.cElementTree as ET


class OurPlotter:
    SOLVER_TIME = 0
    PRE_PROC_TIME = 1
    MEMORY_USAGE = 2
    MIN_MHS_SIZE = 3
    MAX_MHS_SIZE = 4
    DIM = 5
    FOLDER = {
        SOLVER_TIME: "Solver_time",
        PRE_PROC_TIME: "Pre-process_time",
        MEMORY_USAGE: "Memory_usage",
        MIN_MHS_SIZE: "Min_MHS_size",
        MAX_MHS_SIZE: "Max_MHS_size",
        DIM: "Dimensions_of_the_problem"
    }

    def __init__(self):
        self.data = None
        self.reset_data()

    def reset_data(self):
        self.data = []
        for i in range(0, len(self.FOLDER)):
            self.data.insert(i, {})

    def reset_data_type(self, data_type: int):
        self.data[data_type] = {}

    def add_data(self, data_name: str, data, data_type: int):
        if data_name in self.data[data_type]:
            self.data[data_type][data_name].append(data)
        else:
            self.data[data_type][data_name] = []
            self.data[data_type][data_name].append(data)

    def save_data(self):
        file = open("output.xml", "w")
        d: dict = self.data
        root = ET.Element('output')
        for k1, e1 in enumerate(d):
            child1 = ET.SubElement(root, f"{self.FOLDER[int(k1)]}")
            for k2 in e1.keys():
                child2 = ET.SubElement(child1, k2)
                for i, e3 in enumerate(e1[k2]):
                    child3 = ET.SubElement(child2, f'sample-{i}')
                    child3.text = str(e3)
        rough_string = ET.tostring(root, encoding='utf-8', method='xml')
        print(rough_string)
        s = minidom.parseString(rough_string)
        file.write(s.toprettyxml(indent="\t"))
        file.close()

    def plot_data_to_compare(self, data_type, data_name1, data_name2, abscissa_name=None):
        fig, axs = plt.subplots(4, figsize=(10, 7), sharex=True)
        plt.ioff()
        fig.suptitle(self.FOLDER[data_type])
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

        axs[0].plot(x, y1, label=data_name1)
        axs[0].plot(x, y2, label=data_name2)

        # axs[1].plot(x, [((y2[i] - y1[i]) / y2[i] * 100 if y2[i] != 0 and y2[i] - y1[i] > 0 else 0) for i in x], label="y2 - y1")
        axs[1].plot(x, [(y2[i] - y1[i]) / y2[i] * 100 for i in x], label="y2 - y1")

        axs[0].set_title("Absolute values")
        # axs[0].set_xlabel("Problem n°")
        # axs[0].ylabel("Seconds")
        # axs[0].grid()
        axs[0].legend()

        axs[1].set_title("Difference (%)")
        # axs[1].set_xlabel("Problem n°")
        # axs[1].ylabel("Seconds")
        # axs[1].grid()
        # axs[1].legend()
        # plt.show()

        y1 = self.data[self.DIM]["Domain_size"]
        y2 = self.data[self.DIM]["Set_number"]
        while len(y2) > len(y1):
            logging.warning("La lunghezza dei dati che si vogliono plottare e' diversa")
            del y2[-1]
        while len(y1) > len(y2):
            logging.warning("La lunghezza dei dati che si vogliono plottare e' diversa")
            del y1[-1]

        x = range(0, len(y1))

        axs[2].set_title("Problem size")
        axs[2].plot(x, y1, label="Domain size")
        axs[2].plot(x, y2, label="Set number")
        axs[2].legend()

        y1 = self.data[self.MIN_MHS_SIZE]["Min_MHS_size"]
        y2 = self.data[self.MAX_MHS_SIZE]["Max_MHS_size"]
        while len(y2) > len(y1):
            logging.warning("La lunghezza dei dati che si vogliono plottare e' diversa")
            del y2[-1]
        while len(y1) > len(y2):
            logging.warning("La lunghezza dei dati che si vogliono plottare e' diversa")
            del y1[-1]

        axs[3].set_title("MHS size")
        axs[3].plot(x, y1, label="Min_MHS_size")
        axs[3].plot(x, y2, label="Max_MHS_size")
        axs[3].legend()

        axs[3].set_xlabel("Problem n°")

        plt.tight_layout()
        plt.subplots_adjust(wspace=1, hspace=1)

        plt.savefig("last_plot_experience_" + self.FOLDER[data_type] + ".png")
        print(f"Graph saved in main folder: {'last_plot_experience_' + self.FOLDER[data_type] + '.png'}")
