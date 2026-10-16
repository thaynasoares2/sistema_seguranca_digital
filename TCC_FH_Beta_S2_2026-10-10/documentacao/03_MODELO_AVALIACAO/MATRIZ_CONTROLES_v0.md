# Matriz de Controles v0 — revisão técnica para a Fernanda

Fonte: `MATRIZ_CONTROLES_v0.csv`. Revisão técnica assistida em 2026-10-10; versão de importação `v0.1`.

**Prazo da revisão:** 2026-10-15 à noite. Fórmulas em `METODOLOGIA_SCORES.md`.

Escala e pesos experimentais, aguardando validação acadêmica. Códigos CSF conferidos; os mapeamentos são adaptações, não equivalências normativas completas. Veja os limites na metodologia.

## Como revisar

Para cada controle, confira:

1. **A pergunta** está clara para um gestor escolar sem formação técnica? (Etapa 1 e Etapa 3 do protocolo de validação do artigo.)
2. **Os níveis 1 a 4** são objetivos o bastante para duas pessoas diferentes chegarem à mesma resposta?
3. **Contexto, categoria e tipo** estão corretos? O contexto define o peso.
4. **A recomendação** é uma ação concreta que a escola consegue executar?
5. Algum controle sobra ou falta? Sugestões entram como C32, C33…

Marque cada controle como ✅ ok, ✏️ ajustar (com o texto novo) ou ❌ remover.

Não se aplica exige justificativa. Mandatório é prioridade do modelo acadêmico, não afirmação de obrigação jurídica universal. A escala 1–4 não representa automaticamente os Tiers do NIST.

## Resumo

- **31 controles** nas seis funções NIST.
- **9 controles RSDM**.
- **2 mandatórios do modelo**.

| Função | Controles | No RSDM |
|---|---|---|
| Govern (Governar) | 7 | 3 |
| Identify (Identificar) | 5 | 2 |
| Protect (Proteger) | 8 | 2 |
| Detect (Detectar) | 4 | 1 |
| Respond (Responder) | 4 | 1 |
| Recover (Recuperar) | 3 | 0 |

Pesos: Menores 1,5 · Sensíveis 1,3 · Todos 1,2 · Acadêmicos/Pesquisa 1,0; mandatórios × 1,5.

## Govern (Governar)

### C01 · GV.RR-02 — Encarregado (DPO) designado **MANDATÓRIO**

**Pergunta:** A instituição designou formalmente um Encarregado pelo Tratamento de Dados Pessoais (DPO), com identidade e contato publicados no site?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Todos os Dados · Peso: 1.8
- Base legal: LGPD Art. 41
- Evidência sugerida: Ato de nomeação; página do site com o contato do encarregado.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há encarregado. |
| 2 Intermediário | Alguém responde pelo tema informalmente, sem nomeação ou sem contato publicado. |
| 3 Gerenciado | Nomeação formal (portaria ou contrato) e contato publicado no site. |
| 4 Otimizado | Nível 3 + encarregado com tempo e recursos definidos, que presta contas à direção periodicamente. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Nomear formalmente o encarregado e publicar a identidade e o canal de contato no site (LGPD Art. 41 §1º).

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C02 · GV.PO-01 — Política de Segurança da Informação (PSI) **MANDATÓRIO**

**Pergunta:** Existe uma Política de Segurança da Informação aprovada pela direção e comunicada a professores e funcionários?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Todos os Dados · Peso: 1.8
- Base legal: LGPD Arts. 46 e 50
- Evidência sugerida: PSI assinada; registro de ciência; histórico de revisões.

| Nível | Critério |
|---|---|
| 1 Inicial | Não existe PSI. |
| 2 Intermediário | Existe rascunho ou documento não aprovado ou não divulgado. |
| 3 Gerenciado | PSI aprovada pela direção, divulgada e com ciência registrada dos colaboradores. |
| 4 Otimizado | Nível 3 + estrutura em três camadas (política, normas, procedimentos) revisada ao menos uma vez por ano. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Aprovar uma PSI em três camadas (política, normas, procedimentos), divulgá-la e colher a ciência de todos os colaboradores.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C03 · GV.OC-03 — Obrigações legais mapeadas **RSDM**

