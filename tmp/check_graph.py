import os
import sys
from dotenv import load_dotenv

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from app.config import Config
from app.services.graph_builder import GraphBuilderService

def check_graph(graph_id):
    load_dotenv()
    api_key = os.environ.get('ZEP_API_KEY')
    if not api_key:
        print("ZEP_API_KEY not found in .env")
        return

    builder = GraphBuilderService(api_key=api_key)
    try:
        print(f"Fetching data for graph: {graph_id}")
        data = builder.get_graph_data(graph_id)
        print(f"Node count: {data.get('node_count')}")
        print(f"Edge count: {data.get('edge_count')}")
        if data.get('node_count') > 0:
            print("First 5 nodes:")
            for node in data.get('nodes', [])[:5]:
                print(f"  - {node.get('name')} ({node.get('labels')})")
        if data.get('edge_count') > 0:
            print("First 5 edges:")
            for edge in data.get('edges', [])[:5]:
                print(f"  - {edge.get('source_node_name')} -> {edge.get('target_node_name')} ({edge.get('name')})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # From meta.json of report_aed95c7dfa7f
    graph_id = "mirofish_b0bbbe603bd448c5"
    check_graph(graph_id)
