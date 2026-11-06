# Wulin Xie · 谢武林 — Academic Homepage

纯英文个人学术主页。静态 HTML / CSS / JavaScript，无第三方运行时依赖。

## 预览

直接用 Chrome 打开 `index.html`，或在此目录执行：

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

然后访问 http://127.0.0.1:8080 。

## 修改内容

- `build.py`：个人介绍、代表论文、经历、教育等内容；改完运行 `python3 build.py`。
- `style.css`：颜色、排版、响应式布局。
- `script.js`：论文方向筛选、侧边导航。
- `assets/avatar.jpg`：使用本人提供的个人照片。
- 暂不展示 CV 下载入口，网站目录不包含简历附件。
- `assets/papers/`：论文原文图示。

`index.html` 已生成。部署时无需运行 Python 或安装依赖。

## GitHub Pages

公开主页：https://wulinxie.github.io/

源码仓库：https://github.com/WulinXie/wulinxie.github.io

GitHub Pages 使用 `main` 分支的根目录发布。原个人主页仓库保留在 `aba122/aba122.github.io`。

更新内容后运行 `python3 build.py`，将修改提交并推送到 `main`。GitHub Pages 会自动发布。`index.html` 已生成，线上无需 Python 环境或构建依赖。`.nojekyll` 用于直接发布静态资源。

Mac 桌面的 `Wulin-Xie-Homepage` 为本地同步副本，可直接打开 `index.html` 预览。

## 内容与来源

- 内容依据 2026-09-30 的最新学术版简历和本人确认的论文状态；引用量 300+ 是本人提供的截至 2026 年 9 月快照，非自动更新。
- VI-Bench 为 NeurIPS 2026；MME-Unify 为 ICLR 2026；Q-Hawkeye 为 AAAI 2027 Under Review；DivOPD 为 ICLR 2027 Under Review。未将投稿状态写成录用。
- MME-VideoOCR 与 MM-RLHF 使用 Core Contributor，不将贡献标记写成共同一作。
- DivOPD 的 1.87× 指学习器 GPU 效率，不是端到端训练加速。
- 论文图片来自作者现有公开论文 PDF；Paper / Code / Project 按对应原始来源链接。UPDGD-Net 使用 ACM 正式版论文 Figure 1（PDF 第 4 页，出版页码 6659）的总体框架图，来源：https://doi.org/10.1145/3664647.3680932。
- 图标来自现有简历；头像为本人提供的个人照片。
- 布局与页脚图片参考 [w-r-s/academic-homepage-template](https://github.com/w-r-s/academic-homepage-template)，参考版本 `3e688b9`。页面底部保留署名链接；HTML、CSS 和交互为本主页重新实现。

## 验证

已验证 375、390、768、1280、1440 像素布局、四组论文筛选、附加论文展开、所有本地资源/锚点。浏览器未出现 JavaScript 错误。
