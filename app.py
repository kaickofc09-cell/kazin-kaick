import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>KAZIN - Criado pro Kaick Lourenço</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#0a0a0a;color:white;font-family:Arial;text-align:center;padding:20px}
h1{color:#00ff88;font-size:40px}
.card{background:#1a1a1a;border-radius:20px;padding:30px;max-width:400px;margin:20px auto;border:2px solid #00ff88}
button{background:#00ff88;color:black;border:none;padding:15px 30px;border-radius:10px;font-weight:bold;font-size:18px;cursor:pointer;width:100%}
.badge{background:#00ff88;color:black;padding:5px 15px;border-radius:20px;font-weight:bold}
</style>
</head>
<body>
<h1>👑 KAZIN</h1>
<div class="card">
<p><span class="badge">DONO: Kaick Lourenço Nascimento</span></p>
<h2>🎮 BEM VINDO!</h2>
<p>Site oficial criado por KAZIN © 2026</p>
<p>ID: kaickofc09-cell</p>
<button onclick="alert('SALVE KAICK! Site tá ONLINE! 👑')">CLICA AQUI</button>
</div>
<p style="opacity:0.5">kazin-kaick.onrender.com</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
