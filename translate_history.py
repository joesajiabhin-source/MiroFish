import os

history_path = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\components\HistoryDatabase.vue"

translations = {
    "推演记录": "Simulation History",
    "图谱构建": "Graph Building",
    "环境搭建": "Environment Setup",
    "分析报告": "Analysis Report",
    "个文件": " files",
    "暂无文件": "No files",
    "加载中...": "Loading...",
    "'无'": "'None'",
    "模拟需求": "Simulation Req.",
    "关联文件": "Related Files",
    "暂无关联文件": "No related files",
    "推演回放": "Simulation Playback",
    "Step3「开始模拟」与 Step5「深度互动」需在运行中启动，不支持历史回放": "Step 3 (Start Simulation) and Step 5 (Deep Interaction) require execution and do not support historical playback",
    "未命名模拟": "Unnamed Simulation",
    "未开始": "Not Started",
    "已完成": "Completed",
    "进行中": "In Progress",
    "未知文件": "Unknown file",
    "加载历史项目失败:": "Failed to load history:",
    " 轮\"": " Rounds\"",
    " 轮'": " Rounds'"
}

with open(history_path, 'r', encoding='utf-8') as f:
    content = f.read()

for zh, en in translations.items():
    content = content.replace(zh, en)

with open(history_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Translated {history_path}")
