def subagent_product_architect(niche_name):
    print(f"[Agent 2] Generazione del codice SaaS con monetizzazione per: {niche_name}")
    
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
        
        /* Sezione Monetizzazione */
        .monetization-box { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #334155; font-size: 0.85rem; color: #94a3b8; }
        .donate-btn { display: inline-block; margin-top: 0.5rem; padding: 0.5rem 1rem; background: #10b981; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; transition: background 0.2s; }
        .donate-btn:hover { background: #059669; }
        .affiliate-link { color: #38bdf8; text-decoration: none; display: block; margin-top: 0.8rem; }
        .affiliate-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 QuickPrint Studio</h1>
        <p>Crea al volo grafiche promozionali pronte per i tuoi prodotti o social.</p>
        <textarea id="textInput" placeholder="Inserisci il tuo testo o l'offerta speciale..."></textarea>
        <button onclick="generateGraphics()">Genera Asset Ora</button>
        <div id="preview"></div>
        
        <div class="monetization-box">
            <p>Ti è utile questo tool gratuito?</p>
            <!-- Sostituisci il link sotto con il tuo link Ko-fi, Buy Me a Coffee o PayPal.me -->
            <a href="https://www.buymeacoffee.com" target="_blank" class="donate-btn">☕ Offrimi un caffè</a>
            
            <!-- Link di affiliazione o sponsorizzazione automatica -->
            <a href="https://netlify.com" target="_blank" class="affiliate-link">✨ Scopri la piattaforma cloud consigliata per i tuoi progetti</a>
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
</html>
"""
    return html_code
