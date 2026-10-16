# Plano — Beta do Sistema de Maturidade (TCC FH) até 17/10/2026

## Contexto
O artigo do TCC da Fernanda Holanda (BSI/IESGO, orientador Sandir) já foi aceito. Agora o trabalho é **construir o sistema**. A única data oficial é **17/10 (sábado)**: entregar e demonstrar a beta ao Sandir. Pode ser rodando local ou em um link temporário, com dados de teste.

- Em 2026-10-10, S1 implementado e validado: Django/SQLite, importação versionada, questionário e resultado rastreável. Código em `~/Projetos/tcc-fh-maturidade/`. O Plano de Projeto v0.1 deixou a stack "a definir" e as entregas como "Não iniciado".
- O artigo traz só 5 controles de exemplo (Tabela 1) e **não define as fórmulas** dos scores.
- Divisão decidida: **implementação com Claude Code**, Fernanda cuida do conteúdo (matriz, perguntas e textos de recomendação).
- Stack decidida: **Django 5.2 LTS + SQLite + Bootstrap + Chart.js (S2)**. PostgreSQL somente em futuro deploy, sem data confirmada.
- A matriz foi rascunhada em 2026-10-08 e revisada tecnicamente em 2026-10-10; a Fernanda valida o conteúdo.

**Escopo mínimo da beta**, conforme o §16 do Plano de Projeto:
- cadastro de instituição e avaliação;
- matriz inicial de controles;
- questionário;
- Score Geral, Score por Função NIST e RSDM;
- 4 dashboards com dados de teste;
- recomendações básicas;
- rastreabilidade de cada resultado até os controles.

## Capacidade real (agenda conferida)
| Bloco | Janela livre | Horas |
|---|---|---|
| S0 | Sex 09/10, 13:00–16:00. **Opcional e leve** | ~1h |
| S1 | Sáb 10/10, 09:45–17:00 | ~6h |
| S2 | Dom 11/10, 11:30–18:30 | ~5h |
| — | Seg a qui (12–15/10): **sem código**. A Fernanda revisa o conteúdo | 0h |
| S3 | Sex 16/10, 13:10–17:45. | ~4h |
| Demo | Sáb 17/10 | — |

São cerca de 15h de implementação. Só fecha porque o escopo é enxuto e o Claude escreve a maior parte do código.

## Onde fica o código
É um repositório git próprio, fora do vault, para compartilhar com a Fernanda pelo GitHub e depois instalar no servidor do IESGO: `~/Projetos/tcc-fh-maturidade/`.

A documentação acadêmica continua em `IESGO/20_PROJETOS/2026-02/TCC_FH/`. Antes de gravar algo ali, ler o `README.md` e o `CLAUDE.md` do IESGO.

## Arquitetura (um único app Django)
```
tcc-fh-maturidade/
  config/                 settings, urls
  avaliacao/
    models.py             Instituicao, Controle, Avaliacao, Resposta, Resultado, PerfilUsuario
    scoring.py            funções puras: score_funcao, score_geral, rsdm, classificar
    recomendacoes.py      gaps -> ações priorizadas (texto vem do campo do Controle)
    views.py / templates/ cadastro, questionário por função NIST, 4 dashboards
    admin.py              leitura da matriz e gestão de instituições/perfis
    management/commands/   importar_matriz (CSV), seed_alpha (caso sintético)
    tests/test_scoring.py
  docs/METODOLOGIA_SCORES.md
```
- **Controle**: código NIST, função (GV/ID/PR/DE/RS/RC), categoria (Técnico/Administrativo/Físico), tipo funcional (Preventivo/Detectivo/Corretivo), contexto (Menores/Sensíveis/Acadêmicos/Pesquisa/Todos), pergunta, descrição dos níveis 1 a 4, `mandatorio`, `rsdm` (bool), recomendação.
- **Perfis**: Gestor, Técnico, Operacional e Conselheiro. S1 inclui login, grupos e vínculos institucionais; todos veem o resultado tabular. S2 acrescenta as apresentações específicas. Grupos não concedem acesso a outras instituições.
- **Rastreabilidade (RNF05)**: o Resultado guarda os IDs das respostas que o originaram, e o dashboard Técnico lista controle → nível → peso.

