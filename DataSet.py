import networkx as nx
import matplotlib.pyplot as plt
import string


# Creates and displays graph datasets in the ER model:
def showGraphER():
    # erdos renyi graph
    # generate a graph which has n=20 nodes, probablity p = 0.2.
    ER = nx.random_graphs.erdos_renyi_graph(1000, 0.2)
    PW = nx.powerlaw_cluster_graph(20, 3, 0)
    # the shell layout
    pos = nx.shell_layout(ER)
    NER = []
    for e in nx.to_edgelist(ER):
        T = (e[0], e[1], RandomLetter())
        NER.append(T)
    # print(NER)
    return NER
    # nx.draw(ER, pos, with_labels=False, node_size=30)
    # plt.show()


# method to generate Power Law Graphs
def showGraphPW():
    # generates a graph according to the power law model
    PW = nx.powerlaw_cluster_graph(20, 3, 0)
    # the shell layout
    pos = nx.shell_layout(PW)
    NPW = []
    for e in nx.to_edgelist(PW):
        T = (e[0], e[1], RandomLetter())
        NPW.append(T)
    return NPW
    print(NPW)
    nx.draw(PW, pos, with_labels=False, node_size=30)
    plt.show()


# Returns a random lowercase letter in the alphabet
def RandomLetter():
    string.ascii_letters
    import random
    letter = random.choice(string.ascii_lowercase)
    return letter
