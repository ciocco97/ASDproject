from xml.dom import minidom

import matplotlib.pyplot as plt
import xml.etree.cElementTree as ET


class OurPlotter:
    ALONE = 0
    NO_PRE_PROC = 1
    PRE_PROC = 2
    FOLDER = {
        ALONE: "Stand_alone_statistics",
        NO_PRE_PROC: "No_pre_proc_statistics",
        PRE_PROC: "Pre_proc_statistics"
    }

    def __init__(self, log_path):
        self.data = None
        self.reset_data()
        self.log_path = log_path

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
        file = open(self.log_path + "_statistics.xml", "w")
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
        s = minidom.parseString(rough_string)
        file.write(s.toprettyxml(indent="\t"))
        file.close()

    def plot_comparison(self):
        fig, axs = plt.subplots(4, figsize=(10, 7), sharex=True)
        plt.ioff()
        fig.suptitle("Problem data")
        ax_num = 0
        for graph_name in self.data[self.ALONE].keys():
            data = self.data[self.ALONE][graph_name]
            axs[ax_num].set_title(graph_name)
            x = range(0, len(data))
            axs[ax_num].plot(x, data)
            ax_num += 1

        axs[ax_num - 1].set_xlabel("Problem n°")
        self.adjust_and_save_plot(1)

        fig, axs = plt.subplots(8, figsize=(10, 7), sharex=True)
        plt.ioff()
        fig.suptitle("Comparison")
        ax_num = 0

        for graph_name in self.data[self.NO_PRE_PROC].keys():
            y1 = self.data[self.NO_PRE_PROC][graph_name]
            y2 = self.data[self.PRE_PROC][graph_name]
            while len(y1) > len(y2):
                del y1[-1]
            while len(y2) > len(y1):
                del y2[-1]
            x = range(0, len(y1))
            axs[ax_num].plot(x, y1, label=graph_name + " " + self.FOLDER[self.NO_PRE_PROC])
            axs[ax_num].plot(x, y2, label=graph_name + " " + self.FOLDER[self.PRE_PROC])
            axs[ax_num].legend()
            ax_num += 1
            axs[ax_num].set_title(graph_name + " difference")
            axs[ax_num].plot(x, [(y1[i] - y2[i]) / y1[i] * 100 for i in x])
            ax_num += 1

        self.adjust_and_save_plot(2)

    def adjust_and_save_plot(self, n: int):
        plt.tight_layout()
        plt.subplots_adjust(wspace=1, hspace=1)

        path = self.log_path + str(n) + "_graph.png"
        plt.savefig(path)
        print(f"Graph saved in main folder: {path}")
