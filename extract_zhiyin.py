# 运行方法: python extract_zhiyin.py
import os
import re

INPUT_FILE = 'zhiyinsuanming_complete_english.txt'

# 映射关系 "TXT中的文件头" -> "目标文件路径"
output_map = {
    '_config.yml': '_config.yml',
    'app.py': 'app.py',
    'DEPLOY.txt': 'DEPLOY.txt',
    'index.html': 'index.html',
    'README.md': 'README.md',
    'README_GITHUB.md': 'README_GITHUB.md',
    'requirements.txt': 'requirements.txt',
    'verify.py': 'verify.py',
    'static/css/style.css': os.path.join('static', 'css', 'style.css'),
    'templates/index.html': os.path.join('templates', 'index.html'),
    'templates/layout.html': os.path.join('templates', 'layout.html'),
}

# 读取源文件
with open(INPUT_FILE, encoding='utf-8') as f:
    raw = f.read()

# 正则分割各个文件
file_blocks = re.findall(
    r'={80,}\nFILE: (.*?)\n={80,}\n\n`?\$extension\n(.*?)\n`?\n',
    raw, re.S)

created = []

for block in file_blocks:
    filekey, content = block
    target = output_map.get(filekey.strip())
    if not target:
        continue
    d = os.path.dirname(target)
    if d and not os.path.exists(d):
        os.makedirs(d)
    with open(target, 'w', encoding='utf-8') as of:
        of.write(content.strip() + '\n')
    created.append(target)

print('✅ 以下文件已自动生成：')
for f in created:
    print('  -', f)

print('\n下一步：')
print('1. 在这个目录打开命令行，输入：')
print('     git add .')
print('     git commit -m "init: all website files"')
print('2. 将你的本地仓库与GitHub远程仓库关联（只需执行一次，URL请替换成你自己的）：')
print('     git remote add origin https://github.com/你的用户名/zhiyingsuanming.git')
print('   （如果已经有关联，无需重复这步）')
print('3. 推送到 GitHub：')
print('     git push origin main')
print('4. 去 GitHub 网站设置 Settings > Pages，启用 Pages，选择 main 分支 /，等几分钟，')
print('5. 访问你的网址：https://你的用户名.github.io/zhiyingsuanming/')