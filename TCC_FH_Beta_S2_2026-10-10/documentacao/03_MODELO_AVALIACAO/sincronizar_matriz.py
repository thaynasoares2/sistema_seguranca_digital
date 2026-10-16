"""Renderiza CSV revisado em Markdown sem recriar ou sobrescrever o CSV."""
import argparse
import csv
from collections import Counter
from pathlib import Path

FUNCOES = {'GV': 'Govern (Governar)', 'ID': 'Identify (Identificar)', 'PR': 'Protect (Proteger)',
           'DE': 'Detect (Detectar)', 'RS': 'Respond (Responder)', 'RC': 'Recover (Recuperar)'}


def renderizar(csv_path):
    with csv_path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    counts = Counter(r['funcao'] for r in rows)
    out = ['# Matriz de Controles v0 — revisão técnica para a Fernanda', '',
           'Fonte: `MATRIZ_CONTROLES_v0.csv`. Revisão técnica assistida em 2026-10-10; versão de importação `v0.1`.', '',
           '**Prazo da revisão:** 2026-10-15 à noite. Fórmulas em `METODOLOGIA_SCORES.md`.', '',
           'Escala e pesos experimentais, aguardando validação acadêmica. Códigos CSF conferidos; os mapeamentos são adaptações, não equivalências normativas completas. Veja os limites na metodologia.', '',
           '## Como revisar', '',
           'Para cada controle, confira:', '',
           '1. **A pergunta** está clara para um gestor escolar sem formação técnica? (Etapa 1 e Etapa 3 do protocolo de validação do artigo.)',
           '2. **Os níveis 1 a 4** são objetivos o bastante para duas pessoas diferentes chegarem à mesma resposta?',
           '3. **Contexto, categoria e tipo** estão corretos? O contexto define o peso.',
           '4. **A recomendação** é uma ação concreta que a escola consegue executar?',
           '5. Algum controle sobra ou falta? Sugestões entram como C32, C33…', '',
           'Marque cada controle como ✅ ok, ✏️ ajustar (com o texto novo) ou ❌ remover.', '',
           'Não se aplica exige justificativa. Mandatório é prioridade do modelo acadêmico, não afirmação de obrigação jurídica universal. A escala 1–4 não representa automaticamente os Tiers do NIST.', '',
           '## Resumo', '', f'- **{len(rows)} controles** nas seis funções NIST.',
           f'- **{sum(r["rsdm"] == "sim" for r in rows)} controles RSDM**.',
           f'- **{sum(r["mandatorio"] == "sim" for r in rows)} mandatórios do modelo**.', '',
           '| Função | Controles | No RSDM |', '|---|---|---|']
    for f, name in FUNCOES.items():
        out.append(f'| {name} | {counts[f]} | {sum(r["rsdm"] == "sim" for r in rows if r["funcao"] == f)} |')
    out += ['', 'Pesos: Menores 1,5 · Sensíveis 1,3 · Todos 1,2 · Acadêmicos/Pesquisa 1,0; mandatórios × 1,5.', '']
    for funcao, name in FUNCOES.items():
        out += [f'## {name}', '']
        for r in [r for r in rows if r['funcao'] == funcao]:
            tags = ' '.join(tag for key, tag in [('mandatorio', '**MANDATÓRIO**'), ('rsdm', '**RSDM**')] if r[key] == 'sim')
            out += [f'### {r["id"]} · {r["codigo_csf"]} — {r["controle"]} {tags}'.rstrip(), '',
                    f'**Pergunta:** {r["pergunta"]}', '',
                    f'- Categoria: {r["categoria"]} · Tipo: {r["tipo_funcional"]} · Contexto: {r["contexto"]} · Peso: {r["peso"]}',
                    f'- Base legal: {r["base_legal"]}', f'- Evidência sugerida: {r["evidencia_sugerida"]}', '',
                    '| Nível | Critério |', '|---|---|']
            for n, campo in enumerate(['nivel_1_inicial', 'nivel_2_intermediario', 'nivel_3_gerenciado', 'nivel_4_otimizado'], 1):
                nome = ['Inicial', 'Intermediário', 'Gerenciado', 'Otimizado'][n-1]
                out.append(f'| {n} {nome} | {r[campo].replace(chr(124), chr(92)+chr(124))} |')
            out += ['| — | Não se aplica (fica fora do cálculo) |', '',
                    f'**Recomendação quando o nível for baixo:** {r["recomendacao"]}', '',
                    'Revisão: ☐ ✅ ok ☐ ✏️ ajustar ☐ ❌ remover — Observação:', '']
    metodologia = csv_path.with_name('METODOLOGIA_SCORES.md')
    if metodologia.exists() and '## Fontes consultadas' in metodologia.read_text():
        out.append('## Fontes consultadas' + metodologia.read_text().split('## Fontes consultadas', 1)[1])
    return '\n'.join(out).rstrip() + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', type=Path)
    parser.add_argument('--saida', required=True, type=Path)
    parser.add_argument('--substituir', action='store_true', help='Permite substituir MD; faça backup de anotações humanas antes.')
    args = parser.parse_args()
    if args.saida.resolve() == args.csv.resolve():
        parser.error('A saída não pode ser o CSV.')
    if args.saida.exists() and not args.substituir:
        parser.error('Saída existe; use outra saída para preservar anotações humanas.')
    args.saida.write_text(renderizar(args.csv), encoding='utf-8')