**Pergunta:** A instituição identificou e documentou as obrigações legais que se aplicam aos dados que trata, incluindo as regras específicas para crianças e adolescentes (LGPD e ECA)?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 14; ECA Arts. 17 e 100
- Evidência sugerida: Documento de requisitos legais; parecer jurídico.

| Nível | Critério |
|---|---|
| 1 Inicial | As obrigações não foram levantadas. |
| 2 Intermediário | Conhecimento geral da LGPD, sem levantamento documentado. |
| 3 Gerenciado | Levantamento documentado das obrigações (LGPD, ECA, contratos), com responsável definido. |
| 4 Otimizado | Nível 3 + revisão periódica diante de novas normas da ANPD. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Documentar as obrigações legais aplicáveis, com destaque para as regras de tratamento de dados de crianças e adolescentes.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C04 · GV.OC-03 — Base legal e consentimento parental para dados de menores **RSDM**

**Pergunta:** Para cada tratamento de dados de alunos menores, a instituição definiu a base legal e, quando a base é o consentimento, coleta o consentimento específico e destacado de pelo menos um dos pais ou responsáveis?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 14 §1º; Enunciado CD/ANPD nº 1/2023
- Evidência sugerida: Termos de consentimento por finalidade; registro das autorizações e revogações.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há definição de base legal; usa-se dado de aluno sem critério (ex.: fotos em redes sociais sem autorização). |
| 2 Intermediário | Bases legais identificadas parcialmente; quando o consentimento é necessário, usa-se termo genérico sem separar finalidades. |
| 3 Gerenciado | Base legal adequada definida e documentada por finalidade, com melhor interesse avaliado; consentimento específico e destacado registrado quando aplicável. |
| 4 Otimizado | Nível 3 + revisão das bases legais e do melhor interesse; quando aplicável, responsáveis revogam o consentimento por canal simples e a revogação é executada. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Definir a base legal de cada tratamento de dados de alunos e substituir o termo genérico por consentimento granular por finalidade quando o consentimento for a base.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C05 · GV.SC-05 — Proteção de dados nos contratos com fornecedores

**Pergunta:** Os contratos com fornecedores que tratam dados da instituição (sistema acadêmico, plataformas EdTech, nuvem) têm cláusulas de proteção de dados e segurança?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Arts. 39 e 42
- Evidência sugerida: Contratos e aditivos; lista de fornecedores que tratam dados.

| Nível | Critério |
|---|---|
| 1 Inicial | Contratos sem cláusulas de proteção de dados, ou uso de serviços sem contrato. |
| 2 Intermediário | Cláusulas genéricas em parte dos contratos. |
| 3 Gerenciado | Todos os contratos relevantes têm cláusulas de proteção de dados, incidentes e devolução/eliminação. |
| 4 Otimizado | Nível 3 + avaliação periódica do cumprimento pelos fornecedores. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Incluir nos contratos cláusulas de proteção de dados, notificação de incidentes e eliminação de dados ao fim do serviço. A responsabilidade da escola não se transfere ao fornecedor.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C06 · GV.SC-06 — Avaliação de privacidade antes de adotar plataformas e apps (Privacy by Design) **RSDM**

**Pergunta:** Antes de adotar uma nova plataforma ou aplicativo que use dados de alunos (inclusive os escolhidos por professores), a instituição avalia os riscos de privacidade e segurança?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 46 §2º
- Evidência sugerida: Lista de ferramentas aprovadas; formulário de avaliação.

| Nível | Critério |
|---|---|
| 1 Inicial | Cada professor adota as ferramentas que quiser, sem avaliação. |
| 2 Intermediário | Há avaliação só para sistemas grandes, ou de forma informal. |
| 3 Gerenciado | Existe processo formal de avaliação e uma lista de ferramentas aprovadas. |
| 4 Otimizado | Nível 3 + reavaliação periódica das ferramentas aprovadas. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Criar um processo de aprovação de ferramentas digitais, com avaliação de privacidade, e publicar uma lista de ferramentas aprovadas para os professores.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C07 · GV.OV-01 — Acompanhamento da direção

**Pergunta:** A direção acompanha periodicamente os riscos e os resultados de segurança da informação (por exemplo, em reunião ou relatório ao menos semestral)?

