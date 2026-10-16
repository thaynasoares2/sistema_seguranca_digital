# TCC FH — Sistema de Avaliação de Maturidade em Segurança Digital

Ponto de retomada para quem continuar este trabalho. Leia este arquivo primeiro e depois o plano: [`02_PLANEJAMENTO/PLANO_BETA_SISTEMA_ATE_2026-10-17.md`](02_PLANEJAMENTO/PLANO_BETA_SISTEMA_ATE_2026-10-17.md).

Última atualização: 2026-10-10.

**Regra editorial (2026-10-10):** nesta pasta, não incluir identificação pessoal, assinatura ou crédito nominal de implementação técnica. Aplicar a regra ao documento final, à fonte editável e aos metadados. A regra é restrita ao projeto `TCC_FH/`.

## Identificação

| Campo | Valor |
|---|---|
| Título | Sistema de Avaliação de Maturidade em Segurança Digital para Instituições Educacionais com Base no NIST CSF e LGPD |
| Aluna | Fernanda Holanda (BSI, 8º semestre, IESGO) |
| Orientador | MSc. Sandir Rodrigues Campos |
| Caderno de referência | https://notebook.google.com/notebook/e516c873-817b-41f1-9076-018dc6679f7f. Só tem o referencial teórico (NIST CSF 2.0, Tiers, Delphi/CVI, Cronbach, SUS, LGPD art. 14, DPIA, HECVAT, KPIs/KRIs); não tem prazos nem estado do projeto |

## Estado em 2026-10-10

- **O artigo já foi submetido e aceito.** Os prazos de correção e submissão (16/10 e 20/10) não se aplicam mais. Não propor tarefas do artigo.
- O trabalho agora é **construir e implantar o sistema**. **S1 implementado em 2026-10-10** em `~/Projetos/tcc-fh-maturidade/`: Django/SQLite, importação versionada, questionário por função, resultado rastreável e Alpha sintética. 24 testes passaram; `check` e migrações sem pendências; login, resultado e retomada conferidos no Chromium, inclusive em tela móvel. Verificações e retomada estão no README do código. **S2 adiantado em 2026-10-10:** quatro dashboards por perfil, Chart.js local, 33 testes aprovados e conferência no Chromium em desktop e celular. O congelamento/demo S3 permanece pendente.
- **Pacote instalável S2 preparado em 2026-10-10:** [ZIP atualizado para encaminhar à Fernanda](05_DISTRIBUICAO/TCC_FH_Beta_S2_2026-10-10.zip), com código, documentação, manual e dependências. [Instalação e validação](05_DISTRIBUICAO/README.md). Não substitui o congelamento S3.
- **Documentação sem identificação pessoal da implementação técnica em 2026-10-10:** manual PDF e fontes revisados, incluindo documentos de planejamento e retomada.
- **Manual de uso S2 atualizado em 2026-10-10:** [PDF com 16 páginas e capturas reais dos quatro dashboards](04_MANUAL_USO/Manual_de_Uso_TCC_FH_Beta_S2_2026-10-10.pdf). [Fonte e reprodução](04_MANUAL_USO/README.md). Manual e ZIP S1 preservados como histórico. A entrega oficial S3 permanece pendente.
- O Plano de Projeto v0.1 (20/08) está desatualizado: a stack aparece "a definir" e as entregas como "Não iniciado". **As datas dele não valem** (veja Prazos).
- **Conversa com a Fernanda pelo WhatsApp em 08/10, 09:14–09:48:**
  - Ela confirmou que **não há cronograma**: "Tem o que Sandir fala em cima da hora". A única data é **17/10: "preciso enviar o primeiro modelo pronto"**.
  - Ela não mexeu no TCC nesta semana porque estava estudando para provas. Não há material novo dela.
  - O plano (`PLANO_BETA_...`) foi enviado às 09:44 para confirmação. **Ela respondeu "Certo" às 10:00 e aceitou o plano.**
  - Às 10:06 ela esclareceu a entrega: **o Sandir "quer a primeira versão pronta, de como ficará"**. Ou seja, é o **sistema**, não só a matriz. Se a entrega será por envio ou por apresentação, ele "só avisa em cima da hora", como aconteceu na semana anterior.
  - Às 10:06 ela também **se comprometeu a revisar a matriz e as recomendações de segunda a quinta** ("Não é se consigo, eu preciso").

## Prazos

| Data | Entrega | Situação |
|---|---|---|
| **2026-10-17 (sáb)** | **Enviar o "primeiro modelo pronto"** ao Sandir. Confirmado pela Fernanda em 08/10. **É a única data que existe** | em andamento |

As datas de 23/10, 31/10, 03/11 e da banca que aparecem no Plano de Projeto e no pptx do Sandir **não são confirmadas**. O próprio Sandir define os prazos em cima da hora. Não planejar em cima delas.

