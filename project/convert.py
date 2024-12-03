import os
import sys
import re

# 定义要删除的字符串列表
strings_to_remove = [
    '<script src="/livereload.js?mindelay=10&amp;v=2&amp;port=1313&amp;path=livereload" data-no-instant defer></script>',
    '<link rel="stylesheet" href="http://localhost:1313//css/biaslab-font.css">',
    '<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Lato:100,300,400,700|Merriweather:100,400,700|Roboto+Mono">',
    '<script src="//cdnjs.cloudflare.com/ajax/libs/gsap/1.18.4/TweenMax.min.js"></script>'
]

# 检查参数是否正确传递
if len(sys.argv) != 2:
    print("Usage: python script.py <input_file_directory>")
    sys.exit(1)

input_file_directory = sys.argv[1]

# 确保文件路径存在
if not os.path.exists(input_file_directory):
    print(f"Error: The directory {input_file_directory} does not exist.")
    sys.exit(1)

# 获取文件列表
files = [f for f in os.listdir(input_file_directory) if os.path.isfile(os.path.join(input_file_directory, f))]

# 获取public目录的路径
public_dir = os.path.abspath(input_file_directory)
while public_dir != os.path.abspath(os.sep):
    if os.path.basename(public_dir) == 'public':
        break
    public_dir = os.path.dirname(public_dir)

# 如果没有找到public目录，则退出
if public_dir == os.path.abspath(os.sep):
    print("Error: No 'public' directory found in the path hierarchy.")
    sys.exit(1)

# 计算从当前目录到public目录的相对路径
relative_path_to_public = os.path.relpath(public_dir, input_file_directory)

# 对每个文件进行处理
for file_name in files:
    file_path = os.path.join(input_file_directory, file_name)
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        
        # 删除指定的字符串
        for string in strings_to_remove:
            content = content.replace(string, '')
        
        # 替换http://localhost:1313为相对路径到public目录
        content = content.replace('http://localhost:1313', relative_path_to_public)
        
        content = content.replace('<script src="//cdnjs.cloudflare.com/ajax/libs/gsap/latest/plugins/ScrollToPlugin.min.js"></script>', '<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.4.2/ScrollToPlugin.min.js"></script>')
        
        # 替换/#{input}s"为/{input}/index.html"
        content = re.sub(r'\/#{(\w+)}s"', r'/{\1}/index.html"', content)
        
        # 将修改后的内容写回文件
        file.seek(0)
        file.write(content)
        file.truncate()  # 清除文件中的剩余旧内容

print("File processing complete.")
