from amisui.config import Config

Config.cdn = "https://unpkg.com"

from amisui.components import Page

page = Page(title='新页面', body='Hello World')
# 输出为python字典
print(page.to_dict())
# 输出为json
print(page.to_json())
# 输出为str
print(page.render())
# 保存为html文件
with open('HelloWorld.html', 'w', encoding='utf-8') as f:
    f.write(page.render())