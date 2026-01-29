# PromptOps 平台

PromptOps 是一个基于 Qoder 配置驱动的提示词管理和优化平台，采用技能驱动开发（Skills-Driven Development）模式，提供模板管理、A/B测试、提示词优化和用户反馈收集等功能。

## 项目架构

本项目采用模块化架构设计，主要包括以下组件：

### 1. Context Engine（上下文引擎模块）
- **功能**：模板管理和 A/B 测试
- **主要能力**：
  - 提示词模板的 CRUD 操作
  - A/B 测试框架
  - 上下文模板优化
- **API 端点**：
  - `GET /templates` - 列出所有模板
  - `POST /templates` - 创建新模板
  - `GET /templates/{id}` - 获取特定模板
  - `PUT /templates/{id}` - 更新模板
  - `DELETE /templates/{id}` - 删除模板
  - `POST /ab-test` - 运行 A/B 测试
  - `POST /optimize-context` - 优化上下文处理

### 2. Smart Rewriter（智能重写模块）
- **功能**：提示词优化和用户反馈收集
- **主要能力**：
  - 基于 AI 的提示词优化
  - 用户投票和反馈系统
  - 性能跟踪和分析
- **API 端点**：
  - `POST /optimize` - 生成优化提示词
  - `POST /votes` - 提交用户反馈
  - `GET /analytics` - 获取优化分析数据

### 3. API 层
- 基于 Flask 的 REST API 接口
- 提供完整的 Web 服务功能

### 4. Admin 界面
- 基于 Flask-Admin 的管理后台
- 提供可视化管理界面

## 核心概念

### 技能驱动开发（Skills-Driven Development）
项目采用技能驱动开发模式，将核心业务逻辑封装为独立的"技能"（Skills），具有以下优势：

- **模块化**：每个技能负责特定的业务功能
- **可复用**：技能可以在不同模块间共享使用
- **易维护**：独立的技能便于单独测试和维护
- **可扩展**：轻松添加新的技能而不影响现有功能

### 配置驱动架构
通过 `qoder.config.yaml` 配置文件驱动整个项目的结构和功能：

```yaml
project_name: promptops
language: python
target_dir: ./src
database:
  type: sqlite
  path: promptops.db
  schema_file: ./static/schema.sql

modules:
  - name: sdk.context_engine
    spec: specs/context_engine.spec
    skills:
      - manage_templates
      - run_ab_test

  - name: sdk.smart_rewriter
    spec: specs/smart_rewriter.spec
    skills:
      - generate_optimization
      - collect_votes

  - name: api.routes
    depends_on: [sdk.context_engine, sdk.smart_rewriter]
    generate: rest_api

  - name: admin.views
    depends_on: [sdk.context_engine, sdk.smart_rewriter]
    generate: flask_admin_templates
```

## 数据模型

### 主要表结构
- `templates` - 存储提示词模板
- `template_versions` - 模板版本历史
- `ab_tests` - A/B 测试记录
- `evaluation_logs` - 评估日志
- `prompts` - 原始提示词
- `optimized_prompts` - 优化后的提示词
- `user_votes` - 用户投票数据

## 快速开始

### 环境要求
- Python 3.8+
- pip

### 安装依赖
```bash
pip install -r requirements.txt
```

### 初始化数据库
```bash
python -c "from src.main import initialize_database; initialize_database()"
```

### 运行测试
```bash
python test_platform.py
```

### 启动服务
```bash
# 启动 API 服务
python src/api/routes.py

# 启动管理界面
python src/admin/views.py
```

## 测试

项目包含多个测试文件：
- `test_platform.py` - 平台整体功能测试
- `test_context_engine.py` - Context Engine 模块测试
- `test_smart_rewriter.py` - Smart Rewriter 模块测试

## 技术栈

- **后端**: Python, Flask
- **数据库**: SQLite
- **管理界面**: Flask-Admin
- **ORM**: SQLAlchemy
- **配置管理**: YAML

## 项目结构

```
promptops/
├── qoder.config.yaml      # 项目配置文件
├── requirements.txt       # 依赖包列表
├── specs/                # 规范文件
│   ├── context_engine.spec    # 上下文引擎规范
│   └── smart_rewriter.spec    # 智能重写器规范
├── static/               # 静态资源
│   └── schema.sql        # 数据库模式
├── src/                  # 源代码
│   ├── __init__.py
│   ├── sdk/              # SDK模块
│   │   ├── __init__.py
│   │   ├── context_engine/   # 上下文引擎
│   │   │   └── __init__.py
│   │   └── smart_rewriter/   # 智能重写器
│   │       └── __init__.py
│   ├── api/              # API模块
│   │   └── routes.py     # REST API路由
│   ├── admin/            # 管理界面
│   │   └── views.py      # 管理界面视图
│   ├── skills/           # 技能模块
│   │   ├── __init__.py
│   │   ├── manage_templates.py    # 模板管理技能
│   │   ├── run_ab_test.py         # A/B测试技能
│   │   ├── generate_optimization.py # 优化生成技能
│   │   └── collect_votes.py       # 投票收集技能
│   └── main.py           # 主程序入口
├── test_platform.py      # 平台测试
├── test_context_engine.py # Context Engine 测试
├── test_smart_rewriter.py # Smart Rewriter 测试
└── promptops.db          # SQLite数据库文件
```

## 许可证

MIT License