- Categoria: Administrativo · Tipo: Detectivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Art. 50
- Evidência sugerida: Atas; relatórios periódicos.

| Nível | Critério |
|---|---|
| 1 Inicial | O tema não chega à direção. |
| 2 Intermediário | O tema chega à direção só quando há problema. |
| 3 Gerenciado | Há reporte periódico à direção, com registro. |
| 4 Otimizado | Nível 3 + indicadores definidos e decisões de investimento baseadas neles. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Estabelecer um reporte semestral de segurança à direção, usando os indicadores deste sistema.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

## Identify (Identificar)

### C08 · ID.AM-01 — Inventário de hardware

**Pergunta:** A instituição mantém um inventário atualizado dos equipamentos (computadores, notebooks, servidores, equipamentos de rede)?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Dados Acadêmicos · Peso: 1.0
- Base legal: —
- Evidência sugerida: Planilha ou sistema de inventário com data de atualização.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há inventário. |
| 2 Intermediário | Inventário parcial ou desatualizado (ex.: só patrimônio contábil). |
| 3 Gerenciado | Inventário completo, com responsável e atualização regular. |
| 4 Otimizado | Nível 3 + inventário automatizado e conciliado com a rede. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Montar e manter um inventário de equipamentos com responsável, localização e data de atualização.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C09 · ID.AM-02 — Inventário de software e serviços

**Pergunta:** A instituição sabe quais softwares e serviços online são usados (incluindo plataformas pedagógicas e apps usados pelos professores)?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: —
- Evidência sugerida: Lista de softwares e serviços.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há levantamento. |
| 2 Intermediário | Conhece os sistemas principais, mas não os serviços usados pelos professores. |
| 3 Gerenciado | Inventário completo de softwares e serviços, com responsável. |
| 4 Otimizado | Nível 3 + revisão periódica e remoção do que não é mais usado. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Levantar todos os softwares e serviços em uso, incluindo os pedagógicos, e definir um responsável por cada um.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C10 · ID.AM-07 — Inventário de dados pessoais (registro das operações) **RSDM**

**Pergunta:** A instituição mantém um registro das operações de tratamento de dados pessoais, identificando onde estão os dados de menores e os dados sensíveis (ex.: laudos, saúde)?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 37
- Evidência sugerida: ROPA.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há registro. |
| 2 Intermediário | Registro parcial, sem identificar dados de menores ou dados sensíveis. |
| 3 Gerenciado | Registro completo (ROPA), com finalidade, base legal, local e prazo de retenção. |
| 4 Otimizado | Nível 3 + registro revisado sempre que surge um novo tratamento. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Elaborar o registro das operações de tratamento (ROPA), destacando os dados de menores e os dados sensíveis.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C11 · ID.RA-01 — Identificação de vulnerabilidades e atualizações

**Pergunta:** A instituição verifica regularmente vulnerabilidades e mantém sistemas e equipamentos atualizados?

- Categoria: Técnico · Tipo: Detectivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Art. 46
- Evidência sugerida: Relatórios de varredura; histórico de atualizações.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há verificação; há sistemas sem suporte do fabricante. |
| 2 Intermediário | Atualizações feitas de forma esporádica, sem verificação de vulnerabilidades. |
| 3 Gerenciado | Atualizações regulares e verificação periódica de vulnerabilidades, com registro. |
| 4 Otimizado | Nível 3 + priorização por risco e prazos definidos para correção. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Implantar uma rotina mensal de atualizações e uma verificação periódica de vulnerabilidades, substituindo sistemas sem suporte.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C12 · ID.RA-05 — Relatório de impacto (RIPD/DPIA) **RSDM**

**Pergunta:** Para tratamentos de maior risco (dados de menores, dados sensíveis, monitoramento por câmeras), a instituição avalia o impacto à proteção de dados?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Arts. 5º XVII e 38
- Evidência sugerida: RIPD.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há avaliação de impacto. |
| 2 Intermediário | Avaliação informal, sem documento. |
| 3 Gerenciado | RIPD elaborado para os tratamentos de maior risco. |
| 4 Otimizado | Nível 3 + RIPD revisado quando o tratamento muda. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Elaborar o RIPD para os tratamentos de maior risco, a começar pelos que envolvem dados de crianças e adolescentes.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

