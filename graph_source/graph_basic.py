# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 10:43
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : graph_basic.py
# @Software: PyCharm
import sys
import networkx as nx
import data_source
from matplotlib import pyplot as plt

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


def graph_base():
    g = nx.Graph()
    nodes = data_source.create_int_set()
    edges = data_source.create_int_edges(nodes)
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    print(g.number_of_nodes())
    print(g.number_of_edges())

    for n in g.nodes():
        nb = [str(i) for i in g.neighbors(n)]
        print(str(n) +  ': ' + ','.join(nb))

    print(g.degree(1))
    # print(g.degree[1])
    print(g.adj[1])

    # 返回点的临近点及其边的属性
    # for n, brs in g.adjacency_iter():
    #     for br, it in brs.items():
    #         print(n, br, it)
    # 连通分量
    print(len(list(nx.connected_components(g))))


if __name__ == "__main__":
    graph_base()