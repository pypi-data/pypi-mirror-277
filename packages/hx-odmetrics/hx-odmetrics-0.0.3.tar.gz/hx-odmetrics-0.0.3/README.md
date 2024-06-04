
# ODMetrics Package by Haokun Zhang <haokun.zhang@hirain.com>

## 版本发布与迭代
* 版本上线 0.0.2 (2024-06-03)
* 版本简要：降级scipy的版本最低要求适配服务器
* 使用方法: 暂时同步到飞书文档中 [多目标跟踪评测工具: OD](https://zvnz49xxfzh.feishu.cn/docx/LiatdZ9kHojAXuxXP10cD9m8nse?from=from_copylink)


## 安装方式 
via PyPI
```bash
    # 直接安装
    pip install --trusted-host 218.98.160.70 \
    --extra-index-url http://218.98.160.70:30722/simple \
    hx-odmetrics

    # alternative image source 安装
    pip install --trusted-host 218.98.160.70 \
    --extra-index-url http://218.98.160.70:30722/simple \
    hx-odmetrics -U -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 安装时问题：
* 跳出警告(ERROR):
```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
cyber-record 0.1.12 requires protobuf<=3.19.4; python_version >= "3.7", but you have protobuf 3.20.3 which is incompatible.
```
这是由于`cyber-record`要求`protobuf`的版本小于等于3.19.4，(而现在的protobuf版本major已经达到了5)，这可能会在您的安装过程中过处错误，然而更高的版本仍然不会与`cyber-record`冲突，这也不会在您使用的过程中造成影响(除非您的环境中有其他的第三方库对`protobuf`有着不一样的要求)，因此请暂时忽略。

