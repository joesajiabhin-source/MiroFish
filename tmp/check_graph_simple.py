import os
import sys
from dotenv import load_dotenv
from zep_cloud.client import Zep

def fetch_all_nodes(client, graph_id):
    nodes = []
    limit = 100
    cursor = None
    while True:
        try:
            kwargs = {"limit": limit}
            if cursor:
                kwargs["uuid_cursor"] = cursor
            res = client.graph.node.get_by_graph_id(graph_id, **kwargs)
            if not res:
                break
            nodes.extend(res)
            if len(res) < limit:
                break
            cursor = getattr(res[-1], "uuid_", None) or getattr(res[-1], "uuid", None)
            if not cursor:
                break
        except Exception as e:
            print(f"Error fetching nodes: {e}")
            break
    return nodes

def fetch_all_edges(client, graph_id):
    edges = []
    limit = 100
    cursor = None
    while True:
        try:
            kwargs = {"limit": limit}
            if cursor:
                kwargs["uuid_cursor"] = cursor
            res = client.graph.edge.get_by_graph_id(graph_id, **kwargs)
            if not res:
                break
            edges.extend(res)
            if len(res) < limit:
                break
            cursor = getattr(res[-1], "uuid_", None) or getattr(res[-1], "uuid", None)
            if not cursor:
                break
        except Exception as e:
            print(f"Error fetching edges: {e}")
            break
    return edges

def check_graph(graph_id):
    load_dotenv()
    api_key = os.environ.get('ZEP_API_KEY')
    if not api_key:
        print("ZEP_API_KEY not found in .env")
        return

    client = Zep(api_key=api_key)
    try:
        print(f"Fetching data for graph: {graph_id}")
        nodes = fetch_all_nodes(client, graph_id)
        edges = fetch_all_edges(client, graph_id)
        print(f"Node count: {len(nodes)}")
        print(f"Edge count: {len(edges)}")
        if len(nodes) > 0:
            for node in nodes[:5]:
                print(f"  - Node: {node.name}")
        if len(edges) > 0:
            for edge in edges[:5]:
                print(f"  - Edge: {edge.source_node_uuid} -> {edge.target_node_uuid} ({edge.name})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_graph("mirofish_b0bbbe603bd448c5")
