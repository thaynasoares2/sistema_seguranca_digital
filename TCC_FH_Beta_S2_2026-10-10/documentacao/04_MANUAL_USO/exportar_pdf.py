from pathlib import Path
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parent
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page()
 page.goto((root/'manual.html').as_uri())
 page.emulate_media(media='print')
 page.evaluate('document.fonts.ready')
 page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')
 report=page.evaluate('''()=>Array.from(document.querySelectorAll('.page')).map((p,i)=>({pagina:i+1,titulo:p.querySelector('h1').textContent,folga_mm:Math.round((p.querySelector('footer').getBoundingClientRect().top-p.querySelector('.content').getBoundingClientRect().bottom)*25.4/96*10)/10}));''')
 print(json.dumps(report,ensure_ascii=False))
 assert all(i['folga_mm']>=3 for i in report), 'Conteúdo próximo do rodapé: ajuste a diagramação.'
 page.pdf(path=str(root/'Manual_de_Uso_TCC_FH_Beta_S2_2026-10-10.pdf'),format='A4',print_background=True,prefer_css_page_size=True,display_header_footer=False)
 browser.close()