**O que é a entrega de 17/10 (esclarecido em 08/10):** a primeira versão do **sistema**, mostrando "como ficará". O formato (enviar ou apresentar) só será avisado em cima da hora. Por isso, até 16/10 às 17:45, ter **as duas formas prontas**:
1. **Para apresentar:** o sistema rodando localmente, com a Escola Fictícia Alpha carregada e o roteiro da demo ensaiado.
2. **Para enviar:** um pacote que o Sandir abra sem instalar nada. Pode ser um PDF com capturas das telas principais (questionário, os 4 dashboards, recomendações e rastreabilidade) mais um resumo de uma página, e de preferência o link do repositório. Um link temporário do sistema no ar é opcional, se sobrar tempo.

## Decisões tomadas (2026-10-08)

1. **Divisão do trabalho:** implementação com o Claude Code; a Fernanda cuida do conteúdo (matriz de controles, perguntas, textos de recomendação).
2. **Stack:** Django 5.2 LTS, com SQLite na beta, Bootstrap e Chart.js (S2). PostgreSQL somente em futuro deploy, sem data confirmada.
3. **Matriz de controles:** 31 controles rascunhados em 2026-10-08 e revisados tecnicamente com assistência em 2026-10-10; a Fernanda valida o conteúdo.
4. **17/10:** primeira versão do sistema ao Sandir, por envio ou apresentação, avisado em cima da hora. Ter as duas formas prontas (veja Prazos). Não precisa estar publicado. Plano aceito pela Fernanda em 08/10.
5. **Código:** repositório git próprio, fora do vault, em `~/Projetos/tcc-fh-maturidade/`. Este diretório guarda a documentação e o pacote de distribuição; o desenvolvimento do código permanece no repositório próprio.

## Agenda de execução (eventos já criados no Google Calendar)

| Bloco | Quando | Conteúdo | ID do evento |
|---|---|---|---|
| S0 | **feito em 08/10** (adiantado) | Claude rascunhou a matriz v0 e a metodologia (`03_MODELO_AVALIACAO/`). Revisar e enviar à Fernanda até domingo, 11/10, à noite | sem evento |
| S1 | sáb 10/10, 09:45–17:00 | venv, Django, git, models, admin, carga da matriz, `scoring.py` com testes, fluxo do questionário | `rop5rks28tirsv7tjual4pdu8k` |
| S2 | dom 11/10, 11:30–18:30 | 4 dashboards, recomendações, login por perfil, seed da Escola Fictícia Alpha | `6ovsqg9gfbn6420bs8ikj98fqg` |
| — | seg a qui (12–15/10) | Revisão de conteúdo pela Fernanda | — |
| S3 | sex 16/10, 13:15–17:45 | Importar a matriz revisada, ensaiar a demo, README de execução, congelar o código | `bqcf8pa6m9f58adg4r11klqhe4` |
| Demo | sáb 17/10 | Demonstração | — |

Marcos e lembretes (criados em 08/10):

| Evento | Quando | ID do evento |
|---|---|---|
| Revisar matriz v0 + metodologia | sex 09/10, 13:30–14:15 | `kefr02qfafrfojkn9rj2vcmnoc` |
| Enviar matriz + metodologia à Fernanda, com a pergunta 2,03 × 2,4 para ela levar ao Sandir | dom 11/10, 21:45–22:00 | `fj0pm1tlmqhtrkl37fuuof269s` |
| Fernanda devolve a matriz revisada (até a noite) | qui 15/10, dia inteiro | `urkqq2f13ji8q9gm69g8lbki90` |
| Conferir se a matriz voltou; se não, cobrar (o S3 segue com a v0) | sex 16/10, 07:15–07:30 | `es1o9c1n7f0vllasl04oec4ikc` |
| 🎓 ENTREGA ao Sandir (envio ou apresentação) | sáb 17/10, dia inteiro | `n8e0fvuojtkv3le3t0ckrgfafg` |

⚠️ 16/10 também é o prazo final das notas da B1. Lançar as notas antes do S3.

## Especificação mínima da beta (§16 do Plano de Projeto)

- Cadastro de instituição e de avaliação.
- Matriz inicial de controles e questionário estruturado.
- Score de Maturidade Geral, Score por Função NIST e RSDM (Risk Score para Dados de Menores).
- 4 dashboards (Gestor, Técnico, Operacional, Conselheiro) com dados de teste.
- Recomendações básicas.
- Rastreabilidade de cada resultado até os controles e respostas que o originaram (RNF05).

