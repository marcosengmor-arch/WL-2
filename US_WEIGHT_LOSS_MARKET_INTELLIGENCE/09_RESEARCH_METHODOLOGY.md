# 09 — Metodologia de Pesquisa

**Projeto:** US Weight Loss Market Intelligence — VSL para mulheres norte-americanas 40–75
**Data de execução:** 19 de novembro de 2026
**Ambiente:** Claude Code (sessão em nuvem), coordenador + 5 subagentes de pesquisa em paralelo + 1 etapa de síntese (Big Ideas) + consolidação.

## 1. Janelas temporais

| Janela | Início | Uso |
|---|---|---|
| 7 dias | 2026-11-12 | sinais extremamente recentes |
| 30 dias | 2026-10-20 | tendências em aceleração |
| 90 dias | 2026-08-21 | tendências atuais com sustentação (prioridade) |
| 180 dias | 2026-05-23 | crescimento e maturação |
| 12 meses | 2025-11-19 | comparação histórica |

Conteúdo anterior a 12 meses é marcado como **histórico**, mesmo quando ainda acumula visualizações.

## 2. Ferramentas e acesso (verificado em 19/11/2026)

| Fonte / ferramenta | Status | Como foi usada |
|---|---|---|
| WebSearch (busca web, EUA, inglês) | OK | ferramenta principal de todas as frentes; modos standard e extended |
| YouTube — página pública de resultados de busca | OK | coletor `tools/yt_search.py` (parse de `ytInitialData`): título, canal, views, data relativa, duração, snippet; filtros por período e ordenação por views |
| YouTube — página do vídeo e comentários | BLOQUEADO | página redireciona para host de consentimento fora da allowlist; comentários não acessíveis |
| Reddit (reddit.com, old.reddit.com) | BLOQUEADO (proxy 403 no início; após liberação, o próprio Reddit devolve 403 a scripts e redireciona old.reddit; a leitura via navegador headless foi negada pelo classificador de permissões da sessão; o rastreador do WebSearch também não acessa reddit.com) | conteúdo alcançado só indiretamente (estudo JAMA/UMD, citações em imprensa) — **0 threads lidas** |
| Google Trends | BLOQUEADO no início; LIBERADO pelo usuário às ~22:30 UTC | coletor `tools/trends_collect.py` (pytrends, geo US, 3m/12m + related queries, com pausas de 7–14 s e retentativas em 429); 3 lotes: ingredientes (30 termos), avatar/hosts (24), nicho (20). Antes da liberação, prints do usuário (19/11/2026) e cobertura de terceiros |
| TikTok, Instagram | BLOQUEADO no início; liberados depois, mas as páginas públicas não expõem dados sem JS/login | cobertura indireta (imprensa, blogs, YouTube re-uploads) |
| Meta Ad Library, Google Ads Transparency | BLOQUEADO (403) | substituído por biblioteca de anúncios do usuário (print 19/11/2026) + landing pages e advertoriais indexados + reportagens |
| Google autocomplete / People Also Ask | BLOQUEADO | PAA capturado quando presente em resultados de busca |
| Amazon | parcial | prints do usuário + páginas indexadas via WebSearch |
| Playwright/Chromium | disponível, mas uso para raspagem de comentários foi negado pelo classificador de permissões | não usado |

Tentativa de ampliar a allowlist via `update_environment` foi rejeitada pelo serviço; o usuário liberou os hosts manualmente durante a sessão. Nenhuma tentativa de contorno (headers falsos, mirrors, desativar TLS) foi feita; duas tentativas de leitura via navegador headless (YouTube comentários, Reddit) foram negadas pelo classificador de permissões e não repetidas.

## 3. Hierarquia de fontes
1. Comentários originais de consumidoras (Reddit, reviews, comentários citados).
2. Vídeos e publicações originais (YouTube, podcasts, programas).
3. Dados públicos diretamente observáveis (views, datas, contagens).
4. Pesquisas e relatórios confiáveis (Google Trends, Pew, Gallup, KFF, Circana, Spate).
5. Estudos revisados por pares (PubMed via WebSearch, Examine).
6. Notícias e análises secundárias.

