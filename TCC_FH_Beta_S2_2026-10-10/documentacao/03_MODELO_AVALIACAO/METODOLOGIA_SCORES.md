# Metodologia de Cálculo dos Indicadores — v0.1 experimental

Proposta de fórmulas para o Score de Maturidade Geral, o Score por Função NIST e o Risk Score para Dados de Menores (RSDM). O artigo aceito descreve esses indicadores, mas **não define as fórmulas**. Este documento as define para que o sistema seja reproduzível (RNF04) e rastreável (RNF05).

**Status:** revisão técnica assistida em 2026-10-10; modelo experimental, a validar com a Fernanda e o Sandir. Versão implementada: `v0.1-experimental`; matriz: `v0.1` (os nomes dos arquivos v0 são preservados para a revisão). Não representa aprovação acadêmica ou certificação de conformidade. A matriz que alimenta os cálculos está em `MATRIZ_CONTROLES_v0.csv`; a versão para leitura é `MATRIZ_CONTROLES_v0.md`.

## 1. Entrada

Para cada controle *i* da matriz, a avaliação registra uma resposta:

- **Nível** nᵢ ∈ {1, 2, 3, 4}: Inicial, Intermediário, Gerenciado, Otimizado. Os critérios de cada nível estão escritos controle a controle na matriz.
- **Não se aplica**: o controle sai de todos os cálculos (numerador e denominador). Exemplo: a escola não tem rede própria de pesquisa.

O questionário só é dado como concluído quando todo controle tem nível ou "Não se aplica". "Não se aplica" exige justificativa. Resposta pendente não é nível 1 nem exclusão. Sem controles aplicáveis, o indicador mostra **Sem dados aplicáveis** (valor nulo), nunca zero ou baixo risco. A instituição deve justificar também eventuais exclusões dos controles mandatórios do modelo.

## 2. Peso de cada controle

```
pᵢ = peso_contexto(i) × fator_mandatório(i)
```

| Contexto educacional (Dimensão 2 do artigo) | Peso |
|---|---|
| Dados de Menores | 1,5 |
| Dados Sensíveis | 1,3 |
| Todos os Dados | 1,2 |
| Dados Acadêmicos | 1,0 |
| Dados de Pesquisa | 1,0 |

- "Mandatório" identifica prioridade definida pelo artigo/modelo; não comprova obrigação jurídica universal nem impede justificar não aplicabilidade. Exigências e exceções legais dependem do enquadramento da instituição.
- Fator mandatório = **1,5** para DPO (C01) e PSI (C02) e **1,0** para os demais. O artigo diz que esses dois são "requisitos mandatórios na função Govern".
- Por que Menores pesa mais: o artigo atribui "peso majorado" aos dados de menores, com base no Art. 14 da LGPD e no ECA, e maior peso aos dados de alta confidencialidade (tríade CIA).
- Os valores de 1,0 a 1,5 são uma **calibragem inicial** que o protocolo de validação (Etapas 1 e 2) pode ajustar.

## 3. Score por Função NIST

Para cada função *F* ∈ {GV, ID, PR, DE, RS, RC}, sobre os controles respondidos (sem "Não se aplica"):

```
Score(F) = Σ pᵢ·nᵢ / Σ pᵢ        (para i ∈ F)
```

O resultado vai de 1,00 a 4,00. O cálculo usa `Decimal`; somente a exibição é arredondada a 2 casas (`ROUND_HALF_UP`). A classificação usa o valor não arredondado.

## 4. Score de Maturidade Geral

Média ponderada de **todas** as respostas, e não a média dos seis scores de função:

```
Score Geral = Σ pᵢ·nᵢ / Σ pᵢ     (todos os controles respondidos)
```

Faixas experimentais de leitura, usando os nomes de níveis do artigo. A escala 1–4 é construída pelo trabalho; não equivale automaticamente aos Tiers do NIST, que caracterizam o rigor da governança e gestão de riscos:

