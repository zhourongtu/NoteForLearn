
自动生成脚本
- 实际上：在对应路径创建pip.ini文件
```python
import os
import pathlib
from os.path import join, exists

pip_path = join(pathlib.Path.home(), "AppData", "Roaming", "pip")
pip_filename = join(pip_path, "pip.ini")
pip_text = "\n".join([
	"[global]", "timeout = 6000",
	"index-url = https://mirrors.aliyun.com/pypi/simple/",
	"trusted-host = mirrors.aliyun.com"
])

if not exists(pip_path):
	os.makedirs(pip_path)
	
with open(pip_filename, mode='w', encoding='utf8') as fp:
	fp.write(pip_text)

```