## Modelo de scores (proposta, a validar com a Fernanda e o Sandir)
- Cada resposta recebe um nível de 1 a 4, ou "Não se aplica", que fica fora do cálculo.
- Peso = peso do contexto × fator de mandatório (1,5 para DPO e PSI, conforme o artigo). Pesos de contexto: Menores 1,5 · Sensíveis 1,3 · Todos 1,2 · Acadêmicos e Pesquisa 1,0.
- **Score por Função** = média ponderada dos níveis da função.
- **Score Geral** = média ponderada de todas as respostas.
- **RSDM** = só os controles com `rsdm=True` (Art. 14, consentimento, Privacy by Design): `(4 − média ponderada)/3 × 100`. Classes: Baixo < 25 ≤ Moderado < 50 ≤ Alto < 75 ≤ Crítico. C04 nível 1 impõe classe mínima Alto sem mudar o número; todas as regras são experimentais, com justificativas e limites descritos na metodologia v0.1.
- ⚠️ **Inconsistência no artigo:** a média simples das funções da Escola Alpha (2,8 / 2,5 / 1,5 / 1,2 / 2,0 / 2,2) dá **2,03**, mas o texto diz 2,4. O fixture será um caso sintético transparente, sem forçar as notas do artigo; o documento `METODOLOGIA_SCORES.md` vai registrar a fórmula escolhida e essa diferença. Levar a questão ao Sandir.

## Sequência de execução
**Registro de 2026-10-08:** a mensagem para a Fernanda já está redigida. Acrescentar o pedido para que ela revise, de segunda a quinta, a `matriz_v0` (até ~30 controles, 5 por função) e os textos de recomendação.

**S0, sexta (opcional, ~1h):** Claude rascunha `matriz_v0` (planilha CSV/MD para a Fernanda revisar) a partir do NIST CSF 2.0, LGPD Art. 14/41/46/52 e ECA, mais o `METODOLOGIA_SCORES.md`. Revisão pontual, sem reescrita. Entregar à Fernanda até domingo à noite.

**S1, sábado:**
1. venv, Django, repositório git e settings.
2. Models e migrações, admin com filtros por função e contexto. Matrizes/controles/resultados somente leitura; revisão entra via CSV com nova versão.
3. Importação de `MATRIZ_CONTROLES_v0.csv` com `--versao v0.1`, transacional e idempotente.
4. `scoring.py` com testes unitários: reprodutibilidade (RNF04) e fixture da Escola Alpha.
5. Fluxo cadastrar instituição → nova avaliação → questionário paginado por função → resultado salvo.

**S2, concluído antecipadamente em 2026-10-10:**

Quatro dashboards implementados sobre os resultados imutáveis do S1; 33 testes aprovados, gráficos locais conferidos em desktop/celular, manual PDF S2 e pacote instalável atualizados. O bloco abaixo registra o escopo previsto:
1. Os 4 dashboards com Chart.js:
   - Gestor: Score Geral, RSDM e gap LGPD;
   - Técnico: radar por função e controles com falha;
   - Operacional: Detect/Respond e prontidão a incidentes;
   - Conselheiro: Govern e alinhamento estratégico.
2. Recomendações priorizadas por (4 − nível) × peso.
3. Login e grupos de perfil.
4. Seed da "Escola Fictícia Alpha" com 4 usuários de teste.

**Seg a qui:** sem código. A Fernanda devolve a matriz revisada.

**S3, sexta:** importar a matriz revisada, ajustar textos, rodar o roteiro de demo, escrever o `README` com instruções para rodar e corrigir bugs. Congelar o código às 17:45.

**Sábado 17/10:** demonstração.

**Corte de escopo, se atrasar** (nesta ordem): RF07 (upload de evidências) fica para depois de 17/10 → o dashboard do Conselheiro vira uma seção do dashboard do Gestor → o estilo visual fica no Bootstrap padrão. Os scores, o RSDM e a rastreabilidade não são cortados.

