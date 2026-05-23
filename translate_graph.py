import os

graph_panel = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\components\GraphPanel.vue"
step1 = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\components\Step1GraphBuild.vue"

def translate_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for zh, en in replacements.items():
        content = content.replace(zh, en)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated {path}")

graph_replacements = {
    "实时知识图谱": "Real-time Knowledge Graph",
    "节点": "Nodes",
    "关系": "Relationships",
    "刷新图谱": "Refresh Graph",
    "退出全屏": "Exit Fullscreen",
    "全屏显示": "Fullscreen",
    "实时更新中...": "Updating in real-time...",
    "图谱数据加载中...": "Loading graph data...",
    "等待本体生成": "Waiting for Ontology Generation",
    "生成完成后将自动开始构建图谱": "Graph building starts after generation",
    "图谱构建中": "Building Graph",
    "数据即将显示...": "Data will be displayed here...",
    "等待本体生成...": "Waiting for ontology generation..."
}

step1_extra = {
    "进入环境搭建": "Enter Environment Setup"
}

translate_file(graph_panel, graph_replacements)
translate_file(step1, step1_extra)
