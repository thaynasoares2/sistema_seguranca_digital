# Manual de uso — TCC FH — Beta S2

Gerado em 2026-10-10, a partir da aplicação no commit `25a0744`, com capturas reais feitas no Chromium sobre uma cópia isolada do banco e dados fictícios. O banco de uso do sistema não foi alterado para produzir o manual.

**Entrega:** [Manual de uso em PDF](Manual_de_Uso_TCC_FH_Beta_S2_2026-10-10.pdf) — 16 páginas A4, capturas reais dos fluxos e dos quatro dashboards. Cobre login, cadastro, início e retomada de avaliação, questionário, níveis, justificativas, finalização, indicadores, recomendações, rastreabilidade e acesso móvel.

## Arquivos e reprodução

- `manual.html`: fonte editável do PDF; as imagens são referenciadas em `capturas/`.
- `exportar_pdf.py`: exportação via Playwright/Chromium, com verificação de carregamento das imagens e de espaço para os rodapés.
- `capturas/`: PNGs originais da interface; nenhuma senha capturada.
- `Manual_de_Uso_TCC_FH_Beta_S2_2026-10-10.pdf`: entrega pronta para leitura e compartilhamento.

Abra `manual.html` no navegador para revisar. Para reproduzir o PDF, execute `python exportar_pdf.py` em um ambiente Python com Playwright e `/usr/bin/chromium` disponíveis. A produção desta versão usou `/tmp/tcc-fh-build-venv/bin/python`; nenhuma dependência nova foi adicionada ao sistema TCC.

Validação: `pdfinfo` confirmou 16 páginas A4; extração de texto conferiu todas as seções; as 16 páginas foram renderizadas e inspecionadas; imagens referenciadas e ausência de senha no texto foram verificadas. O exportador confere a folga entre conteúdo e rodapé em todas as páginas.

O manual cobre S2. A revisão do conteúdo e a entrega oficial S3 ainda exigem ensaio e congelamento. O PDF e os PNGs permanecem no disco, fora do git, conforme a política de binários do vault IESGO; fonte HTML, exportador e README são versionáveis.

## Fontes consultadas

Data de acesso: 2026-10-10. Fontes metodológicas **parcialmente validadas**, por indisponibilidade do INFOSEC e pendências acadêmicas do modelo.

- [Notebook TCC FH](https://notebook.google.com/notebook/e516c873-817b-41f1-9076-018dc6679f7f): consulta sobre Tiers, escala numérica, validação de fórmulas, LGPD e respostas da Alpha; referencial não fornece fórmula RSDM fechada nem respostas brutas da Alpha.
- [Notebook obrigatório S17](https://notebook.google.com/notebook/c204a5de-6f06-4f76-b07a-f6681b51ad6a): consulta sobre segurança feita na sessão de implementação de 2026-10-10 reutilizada; nova tentativa nesta etapa expirou por timeout. Não foi usada para validar os scores.
- INFOSEC: `/run/media/r3v4n/jpeg_2tb/CyberVault_V2/Storage-Vault/10_RECURSOS/13_EDUCACIONAL/133_Bibliotecas_e_Acervos/11-PDFS_ESTUDOS_TIC/INFOSEC/` indisponível; nenhum arquivo ou página lido.
- HackTricks: `80-APOIO/81-HACKTRICKS/hacktricks/src/network-services-pentesting/pentesting-web/django.md`, seção “Host Header / Password Reset Poisoning”, consultada para os cuidados técnicos de acesso.
- [MITRE ATT&CK T1078 — Valid Accounts](https://attack.mitre.org/techniques/T1078/): contexto de proteção de credenciais, sem fundamentar os scores.
- Aplicação local: README, templates, formulários e `avaliacao/scoring.py`; projeto: [README](../README.md) e [METODOLOGIA_SCORES.md](../03_MODELO_AVALIACAO/METODOLOGIA_SCORES.md). A lista completa e as limitações estão também na última página do PDF.

Atualização S2 em 2026-10-10: quatro dashboards com gráficos reais; código de referência `25a0744`. Manual S1 preservado como histórico. Os indicadores permanecem experimentais; fontes e limitações constam na última página do PDF.
