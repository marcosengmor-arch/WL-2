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
| Reddit (reddit.com, old.reddit.com) | BLOQUEADO (proxy 403) | conteúdo alcançado indiretamente via resumos do WebSearch |
| Google Trends | BLOQUEADO (proxy 403) | substituído pelos prints do usuário (19/11/2026) e por cobertura de terceiros |
| TikTok, Instagram | BLOQUEADO (DNS/proxy) | cobertura indireta (imprensa, blogs, YouTube re-uploads) |
| Meta Ad Library, Google Ads Transparency | BLOQUEADO (403) | substituído por biblioteca de anúncios do usuário (print 19/11/2026) + landing pages e advertoriais indexados + reportagens |
| Google autocomplete / People Also Ask | BLOQUEADO | PAA capturado quando presente em resultados de busca |
| Amazon | parcial | prints do usuário + páginas indexadas via WebSearch |
| Playwright/Chromium | disponível, mas uso para raspagem de comentários foi negado pelo classificador de permissões | não usado |

Tentativa de ampliar a allowlist de rede via `update_environment` foi rejeitada pelo serviço. Nenhuma tentativa de contorno (headers falsos, mirrors, desativar TLS) foi feita.

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

## 7. Amostragem efetiva
Preenchido na consolidação (ver seção "Amostra efetiva" no 01_EXECUTIVE_SUMMARY.md e os CSVs em `data/`).

## 8. Arquivos
- `tools/yt_search.py` — coletor YouTube.
- `tools/COMMON_BRIEF.md` — brief comum aos subagentes.
- `raw/` — saídas brutas (JSONL) do coletor.
- `data/` — CSVs estruturados.
