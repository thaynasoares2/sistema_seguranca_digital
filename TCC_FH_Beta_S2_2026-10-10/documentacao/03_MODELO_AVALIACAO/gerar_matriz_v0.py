"""Gera MATRIZ_CONTROLES_v0.csv (fonte) e MATRIZ_CONTROLES_v0.md (leitura) para o TCC FH."""
import csv
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

PESO_CONTEXTO = {
    "Dados de Menores": 1.5,
    "Dados Sensíveis": 1.3,
    "Todos os Dados": 1.2,
    "Dados Acadêmicos": 1.0,
    "Dados de Pesquisa": 1.0,
}
FATOR_MANDATORIO = 1.5

FUNCOES = {
    "GV": "Govern (Governar)",
    "ID": "Identify (Identificar)",
    "PR": "Protect (Proteger)",
    "DE": "Detect (Detectar)",
    "RS": "Respond (Responder)",
    "RC": "Recover (Recuperar)",
}

# (id, funcao, codigo_csf, controle, pergunta, categoria, tipo, contexto, base_legal,
#  mandatorio, rsdm, n1, n2, n3, n4, evidencia, recomendacao)
C = [
    ("C01", "GV", "GV.RR-02", "Encarregado (DPO) designado",
     "A instituição designou formalmente um Encarregado pelo Tratamento de Dados Pessoais (DPO), com identidade e contato publicados no site?",
     "Administrativo", "Preventivo", "Todos os Dados", "LGPD Art. 41",
     True, False,
     "Não há encarregado.",
     "Alguém responde pelo tema informalmente, sem nomeação ou sem contato publicado.",
     "Nomeação formal (portaria ou contrato) e contato publicado no site.",
     "Nível 3 + encarregado com tempo e recursos definidos, que presta contas à direção periodicamente.",
     "Ato de nomeação; página do site com o contato do encarregado.",
     "Nomear formalmente o encarregado e publicar a identidade e o canal de contato no site (LGPD Art. 41 §1º)."),
    ("C02", "GV", "GV.PO-01", "Política de Segurança da Informação (PSI)",
     "Existe uma Política de Segurança da Informação aprovada pela direção e comunicada a professores e funcionários?",
     "Administrativo", "Preventivo", "Todos os Dados", "LGPD Arts. 46 e 50",
     True, False,
     "Não existe PSI.",
     "Existe rascunho ou documento não aprovado ou não divulgado.",
     "PSI aprovada pela direção, divulgada e com ciência registrada dos colaboradores.",
     "Nível 3 + estrutura em três camadas (política, normas, procedimentos) revisada ao menos uma vez por ano.",
     "PSI assinada; registro de ciência; histórico de revisões.",
     "Aprovar uma PSI em três camadas (política, normas, procedimentos), divulgá-la e colher a ciência de todos os colaboradores."),
    ("C03", "GV", "GV.OC-03", "Obrigações legais mapeadas",
     "A instituição identificou e documentou as obrigações legais que se aplicam aos dados que trata, incluindo as regras específicas para crianças e adolescentes (LGPD e ECA)?",
     "Administrativo", "Preventivo", "Dados de Menores", "LGPD Art. 14; ECA Arts. 17 e 100",
     False, True,
     "As obrigações não foram levantadas.",
     "Conhecimento geral da LGPD, sem levantamento documentado.",
     "Levantamento documentado das obrigações (LGPD, ECA, contratos), com responsável definido.",
     "Nível 3 + revisão periódica diante de novas normas da ANPD.",
     "Documento de requisitos legais; parecer jurídico.",
     "Documentar as obrigações legais aplicáveis, com destaque para as regras de tratamento de dados de crianças e adolescentes."),
    ("C04", "GV", "GV.OC-03", "Base legal e consentimento parental para dados de menores",
     "Para cada tratamento de dados de alunos menores, a instituição definiu a base legal e, quando a base é o consentimento, coleta o consentimento específico e destacado de pelo menos um dos pais ou responsáveis?",
     "Administrativo", "Preventivo", "Dados de Menores", "LGPD Art. 14 §1º; Enunciado CD/ANPD nº 1/2023",
     False, True,
     "Não há definição de base legal; usa-se dado de aluno sem critério (ex.: fotos em redes sociais sem autorização).",
     "Termo genérico na matrícula, que cobre tudo de uma vez.",
     "Base legal definida por finalidade, com consentimento granular (por finalidade) quando aplicável e registrado.",
     "Nível 3 + responsáveis conseguem revogar o consentimento por canal simples, e a revogação é aplicada.",
     "Termos de consentimento por finalidade; registro das autorizações e revogações.",
     "Definir a base legal de cada tratamento de dados de alunos e substituir o termo genérico por consentimento granular por finalidade quando o consentimento for a base."),
    ("C05", "GV", "GV.SC-05", "Proteção de dados nos contratos com fornecedores",
     "Os contratos com fornecedores que tratam dados da instituição (sistema acadêmico, plataformas EdTech, nuvem) têm cláusulas de proteção de dados e segurança?",
     "Administrativo", "Preventivo", "Todos os Dados", "LGPD Arts. 39 e 42",
     False, False,
     "Contratos sem cláusulas de proteção de dados, ou uso de serviços sem contrato.",
     "Cláusulas genéricas em parte dos contratos.",
     "Todos os contratos relevantes têm cláusulas de proteção de dados, incidentes e devolução/eliminação.",
     "Nível 3 + avaliação periódica do cumprimento pelos fornecedores.",
     "Contratos e aditivos; lista de fornecedores que tratam dados.",
     "Incluir nos contratos cláusulas de proteção de dados, notificação de incidentes e eliminação de dados ao fim do serviço. A responsabilidade da escola não se transfere ao fornecedor."),
    ("C06", "GV", "GV.SC-06", "Avaliação de privacidade antes de adotar plataformas e apps (Privacy by Design)",
     "Antes de adotar uma nova plataforma ou aplicativo que use dados de alunos (inclusive os escolhidos por professores), a instituição avalia os riscos de privacidade e segurança?",
     "Administrativo", "Preventivo", "Dados de Menores", "LGPD Art. 46 §2º",
     False, True,
     "Cada professor adota as ferramentas que quiser, sem avaliação.",
     "Há avaliação só para sistemas grandes, ou de forma informal.",
     "Existe processo formal de avaliação e uma lista de ferramentas aprovadas.",
     "Nível 3 + reavaliação periódica das ferramentas aprovadas.",
     "Lista de ferramentas aprovadas; formulário de avaliação.",
     "Criar um processo de aprovação de ferramentas digitais, com avaliação de privacidade, e publicar uma lista de ferramentas aprovadas para os professores."),
    ("C07", "GV", "GV.OV-01", "Acompanhamento da direção",
     "A direção acompanha periodicamente os riscos e os resultados de segurança da informação (por exemplo, em reunião ou relatório ao menos semestral)?",
     "Administrativo", "Detectivo", "Todos os Dados", "LGPD Art. 50",
     False, False,
     "O tema não chega à direção.",
     "O tema chega à direção só quando há problema.",
     "Há reporte periódico à direção, com registro.",
     "Nível 3 + indicadores definidos e decisões de investimento baseadas neles.",
     "Atas; relatórios periódicos.",
     "Estabelecer um reporte semestral de segurança à direção, usando os indicadores deste sistema."),
    ("C08", "ID", "ID.AM-01", "Inventário de hardware",
     "A instituição mantém um inventário atualizado dos equipamentos (computadores, notebooks, servidores, equipamentos de rede)?",
     "Administrativo", "Preventivo", "Dados Acadêmicos", "—",
     False, False,
     "Não há inventário.",
     "Inventário parcial ou desatualizado (ex.: só patrimônio contábil).",
     "Inventário completo, com responsável e atualização regular.",
     "Nível 3 + inventário automatizado e conciliado com a rede.",
     "Planilha ou sistema de inventário com data de atualização.",
     "Montar e manter um inventário de equipamentos com responsável, localização e data de atualização."),
    ("C09", "ID", "ID.AM-02", "Inventário de software e serviços",
     "A instituição sabe quais softwares e serviços online são usados (incluindo plataformas pedagógicas e apps usados pelos professores)?",
     "Administrativo", "Preventivo", "Todos os Dados", "—",
     False, False,
     "Não há levantamento.",
     "Conhece os sistemas principais, mas não os serviços usados pelos professores.",
     "Inventário completo de softwares e serviços, com responsável.",
     "Nível 3 + revisão periódica e remoção do que não é mais usado.",
     "Lista de softwares e serviços.",
     "Levantar todos os softwares e serviços em uso, incluindo os pedagógicos, e definir um responsável por cada um."),
    ("C10", "ID", "ID.AM-07", "Inventário de dados pessoais (registro das operações)",
     "A instituição mantém um registro das operações de tratamento de dados pessoais, identificando onde estão os dados de menores e os dados sensíveis (ex.: laudos, saúde)?",
     "Administrativo", "Preventivo", "Dados de Menores", "LGPD Art. 37",
     False, True,
     "Não há registro.",
     "Registro parcial, sem identificar dados de menores ou dados sensíveis.",
     "Registro completo (ROPA), com finalidade, base legal, local e prazo de retenção.",
     "Nível 3 + registro revisado sempre que surge um novo tratamento.",
     "ROPA.",
     "Elaborar o registro das operações de tratamento (ROPA), destacando os dados de menores e os dados sensíveis."),
    ("C11", "ID", "ID.RA-01", "Identificação de vulnerabilidades e atualizações",
     "A instituição verifica regularmente vulnerabilidades e mantém sistemas e equipamentos atualizados?",
     "Técnico", "Detectivo", "Todos os Dados", "LGPD Art. 46",
     False, False,
     "Não há verificação; há sistemas sem suporte do fabricante.",
     "Atualizações feitas de forma esporádica, sem verificação de vulnerabilidades.",
     "Atualizações regulares e verificação periódica de vulnerabilidades, com registro.",
     "Nível 3 + priorização por risco e prazos definidos para correção.",
     "Relatórios de varredura; histórico de atualizações.",
     "Implantar uma rotina mensal de atualizações e uma verificação periódica de vulnerabilidades, substituindo sistemas sem suporte."),
    ("C12", "ID", "ID.RA-05", "Relatório de impacto (RIPD/DPIA)",
     "Para tratamentos de maior risco (dados de menores, dados sensíveis, monitoramento por câmeras), a instituição avalia o impacto à proteção de dados?",
     "Administrativo", "Preventivo", "Dados de Menores", "LGPD Arts. 5º XVII e 38",
     False, True,
     "Não há avaliação de impacto.",
     "Avaliação informal, sem documento.",
     "RIPD elaborado para os tratamentos de maior risco.",
     "Nível 3 + RIPD revisado quando o tratamento muda.",
     "RIPD.",
     "Elaborar o RIPD para os tratamentos de maior risco, a começar pelos que envolvem dados de crianças e adolescentes."),
    ("C13", "PR", "PR.AA-01", "Gestão de identidades e contas",
     "Cada pessoa tem conta individual nos sistemas, e as contas são criadas e removidas quando alguém entra ou sai da instituição (alunos, professores, funcionários)?",
     "Técnico", "Preventivo", "Dados Sensíveis", "LGPD Art. 46",
     False, False,
     "Há contas compartilhadas, e as contas de quem saiu continuam ativas.",
     "Contas individuais, mas a remoção depende de lembrança.",
     "Processo formal de criação e remoção, ligado à matrícula e ao desligamento.",
     "Nível 3 + revisão periódica das contas ativas.",
     "Procedimento; lista de contas comparada com a lista de pessoas ativas.",
     "Eliminar contas compartilhadas e vincular a remoção de contas ao processo de desligamento e de fim de matrícula."),
    ("C14", "PR", "PR.AA-03", "Autenticação multifator (MFA)",
     "Os sistemas críticos (sistema acadêmico, e-mail, financeiro) exigem autenticação multifator?",
     "Técnico", "Preventivo", "Dados Sensíveis", "LGPD Art. 46",
     False, False,
     "Só senha.",
     "MFA disponível, mas opcional ou só para alguns usuários.",
     "MFA obrigatório para todos os acessos administrativos e para o e-mail.",
     "Nível 3 + MFA resistente a phishing para administradores.",
     "Configuração dos sistemas; relatório de adesão ao MFA.",
     "Tornar o MFA obrigatório no e-mail e nos sistemas acadêmico e financeiro, começando pelas contas administrativas."),
    ("C15", "PR", "PR.AA-05", "Acesso por perfil e menor privilégio",
     "O acesso aos dados de alunos é limitado ao necessário para cada função (ex.: o professor vê só as suas turmas, a secretaria não vê dados de saúde sem necessidade)?",
     "Técnico", "Preventivo", "Dados de Menores", "LGPD Arts. 6º III e 46",
     False, True,
     "Todos acessam tudo.",
     "Há perfis, mas amplos demais.",
     "Perfis definidos por função (RBAC), seguindo o menor privilégio.",
     "Nível 3 + revisão periódica das permissões.",
     "Matriz de perfis e permissões; relatório de acessos.",
     "Definir perfis de acesso por função (RBAC) e restringir o acesso a dados de alunos ao mínimo necessário."),
    ("C16", "PR", "PR.DS-01", "Proteção de dados armazenados",
     "Os dados de alunos armazenados (bancos de dados, notebooks, arquivos com laudos e fichas) estão protegidos por criptografia ou controle equivalente?",
     "Técnico", "Preventivo", "Dados de Menores", "LGPD Art. 46",
     False, True,
     "Dados sem proteção, inclusive em notebooks e pen drives.",
     "Proteção só em parte dos locais.",
     "Criptografia nos bancos de dados e nos dispositivos que guardam dados de alunos.",
     "Nível 3 + gestão de chaves e verificação periódica.",
     "Configuração de criptografia; política de uso de dispositivos.",
     "Ativar a criptografia nos bancos de dados e nos notebooks que armazenam dados de alunos, e proibir o uso de pen drives sem proteção."),
    ("C17", "PR", "PR.DS-11", "Backups",
     "A instituição faz backups regulares dos dados importantes, com pelo menos uma cópia protegida contra ransomware (offline ou imutável)?",
     "Técnico", "Corretivo", "Dados Acadêmicos", "LGPD Art. 46",
     False, False,
     "Não há backup.",
     "Backup existe, mas fica na mesma rede ou não é regular.",
     "Backups regulares, com cópia offline ou imutável.",
     "Nível 3 + backups monitorados e testados periodicamente.",
     "Política de backup; registros das execuções.",
     "Implantar backups regulares na regra 3-2-1, com uma cópia offline ou imutável."),
    ("C18", "PR", "PR.IR-01", "Segmentação da rede",
     "A rede é separada por finalidade (administrativa, pedagógica, alunos/visitantes), de modo que um aparelho de visitante não alcance os sistemas administrativos?",
     "Técnico", "Preventivo", "Todos os Dados", "LGPD Art. 46",
     False, False,
     "Uma rede só para todos.",
     "Wi-Fi de visitantes separado, mas a rede interna não é segmentada.",
     "Redes segmentadas por VLAN, com regras de firewall entre elas.",
     "Nível 3 + regras revisadas periodicamente.",
     "Diagrama de rede; configuração de VLANs e do firewall.",
     "Segmentar a rede em VLANs (administrativa, pedagógica, visitantes) com regras de firewall entre elas."),
    ("C19", "PR", "PR.AT-01", "Conscientização e treinamento",
     "Professores e funcionários recebem orientação periódica sobre segurança e proteção de dados (ex.: phishing, uso de dados de alunos)?",
     "Administrativo", "Preventivo", "Todos os Dados", "LGPD Art. 50 §2º",
     False, False,
     "Não há orientação.",
     "Orientação esporádica, sem registro.",
     "Treinamento anual com registro de participação.",
     "Nível 3 + simulações de phishing e medição de resultados.",
     "Lista de presença; material; resultados de simulações.",
     "Instituir um treinamento anual sobre segurança e proteção de dados, com registro de participação."),
    ("C20", "PR", "PR.AA-06", "Controle de acesso físico",
     "O acesso físico a locais com dados sensíveis (secretaria, sala de servidores, arquivos de prontuários e fichas) é controlado?",
     "Físico", "Preventivo", "Dados Sensíveis", "LGPD Art. 46",
     False, False,
     "Locais abertos, sem controle.",
     "Há chaves ou trancas, mas sem controle de quem acessa.",
     "Acesso restrito a pessoas autorizadas, com controle de chaves ou crachá.",
     "Nível 3 + registro de acesso e revisão periódica.",
     "Controle de chaves; registros de acesso.",
     "Restringir o acesso físico à secretaria, ao arquivo e à sala de servidores, e controlar quem tem chaves."),
    ("C21", "DE", "DE.CM-01", "Monitoramento da rede",
     "A rede é monitorada para identificar tráfego ou acessos anormais?",
     "Técnico", "Detectivo", "Dados de Pesquisa", "—",
     False, False,
     "Não há monitoramento.",
     "Monitoramento só de disponibilidade (se a internet está funcionando).",
     "Monitoramento de segurança com alertas definidos.",
     "Nível 3 + alertas analisados continuamente e regras ajustadas.",
     "Ferramenta de monitoramento; exemplos de alertas.",
     "Ativar o monitoramento de segurança da rede (logs do firewall com alertas) e definir quem analisa os alertas."),
    ("C22", "DE", "DE.CM-03", "Registro de acessos a dados de alunos",
     "Os sistemas registram quem acessou ou alterou dados de alunos, e esses registros são consultados quando necessário?",
     "Técnico", "Detectivo", "Dados de Menores", "LGPD Arts. 37 e 46",
     False, True,
     "Não há registro de acessos.",
     "Há registros, mas ninguém os consulta, ou eles são apagados rapidamente.",
     "Registros mantidos por prazo definido e consultados em caso de suspeita.",
     "Nível 3 + revisão periódica e alertas para acessos fora do padrão.",
     "Exemplo de log de acesso; política de retenção de logs.",
     "Ativar e reter os registros de acesso aos dados de alunos, definindo prazo de retenção e quem os revisa."),
    ("C23", "DE", "DE.CM-09", "Antimalware nas estações",
     "Os computadores (inclusive os dos laboratórios) têm proteção antimalware ativa e atualizada?",
     "Técnico", "Detectivo", "Todos os Dados", "LGPD Art. 46",
     False, False,
     "Sem proteção em parte relevante das máquinas.",
     "Proteção instalada, mas sem gestão central nem verificação de atualização.",
     "Proteção em todas as máquinas, com gestão central.",
     "Nível 3 + EDR com resposta automatizada.",
     "Console de gestão do antimalware.",
     "Garantir antimalware ativo e atualizado em todas as máquinas, com gestão centralizada."),
    ("C24", "DE", "DE.AE-02", "Análise de eventos suspeitos",
     "Quando surge um alerta ou um relato suspeito (ex.: e-mail de phishing, conta bloqueada), alguém analisa e registra o caso?",
     "Administrativo", "Detectivo", "Todos os Dados", "—",
     False, False,
     "Ninguém é responsável; os alertas são ignorados.",
     "Análise informal, sem registro.",
     "Responsável definido, canal de reporte conhecido e registro das análises.",
     "Nível 3 + análise com prazos definidos e indicadores.",
     "Canal de reporte; registros de análise.",
     "Definir um responsável e um canal único para reportar suspeitas, e registrar cada análise."),
    ("C25", "RS", "RS.MA-01", "Plano de resposta a incidentes",
     "A instituição tem um plano de resposta a incidentes, com responsáveis e etapas definidos, que já foi testado ou usado?",
     "Administrativo", "Corretivo", "Todos os Dados", "LGPD Art. 46",
     False, False,
     "Não há plano.",
     "Plano informal, que existe só na cabeça de alguém.",
     "Plano documentado, com papéis e as seis fases do ciclo de resposta.",
     "Nível 3 + plano testado em simulação ao menos uma vez por ano.",
     "Plano de resposta; registro de simulações.",
     "Documentar um plano de resposta a incidentes com papéis definidos e testá-lo em simulação anual."),
    ("C26", "RS", "RS.CO-02", "Comunicação de incidentes à ANPD e aos responsáveis",
     "A instituição sabe quando e como comunicar um incidente com dados pessoais à ANPD e aos titulares (no caso de alunos menores, aos pais ou responsáveis)?",
     "Administrativo", "Corretivo", "Dados de Menores", "LGPD Art. 48; Resolução CD/ANPD nº 15/2024",
     False, True,
     "Não sabe que existe essa obrigação.",
     "Conhece a obrigação, mas não tem procedimento.",
     "Procedimento definido, com prazo (3 dias úteis), responsável e modelos de comunicação.",
     "Nível 3 + procedimento testado em simulação.",
     "Procedimento de comunicação; modelos de comunicado.",
     "Criar um procedimento de comunicação de incidentes à ANPD e aos responsáveis, com modelos prontos e responsável definido."),
    ("C27", "RS", "RS.MI-01", "Contenção de incidentes",
     "Em um incidente, a instituição consegue conter o problema rapidamente (ex.: isolar uma máquina, bloquear uma conta, desligar um acesso)?",
     "Técnico", "Corretivo", "Todos os Dados", "—",
     False, False,
     "Não há meios ou conhecimento para conter.",
     "Contenção depende de um fornecedor externo, sem prazo definido.",
     "Procedimentos de contenção documentados e pessoas capacitadas.",
     "Nível 3 + contenção parcialmente automatizada.",
     "Procedimentos; contrato de suporte com SLA.",
     "Documentar procedimentos de contenção (isolar máquina, bloquear conta) e garantir suporte com prazo definido."),
    ("C28", "RS", "RS.AN-03", "Análise de causa e lições aprendidas",
     "Depois de um incidente, a instituição investiga a causa e registra o que vai mudar para evitar que se repita?",
     "Administrativo", "Corretivo", "Todos os Dados", "—",
     False, False,
     "Não há análise; o problema é só resolvido.",
     "Análise informal, sem registro.",
     "Análise de causa registrada, com ações de melhoria.",
     "Nível 3 + acompanhamento das ações até a conclusão.",
     "Relatórios pós-incidente.",
     "Registrar a análise de causa de cada incidente e acompanhar as ações de melhoria até a conclusão."),
    ("C29", "RC", "RC.RP-01", "Plano de recuperação e continuidade",
     "Existe um plano para manter ou retomar atividades críticas se os sistemas ficarem fora do ar (ex.: em período de matrícula ou de provas)?",
     "Administrativo", "Corretivo", "Dados Acadêmicos", "—",
     False, False,
     "Não há plano.",
     "Há ideias de contorno, sem documento.",
     "Plano documentado, com prioridades e tempos de recuperação definidos.",
     "Nível 3 + plano testado periodicamente.",
     "Plano de continuidade/recuperação.",
     "Documentar um plano de recuperação com as atividades prioritárias e o tempo máximo aceitável de parada."),
    ("C30", "RC", "RC.RP-03", "Teste de restauração dos backups",
     "A instituição já testou restaurar dados a partir do backup e verifica a integridade dos backups antes de usá-los?",
     "Técnico", "Corretivo", "Dados Acadêmicos", "—",
     False, False,
     "Nunca testou.",
     "Testou uma vez, sem rotina.",
     "Testes periódicos de restauração, com registro.",
     "Nível 3 + tempo de restauração medido e dentro do plano.",
     "Registros de testes de restauração.",
     "Instituir um teste de restauração de backup ao menos semestral, com registro do resultado e do tempo gasto."),
    ("C31", "RC", "RC.CO-03", "Comunicação com a comunidade escolar na recuperação",
     "Durante a recuperação de um incidente, a instituição comunica a professores, alunos e famílias o que aconteceu e o andamento, por canais oficiais?",
     "Administrativo", "Corretivo", "Dados de Menores", "LGPD Art. 48",
     False, False,
     "Não comunica, ou comunica de forma desencontrada.",
     "Comunica de forma improvisada.",
     "Responsável e canais oficiais definidos, com modelos de mensagem.",
     "Nível 3 + comunicação ensaiada em simulação.",
     "Plano de comunicação; modelos de mensagem.",
     "Definir um porta-voz, os canais oficiais e modelos de mensagem para comunicar incidentes à comunidade escolar."),
]

