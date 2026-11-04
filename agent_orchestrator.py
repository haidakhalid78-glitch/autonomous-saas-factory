import os
import datetime

def log_to_file(filepath, content):
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def subagent_trend_scraper():
    print("[Agent 1] Analisi dei problemi e della domanda in corso...")
    return "Micro-Tool Web di Generazione Asset e Mockup Promozionali"

def subagent_product_architect(niche_name):
    print(f"[Agent 2] Generazione del codice SaaS per: {niche_name}")
    
    html_code = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuickPrint Studio - Tool Grafico Gratuito</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 1rem; }
        .container { background: #1e293b; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.4); max-width: 480px; width: 100%; text-align: center; }
        h1 { font-size: 1.8rem; margin-bottom: 0.5rem; color: #38bdf8; }
        p { font-size: 0.95rem; color: #94a3b8; margin-bottom: 1.5rem; }
        textarea { width: 100%; padding: 0.8rem; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: #fff; resize: vertical; min-height: 90px; margin-bottom: 1rem; font-size: 1rem; }
        button { width: 100%; padding: 0.9rem; background: #0284c7; color: white; border: none; border-radius: 8px; font-size: 1rem; font-weight: bold; cursor: pointer; transition: background 0.2s; }
        button:hover { background: #0369a1; }
        #preview { margin-top: 1.5rem; display: none; padding: 1.5rem; border-radius: 8px; background: linear-gradient(135deg, #6366f1, #a855f7); color: white; font-weight: bold; font-size: 1.2rem; word-wrap: break-word; }
        .footer-cta { margin-top: 1.5rem; font-size: 0.85rem; color: #64748b; }
        .footer-cta a { color: #38bdf8; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 QuickPrint Studio</h1>
        <p>Crea al volo grafiche promozionali pronte per i tuoi prodotti o social.</p>
        <textarea id="textInput" placeholder="Inserisci il tuo testo o l'offerta speciale..."></textarea>
        <button onclick="generateGraphics()">Genera Asset Ora</button>
        <div id="preview"></div>
        <div class="footer-cta">
            <p>Ti piace questo tool? <a href="#" target="_blank">Supporta il progetto o scopri di più</a></p>
        </div>
    </div>
    <script>
        function generateGraphics() {
            const input = document.getElementById('textInput').value;
            const preview = document.getElementById('preview');
            if (!input.trim()) { alert('Per favore inserisci un testo!'); return; }
            preview.style.display = 'block';
            preview.innerHTML = "✨ " + input + " ✨<br><small style='font-size: 0.75rem; font-weight: normal; opacity: 0.9; display: block; margin-top: 0.5rem;'>Creato con QuickPrint Studio</small>";
        }
    </script>
</body>
</html>"""
    return html_code

def main():
    print("=== AVVIO SISTEMA MULTI-AGENTE AGENTE AUTONOMO ===")
    niche = subagent_trend_scraper()
    saas_html = subagent_product_architect(niche)
    
    # Salva la landing page del SaaS nella cartella public
    log_to_file("public/index.html", saas_html)
    
    # Genera un log delle operazioni
    report = f"# SaaS Execution Log\n- Data: {datetime.datetime.now()}\n- Focus: {niche}\n- Status: Generazione completata con successo."
    log_to_file("agent_log.md", report)
    print("=== PROCESSO COMPLETATO ===")

if __name__ == "__main__":
    main()