## 4. Regras de evidência
- Citações marcadas como **QUOTE** (verbatim no output da ferramenta) ou **PARAPHRASE**.
- Nenhum número, data, URL ou métrica inventada; campo desconhecido = `n/d`.
- Views = atenção, não conversão. Popularidade ≠ eficácia. Crença popular ≠ fato médico.
- Idade/gênero: "declarada" vs "pista contextual" vs "inferência incerta".
- Status de tendência: Emergente / Em aceleração / Consolidada / Saturada / Em declínio / Evidência insuficiente.
- Confiança: ALTA / MÉDIA / BAIXA.
- Níveis de validação competitiva: 1 Existência, 2 Continuidade, 3 Escala aparente, 4 Resultado comercial.

## 5. Critérios de inclusão / exclusão
- Inclusão: conteúdo em inglês, público dos EUA (ou sem marca de país quando a plataforma é predominantemente US), relacionado a emagrecimento feminino 40+, com URL verificável.
- Exclusão: conteúdo claramente não-US (UK/AU marcados quando usados como apoio), spam/bots, conteúdo comercial disfarçado sem sinalização, republicações sem atribuição.

## 6. Fórmulas de pontuação
- **Formatos (0–100):** 25% relevância 40+; 20% engajamento observável; 20% recência/trajetória; 20% utilidade narrativa; 15% diferenciação vs benchmarks internos.
- **Ingredientes (0–100):** 20% crescimento; 15% conversa espontânea; 15% curiosidade; 15% fit 40+; 10% novidade; 10% demonstrabilidade; 15% sustentação científica/segurança. Segurança é eliminatória.
- **Combinações VSL (0–100):** 20% alinhamento dores/desejos; 20% momentum; 15% familiaridade/credibilidade do formato; 15% diferenciação; 15% curiosidade/storytelling; 15% viabilidade verificável e segura.

## 7. Amostragem efetiva (consolidada)

| Frente | Buscas web | Consultas YouTube | Fontes únicas | Verbatim | Observações |
|---|---|---|---|---|---|
| F0 coordenador | 9 | 8 (hot list 7d) | 14 | — | contexto macro |
| F1 Voz da consumidora | 35 efetivas (46 tentadas) | 35 | 235 | 73 | 0 Reddit direto; 0 comentários YouTube |
| F2 Formatos | 10 (cota esgotada) | 123 (1.156 vídeos únicos) | 129 | 17 | likes/comentários n/d |
| F3 Ingredientes | 25 (+3 negadas) | 120 + 120 velocidade | 145 | 9 | PubMed inacessível |
| F4 Hosts/experts | 50 | 40 (292 vídeos) | 82 | ~12 | credenciais autodeclaradas |
| F5 Concorrência | 55 | 55 (327 vídeos) | 97 | 21 | ad libraries bloqueadas; dados do usuário = Nível 3 |
| **Total** | **~184 web + 9** | **~500** | **645 únicas (após dedupe por URL)** | **~130** | cota de WebSearch compartilhada (200/turno) esgotou em F1, F2, F3 e F5 |

Metas não atingidas: 150 comentários Reddit (0), 300 comentários YouTube (0), 50 interações de outras redes (23). Metas atingidas: ≥30 expressões verbatim (73), 40 vídeos + 20 segmentos (109), 20 ingredientes (41), 20 personalidades (61), 15 concorrentes (40).

Critérios de exclusão aplicados: fóruns UK/AU marcados "non-US" e usados só como linguagem; sites de scam-review/afiliados usados só quando confirmados por Snopes/BBB/imprensa/tribunais; advertoriais pagos em newswire tratados como material do anunciante.

## 8. Arquivos
- `tools/yt_search.py` — coletor YouTube.
- `tools/trends_collect.py` — coletor Google Trends (pytrends, paced).
- `tools/merge_sources.py` — consolida `data/F*_sources.csv` em `SOURCES_DATABASE.csv`.
- `tools/build_dashboard.py` — gera `EXECUTIVE_DASHBOARD.html` a partir dos CSVs.
- `tools/COMMON_BRIEF.md` — brief comum aos subagentes.
- `raw/` — saídas brutas (JSONL) do coletor.
- `data/` — CSVs estruturados.