## Protect (Proteger)

### C13 · PR.AA-01 — Gestão de identidades e contas

**Pergunta:** Cada pessoa tem conta individual nos sistemas, e as contas são criadas e removidas quando alguém entra ou sai da instituição (alunos, professores, funcionários)?

- Categoria: Técnico · Tipo: Preventivo · Contexto: Dados Sensíveis · Peso: 1.3
- Base legal: LGPD Art. 46
- Evidência sugerida: Procedimento; lista de contas comparada com a lista de pessoas ativas.

| Nível | Critério |
|---|---|
| 1 Inicial | Há contas compartilhadas, e as contas de quem saiu continuam ativas. |
| 2 Intermediário | Contas individuais, mas a remoção depende de lembrança. |
| 3 Gerenciado | Processo formal de criação e remoção, ligado à matrícula e ao desligamento. |
| 4 Otimizado | Nível 3 + revisão periódica das contas ativas. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Eliminar contas compartilhadas e vincular a remoção de contas ao processo de desligamento e de fim de matrícula.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C14 · PR.AA-03 — Autenticação multifator (MFA)

**Pergunta:** Os sistemas críticos (sistema acadêmico, e-mail, financeiro) exigem autenticação multifator?

- Categoria: Técnico · Tipo: Preventivo · Contexto: Dados Sensíveis · Peso: 1.3
- Base legal: LGPD Art. 46
- Evidência sugerida: Configuração dos sistemas; relatório de adesão ao MFA.

| Nível | Critério |
|---|---|
| 1 Inicial | Só senha. |
| 2 Intermediário | MFA disponível, mas opcional ou só para alguns usuários. |
| 3 Gerenciado | MFA obrigatório para todos os acessos administrativos e para o e-mail. |
| 4 Otimizado | Nível 3 + MFA resistente a phishing para administradores. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Tornar o MFA obrigatório no e-mail e nos sistemas acadêmico e financeiro, começando pelas contas administrativas.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C15 · PR.AA-05 — Acesso por perfil e menor privilégio **RSDM**

**Pergunta:** O acesso aos dados de alunos é limitado ao necessário para cada função (ex.: o professor vê só as suas turmas, a secretaria não vê dados de saúde sem necessidade)?

- Categoria: Técnico · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Arts. 6º III e 46
- Evidência sugerida: Matriz de perfis e permissões; relatório de acessos.

| Nível | Critério |
|---|---|
| 1 Inicial | Todos acessam tudo. |
| 2 Intermediário | Há perfis, mas amplos demais. |
| 3 Gerenciado | Perfis definidos por função (RBAC), seguindo o menor privilégio. |
| 4 Otimizado | Nível 3 + revisão periódica das permissões. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Definir perfis de acesso por função (RBAC) e restringir o acesso a dados de alunos ao mínimo necessário.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C16 · PR.DS-01 — Proteção de dados armazenados **RSDM**

**Pergunta:** Os dados de alunos armazenados (bancos de dados, notebooks, arquivos com laudos e fichas) estão protegidos por criptografia ou controle equivalente?

- Categoria: Técnico · Tipo: Preventivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 46
- Evidência sugerida: Configuração de criptografia; política de uso de dispositivos.

| Nível | Critério |
|---|---|
| 1 Inicial | Dados sem proteção, inclusive em notebooks e pen drives. |
| 2 Intermediário | Proteção só em parte dos locais. |
| 3 Gerenciado | Criptografia nos bancos de dados e nos dispositivos que guardam dados de alunos. |
| 4 Otimizado | Nível 3 + gestão de chaves e verificação periódica. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Ativar a criptografia nos bancos de dados e nos notebooks que armazenam dados de alunos, e proibir o uso de pen drives sem proteção.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C17 · PR.DS-11 — Backups

**Pergunta:** A instituição faz backups regulares dos dados importantes, com pelo menos uma cópia protegida contra ransomware (offline ou imutável)?

