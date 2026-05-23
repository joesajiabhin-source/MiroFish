import os

main_view = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\views\MainView.vue"
step1 = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\components\Step1GraphBuild.vue"

def translate_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for zh, en in replacements.items():
        content = content.replace(zh, en)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated {path}")

main_replacements = {
    "图谱构建": "Graph Building",
    "环境搭建": "Environment Setup",
    "开始模拟": "Start Simulation",
    "报告生成": "Report Generation",
    "深度互动": "Deep Interaction",
    "{ graph: '图谱', split: '双栏', workbench: '工作台' }": "{ graph: 'Graph', split: 'Dual Column', workbench: 'Workbench' }",
    "进入 Step": "Entering Step",
    "返回 Step": "Returning to Step",
    "自定义模拟轮数:": "Custom simulation rounds:"
}

step1_replacements = {
    "图谱构建": "Graph Building",
    "本体生成": "Ontology Generation",
    "LLM分析文档内容与模拟需求，提取出现实种子，自动生成合适的本体结构": "LLM analyzes document content and simulation requirements to extract reality seeds and auto-generate suitable ontology structure",
    "GraphRAG构建": "GraphRAG Build",
    "基于生成的本体，将文档自动分块后调用 Zep 构建知识图谱，提取实体和关系，并形成时序记忆与社区摘要": "Based on generated ontology, automatically chunk document and call Zep to build knowledge graph, extracting entities/relations, and form sequential memory and community summaries",
    "实体节点": "Entity Nodes",
    "关系边": "Relationship Edges",
    "SCHEMA类型": "SCHEMA Types",
    "构建完成": "Build Complete",
    "图谱构建已完成，请进入下一步进行模拟环境搭建": "Graph building complete, please proceed to next step for simulation environment setup",
    "等待": "Wait",
    "进行中": "In Progress",
    "完成": "Complete",
    "失败": "Failed"
}

translate_file(main_view, main_replacements)
translate_file(step1, step1_replacements)
