# general-project-template

```bash
.
├── README.md
├── checkpoints
│   └── about.md
├── config
│   ├── __init__.py
│   └── yml
│       ├── default.yml
│       └── local.yml
├── data
│   └── about.md
├── log
│   └── about.md
├── main.py
├── models
│   └── __init__.py
├── src
│   └── __init__.py
└── utils
    └── __init__.py
```
一个通用项目模版，采用`.yml`文件做配置。
导入配置：`from config import config`

- checkpoints: 保存模型参数目录
- config: 项目配置
- data: 原始数据，数据集存放目录
- log: 日志文件
- main.py 主程序入口
- models: 模型Object
- src: 业务代码
- utils: 通用工具