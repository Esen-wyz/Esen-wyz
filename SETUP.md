# 主页文件说明

这套主页用于 GitHub 账号 `Esen-wyz` 的个人资料页。

## 发布

将 `README.md` 与整个 `assets/` 文件夹放入公开仓库 `Esen-wyz/Esen-wyz` 的默认分支。README 位于仓库根目录后，GitHub 会将它显示在个人主页。此规则见 [GitHub 官方文档](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)。

如果仓库已有内容，先保留现有文件，只更新本套主页对应的文件。不要用整目录覆盖其他项目。

## 内容与素材

- `README.md`：实际主页正文，可直接在 GitHub 编辑。
- `assets/hero.svg`：地面与空中视角的概念插画，含轻量动画。
- `assets/after-hours.svg`：小实验主题插画，含轻量动画。
- `preview.html`：本地预览，读取 README 生成，支持切换深浅色和窄屏。GitHub 显示会以实际 Markdown 渲染为准。
- `build_preview.py`：重新生成预览，运行 `python build_preview.py`。需要 Python 的 `markdown` 包。

插画为概念示意，不代表真实数据、实验结果或已完成的方法。视觉素材为独立 SVG，不依赖外部统计卡片、字体服务或定时工作流。浏览器开启“减少动态效果”时，动画对应的静态图形仍然可见。

## 修改建议

正文以已确认的计算机视觉和地空步态识别方向为基础，没有填写未经确认的学校、职位、论文、性能数据和联系方式。小项目只表达兴趣，没有展示尚未成熟的具体项目。

后续可以在 Research 部分追加真实公开的论文或代码链接；有小项目成熟后，再加入少量精选项目。
