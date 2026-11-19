# CONTEXTO COMUM A TODAS AS FRENTES (ler antes de começar)

DATA ATUAL: 2026-11-19. Janelas: 7d (desde 2026-11-12), 30d (desde 2026-10-20), 90d (desde 2026-08-21), 180d (desde 2026-05-23), 12m (desde 2025-11-19). Priorize 90d. Conteúdo mais antigo = "histórico" (marque assim), mesmo que ainda acumule views.

MERCADO: Estados Unidos. TODAS as buscas em inglês americano, com termos naturais usados pelas próprias consumidoras. Nada de Brasil/português nas buscas. Relatórios em português brasileiro, preservando citações originais em inglês.

AVATAR: mulheres norte-americanas 40–75 (segmentos 40–49, 50–59, 60–69, 70–75), insatisfeitas com o peso, já tentaram dietas/exercício/suplementos, sentem que ficou mais difícil depois dos 40, mencionam menopausa/perimenopausa/hormônios/cortisol/metabolismo/gordura abdominal, frustração por recuperar peso, céticas. Isso são HIPÓTESES: confirme, conteste e aprofunde com evidência. Não atribua idade/gênero a autores sem indicação confiável; marque "idade declarada" vs "pista contextual" vs "inferência incerta".

BENCHMARKS INTERNOS (já validados em campanhas anteriores da operação; NÃO são validação pública): formatos — programa de Jenna Bush Hager & Sheinelle Jones; podcast da Oprah; Hoda & Jenna; TODAY Show; entrevistas estilo podcast com Jillian Michaels. Ingredientes — Gelatin Trick, Baking Soda Trick. Verifique a situação ATUAL desses programas/formações (não presuma que continuam iguais). Procure o que vem DEPOIS deles.

DADOS JÁ COLETADOS PELO USUÁRIO (leia e cite como "Google Trends/Amazon/biblioteca de anúncios — print do usuário, 19/11/2026"): /home/user/WL-2/01-pesquisa/01-pesquisa-usuario-briefing.md

## FERRAMENTAS DISPONÍVEIS E LIMITES (verificados)
- WebSearch (modo "standard" barato; "extended" para nichos, recência e profundidade). É a ferramenta PRINCIPAL. Os resultados trazem resumos do conteúdo das páginas (incluindo threads do Reddit, artigos, notícias, cobertura de TikTok/Instagram, Google Trends reportado por terceiros). Faça MUITAS buscas (40–80 por frente), variando termos, adicionando "reddit", "site:reddit.com", nomes de subreddits, "2025", "2026", "November 2026", etc.
- YouTube: use o coletor público `python3 -I /home/user/WL-2/US_WEIGHT_LOSS_MARKET_INTELLIGENCE/tools/yt_search.py "query" FILTRO MAX` (FILTRO: any|week|month|year|views_week|views_month|views_year|date|views; MAX = nº de vídeos). Retorna JSON lines com videoId, title, channel, views, views_num, published (relativo, ex. "2w ago"), length, url, snippet. Rode várias queries e filtros. Salve a saída bruta em /home/user/WL-2/US_WEIGHT_LOSS_MARKET_INTELLIGENCE/raw/<frente>_<slug>.jsonl (use `>>`).
- BLOQUEADOS neste ambiente (proxy de rede recusa): reddit.com direto, trends.google.com, tiktok.com, instagram.com, Meta Ad Library e Google Ads Transparency diretos, Google autocomplete, páginas de vídeo do YouTube (comentários não acessíveis), pubmed direto. WebFetch só alcança youtube.com/facebook.com e devolve página vazia (JS). NÃO tente contornar (sem Playwright, sem headers falsos, sem mirrors, sem curl a hosts bloqueados). Use WebSearch para alcançar o conteúdo dessas fontes de forma indireta e REGISTRE a limitação no relatório.

## REGRAS DE EVIDÊNCIA (inegociáveis)
- Só registre citações que apareçam LITERALMENTE no output das ferramentas. Marque cada uma como QUOTE (verbatim) ou PARAPHRASE. Nunca invente comentário, número, data, URL, view count, métrica.
- Campo desconhecido = "n/d". Data de coleta = 2026-11-19.
- Diferencie claramente DADO / INTERPRETAÇÃO / HIPÓTESE.
- Para cada tendência: Emergente / Em aceleração / Consolidada / Saturada / Em declínio / Evidência insuficiente.
- Confiança: ALTA (múltiplas evidências independentes, recentes, diretamente relevantes) / MÉDIA / BAIXA.
- Para cada insight estratégico use: DESCOBERTA / EVIDÊNCIA (onde, links, dados) / INTERPRETAÇÃO / IMPLICAÇÃO PARA A VSL / CONFIANÇA.
- Views altas = atenção, não conversão. Não confunda popularidade com eficácia. Crenças populares não são fatos médicos.
- Referência criativa ≠ autorização de uso de imagem/voz/endosso. Nunca escreva falas inventadas atribuídas a pessoas reais.
- Metas numéricas são de cobertura: se não houver material, entregue o que foi efetivamente observado e informe a contagem real.

## ARQUIVOS
Pasta: /home/user/WL-2/US_WEIGHT_LOSS_MARKET_INTELLIGENCE/
- Seu relatório .md na raiz da pasta (nome indicado no seu brief).
- Seu CSV de fontes em data/<frente>_sources.csv com colunas EXATAS:
  id,url,platform,title,author,date_published,date_collected,metrics,excerpt,category,audience_segment,confidence,limitations,frente
  (id = prefixo da frente + número, ex. F1-001; excerpt sem quebras de linha; use aspas para campos com vírgula).
- CSVs adicionais indicados no seu brief em data/.
- Escreva arquivos com heredoc no Bash ou com a ferramenta Write. Use Python para gerar/validar CSVs quando houver muitas linhas.

## RETORNO FINAL (sua última mensagem para o coordenador)
Máximo 500 palavras: (1) 8–12 descobertas principais com confiança; (2) lista de arquivos escritos com contagem de linhas; (3) amostra efetiva (nº de buscas, nº de fontes únicas, nº de citações verbatim); (4) limitações e bloqueios.
