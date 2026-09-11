# Daily Stock Analysis Enhanced 📈

基于原始 daily_stock_analysis 的深度改进版本，集成最新的AI、深度学习和量化投资理论。

## 🎯 核心改进

### Phase 1（已实现）
- ✅ Transformer Attention 时间序列分析
- ✅ 多因子评分系统（Smart Beta）
- ✅ VaR/CVaR 风险管理框架
- ✅ BERT 新闻情感分析
- ✅ 强化学习交易智能体（DQN）
- ✅ 高频回测引擎

### Phase 2（规划中）
- 🔄 CNN 图形模式识别
- 🔄 LSTM 集成预测器
- 🔄 GNN 相关性分析
- 🔄 投资组合优化器

## 📁 项目结构

```
daily_stock_analysis_enhanced/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ml_models/
│   │   │   ├── __init__.py
│   │   │   ├── transformer_analyzer.py      # Transformer注意力分析
│   │   │   ├── lstm_predictor.py            # LSTM时间序列预测
│   │   │   └── ensemble_model.py            # 集成学习模型
│   │   ├── factor_models/
│   │   │   ├── __init__.py
│   │   │   ├── value_factors.py             # 价值因子
│   │   │   ├── momentum_factors.py          # 动量因子
│   │   │   ├── quality_factors.py           # 质量因子
│   │   │   ├── growth_factors.py            # 成长因子
│   │   │   ├── sentiment_factors.py         # 情绪因子
│   │   │   └── multi_factor_scorer.py       # 多因子综合评分
│   │   ├── risk_management/
│   │   │   ├── __init__.py
│   │   │   ├── var_calculator.py            # VaR计算器
│   │   │   ├── cvar_calculator.py           # CVaR计算器
│   │   │   ├── stress_test.py               # 压力测试
│   │   │   ├── portfolio_optimizer.py       # 组合优化器
│   │   │   └── drawdown_analyzer.py         # 最大回撤分析
│   │   ├── multimodal_analysis/
│   │   │   ├── __init__.py
│   │   │   ├── news_sentiment_analyzer.py   # 新闻情感分析
│   │   │   └── fundamental_analyzer.py      # 基本面分析
│   │   ├── rl_trading/
│   │   │   ├── __init__.py
│   │   │   ├── dqn_agent.py                 # DQN交易智能体
│   │   │   ├── environment.py               # 交易环境
│   │   │   └── replay_buffer.py             # 经验回放
│   │   └── backtesting/
│   │       ├── __init__.py
│   │       ├── backtest_engine.py           # 回测引擎
│   │       └── performance_analyzer.py      # 性能分析
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py                   # 数据加载器
│   │   └── preprocessor.py                  # 数据预处理
│   └── utils/
│       ├── __init__.py
│       ├── config.py                        # 配置管理
│       ├── logger.py                        # 日志工具
│       └── metrics.py                       # 评估指标
├── tests/
│   ├── __init__.py
│   ├── test_transformer.py
│   ├── test_factor_models.py
│   ├── test_risk_management.py
│   └── test_rl_agent.py
└── examples/
    ├── 01_transformer_analysis.py
    ├── 02_factor_scoring.py
    ├── 03_risk_analysis.py
    ├── 04_sentiment_analysis.py
    └── 05_rl_trading.py
```

## 🚀 快速开始

### 安装依赖

```bash
git clone https://github.com/jacksonmaner/daily_stock_analysis_enhanced.git
cd daily_stock_analysis_enhanced
pip install -r requirements.txt
```

### 基础使用

```python
from src.core.ml_models.transformer_analyzer import StockTransformerAnalyzer
from src.core.factor_models.multi_factor_scorer import MultiFactorScorer
from src.core.risk_management.var_calculator import VaRCalculator

# 1. Transformer分析
analyzer = StockTransformerAnalyzer()
result = analyzer.analyze(stock_code='600519')

# 2. 多因子评分
scorer = MultiFactorScorer()
score = scorer.score_stock('600519')

# 3. 风险评估
var_calc = VaRCalculator()
risk = var_calc.calculate('600519')
```

## 📚 文档

- [使用指南](docs/USAGE.md)
- [API文档](docs/API.md)
- [开发指南](docs/DEVELOPMENT.md)

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 License

MIT License