Matriz do artigo, com 3 dimensões:
1. **Tipo de controle:** categoria (Técnico/Administrativo/Físico) × tipo funcional (Preventivo/Detectivo/Corretivo).
2. **Contexto educacional:** Dados de Menores, Acadêmicos, Sensíveis, de Pesquisa, Todos.
3. **Nível de maturidade:** 1 Inicial, 2 Intermediário, 3 Gerenciado, 4 Otimizado.

O que cada dashboard mostra, segundo o artigo:

| Dashboard | Conteúdo |
|---|---|
| Gestor | Score Geral, RSDM e gap de conformidade com a LGPD (justificar orçamento) |
| Técnico | Falhas em controles específicos (ex.: MFA, VLANs) |
| Operacional | Tarefas diárias e prontidão de resposta a incidentes |
| Conselheiro | Alinhamento estratégico e soberania digital |

## Modelo de avaliação — v0 (rascunho, aguardando revisão)

Fica em `03_MODELO_AVALIACAO/`:
- **`MATRIZ_CONTROLES_v0.csv`**: a fonte que o sistema importa no S1. São **31 controles**: GV 7, ID 5, PR 8, DE 4, RS 4, RC 3. **9 entram no RSDM** e **2 são mandatórios** (DPO e PSI). Cada controle traz pergunta, critérios objetivos dos níveis 1 a 4, evidência sugerida e recomendação.
- **`MATRIZ_CONTROLES_v0.md`**: a mesma matriz em formato de leitura, com campos de revisão. É o arquivo que vai para a Fernanda.
- **`METODOLOGIA_SCORES.md`**: as fórmulas de peso, Score por Função, Score Geral, RSDM (com a regra de piso do consentimento), gap LGPD e prioridade das recomendações. Traz também a correspondência CSF 1.1 → 2.0 dos 5 controles do artigo e as fontes consultadas.
- **`gerar_matriz_v0.py`**: script que gerou o CSV e o MD da v0. **Da v1 em diante, a fonte é o CSV**, e as mudanças da Fernanda entram direto nele.

Resumo das fórmulas:
- peso = contexto (Menores 1,5 · Sensíveis 1,3 · Todos 1,2 · Acadêmicos/Pesquisa 1,0) × 1,5 se mandatório;
- Score = média ponderada dos níveis;
- RSDM = `(4 − m)/3 × 100` sobre os controles RSDM, com classe mínima "Alto" quando o C04 (base legal não definida) está no nível 1.

**O modelo está parcialmente validado:** NotebookLM consultado e códigos CSF 2.0 conferidos no texto oficial em 2026-10-10; INFOSEC indisponível. Validação acadêmica das fórmulas e análise jurídica integral permanecem pendentes. Metodologia implementada: `v0.1-experimental`; matriz importada: `v0.1`.

**⚠️ Inconsistência no artigo, a levar ao Sandir:** na Escola Fictícia Alpha, as notas por função são ID 2,8 · PR 2,5 · DE 1,5 · RS 1,2 · RC 2,0 · GV 2,2. A média simples dá **2,03**, mas o artigo diz que o Score Geral é **2,4**. Veja a seção 7 da metodologia.

## Pendências

- [x] Confirmar a data com a Fernanda: 17/10 é a única (WhatsApp, 08/10).
- [x] Enviar o plano à Fernanda (08/10, 09:44).
- [x] Receber a resposta dela ao "concorda?": "Certo", às 10:00.
- [x] Esclarecer o "primeiro modelo pronto": é o sistema, e o formato só sai em cima da hora.
- [x] Combinar a revisão da matriz: ela revisa de segunda a quinta e devolve até quinta, 15/10, à noite.
- [x] Rascunhar a matriz v0 e a metodologia (S0), feito em 08/10.
- [x] Revisão técnica assistida de `03_MODELO_AVALIACAO/MATRIZ_CONTROLES_v0.md` e `METODOLOGIA_SCORES.md` (2026-10-10); alterações em `REVISAO_PROFESSOR_2026-10-10.md`. Leitura e aprovação acadêmica permanecem pendentes.
- [x] S1 implementado e testado em 2026-10-10.
- [x] S2: quatro dashboards gráficos por perfil, concluídos antecipadamente em 2026-10-10.
- [x] Manual S2 com capturas e PDF atualizado em 2026-10-10 (16 páginas).
- [ ] S3: ensaio, atualização das capturas/PDF para a versão final e congelamento.
- [ ] Mandar os dois arquivos à Fernanda até **domingo, 11/10, à noite**. Esse compromisso foi assumido por WhatsApp.
- [x] Conferir os 31 códigos CSF 2.0 e os limites de seus mapeamentos (2026-10-10).
- [ ] Concluir análise jurídica de enquadramento, exceções e demais normas citadas antes da versão final.
- [ ] S3: preparar o pacote de envio (PDF com capturas e resumo) além da demo local.
- [ ] Concluir no Google Tasks a tarefa "[PSSL] Planejar TCC da FH" (lista OBJETIVOS DO DIA) e anotar o caminho do plano. O agente não conseguiu porque a permissão foi negada.
- [ ] Levar ao Sandir a divergência 2,03 × 2,4.
- [ ] Opcional: subir o Plano de Projeto e o pptx do Sandir como fontes do caderno e516c873.


