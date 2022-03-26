import httpx

with open('mark.md', 'r') as f:
    body = f.read()

response = httpx.post(
    "https://api.github.com/markdown",
    json={
        "mode": "markdown",
        "text": body,
    },
)
if response.status_code == 200:
    with open('index.html', 'w') as f:
        f.write(f'''
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
	<link rel="stylesheet" type="text/css" href="github-markdown.css">
</head>
<body>
<article class="markdown-body">
	{response.text}
</article>
 <script>
  MathJax = {{
    tex: {{inlineMath: [['$', '$'], ['\\(', '\\)']]}}
  }};
  </script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</body>
</html>
''')