## Persistência e agenda (plano aceito em 2026-10-08)
- Plano já gravado e aceito; manter `METODOLOGIA_SCORES.md` em `IESGO/20_PROJETOS/2026-02/TCC_FH/` e fazer o commit no repositório do IESGO.
- Blocos S1, S2 e S3 já criados (IDs no README). Não duplicá-los. Pendente atualizar a tarefa "[PSSL] Planejar TCC da FH": notas com o plano e o caminho do repositório, e concluir a tarefa, já que o planejamento estará feito.

## Verificação
- `python manage.py test avaliacao`: cálculos e limites reproduzíveis, importação transacional/idempotente, imutabilidade, fluxo completo e isolamento institucional. Alpha é sintética; as notas do artigo não são critérios de aprovação.
- `python manage.py check` e `python manage.py makemigrations --check --dry-run` devem passar.
- `python manage.py runserver` → ensaiar o roteiro da demo:
  1. login como Gestor;
  2. criar instituição e avaliação;
  3. responder o questionário;
  4. ver o Score Geral e o RSDM;
  5. trocar para os outros 3 perfis e ver cada dashboard;
  6. abrir uma recomendação e rastreá-la até o controle e a resposta.
- Checklist final contra as "Condições mínimas para a beta" do §16 do Plano de Projeto.

## Fontes consultadas

Acesso em **2026-10-10**. Revisão **parcialmente validada**: INFOSEC indisponível; a validação acadêmica, análise de enquadramentos/exceções e conferência jurídica integral continuam pendentes.

| Fonte | Consulta / seção lida | Resultado |
|---|---|---|
| [Caderno TCC](https://notebook.google.com/notebook/e516c873-817b-41f1-9076-018dc6679f7f) | Query sobre Tiers, pesos, consentimento, lacunas, fórmulas e Escola Alpha; resposta e trechos citados de “Metodologias para a Validação…” e “Maturidade e Conformidade com a LGPD no Tratamento de Dados de Menores” | Sem fórmula específica do RSDM e sem respostas da Alpha; a escala e pesos do trabalho exigem validação |
| [Notebook obrigatório S17](https://notebook.google.com/notebook/c204a5de-6f06-4f76-b07a-f6681b51ad6a) | Query sobre autenticação, entradas e auditoria; resposta e trechos citados | Material defensivo geral; sem instruções específicas de Django ou multitenancy |
| INFOSEC — `/run/media/r3v4n/jpeg_2tb/CyberVault_V2/Storage-Vault/10_RECURSOS/13_EDUCACIONAL/133_Bibliotecas_e_Acervos/11-PDFS_ESTUDOS_TIC/INFOSEC/` | Tentativa de acesso ao diretório; `/mnt/seagate` também ausente | Indisponível; nenhum arquivo/página consultado |
| HackTricks local — `80-APOIO/81-HACKTRICKS/hacktricks/src/network-services-pentesting/pentesting-web/django.md` | “Cache Manipulation to RCE”; “Host Header / Password Reset Poisoning” | Preservar validações do framework, isolamento local e evitar cache compartilhado inseguro |
| [MITRE ATT&CK T1078 — Valid Accounts](https://attack.mitre.org/techniques/T1078/) | Descrição da técnica; acesso inicial e abuso de contas | Contexto de identidade/acesso, sem fundamentar os scores |
| [NIST CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) | §3 e Apêndices A/B; páginas impressas 15–24 | Códigos e resultados do CSF 2.0, Tiers e limites dos mapeamentos |
| [Enunciado ANPD nº 1/2023](https://bibliotecadigital.mj.gov.br/bitstream/1/10215/2/Enunciado_ANPD_2023_1.html) | Texto do enunciado | Hipóteses dos Arts. 7º/11 e prevalência do melhor interesse |
| [LGPD, texto oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) | Texto acessado; Arts. 14, 37, 38, 41, 46, 48 e 50 | Referência primária; não substitui análise de enquadramento e exceções |
| Documentos locais | README, plano beta aprovado, CSV/MD e metodologia v0 | Estado, divisão do trabalho, compromissos e proposta de fórmulas |

A aceitação do artigo não valida automaticamente este novo instrumento. Delphi/CVI, consistência estatística e usabilidade permanecem etapas acadêmicas futuras, sem alegação de que tenham sido executadas.
