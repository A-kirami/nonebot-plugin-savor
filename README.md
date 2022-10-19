<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-savor

_✨ 二次元图像分析 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-savor.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-savor">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-savor.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>


## 📖 介绍

使用 DeepDanbooru 进行图像分析

[DeepDanbooru 在线使用](https://huggingface.co/spaces/hysts/DeepDanbooru)

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-savor

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-savor
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-savor
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-savor
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-savor
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_savor')

</details>

## 🎉 使用
### 指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| 鉴赏/分析 + 图片 | 否 | 群聊/私聊 | 分析发送的图片, 支持回复图片 |

**注意**

默认情况下, 您应该在指令前加上命令前缀, 通常是 /