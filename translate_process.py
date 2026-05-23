import os

vue_path = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\views\Process.vue"

translations = {
    "图谱构建": "Graph Building",
    "图谱": "Graph",
    "双栏": "Split View",
    "工作台": "Workbench",
    "实时知识图谱": "Real-time Knowledge Graph",
    "节点": "Nodes",
    "关系": "Relationships",
    "刷新图谱": "Refresh Graph",
    "退出全屏": "Exit Fullscreen",
    "全屏显示": "Fullscreen",
    "实时更新中...": "Updating real-time...",
    "图谱数据加载中...": "Loading graph data...",
    "等待本体生成": "Waiting for Ontology Generation",
    "生成完成后将自动开始构建图谱": "Graph building will automatically start once generation is complete",
    "图谱构建中": "Graph Building in Progress",
    "数据即将显示...": "Data will be displayed soon...",
    "构建流程": "Build Process",
    "本体生成": "Ontology Generation",
    "接口说明": "API Description",
    "上传文档后，LLM分析文档内容，自动生成适合舆论模拟的本体结构（实体类型 + 关系类型）": "After uploading documents, LLM analyzes the content and automatically generates an ontology structure suitable for public opinion simulation (Entity types + Relationship types)",
    "生成进度": "Generation Progress",
    "生成的实体类型": "Generated Entity Types",
    "生成的关系类型": "Generated Relationship Types",
    "更多关系...": "More relationships...",
    "等待本体生成...": "Waiting for ontology generation...",
    "基于生成的本体，将文档分块后调用 Zep API 构建知识图谱，提取实体和关系": "Based on the generated ontology, the document is chunked and Zep API is called to build knowledge graph, extracting entities and relationships",
    "等待本体生成完成...": "Waiting for ontology generation to complete...",
    "构建进度": "Build Progress",
    "构建结果": "Build Result",
    "实体节点": "Entity Nodes",
    "关系边": "Relationship Edges",
    "实体类型": "Entity Types",
    "构建完成": "Build Complete",
    "准备进入下一步骤": "Ready to go to the next step",
    "已完成": "Completed",
    "进行中": "In Progress",
    "等待中": "Waiting",
    "进入环境搭建": "Enter Environment Setup",
    "项目信息": "Project Information",
    "项目名称": "Project Name",
    "项目ID": "Project ID",
    "图谱ID": "Graph ID",
    "模拟需求": "Simulation Req",
    "没有待处理的模拟需求，请返回首页重新操作": "No pending simulation requirements, please return to home page and try again",
    "正在分析需求并生成本体...": "Analyzing requirements and generating ontology...",
    "本体生成失败": "Ontology Generation Failed",
    "项目初始化失败:": "Project initialization failed:",
    "加载项目失败": "Failed to load project",
    "图谱正在构建中，请勿重复提交。如需强制重建，请添加 force: true": "Graph is currently building, please do not resubmit. To force rebuild, add force: true",
    "项目尚未生成本体，请先调用 /ontology/generate": "Project has not generated ontology yet, please call /ontology/generate first",
    "未找到提取的文本内容": "Extract text content not found",
    "未找到本体定义": "Ontology definition not found",
    "构建失败": "Build Failed",
    "正在启动图谱构建...": "Starting graph building...",
    "图谱构建任务已启动...": "Graph building task started...",
    "启动图谱构建失败": "Failed to start graph building",
    "处理中...": "Processing...",
    "图谱构建完成": "Graph Build Complete",
    "正在上传文件并分析文档...": "Uploading and analyzing documents...",
    "环境搭建功能开发中...": "Environment setup feature in development...",
    "没有待上传的文件，请返回首页重新操作": "No pending files found, please return to home to restart process"
}

with open(vue_path, 'r', encoding='utf-8') as f:
    content = f.read()

for zh, en in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
    content = content.replace(zh, en)

with open(vue_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Translated {vue_path}")
