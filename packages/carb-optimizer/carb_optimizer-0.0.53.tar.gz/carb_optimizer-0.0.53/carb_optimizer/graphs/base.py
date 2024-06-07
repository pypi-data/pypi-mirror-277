"""
base class for the graphs module

---
(c) Copyright Bprotocol foundation 2023. 
Licensed under MIT
"""
__VERSION__ = "1.0-rc3" # TODO-RELEASE
__DATE__ = "01/Jun/2024+"

import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
#from abc import ABC
from enum import Enum

@dataclass
class GraphBase():
    """
    lightweight base class for graphs, containing useful analytics for the derived graph implementations
    
    :G:     the graph object (``networkx`` graph, either undirected or directed)
    """
    __VERSION__ = __VERSION__
    __DATE__ = __DATE__
    
    _G: nx.Graph = field(default=None, init=True, repr=False)
    
    @property
    def nodes(self):
        """returns the nodes of the graph"""
        return self.G.nodes
    
    @property
    def edges(self):
        """returns the edges of the graph"""
        return self.G.edges
    
    @property
    def G(self):
        """returns the graph _G"""
        return self._G
    
    @classmethod
    def reachable_nodes_paths(cls, G, start, *, preferred=None):
        """
        find all reachable nodes on a graph ``G``, starting from ``start``

        :G:             symmetric ``networkx`` graph (``G=nx.Graph()``)
        :start:         node on ``G``
        :preferred:     list of nodes to prefer when multiple paths are available
        :returns:       dictionary of nodes and paths, distance from ``start`` as key (1)
        
        USAGE
        :: 
        
            G=nx.Graph()
            G.add_edges_from([...])
            result = GraphBase.reachable_nodes_paths(G, start)
            
        NOTE 1. The return format is as follows
        
        ::

            result = {
                1: [
                        (node11, [path-to-node11]), 
                        (node12, [path-to-node12]), 
                        ...
                    ],
                2: [
                        (node21, [path-to-node21]), 
                        (node22, [path-to-node22]), ...
                    ],
                ...
            }
            
            [path-to-node11] = [start, node11]
            [path-to-node21] = [start, node1x, node21]
            ...
        """
        paths = {start: [start]}        # keeps track of the paths for reaching a node
        levels = {start: 0}             # keeps track of the level for each  node
        visited = {start}               # keeps track of nodes already visited

        # current_level_nodes are the one we search from
        current_level_nodes = [start]

        result = {}
        level = 1

        # iterate over the levels (=closest distance from start_node)
        while current_level_nodes:

            # next_level_nodes are the ones we find in this iteration
            next_level_nodes = []

            # go through all the nodes in this search...
            for node in current_level_nodes:

                # ...and identify all of their neighbors
                for node_found in cls.successors(G, node, sorted=True, preferred=preferred):

                    # if we haven't been there before
                    if node_found not in visited:

                        # remember level and path
                        levels[node_found] = level
                        paths[node_found] = paths[node] + [node_found]
                        
                        # remember the node for the next iteration
                        next_level_nodes.append(node_found)

                        # add `(node, path-to-node)` to the result
                        try:
                            result[level].append((node_found, paths[node_found]))
                        except KeyError:
                            result[level] = [((node_found, paths[node_found]))]
                        
                        # finally remember that we've seen that node
                        visited.add(node_found)

            # prepare for the next iteration
            current_level_nodes = next_level_nodes
            level += 1

        return result
    
    @classmethod
    def digest(cls, reachable_info):
        """
        digest the info obtained from ``reachable_nodes_paths``

        :reachable_info:    the result of the call to ``reachable_nodes_paths``
        :return`:           a ``tuple`` with ``{level: #nodes at level}`` and total items reached
        """
        digest = {k:len(v) for k,v in reachable_info.items()}
        return digest, sum(digest.values())
    
    @classmethod
    def successors(cls, G, node, sorted=True, reverse=False, preferred=None):
        """
        find the successors (1) of a node on a directed or undirected graph
        
        :G:         ``networkx`` graph (``G=nx.DiGraph()`` or ``G=nx.Graph()``)
        :node:      node on ``G``
        :sorted:    boolean, whether to sort the result
        :reverse:   boolean, whether to sort in reverse order
        :preferred: list of nodes to prefer when multiple paths are available
        :returns:   list of successors
        
        NOTE 1. For the purpose of this function, undirected graphs are treated 
        as directed graphs with two edges between each pair of nodes, and therefore
        ``neighbors`` and ``successors`` are equivalent
        """
        if isinstance(G, nx.DiGraph):
            successors = list(G.successors(node))
        elif isinstance(G, nx.Graph):
            successors = list(G.neighbors(node))
        else:
            raise ValueError("unsupported graph type", G, type(G))
        if preferred:
            successorsp = [n for n in preferred if n in successors]
            successors  = [n for n in successors if not n in successorsp]
        else:
            successorsp = []
        if sorted:
            successors.sort(reverse=reverse)
        return successorsp + successors
    
    @classmethod
    def find_circuits_of_length(cls, G, start, length, *, preferred=None):
        """
        find circuits (1) of a given length starting from a given node
        
        :G:         symmetric ``networkx`` graph (``G=nx.Graph()``)
        :start:     node on ``G``, the starting point
        :length:    integer, the length of the paths to find (1-2-1 is length 3)
        :preferred: list of nodes to prefer when multiple paths are available
        :returns:   list of paths
        
        NOTE 1. A circuit is a closed path the does not double back, ie a path that 
        starts and ends at the same node and that visits no node more than once
        """
        def dfs(current_path):
            if len(current_path) == length:
                if current_path[-1] == start:
                    paths.append(current_path)
                return
            
            current_node = current_path[-1]
            for successor in cls.successors(G, current_node, sorted=True, preferred=preferred):
                if successor not in current_path or (successor == start and len(current_path) == length - 1):
                    dfs(current_path + [successor])
        
        paths = []
        dfs([start])
        return paths
    
    PLOT_DEFAULTS = {
        "labels": True,
        "edge_labels": False,
        "node_color": "lightblue",
        "node_size": 30,
        "show": True,
        "font_size": 12,
        "font_color": "k",
    }
    
    
    class LT(Enum):
        """
        list of graph layouts for plotting(``enum``)
        
        see https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pydot.graphviz_layout.html
        """
        KAMADA_KAWAI = 1
        SPRING = 2
        #GRAPHVIZ = 3
        #PYDOT = 4
        BIPARTITE = 5
        #BFS = 6
        CIRCULAR = 7
        PLANAR = 8
        RANDOM = 9
        RESCALE = 10
        SHELL = 11
        SPECTRAL = 12
        SPIRAL = 13
        MULTIPARTITE = 14
        
    LAYOUTS = {
        LT.KAMADA_KAWAI: nx.kamada_kawai_layout,
        LT.SPRING: nx.spring_layout,
        #LT.GRAPHVIZ: nx.graphviz_layout,
        #LT.PYDOT: nx.pydot_layout,
        LT.BIPARTITE: nx.bipartite_layout,
        #LT.BFS: nx.bfs_layout,
        LT.CIRCULAR: nx.circular_layout,
        LT.PLANAR: nx.planar_layout,
        LT.RANDOM: nx.random_layout,
        LT.RESCALE: nx.rescale_layout,
        LT.SHELL: nx.shell_layout,
        LT.SPECTRAL: nx.spectral_layout,
        LT.SPIRAL: nx.spiral_layout,
        LT.MULTIPARTITE: nx.multipartite_layout,
    }

    def plot(self, *, layout=None, **params):
        """
        plot the graph
        
        :layout:        layout for the plot (default: ``LT.KAMADA_KAWAI``)
        :labels:        if ``True`` (default), plot node labels
        :edge_labels:   if ``True`` (default), plot edge labels
        :node_color:    node color (default: ``lightblue``)
        :node_size:     node size (default: ``20``)
        :font_size:     font size (default: ``12``)
        :font_color:    font color (default: ``k``)
        :show:          if ``True`` (default), ``plt.show`` the plot
        """
        return self.plot_(self.G, layout=layout, **params)
    
    @classmethod
    def plot_(cls, G, *, layout=None, **params):
        """
        plot the graph (see ``plot`` for details)
        
        NOTE. ``plot_`` is implemented as classmethod to allow for standalone use;
        for convenience, ``plot`` will usually be used
        """
        p = lambda name: params.get(name, cls.PLOT_DEFAULTS.get(name))
        layout = layout or cls.LT.KAMADA_KAWAI
        pos = cls.LAYOUTS[layout](G)
        #print(pos)
        nx.draw(
            G,
            pos,
            with_labels=p("labels"),
            labels=nx.get_node_attributes(G, "label"),
            node_color=p("node_color"),
            node_size=p("node_size"),
            font_size=p("font_size"),
            font_color=p("font_color"),
        )
        if p("edge_labels"):
            edge_labels = nx.get_edge_attributes(G, "label")
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        if p("show"):
            plt.show()

        
    @classmethod
    def _(cls):
        """
        can be used as terminator for function that otherwise return ``self``
        """
        pass
    
    def reachable(self, start, *, raw=False, preferred=None):
        """
        returns the reachable nodes from ``start``
        
        :start:         node on the graph ``self.G``; the starting point
        :raw:           if True, returns the raw result of ``reachable_nodes_paths``
        :preferred:     list of nodes to prefer when walking the graph
        :returns:       a ``dic`` ``{node: path-to-node}``
        """
        reachable =  self.reachable_nodes_paths(self.G, start)
        if raw: return reachable
        reachable = list(reachable.values())
        reachable = [item for sublist in reachable for item in sublist]
        return {r[0]: r[1] for r in reachable}
    
    def circuits(self, start, length, *, path_format=None):
        """
        returns the circuits (closed paths) from ``start`` of a given length
        
        :start:     node on the graph; the starting point
        :length:    int; the length of the circuits to look for (1-2-3-1 is length 3)
        :returns:   list of paths
        """
        paths = self.find_circuits_of_length(self.G, start, length+1)
        paths = [self._path_format(p, path_format=path_format) for p in paths]
        return paths
    
    def circuits3(self, start, *, path_format=None):
        """
        returns the triangles (closed paths of length 3) from ``start``
        
        :start:     node on the graph; the starting point
        :returns:   list of paths
        """
        return self.circuits(start, 3, path_format=path_format)
    triangles = circuits3
    
    def circuits2(self, start, *, path_format=None):
        """
        returns the (circle) pairs (closed paths of length 2) from ``start``
        
        :start:     node on the graph; the starting point
        :returns:   list of paths
        """
        return self.circuits(start, 2, path_format=path_format)
    
    @staticmethod
    def path2edges(path):
        """
        returns the edges of a path
        
        :path:          iterable of nodes
        :returns:       list of edges
        
        EXAMPLE
        ::
        
            [1, 2, 3] -> [(1, 2), (2, 3)]
        """
        return list(zip(path, path[1:]))
    p2e = path2edges
    
    @staticmethod
    def touchpoints(edges):
        """
        returns the touchpoints of a node
        
        :edges:     iterable of edges
        :returns:   list of touchpoints
        
        ::

            [(1, 2), (2, 3), (3, 4), (5, 6)] -> [(2, 2), (3, 3), (4, 5)]
        """
        return [(a[1], b[0]) for a, b in zip(edges, edges[1:])]
    
    @classmethod
    def is_contiguous(cls, edges):
        """
        returns whether the edges are contiguous
        
        :edges:     iterable of edges
        :returns:   bool
        """
        return all(a[1] == b[0] for a, b in zip(edges, edges[1:]))
    
    @classmethod
    def edges2path(cls, edges):
        """
        returns the path of edges
        
        :edges:     iterable of edges
        :returns:   list of nodes (raises ``ValueError`` if not contiguous)
        """
        if not cls.is_contiguous(edges):
            raise ValueError("edges are not contiguous", edges)
        return [edges[0][0]] + [b for _, b in edges]
    
    def _build_graph(self):
        """(re)builds the graph"""
        self._G = type(self._G)()
            # clear the graph and recreate one of the same type
        self._G.add_edges_from(self._create_edges())
        
    def _create_edges(self):
        """
        creates and returns the edges of the graph
        
        NOTE. This method should be implemented in the derived class and return a list 
        of edges. This method is called by ``_build_graph`` to create the graph.
        """
        return []
    
    class PF(Enum):
        """
        path format for the graph
        """
        NODES = 1
        EDGES = 2

    @classmethod
    def _path_format(cls, path, *, path_format):
        """
        formats a path
        
        :path:          the path, in ``list of nodes`` format
        :path_format:   one of the ``PF`` enums (1)
        
        NOTE 1. The following formats are available
        ===================  ====================================================
        ``PF.NODES``         ``list`` of nodes (eg [1, 2, 3])
        ``PF.EDGES``         ``list`` of edges (eg [(1, 2), (2, 3)])
        ===================  ====================================================
        """
        path_format = path_format or cls.PF.NODES
        if path_format == cls.PF.NODES:
            return path
        elif path_format == cls.PF.EDGES:
            return cls.path2edges(path)
        else:
            raise ValueError("unsupported path format", path_format)
    
        