- Categoria: Técnico · Tipo: Corretivo · Contexto: Dados Acadêmicos · Peso: 1.0
- Base legal: LGPD Art. 46
- Evidência sugerida: Política de backup; registros das execuções.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há backup. |
| 2 Intermediário | Backup existe, mas fica na mesma rede ou não é regular. |
| 3 Gerenciado | Backups regulares, com cópia offline ou imutável. |
| 4 Otimizado | Nível 3 + backups monitorados e testados periodicamente. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Implantar backups regulares na regra 3-2-1, com uma cópia offline ou imutável.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C18 · PR.IR-01 — Segmentação da rede

**Pergunta:** A rede é separada por finalidade (administrativa, pedagógica, alunos/visitantes), de modo que um aparelho de visitante não alcance os sistemas administrativos?

- Categoria: Técnico · Tipo: Preventivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Art. 46
- Evidência sugerida: Diagrama de rede; configuração de VLANs e do firewall.

| Nível | Critério |
|---|---|
| 1 Inicial | Uma rede só para todos. |
| 2 Intermediário | Wi-Fi de visitantes separado, mas a rede interna não é segmentada. |
| 3 Gerenciado | Redes segmentadas por VLAN, com regras de firewall entre elas. |
| 4 Otimizado | Nível 3 + regras revisadas periodicamente. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Segmentar a rede em VLANs (administrativa, pedagógica, visitantes) com regras de firewall entre elas.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C19 · PR.AT-01 — Conscientização e treinamento

**Pergunta:** Professores e funcionários recebem orientação periódica sobre segurança e proteção de dados (ex.: phishing, uso de dados de alunos)?

- Categoria: Administrativo · Tipo: Preventivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Art. 50 §2º
- Evidência sugerida: Lista de presença; material; resultados de simulações.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há orientação. |
| 2 Intermediário | Orientação esporádica, sem registro. |
| 3 Gerenciado | Treinamento anual com registro de participação. |
| 4 Otimizado | Nível 3 + simulações de phishing e medição de resultados. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Instituir um treinamento anual sobre segurança e proteção de dados, com registro de participação.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C20 · PR.AA-06 — Controle de acesso físico

**Pergunta:** O acesso físico a locais com dados sensíveis (secretaria, sala de servidores, arquivos de prontuários e fichas) é controlado?

- Categoria: Físico · Tipo: Preventivo · Contexto: Dados Sensíveis · Peso: 1.3
- Base legal: LGPD Art. 46
- Evidência sugerida: Controle de chaves; registros de acesso.

| Nível | Critério |
|---|---|
| 1 Inicial | Locais abertos, sem controle. |
| 2 Intermediário | Há chaves ou trancas, mas sem controle de quem acessa. |
| 3 Gerenciado | Acesso restrito a pessoas autorizadas, com controle de chaves ou crachá. |
| 4 Otimizado | Nível 3 + registro de acesso e revisão periódica. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Restringir o acesso físico à secretaria, ao arquivo e à sala de servidores, e controlar quem tem chaves.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

## Detect (Detectar)

### C21 · DE.CM-01 — Monitoramento da rede

**Pergunta:** A rede é monitorada para identificar tráfego ou acessos anormais?

- Categoria: Técnico · Tipo: Detectivo · Contexto: Dados de Pesquisa · Peso: 1.0
- Base legal: —
- Evidência sugerida: Ferramenta de monitoramento; exemplos de alertas.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há monitoramento. |
| 2 Intermediário | Monitoramento só de disponibilidade (se a internet está funcionando). |
| 3 Gerenciado | Monitoramento de segurança com alertas definidos. |
| 4 Otimizado | Nível 3 + alertas analisados continuamente e regras ajustadas. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Ativar o monitoramento de segurança da rede (logs do firewall com alertas) e definir quem analisa os alertas.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C22 · DE.CM-03 — Registro de acessos a dados de alunos **RSDM**

**Pergunta:** Os sistemas registram quem acessou ou alterou dados de alunos, e esses registros são consultados quando necessário?

- Categoria: Técnico · Tipo: Detectivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Arts. 37 e 46
- Evidência sugerida: Exemplo de log de acesso; política de retenção de logs.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há registro de acessos. |
| 2 Intermediário | Há registros, mas ninguém os consulta, ou eles são apagados rapidamente. |
| 3 Gerenciado | Registros mantidos por prazo definido e consultados em caso de suspeita. |
| 4 Otimizado | Nível 3 + revisão periódica e alertas para acessos fora do padrão. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Ativar e reter os registros de acesso aos dados de alunos, definindo prazo de retenção e quem os revisa.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C23 · DE.CM-09 — Antimalware nas estações