| Score | Leitura |
|---|---|
| 1,00 ≤ score < 1,75 | Inicial |
| 1,75 ≤ score < 2,50 | Intermediário |
| 2,50 ≤ score < 3,25 | Gerenciado |
| 3,25 ≤ score ≤ 4,00 | Otimizado |

Por que a média de todas as respostas: cada controle conta com o seu peso, e uma função com mais controles (Protect tem 8) não fica diluída. A alternativa, média simples das funções, dá o mesmo peso a GV e RC mesmo que RC tenha 3 controles. **Decisão a confirmar com o Sandir** (veja a seção 7).

## 5. RSDM — Risk Score para Dados de Menores

Considera só os controles marcados `rsdm = sim` na matriz. Na v0 são 9: C03, C04, C06, C10, C12, C15, C16, C22 e C26. Eles cobrem consentimento (Art. 14), Privacy by Design (Art. 46 §2º), inventário, RIPD, acesso, proteção, registros e comunicação de incidente.

```
m       = Σ pᵢ·nᵢ / Σ pᵢ           (i ∈ RSDM)
RSDM    = (4 − m) / 3 × 100        (0 = risco mínimo; 100 = risco máximo)
```

O RSDM é um **risco**: quanto maior, pior. Por isso a escala é invertida em relação aos scores de maturidade.

| RSDM | Classe |
|---|---|
| 0 ≤ RSDM < 25 | Baixo |
| 25 ≤ RSDM < 50 | Moderado |
| 50 ≤ RSDM < 75 | Alto |
| 75 ≤ RSDM ≤ 100 | Crítico |

**Regra de piso:** se **C04 (base legal e consentimento parental)** estiver no nível 1, a classe é **no mínimo "Alto"**, qualquer que seja o valor numérico. É uma regra experimental inspirada no caso do artigo, ainda sem validação empírica. **O valor numérico não muda**; o sistema mostra o motivo da elevação da classe. C04 nível 1 significa base legal não definida, não mera ausência de consentimento. Tratamento adequadamente fundamentado em outra hipótese legal não recebe a penalidade por dispensar consentimento; deve-se preservar o melhor interesse (Enunciado ANPD nº 1/2023).

## 6. Indicadores derivados (dashboards)

- **Lacunas nos controles associados à LGPD** (dashboard do Gestor): % do peso dos controles aplicáveis com base legal na LGPD abaixo do nível 3. O nível 3 é um **limiar experimental**, não "conformidade mínima" jurídica. O indicador não é parecer, atestado ou certificação de conformidade.
  ```
  Gap LGPD (%) = 100 × Σ pᵢ [nᵢ < 3] / Σ pᵢ
  (i aplicável com base_legal contendo "LGPD")
  ```
- **Prioridade de recomendação** (todos os dashboards):
  ```
  prioridade(i) = (4 − nᵢ) × pᵢ
  ```
  A lista sai em ordem decrescente. Empates: mandatórios primeiro, depois RSDM, depois o código do controle. Controles no nível 4 não geram recomendação.
- **Prontidão de resposta** (dashboard Operacional): Score das funções DE e RS juntas, pela fórmula da seção 3 aplicada a DE ∪ RS.

## 7. ⚠️ Inconsistência no artigo (levar ao Sandir)

Na simulação da "Escola Fictícia Alpha", o artigo informa:

| ID | PR | DE | RS | RC | GV | Geral |
|---|---|---|---|---|---|---|
| 2,8 | 2,5 | 1,5 | 1,2 | 2,0 | 2,2 | **2,4** |

- A **média simples** das seis funções é **2,03**, não 2,4.
- Para chegar a 2,4 com pesos por função, ID e PR precisariam pesar muito mais que o resto, porque 2,4 está acima de quatro das seis notas. O artigo não descreve esse peso.

Encaminhamento proposto:
1. O sistema adota as fórmulas acima, que são reproduzíveis.
2. A demonstração usa a **Escola Fictícia Alpha (caso sintético)**, com respostas explicitamente construídas para testar o fluxo. Não há respostas originais por controle no caderno. Não calibrar dados para reproduzir as notas por função ou o 2,4 publicado. Os resultados são calculados e a divergência fica documentada.
3. Perguntar ao Sandir se ele prefere (a) registrar a divergência na apresentação ou (b) adotar a média simples das funções, que dá 2,03.

