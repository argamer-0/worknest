with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Inject qualification tasks script if missing
if "test_batch.js" not in content:
    content = content.replace("</head>", '<script src="test_batch.js"></script>\n</head>')

# Update Task UI with Evaluation Mode & Coming Soon Banner
badge_snippet = '''
<div style="background:rgba(234,179,8,0.15); border:1px solid #eab308; border-radius:10px; padding:12px; margin-bottom:15px; text-align:center;">
  <span style="color:#fde047; font-weight:700; font-size:14px;">🎯 WORKER SKILL QUALIFICATION (20 TASKS)</span>
  <p style="color:#94a3b8; font-size:12px; margin:4px 0 0 0;">Har audio sunkar sahi ya galat chuniye. Galti hone par turant feedback milega.</p>
</div>
'''

content = content.replace('<!-- TASK_CONTAINER_START -->', '<!-- TASK_CONTAINER_START -->\n' + badge_snippet)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
