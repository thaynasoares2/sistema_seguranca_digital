# Revisão técnica assistida — matriz e metodologia

Revisão pontual realizada em 2026-10-10. Pronta para leitura e envio à Fernanda, sem envio automático. A aprovação acadêmica permanece pendente.

## O que mudou

- Preservados os 31 IDs, distribuição por função, 9 controles RSDM, 2 mandatórios do modelo e os pesos.
- C04: critérios aceitam base legal adequada distinta de consentimento e preservam melhor interesse; nível 2 não penaliza mera ausência de consentimento.
- C25 e C29: critérios incluem acionamento/execução, coerentes com RS.MA-01 e RC.RP-01.
- C30: critérios incluem integridade antes de restaurar, coerente com RC.RP-03.
- Documentadas adaptações e correspondências parciais do CSF, incluindo causa raiz versus melhoria em C28.
- Escala, pesos, faixas e piso identificados como experimentais. Gap renomeado para lacunas e expresso em percentual.
- Definidos não aplicabilidade, resposta pendente, denominador vazio, arredondamento, versionamento e rastreabilidade.
- Alpha será caso sintético transparente. Não forçar resultado 2,4.

## Pendências humanas

- Fernanda: revisar clareza, critérios, contexto e recomendações até 2026-10-15 à noite.
- Sandir: validar média ponderada, pesos, faixas, piso RSDM e encaminhar divergência 2,03 × 2,4.
- Enviar matriz MD e metodologia até 2026-10-11 à noite; estes arquivos não foram enviados nesta sessão.
- Enquadramento jurídico/exceções e demais normas citadas: confirmação antes da versão acadêmica final.

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