**Pergunta:** Os computadores (inclusive os dos laboratórios) têm proteção antimalware ativa e atualizada?

- Categoria: Técnico · Tipo: Detectivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Art. 46
- Evidência sugerida: Console de gestão do antimalware.

| Nível | Critério |
|---|---|
| 1 Inicial | Sem proteção em parte relevante das máquinas. |
| 2 Intermediário | Proteção instalada, mas sem gestão central nem verificação de atualização. |
| 3 Gerenciado | Proteção em todas as máquinas, com gestão central. |
| 4 Otimizado | Nível 3 + EDR com resposta automatizada. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Garantir antimalware ativo e atualizado em todas as máquinas, com gestão centralizada.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C24 · DE.AE-02 — Análise de eventos suspeitos

**Pergunta:** Quando surge um alerta ou um relato suspeito (ex.: e-mail de phishing, conta bloqueada), alguém analisa e registra o caso?

- Categoria: Administrativo · Tipo: Detectivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: —
- Evidência sugerida: Canal de reporte; registros de análise.

| Nível | Critério |
|---|---|
| 1 Inicial | Ninguém é responsável; os alertas são ignorados. |
| 2 Intermediário | Análise informal, sem registro. |
| 3 Gerenciado | Responsável definido, canal de reporte conhecido e registro das análises. |
| 4 Otimizado | Nível 3 + análise com prazos definidos e indicadores. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Definir um responsável e um canal único para reportar suspeitas, e registrar cada análise.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

## Respond (Responder)

### C25 · RS.MA-01 — Execução coordenada do plano de resposta a incidentes

**Pergunta:** Existe um plano de resposta com responsáveis e etapas definidos, e a instituição consegue executá-lo de forma coordenada quando declara um incidente?

- Categoria: Administrativo · Tipo: Corretivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: LGPD Art. 46
- Evidência sugerida: Plano de resposta; registros de acionamento, simulações ou incidentes e coordenação com terceiros.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há plano nem responsáveis definidos para executar a resposta. |
| 2 Intermediário | Resposta improvisada; etapas ou responsáveis conhecidos apenas informalmente. |
| 3 Gerenciado | Plano documentado e comunicado, com papéis, acionamento e coordenação com terceiros relevantes definidos e demonstráveis. |
| 4 Otimizado | Nível 3 + execução coordenada testada em simulação ou incidente, com registro e correção das falhas identificadas. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Documentar e comunicar o plano, definir acionamento e coordenação com terceiros relevantes e testar sua execução.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C26 · RS.CO-02 — Comunicação de incidentes à ANPD e aos responsáveis **RSDM**

**Pergunta:** A instituição sabe quando e como comunicar um incidente com dados pessoais à ANPD e aos titulares (no caso de alunos menores, aos pais ou responsáveis)?

- Categoria: Administrativo · Tipo: Corretivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 48; Resolução CD/ANPD nº 15/2024
- Evidência sugerida: Procedimento de comunicação; modelos de comunicado.

| Nível | Critério |
|---|---|
| 1 Inicial | Não sabe que existe essa obrigação. |
| 2 Intermediário | Conhece a obrigação, mas não tem procedimento. |
| 3 Gerenciado | Procedimento definido, com prazo (3 dias úteis), responsável e modelos de comunicação. |
| 4 Otimizado | Nível 3 + procedimento testado em simulação. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Criar um procedimento de comunicação de incidentes à ANPD e aos responsáveis, com modelos prontos e responsável definido.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C27 · RS.MI-01 — Contenção de incidentes

**Pergunta:** Em um incidente, a instituição consegue conter o problema rapidamente (ex.: isolar uma máquina, bloquear uma conta, desligar um acesso)?