## Arquivos desta pasta

```text
TCC_FH/
├── README.md                     ← ponto de retomada (este arquivo)
├── 01_REFERENCIAS/               ← documentos de origem (binários, fora do git)
├── 02_PLANEJAMENTO/              ← plano de execução
├── 03_MODELO_AVALIACAO/          ← matriz de controles e metodologia dos scores
├── 04_MANUAL_USO/                ← manual S2, fonte HTML, capturas e PDF
└── 05_DISTRIBUICAO/              ← pacotes S1 histórico e S2 atualizado para envio
```

O código de trabalho fica no repositório próprio `~/Projetos/tcc-fh-maturidade/`, criado no S1.

| Arquivo | O que é | Versionado |
|---|---|---|
| `README.md` | Este ponto de retomada | sim |
| `04_MANUAL_USO/manual.html`, `exportar_pdf.py`, `README.md` | Fonte do manual e reprodução | sim |
| `04_MANUAL_USO/Manual_de_Uso_TCC_FH_Beta_S1_2026-10-10.pdf` e `capturas/` | Manual S1 em PDF e prints reais | não (binários locais) |
| `02_PLANEJAMENTO/PLANO_BETA_SISTEMA_ATE_2026-10-17.md` | Plano de execução aprovado (arquitetura, sequência, verificação) | sim |
| `03_MODELO_AVALIACAO/MATRIZ_CONTROLES_v0.csv` | Matriz de 31 controles; fonte de importação do sistema | sim |
| `03_MODELO_AVALIACAO/MATRIZ_CONTROLES_v0.md` | Matriz para leitura e revisão da Fernanda | sim |
| `03_MODELO_AVALIACAO/METODOLOGIA_SCORES.md` | Fórmulas dos indicadores, inconsistência do artigo, fontes consultadas | sim |
| `03_MODELO_AVALIACAO/gerar_matriz_v0.py` | Gerador da v0 (CSV + MD) | sim |
| `01_REFERENCIAS/Plano de Projeto - Seguranca Digital - Holanda.docx` | Plano de Projeto v0.1 da Fernanda: requisitos RF01–RF07, RNF01–RNF05, modelo de dados, §16 | não (binário) |
| `01_REFERENCIAS/Praticas orientadas e Trabalho de curso 2026.pptx` | Slides do Sandir com os prazos da disciplina | não (binário) |
| `01_REFERENCIAS/Artigo_Formatado_FHolanda_2026.pdf` | Artigo aceito: metodologia, Tabela 1, Escola Alpha, dashboards | não (binário) |
| `01_REFERENCIAS/Artigo_Formatado_FHolanda_2026_WORKING_COPY.pdf` | Cópia de trabalho do artigo | não (binário) |

## Como retomar (para um agente)

1. Leia este README e o plano.
2. Confira a pendência mais antiga em aberto e o bloco da agenda mais próximo (IDs dos eventos acima).
3. **Retomada atual: S2.** Rode os testes antes de alterar o código; não recrie o S1. Se o repositório `~/Projetos/tcc-fh-maturidade/` já existir, rode `.venv/bin/python manage.py test avaliacao` para saber em que ponto está. Se não existir, o próximo passo é o S1, que importa `03_MODELO_AVALIACAO/MATRIZ_CONTROLES_v0.csv` (ou a versão revisada mais recente) e implementa as fórmulas de `METODOLOGIA_SCORES.md`.
4. **Corte de escopo** se faltar tempo, nesta ordem: upload de evidências (RF07) → dashboard do Conselheiro vira seção do dashboard do Gestor → visual no Bootstrap padrão. **Não cortar** os scores, o RSDM nem a rastreabilidade.
5. Ao terminar uma sessão, atualize a seção **Estado**, marque as pendências concluídas e faça o commit no repositório do IESGO, branch `main`.

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

Manual S1: capturas e documentação local conferidas em 2026-10-10; nova consulta ao Notebook TCC realizada. A tentativa adicional ao Notebook S17 nesta etapa expirou por timeout; consulta anterior do mesmo dia reutilizada. Detalhes em [Fontes do manual](04_MANUAL_USO/README.md#fontes-consultadas).

A aceitação do artigo não valida automaticamente este novo instrumento. Delphi/CVI, consistência estatística e usabilidade permanecem etapas acadêmicas futuras, sem alegação de que tenham sido executadas.