CAMPOS = ["id", "funcao", "codigo_csf", "controle", "pergunta", "categoria", "tipo_funcional",
          "contexto", "base_legal", "mandatorio", "rsdm", "nivel_1_inicial", "nivel_2_intermediario",
          "nivel_3_gerenciado", "nivel_4_otimizado", "evidencia_sugerida", "recomendacao", "peso"]


def peso(contexto, mandatorio):
    return round(PESO_CONTEXTO[contexto] * (FATOR_MANDATORIO if mandatorio else 1.0), 2)


linhas = []
for c in C:
    assert len(c) == 17, c[0]
    d = dict(zip(CAMPOS[:-1], c))
    assert d["contexto"] in PESO_CONTEXTO, d["id"]
    d["peso"] = peso(d["contexto"], d["mandatorio"])
    linhas.append(d)

with open(OUT / "MATRIZ_CONTROLES_v0.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=CAMPOS)
    w.writeheader()
    for d in linhas:
        row = dict(d)
        row["mandatorio"] = "sim" if d["mandatorio"] else "não"
        row["rsdm"] = "sim" if d["rsdm"] else "não"
        w.writerow(row)

md = []
md.append("# Matriz de Controles v0 — rascunho para revisão da Fernanda\n")
md.append("Gerado a partir de `MATRIZ_CONTROLES_v0.csv`, que é a fonte que o sistema importa. "
          "Revise neste arquivo e anote as mudanças; elas serão levadas ao CSV.\n")
md.append("**Prazo da revisão:** quinta-feira, 15/10/2026, à noite.\n")
md.append("As fórmulas de peso, scores e RSDM estão em `METODOLOGIA_SCORES.md`. "
          "Os códigos NIST CSF 2.0 e os artigos de lei citados ainda precisam ser conferidos no texto original antes da versão final.\n")
md.append("## Como revisar\n")
md.append("Para cada controle, confira:\n")
md.append("1. **A pergunta** está clara para um gestor escolar sem formação técnica? (Etapa 1 e Etapa 3 do protocolo de validação do artigo.)")
md.append("2. **Os níveis 1 a 4** são objetivos o bastante para duas pessoas diferentes chegarem à mesma resposta?")
md.append("3. **Contexto, categoria e tipo** estão corretos? O contexto define o peso.")
md.append("4. **A recomendação** é uma ação concreta que a escola consegue executar?")
md.append("5. Algum controle sobra ou falta? Sugestões entram como C32, C33…\n")
md.append("Marque cada controle como ✅ ok, ✏️ ajustar (com o texto novo) ou ❌ remover.\n")

tot = len(linhas)
n_rsdm = sum(d["rsdm"] for d in linhas)
md.append("## Resumo\n")
md.append(f"- **{tot} controles** distribuídos pelas 6 funções do NIST CSF 2.0.")
md.append(f"- **{n_rsdm} controles compõem o RSDM** (Risk Score para Dados de Menores).")
md.append("- **2 controles mandatórios** (DPO e PSI), como define o artigo para a função Govern.")
md.append("- Os códigos seguem o **NIST CSF 2.0**. O artigo usa códigos do CSF 1.1 na Tabela 1; a correspondência está em `METODOLOGIA_SCORES.md`.\n")
md.append("| Função | Controles | No RSDM |")
md.append("|---|---|---|")
for f_, nome in FUNCOES.items():
    fs = [d for d in linhas if d["funcao"] == f_]
    md.append(f"| {nome} | {len(fs)} | {sum(d['rsdm'] for d in fs)} |")
md.append("")
md.append("Pesos por contexto: " + " · ".join(f"{k} {v}" for k, v in PESO_CONTEXTO.items())
          + f". Controles mandatórios × {FATOR_MANDATORIO}.\n")

for f_, nome in FUNCOES.items():
    md.append(f"## {nome}\n")
    for d in [x for x in linhas if x["funcao"] == f_]:
        tags = []
        if d["mandatorio"]:
            tags.append("**MANDATÓRIO**")
        if d["rsdm"]:
            tags.append("**RSDM**")
        md.append(f"### {d['id']} · {d['codigo_csf']} — {d['controle']} {' '.join(tags)}\n")
        md.append(f"**Pergunta:** {d['pergunta']}\n")
        md.append(f"- Categoria: {d['categoria']} · Tipo: {d['tipo_funcional']} · Contexto: {d['contexto']} · Peso: {d['peso']}")
        md.append(f"- Base legal: {d['base_legal']}")
        md.append(f"- Evidência sugerida: {d['evidencia_sugerida']}\n")
        md.append("| Nível | Critério |")
        md.append("|---|---|")
        md.append(f"| 1 Inicial | {d['nivel_1_inicial']} |")
        md.append(f"| 2 Intermediário | {d['nivel_2_intermediario']} |")
        md.append(f"| 3 Gerenciado | {d['nivel_3_gerenciado']} |")
        md.append(f"| 4 Otimizado | {d['nivel_4_otimizado']} |")
        md.append("| — | Não se aplica (fica fora do cálculo) |\n")
        md.append(f"**Recomendação quando o nível for baixo:** {d['recomendacao']}\n")
        md.append("Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:\n")

(OUT / "MATRIZ_CONTROLES_v0.md").write_text("\n".join(md), encoding="utf-8")
print(f"{tot} controles, {n_rsdm} RSDM")
for f_ in FUNCOES:
    print(f_, sum(1 for d in linhas if d["funcao"] == f_))