- Categoria: Técnico · Tipo: Corretivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: —
- Evidência sugerida: Procedimentos; contrato de suporte com SLA.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há meios ou conhecimento para conter. |
| 2 Intermediário | Contenção depende de um fornecedor externo, sem prazo definido. |
| 3 Gerenciado | Procedimentos de contenção documentados e pessoas capacitadas. |
| 4 Otimizado | Nível 3 + contenção parcialmente automatizada. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Documentar procedimentos de contenção (isolar máquina, bloquear conta) e garantir suporte com prazo definido.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C28 · RS.AN-03 — Análise de causa e lições aprendidas

**Pergunta:** Depois de um incidente, a instituição investiga a causa e registra o que vai mudar para evitar que se repita?

- Categoria: Administrativo · Tipo: Corretivo · Contexto: Todos os Dados · Peso: 1.2
- Base legal: —
- Evidência sugerida: Relatórios pós-incidente.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há análise; o problema é só resolvido. |
| 2 Intermediário | Análise informal, sem registro. |
| 3 Gerenciado | Análise de causa registrada, com ações de melhoria. |
| 4 Otimizado | Nível 3 + acompanhamento das ações até a conclusão. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Registrar a análise de causa de cada incidente e acompanhar as ações de melhoria até a conclusão.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

## Recover (Recuperar)

### C29 · RC.RP-01 — Execução do plano de recuperação e continuidade

**Pergunta:** A instituição tem um plano documentado e consegue acioná-lo para retomar atividades críticas quando a recuperação de um incidente é iniciada?

- Categoria: Administrativo · Tipo: Corretivo · Contexto: Dados Acadêmicos · Peso: 1.0
- Base legal: —
- Evidência sugerida: Plano de continuidade/recuperação; registros de acionamento e testes.

| Nível | Critério |
|---|---|
| 1 Inicial | Não há plano nem processo para iniciar a recuperação. |
| 2 Intermediário | Há ideias de contorno, sem plano documentado ou acionamento definido. |
| 3 Gerenciado | Plano documentado, com prioridades, tempos de recuperação, responsáveis e critérios de acionamento definidos. |
| 4 Otimizado | Nível 3 + execução testada periodicamente, com registro do acionamento e da retomada das atividades críticas. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Documentar e testar a execução do plano de recuperação, com critérios de acionamento, atividades prioritárias e tempo máximo aceitável de parada.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C30 · RC.RP-03 — Integridade dos backups antes da restauração

**Pergunta:** Antes de restaurar dados, a instituição verifica a integridade dos backups e dos demais recursos de restauração, inclusive nos testes periódicos?

- Categoria: Técnico · Tipo: Corretivo · Contexto: Dados Acadêmicos · Peso: 1.0
- Base legal: —
- Evidência sugerida: Registros de verificação de integridade e de testes de restauração.

| Nível | Critério |
|---|---|
| 1 Inicial | Não verifica a integridade e nunca testou restaurar os backups. |
| 2 Intermediário | Fez teste isolado, sem rotina ou verificação documentada de integridade. |
| 3 Gerenciado | Verificação de integridade antes da restauração e testes periódicos documentados. |
| 4 Otimizado | Nível 3 + verificação automatizada quando possível e validação dos dados restaurados e do tempo de recuperação. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Verificar a integridade antes de restaurar e testar periodicamente a recuperação, registrando integridade, resultado e tempo gasto.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

### C31 · RC.CO-03 — Comunicação com a comunidade escolar na recuperação

**Pergunta:** Durante a recuperação de um incidente, a instituição comunica a professores, alunos e famílias o que aconteceu e o andamento, por canais oficiais?

- Categoria: Administrativo · Tipo: Corretivo · Contexto: Dados de Menores · Peso: 1.5
- Base legal: LGPD Art. 48
- Evidência sugerida: Plano de comunicação; modelos de mensagem.

| Nível | Critério |
|---|---|
| 1 Inicial | Não comunica, ou comunica de forma desencontrada. |
| 2 Intermediário | Comunica de forma improvisada. |
| 3 Gerenciado | Responsável e canais oficiais definidos, com modelos de mensagem. |
| 4 Otimizado | Nível 3 + comunicação ensaiada em simulação. |
| — | Não se aplica (fica fora do cálculo) |

**Recomendação quando o nível for baixo:** Definir um porta-voz, os canais oficiais e modelos de mensagem para comunicar incidentes à comunidade escolar.

Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:

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
