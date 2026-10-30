from flask import Flask, request

app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width">
<title>Meta AI Clone</title>
<style>
body{margin:0;font-family:system-ui;background:#0a0a0a;color:white;display:flex;height:100vh}
.side{width:240px;background:#111;border-right:1px solid #222;padding:15px}
.main{flex:1;display:flex;flex-direction:column}
.top{padding:15px;border-bottom:1px solid #222;text-align:center;color:#aaa}
.chat{flex:1;padding:20px;overflow:auto}
.msg{max-width:70%;padding:12px 16px;border-radius:18px;margin:10px 0}
.user{background:#0064e0;margin-left:auto}
.ai{background:#262626}
.bar{display:flex;padding:15px;border-top:1px solid #222;gap:10px}
input{flex:1;padding:14px;border-radius:24px;border:none;background:#222;color:white;outline:none}
button{padding:12px 20px;border-radius:24px;border:none;background:#0064e0;color:white;font-weight:bold;cursor:pointer}
</style></head><body>
<div class="side"><h3>Meta AI</h3><p style="color:#666">Novo chat</p></div>
<div class="main">
<div class="top">Meta AI - Clone feito por você</div>
<div id="chat" class="chat"><div class="msg ai">Oi! Eu sou o Meta AI clone. Me pergunta algo!</div></div>
<div class="bar"><input id="inp" placeholder="Pergunte algo..."><button onclick="enviar()">Enviar</button></div>
</div>
<script>
function enviar(){
 let t=document.getElementById('inp').value; if(!t) return;
 let c=document.getElementById('chat');
 c.innerHTML+=`<div class="msg user">${t}</div>`;
 document.getElementById('inp').value='';
 setTimeout(()=>{c.innerHTML+=`<div class="msg ai">Você disse: "${t}". Legal! Isso é meu clone funcionando 100% local no seu PC. 😎</div>`; c.scrollTop=c.scrollHeight;},500);
 c.scrollTop=c.scrollHeight;
}
document.getElementById('inp').addEventListener('keydown',e=>{if(e.key==='Enter')enviar()})
</script></body></html>"""

@app.route('/')
def home(): return HTML

app.run(port=5000, debug=True)