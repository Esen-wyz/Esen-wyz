"""Render the actual profile README into an offline, GitHub-like preview."""
from pathlib import Path
import re
import markdown

ROOT = Path(__file__).resolve().parent


def github_slug(value, _separator):
    return re.sub(r"[^\w\- ]", "", value.lower()).replace(" ", "-")


body = markdown.markdown(
    (ROOT / "README.md").read_text(encoding="utf-8"),
    extensions=["tables", "toc", "md_in_html"],
    extension_configs={"toc": {"slugify": github_slug}},
)

template = r'''<!doctype html>
<html lang="zh-CN" data-theme="dark">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Esen-wyz · Profile preview</title>
<style>
*{box-sizing:border-box}
:root{color-scheme:dark;--bg:#0d1117;--panel:#0d1117;--text:#e6edf3;--muted:#919ca9;--line:#30363d;--link:#75c5fc;--row:#151b23;--control:#212830}
[data-theme="light"]{color-scheme:light;--bg:#f6f8fa;--panel:#fff;--text:#1f2328;--muted:#59636e;--line:#d1d9e0;--link:#0969da;--row:#f6f8fa;--control:#f6f8fa}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans SC","Microsoft YaHei",sans-serif}
.toolbar{max-width:1012px;margin:22px auto 18px;padding:0 18px;display:flex;gap:12px;align-items:center;justify-content:space-between;color:var(--muted);font-size:12px}
.toolbar span{letter-spacing:.1em}.actions{display:flex;gap:8px}
button{border:1px solid var(--line);border-radius:7px;background:var(--control);color:var(--text);padding:7px 12px;font:inherit;cursor:pointer}
button:hover{border-color:var(--muted)}button:focus-visible,summary:focus-visible{outline:2px solid var(--link);outline-offset:3px}
main{max-width:976px;margin:0 auto 36px;border:1px solid var(--line);border-radius:7px;background:var(--panel);padding:25px 32px 20px;transition:max-width .2s ease}
body.narrow main{max-width:390px;padding:20px 16px}
.file-label{font:12px/1.5 ui-monospace,SFMono-Regular,Consolas,monospace;margin-bottom:24px}.file-label strong{font-weight:600}.file-label span{color:var(--muted)}
.markdown-body{word-wrap:break-word}.markdown-body>:first-child{margin-top:0}.markdown-body>:last-child{margin-bottom:0}
.markdown-body p,.markdown-body table,.markdown-body blockquote,.markdown-body ul,.markdown-body details{margin-top:0;margin-bottom:16px}
.markdown-body h1,.markdown-body h2,.markdown-body h3{font-weight:600;line-height:1.25;margin:24px 0 16px;scroll-margin-top:24px}
.markdown-body h1{font-size:2em;padding-bottom:.3em;border-bottom:1px solid var(--line)}
.markdown-body h2{font-size:1.5em;padding-bottom:.3em;border-bottom:1px solid var(--line);margin-top:32px}
.markdown-body h3{font-size:1.25em}.markdown-body img{max-width:100%;height:auto;vertical-align:middle}
.markdown-body a{color:var(--link);text-decoration:none}.markdown-body a:hover{text-decoration:underline}
.markdown-body table{border-spacing:0;border-collapse:collapse;display:block;max-width:100%;overflow:auto;width:max-content}
.markdown-body td,.markdown-body th{padding:10px 14px;border:1px solid var(--line);text-align:left}
.markdown-body tr:nth-child(2n){background:var(--row)}.markdown-body td:first-child{min-width:240px}
.markdown-body blockquote{padding:0 1em;color:var(--muted);border-left:.25em solid var(--line)}
.markdown-body blockquote p{padding:4px 0}.markdown-body summary{cursor:pointer;padding:5px 0}.markdown-body details[open] summary{margin-bottom:8px}
.markdown-body ul{padding-left:2em}.markdown-body li+li{margin-top:.4em}.markdown-body sub{font-size:12px;color:var(--muted)}
.footnote{text-align:center;font-size:12px;color:var(--muted);padding:0 20px 24px}
@media(max-width:700px){.toolbar{margin-top:14px}.toolbar span{letter-spacing:0;font-size:11px}.actions{gap:4px}button{padding:6px 8px}main{margin:0 10px 20px;padding:18px 16px}.markdown-body{font-size:14px}.markdown-body h1{font-size:1.7em}.markdown-body td:first-child{min-width:180px}.file-label{margin-bottom:18px}}
@media(prefers-reduced-motion:reduce){main{transition:none}}
</style>
</head>
<body>
<nav class="toolbar" aria-label="预览显示选项"><span>PROFILE README / LOCAL PREVIEW</span><div class="actions"><button id="theme" type="button" aria-pressed="false">浅色预览</button><button id="width" type="button" aria-pressed="false">窄屏预览</button></div></nav>
<main><div class="file-label"><strong>Esen-wyz</strong><span> / README.md</span></div><article class="markdown-body">__BODY__</article></main>
<p class="footnote">由实际 README 生成 · GitHub 的最终排版以在线页面为准</p>
<script>
document.querySelector('#theme').addEventListener('click',function(){const light=document.documentElement.dataset.theme!=='light';document.documentElement.dataset.theme=light?'light':'dark';this.textContent=light?'深色预览':'浅色预览';this.setAttribute('aria-pressed',String(light));});
document.querySelector('#width').addEventListener('click',function(){const narrow=document.body.classList.toggle('narrow');this.textContent=narrow?'宽屏预览':'窄屏预览';this.setAttribute('aria-pressed',String(narrow));});
</script>
</body></html>'''

(ROOT / "preview.html").write_text(template.replace("__BODY__", body), encoding="utf-8")
print("Preview generated from README.md")
