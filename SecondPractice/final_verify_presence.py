import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

content = "".join([str(c['source']) for c in nb['cells']])

print(f"Auto Report Found: {'Strategic Car Price Analysis' in content}")
print(f"Wine Report Found: {'Chemical Signatures of Wine Quality' in content}")
print(f"Infographic 3 Reference: {'unnamed (3).png' in content}")
print(f"Infographic 4 Reference: {'unnamed (4).png' in content}")
print(f"Wine Prompt Fragment: {'Decanting Data' in content}")
