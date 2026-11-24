# pairwise-pso-cache-warmup

## 领域

游戏、图形与多媒体

## 主题

管线状态缓存预热

## 说明

异步预热、规范化变体键与代际校验。

初始状态下 `graphics/pso_cache_warmup.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
