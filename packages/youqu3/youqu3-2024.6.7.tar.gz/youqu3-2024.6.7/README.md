<p align="center">
  <a href="https://github.com/funny-dream/youqu3">
    <img src="./docs/assets/logo.png" width="100" alt="YouQu3">
  </a>
</p>
<p align="center">
    <em>YouQu3，下一代 Linux 自动化测试框架。</em>
</p>


# [YouQu3]()

YouQu3 是下一代 Linux 自动化测试框架，整体架构重新设计，全新的插件化及模块化功能，带来全新的使用效果。

[YouQu3架构设计](docs/YouQu3架构设计.md)

## [特性]()

- 支持离线部署
- 极致轻量化依赖
- 功能可插拔
- 可视化配置
- 支持非开发者下运行

## [安装]()

安装基础环境：

```shell
pip install youqu3
```

桌面 UI 自动化测试：

```shell
pip install youqu3[desktop-ui]
```

Web UI 自动化测试：

```shell
pip install youqu3[webui]
```

## [YouQu3 插件生态]()

| YouQu3 插件名称                                              | 说明                                 |
| ------------------------------------------------------------ | ------------------------------------ |
| [youqu-dogtail](https://github.com/funny-dream/youqu-dogtail) | 属性定位插件                         |
| [youqu-imagecenter-rpc](https://github.com/funny-dream/youqu-imagecenter-rpc) | 基于 RPC 服务的图像识别插件      |
| [youqu-mousekey](https://github.com/funny-dream/youqu-mousekey) | 键鼠操作插件                         |
| [pytest-youqu-playwright](https://github.com/funny-dream/pytest-youqu-playwright) | 基于 Playwright 的 Web UI 自动化插件 |
| [funnylog](https://linuxdeepin.github.io/funnylog/)          | 全自动日志插件                       |
| [pdocr-rpc](https://linuxdeepin.github.io/pdocr-rpc/)        | 基于 RPC 服务的 OCR 识别插件         |
| [pytest-mark-manage](https://github.com/funny-dream/pytest-mark-manage) | 用例标签化管理插件 |
| [wdotool](https://github.com/funny-dream/wdotool) | Wayland下完美的键鼠工具 |