## 8. Correspondência entre os códigos do artigo (CSF 1.1) e da matriz (CSF 2.0)

A Tabela 1 do artigo usa códigos do NIST CSF 1.1, mas o texto fundamenta o trabalho no CSF 2.0. A matriz usa os códigos do 2.0:

| Artigo (CSF 1.1) | Matriz (CSF 2.0) | Controle |
|---|---|---|
| ID.AM-1 Inventário de hardware | ID.AM-01 | C08 |
| PR.AC-1 Gerenciamento de identidade | PR.AA-01 (a categoria PR.AC passou a PR.AA no 2.0) | C13 |
| PR.DS-1 Proteção de dados em repouso | PR.DS-01 | C16 |
| DE.CM-1 Monitoramento de rede | DE.CM-01 | C21 |
| RS.RP-1 Plano de resposta a incidentes | RS.MA-01 (a categoria RS.RP foi absorvida por RS.MA) | C25 |

Os contextos e categorias da Tabela 1 foram mantidos nesses 5 controles.

**Revisão técnica em 2026-10-10:** os 31 códigos foram conferidos no Apêndice A do NIST CSWP 29. São mapeamentos de contribuição a resultados esperados, não equivalências normativas completas ou uma checklist oficial. A correspondência CSF 1.1 → 2.0 da tabela é aproximada; não representa uma migração integral de categorias.

- C01/GV.RR-02 é adaptação de papéis e responsabilidades ao encarregado; a subcategoria não exige especificamente DPO.
- C04/GV.OC-03 adapta obrigações de privacidade e bases legais; o CSF não define consentimento parental.
- C12/ID.RA-05 conecta análise de risco ao RIPD; não o torna obrigatório universalmente.
- C25/RS.MA-01 passou a enfatizar execução coordenada; estabelecimento/manutenção do plano também contribui a ID.IM-04.
- C28/RS.AN-03 corresponde à investigação e causa raiz; ações de melhoria também contribuem a ID.IM-03.
- C29/RC.RP-01 passou a incluir acionamento/execução; planejamento também contribui a ID.IM-04.
- C30/RC.RP-03 passou a exigir integridade antes de restaurar; testes periódicos também contribuem a PR.DS-11 e validação dos ativos restaurados a RC.RP-05.
- C31/RC.CO-03 é comunicação da recuperação; LGPD Art. 48 rege comunicação de incidente relevante, sem tornar todo comunicado de continuidade uma notificação legal.

## 9. Rastreabilidade (RNF05)

Todo resultado exibido guarda:
- os IDs dos controles e das respostas que entraram no cálculo;
- o nível e o peso de cada um;
- a versão da matriz (v0, v1…) e a versão desta metodologia.

Uma mesma avaliação calculada com as mesmas respostas e versões deve dar exatamente os mesmos números (RNF04). O Resultado preserva snapshot das entradas, contribuições, recomendações, hash lógico da matriz e versões. Avaliação finalizada é imutável. Revisão exige uma nova versão da matriz e uma nova avaliação, sem alterar resultados anteriores.

A importação é transacional e idempotente. Versão existente com conteúdo diferente é rejeitada. Mudança de pesos requer nova metodologia e testes; não basta editar a coluna peso do CSV.

## 10. Pontos para a revisão da Fernanda

- [ ] Os pesos de contexto (1,0 a 1,5) fazem sentido para ela e para o orientador?
- [ ] O Score Geral deve ser média de todas as respostas (proposta) ou média das funções?
- [ ] Os 9 controles do RSDM estão certos? Falta algum? Por exemplo, câmeras e uso de imagem de alunos.
- [ ] A regra de piso do C04 é aceitável academicamente?
- [ ] O nível 3 como limiar experimental do indicador de lacunas está adequado?

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
