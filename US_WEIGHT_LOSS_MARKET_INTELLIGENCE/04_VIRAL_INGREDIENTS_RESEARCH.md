# FRENTE 03 — INGREDIENTES VIRAIS E TENDÊNCIAS NATURAIS
**Mercado:** EUA · **Avatar:** mulheres 40–75 insatisfeitas com o peso · **Data de coleta:** 2026-11-19 · **Janela prioritária:** 90d (desde 2026-08-21)
**Arquivos irmãos:** `data/INGREDIENT_TRENDS.csv` (41 linhas, 34 colunas, com componentes de nota) · `data/F3_sources.csv` (145 fontes) · `raw/F3_*.jsonl` (675 linhas brutas do YouTube, 120 queries + 40 termos × 3 filtros de velocidade)

> Convenções: **DATA** = observado literalmente no output das ferramentas · **INTERPRETAÇÃO** = leitura minha · **HIPÓTESE** = a testar. Citações marcadas **QUOTE** (verbatim) ou **PARAPHRASE**. "n/d" = não disponível. Views = atenção, não conversão. Crença popular ≠ fato médico.

---

## 0. Sumário executivo (10 linhas)

1. **O "Gelatin Trick" está saturado no lado dos anúncios e já em declínio no orgânico.** 10 das 20 VSLs mais escaladas do print usam gelatina; Snopes (24/abr/2026) classificou como scam; no YouTube, as únicas produções novas (últimos 30 dias) são uma content farm brasileira com 20–68 views por vídeo e duas **mutações** ("Korean Pink Gelatin Trick for Firmer Skin", "Horse Gelatin Trick – salt tonic for men"). O pico de busca "+120% bariatric gelatin recipe" (7d) é resíduo do gasto em mídia, não curiosidade nova. Confiança ALTA.
2. **O "Baking Soda Shot" é mais novo (abril/2026) e ainda ativo em anúncios (Sodatide, 13/ago), mas a busca de 7 dias já cai (-6% a -10%)** e o mecanismo está migrando para o nicho masculino ("baking soda trick for men in the shower", "honey + baking soda for men"). Eliminado como ingrediente central por **segurança** (sódio, alcalose) e porque só funciona com endosso deepfake (Oprah/Dra. Jastreboff/"Jenna & Sheinelle"). Confiança ALTA.
3. **O que vem depois (pré-pico, orgânico, sem VSL ainda):** (a) **creatina para mulheres 40+** — 6,1M views (Diary of a CEO), 3,85M ("dei creatina para minha mãe de 70"), 3,66M (Berg, "após os 50"), 11 vídeos novos em 30d, gummies "for women over 40" chegando ao varejo, zero VSL; (b) **fibra/psyllium "1 colher antes das refeições"** com rótulo "GLP-1 Friendly" já na Amazon (Metamucil 70K+/mês) e vídeos novos nesta semana; (c) **black seed oil**, com salto em novembro/2026 (Berg 385k em 1 dia, DeLauer 323k) e um produto (Resilia) sendo semeado em canais de mulheres 50+; (d) **cortisol cocktail**, a única bebida "ritual" com busca em aceleração (+80% 7d, "Grande aumento" 30d) e produtos prontos surgindo (Nature Aurora, Loroc'e, Harmonia).
4. **A narrativa mãe não é um ingrediente: é "menopausa/cortisol/metabolismo após os 40".** Um vídeo ("Menopause Weight Gain Wasn't a Thing in 1945 — What Changed?") fez **1,58M views em 7 dias**; "does your metabolism slow down as you get older" +200% (print). Todo ingrediente candidato deve ser embalado nessa narrativa.
5. **"Natural GLP-1" é o frame dominante e já está em anúncio** (VSL #5 "GLP-1 Reset", #8 "GLP-1 Natural com Gelatina"); como frame segue forte, mas o nome "GLP-1" como mecanismo central está em saturação média-alta.
6. **Ciclo de vida observado das "tricks" ad-driven:** nasce em VSL → blogs de receita (SEO farms em subdomínios .edu) → vídeos "explicador/afiliado" (Bastideon, Trafity, Odilon Huamani) → fact-checks (Snopes, Jordan Liles, myantispyware, Dr. Jen Caudle) → mutação para outro nicho (homens, pele, neuropatia) → declínio. Gelatina está na fase 5; baking soda na fase 4; pink salt na fase 5/6.
7. **Nenhuma das bebidas virais tem evidência de perda de gordura.** As únicas famílias com suporte moderado são proteína (cottage cheese, protein jello), fibra solúvel (psyllium/chia) e creatina (massa magra + treino). Tabela "alegação × evidência" na seção 6.
8. **Mecanismos de anúncio antigos (coffee loophole, ice hack, blue tonic, exotic rice, purple peel, 7-second ritual) estão mortos no orgânico** (vídeos com 2–143 views). "Filipino bariatric oil" nunca existiu fora da VSL.
9. **Sinal de formato emergente para 50+:** canal "Tai Chi for Health Daily/Life" publica 6+ vídeos "Tai Chi After 50 — Burn Belly Fat, Lower Cortisol" com 58k–117k views cada em 30 dias — exercício suave + cortisol + 50+ é um veículo narrativo pouco explorado em VSL.
10. **Limitação central:** Google Trends, TikTok, Reddit, Instagram e bibliotecas de anúncios estavam bloqueados; o orçamento de WebSearch do turno acabou após 25 buscas (3 negadas); WebFetch bloqueado para Noom/Women's Fitness. Dados do print do usuário foram usados como proxy de Trends. Ver seção 10.

---

## 1. Metodologia e amostra efetiva

| Item | Quantidade |
|---|---|
| Buscas WebSearch executadas (modo extended) | 25 (+3 negadas por limite de orçamento compartilhado) |
| WebFetch | 2 tentativas, ambas bloqueadas pela rede (noom.com, womensfitness.co.uk) |
| Queries YouTube (yt_search) | 120 queries diretas + 120 chamadas de "velocidade" (40 termos × week/month/year) |
| Linhas brutas salvas em `raw/F3_*.jsonl` | 675 (635 vídeos + 40 registros de velocidade) |
| Fontes únicas em `data/F3_sources.csv` | 145 (58 web + 87 vídeos) |
| Citações verbatim (QUOTE) | 9 (o restante é PARAPHRASE de resumos de busca) |
| Comentários de público literais | 0 — comentários do YouTube/TikTok/Reddit inacessíveis neste ambiente |

**Velocidade YouTube (proxy de "novos vídeos por mês")**: para cada termo rodei os filtros `week`, `month`, `year` (máx. 20 resultados) e registrei nº de vídeos, mediana e máximo de views (`raw/F3_velocity.jsonl`). O coletor público retorna resultados ruidosos (ex.: "baking soda trick" na semana devolve vídeos de limpeza de tapete), por isso tratei os números como **sinal direcional**, não como contagem absoluta. Onde a busca retornou 0 por falha de parsing (ex.: "baking soda trick" year), marquei n/d.

---

## 2. PARTE A — Ciclo dos benchmarks: Gelatin Trick × Baking Soda Shot (× Pink Salt Trick)

### 2.1 Linha do tempo comparativa (DATA)

| Marco | Pink Salt Trick | Gelatin Trick | Baking Soda Shot |
|---|---|---|---|
| Primeiro sinal rastreável | ago/2025: Snopes documenta sites/vídeos fraudulentos "Oprah pink salt trick" | 14/out/2025: VSL #9 "Truque Simples com Gelatina" (print); 30/dez/2025: Gelatide "Truque da Gelatina Rosa" | abr/2026: vídeo Jordan Liles "'Baking Soda Water Shot'… Don't Fall for Oprah Scam Ad" (7mo ago, 20.965 views) |
| Onda de VSLs (print) | não aparece no top-20 de 2026 | #2 Melt Drops (28/jul, 20.707 anúncios), #3 Mounja Gummy (21/jan, 20.159), #4 Fit Burn (25/abr, 15.878), #6 Gelatide (30/dez, 14.324), #8 LipoMax (11/abr), #9 (14/out), #10 BurnSlim (05/jan), #12 Burn Gummy "Jelly Trick" (08/mai), #13 "Chia Gelatin Trick" LipoFit (21/jan), #18 Jelly Lean (02/jan), #20 Jelly Tide (20/mai) = **10/20** | #7 Sodatide "Baking Soda Shot" (13/ago, 6.780 anúncios, 2 meses), #17 Slim Metrix "Baking Soda Water Shot" (05/jun, 2.487) = **2/20** |
| Vídeos "explicador/afiliado" (YouTube) | Mattos Legendas 13,8k (11mo), Lukas Graves 3,3k (8mo) | **Bastideon**: 12+ vídeos entre 30k e 154k views, todos 6–9 meses atrás (fev–mai/2026); Patricia Delicious Nutrition (receita de gelatina proteica, 366k, 11mo — não é o "trick") | Bastideon 37k (4mo), Trafity 30k e 29k (3mo), Odilon Huamani 43k "honey and baking soda for men" (3mo) |
| Fact-checks com data | Snopes ago/2025; Yahoo/Lead Stories 2025 | **Snopes 24/abr/2026** ("scam"); Yahoo mai/2026; myantispyware 26/mai/2026 (Dr. Jennifer Ashton + Jillian Michaels); Jordan Liles (Serena Williams, abr/2026); streetsofkante (Jillian Michaels deepfake, fev/2026); Dr. Jen Caudle (vídeo 105k, 5mo) | Jordan Liles (abr/2026); MalwareTips (produtos Alka Slim, Soda Slim, SlimSoda, SodaSlim, EvoSlim, Thermo Ignite); BU-hosted analysis; Ibisik ("as of July 20, 2026 I found no credible statement from Oprah"); Noom; Dr. Jen Caudle 105k (jun/2026) |
| Google Trends (print do usuário, 19/11/2026) | ausente | "bariatric gelatin recipe for weight loss" **+120% (7d)**; "jello recipe for weight loss" **Grande aumento (30d)**; "Medicina bariátrica" +170% (7d) | "baking soda recipe for weight loss" **#1 em 'recipe for weight loss'**; 30d: +20% e "baking soda trick" Grande aumento; **7d: -6% / -10%** |
| Produção nova no YouTube (últimos 30d) | 2 vídeos (190 e 12 views); 1 mutação: "Pink Salt Trick for Neuropathy" (8d) | 0 vídeos relevantes na semana; no mês só a content farm **BATIDÃO DUH PARÁ** (12+ vídeos, 20–68 views, 3w) + "Korean Pink Gelatin Trick for Firmer Skin" (4d, 49 views) + "HORSE GELATIN TRICK – Salt Tonic For Men" (6d, 71 views) | Semana: Traducciones G 1.427 views (7d), Salud Sin Complicaciones 9 views, Odilon 27 views; mês: Trafity 6.008 (2w), Odilon 4.904 (13d), "unhappier." 4.601/4.302, **sadland "Baking Soda Trick for Men: 30-Second Morning Recipe" 12.531 (4w)** |
| Mutações observadas | → neuropatia; → "gelatin and pink salt trick" (SEO) | → pele ("firmer skin", "homemade Botox jello"); → homens ("horse gelatin trick"); → "gelatin and baking soda" (SEO farm) | → homens ("for men in the shower", "honey + baking soda") |
| Status (classificação) | **Em declínio** (ad-driven, histórico) | **Saturada** (anúncios) / **Em declínio** (orgânico) | **Consolidada** (anúncios ativos) com **platô → início de declínio** na busca de 7d |

### 2.2 Como cada um ganhou visibilidade (DATA + INTERPRETAÇÃO)

**Gelatin Trick.** O padrão é o de um mecanismo nascido em VSL: a "receita" (1 colher de gelatina sem sabor + ½ xícara de líquido morno, versão "pink" com suco de cranberry, 15–30 min antes da refeição) nunca é revelada no anúncio; o público vai ao Google/YouTube procurar "what is the gelatin trick recipe" e encontra (a) blogs de receita e páginas SEO em subdomínios universitários invadidos (agtechdata.uga.edu, students.rossier.usc.edu, closup.umich.edu, latest.sites.northeastern.edu — todos aparecem nos resultados), (b) canais "explicadores" com link de afiliado (Bastideon, Batch Recipes), (c) fact-checks. A crença associada: "gelatina enche o estômago como cirurgia bariátrica" + "natural GLP-1" + endossos falsos (Oprah, Dr. Oz, Jillian Michaels, Kelly Clarkson, Dr. Jennifer Ashton, Dr. Sanjay Gupta, Serena Williams). **QUOTE** (Jordan Liles): *"those scammers, likely in Brazil, came up with the fake recipe idea to use as a hook to get consumers to watch very long videos on other websites."* O fact-check mais brando (cirurgião bariátrico, site comercial): **QUOTE** *"not a scam but it is wildly oversold."* Origem clínica real: **QUOTE** (hollyherman.com) *"Gelatin was a hospital recovery tool for bariatric patients long before it became a TikTok weight loss trend."*

**Baking Soda Shot.** Mesmo funil, mas com deepfake explícito: **QUOTE** (Jordan Liles) *"The footage of Oprah, Jastreboff, 'Jenna and Sheinelle,' and Dr. Oz consisted entirely of deepfake AI depictions with manipulated lip movements and fake vocals"* — ou seja, o benchmark de formato (programa de Jenna & Sheinelle) foi literalmente clonado por IA, o que explica por que a busca "baking soda trick weight loss" no YouTube devolve em 1º lugar o vídeo real "Oprah Winfrey on How She Found 'New Freedom' After Weight Loss" (TODAY with Jenna & Sheinelle, 341k). A receita circulante: ¼–½ colher de chá de bicarbonato em água (+ limão/gelo) em jejum. Crenças: "alcaliniza o corpo", "destrava o metabolismo". Reação: Noom (PARAPHRASE: nenhuma evidência de queima de gordura; riscos de irritação gástrica e alcalose), Dr. Jen Caudle (105k views), MalwareTips lista seis marcas que usaram o mesmo gancho.

**Pink Salt Trick** foi o antecessor direto (meados de 2025) com a mesma arquitetura (Oprah, "Dr. Casey Means"); o YouTube de 2026 já responde "pink salt trick" com vídeos de gelatina e baking soda — a audiência migrou.

### 2.3 Tendências vizinhas e o que elas dizem

- **Protein jello / "fluffy Jell-O" / cottage-cheese mousse** é o primo **orgânico** do gelatin trick (Steph's Stove 83,8k; Small Town Southern Wife 54k; Clean & Delicious 746k; Grace Over Glucose 20k há 2 semanas). Yahoo Health publicou "Do TikTok Weight-Loss Hacks Like Protein Jell-O Really Work?" — a imprensa já trata "protein Jell-O" como hack legítimo. INTERPRETAÇÃO: a gelatina como *alimento proteico de saciedade* sobrevive; o "trick" com celebridade morre.
- **"Chia Gelatin Trick" (VSL #13)** e páginas SEO "Gelatin and Baking Soda", "Gelatin and Pink Salt" mostram a tentativa de **fundir mecanismos** — sinal clássico de fase tardia.
- **Bariatric yogurt (VSL #19, 17/ago)** e **"bariatric"** como adjetivo (+170% "Medicina bariátrica" no print) indicam que o próximo mecanismo ad-driven provavelmente manterá o prefixo "bariatric" trocando o alimento (iogurte, sopa, caldo, cottage cheese). HIPÓTESE.

### 2.4 Veredito de ciclo
- **Gelatin Trick: fase de mutação/exaustão.** Não há criador orgânico novo nos últimos 30 dias; a busca de 7d sobe por pressão de mídia paga de 10 VSLs simultâneas. Copiar agora = disputar CPM saturado com fact-check indexado em 1ª página.
- **Baking Soda Shot: fase 4 (fact-check) entrando em 5 (mutação para homens).** Vida útil residual de semanas a poucos meses na avatar feminina; segurança o elimina como mecanismo central.

---

## 3. PARTE B — Fichas dos candidatos (Top 20 + extras)

Formato de cada ficha: nome · aliases/apelidos · receita/ritual · primeiros sinais · evolução (30d/90d/180d quando há dado) · principais vídeos e criadores (DATA YouTube) · pesquisas relacionadas · dúvidas/alegações do público · o que a ciência sustenta · riscos · saturação (cruzado com as 20 VSLs) · novidade · associação 40+/menopausa · oportunidade narrativa · confiança. Pontuação completa em `data/INGREDIENT_TRENDS.csv`.

### F1. Creatine for women over 40 — **Score 80 · Em aceleração · ORGÂNICO**
- **Aliases:** creatine monohydrate; creatine gummies for women; "creatine menopause"; "creatine brain fog".
- **Ritual:** 3–5 g/dia em água ou café, diária, combinada com treino de força (2x/semana é o enquadramento mais comum).
- **Primeiros sinais:** Dr. Lutz Graumann "Creatine for women: this is what happens when you take it EVERY DAY" 475k (11mo); Stacy Sims 567k (8mo). **Aceleração mai–nov/2026:** Diary of a CEO "Creatine Is The Secret To Weight Loss" **6,1M (5mo)**; Ben Azadi 3,95M (5mo); Dr. Carlos Jaramillo "I Gave My Mom Over 70 Creatine" **3,85M (3mo)**; Dr. Eric Berg "After Age 50" **3,66M (1mo)**; Doctor Alex "Creatine After 50" 442k (4mo).
- **Últimos 30 dias (pré-pico):** Physionic 91,6k (9h); Dr. Mindy Pelz "I Started Taking Creatine After 50" 17,9k (7d); Stacy Sims/Commune Podcast 26k (7d); Harry Mander "My Mom Started Taking Creatine" 26,6k (3w); Elodie Beaucent "CREATINE 30 DAYS after 45" 25,6k (2w); Tamsen Fadal 123k (1mo); Nurse Tanya, Med Matrix, Varium Health (micro-canais 40+). **Produtos:** reviews de gummies "for women over 40" (Legion, Arrae, "6000mg creatine + collagen") — varejo já segmenta a avatar. Amazon (print): Optimum Nutrition Creatine 40K+/mês, 84,8K reviews.
- **Imprensa:** ABC17/Stacker 03/nov/2026 "Should women take creatine during perimenopause?"; Medical News Today; Business Upturn "why interest is growing in 2026".
- **Pesquisas relacionadas:** creatine for women over 40; creatine menopause; 5g or 10g; creatine bloating; creatine brain fog.
- **Alegações populares:** "segredo da perda de peso"; preserva músculo na menopausa; clareza mental; "shrinks fat cells by 30%" (Azadi — sem fonte).
- **Ciência:** **moderada.** PARAPHRASE (Stacker/ABC17): meta-análise 2026 de 7 ensaios (608 mulheres, idade média ~62) — ganhos modestos de massa magra e força **apenas com treino de resistência**; evidência em perimenopausa e cérebro/sono é fraca; dose ~5 g/dia; eventos adversos semelhantes ao placebo.
- **Riscos:** retenção hídrica inicial (1–2 lb no scale — precisa ser antecipada na copy); cautela em doença renal; não é emagrecedor direto.
- **Saturação:** **zero VSLs** no top-20; produto commodity barato ($18/60 doses) — a VSL precisa de bundle/mecanismo (ex.: "creatina + proteína + fibra para o metabolismo após os 40").
- **Novidade:** 4/5 para a avatar (creatina era "coisa de academia masculina"; a inversão "minha mãe de 70" é o gancho).
- **Associação 40+:** 5/5 — todos os vídeos-topo usam "after 40/50/70", "menopause", "mom".
- **Oportunidade narrativa:** "O suplemento que os fisiculturistas usam há 30 anos e que os médicos agora dão para as mães" / "Por que o músculo, e não a dieta, é o que trava seu metabolismo após os 50". Demonstração visual média (pó em água) — compensar com antes/depois de força e sarcopenia.
- **Confiança:** ALTA (múltiplos criadores independentes, imprensa datada, produto no varejo, zero anúncio).

### F2. Psyllium husk / fibermaxxing / "GLP-1-friendly fiber" — **Score 77 · Em aceleração · ORGÂNICO**
- **Aliases:** psyllium, Metamucil, isabgol; fibermaxxing/fiber maxxing; "GLP-1 friendly fiber"; "1 spoonful before meals".
- **Ritual:** 1 colher (5 g) de psyllium em 250 ml de água 15–30 min antes das refeições (o gel se forma no copo — demonstração visual 5/5); meta de 25–38 g de fibra/dia.
- **Primeiros sinais:** Keltie O'Connor "debunking fibremaxxing" 245k (11mo, jan/2026); Dr Karan "I Fibermaxxed" 130k (8mo); Amazon já rotula "GLP-1 Friendly" (Vitafusion 40K+/mês) e "Fiber Gummies for GLP-1 Support" (Physician's Choice 50K+/mês); Metamucil 70K+/mês (print).
- **Últimos 30–90 dias:** Abbey Sharp "Fiber is TikTok's New Protein" 109k (2mo); Calvin Landis 115k (2mo); Gundry 49k (2mo); KSTP 5 (TV local) 4w; Dr. Janine Bowring 4,4k (2w); **psyllium:** Dr Meghna 182k (2w), Doctor Sethi 106k (3w), **Natureza que Cura "1 SPOONFUL Before MEALS to FLATTEN YOUR BELLY! (Costs Less Than 50 Cents)" 52k em 2 dias**; 20 vídeos/semana no termo. Trade: Datassential/Perfect Daily Grind (ago/2026) — "fibre is already emerging as the next focus" depois da proteína.
- **Pesquisas relacionadas:** fibermaxxing; psyllium husk weight loss; GLP-1 friendly fiber; how much fiber is too much; fiber vs protein.
- **Alegações populares:** "faz o corpo produzir o próprio GLP-1"; saciedade; "flatten your belly"; barato.
- **Ciência:** **moderada.** PARAPHRASE (WW, GoodRx): fibra solúvel/fermentável aumenta saciedade, achata glicemia pós-prandial e eleva GLP-1 endógeno de forma **modesta e curta** vs. drogas; psyllium é "the cheapest, best-evidence intervention" (WW natural-ozempic). Alegação "igual a GLP-1 farmacêutico" é marketing.
- **Riscos:** engasgo se tomado seco; gases/inchaço no início (subir gradualmente); separar 2h de medicamentos; cautela em disfagia/diverticulite. Perfil de segurança excelente.
- **Saturação:** nenhuma VSL explícita de fibra no top-20 (VSL #5 "GLP-1 Reset" pode conter). Varejo saturado em produto, **não em narrativa DR**.
- **Novidade:** 3/5 (psyllium é velho; "fibermaxxing" + "GLP-1 friendly" é a roupagem nova).
- **Associação 40+:** 4/5 (constipação, colesterol, glicemia, "GLP-1" para quem não quer/pode injetar).
- **Oportunidade narrativa:** "A colher de 50 centavos que os usuários de Ozempic tomam para não recuperar o peso"; "o copo que vira gel" como prova visual em 30 segundos.
- **Confiança:** ALTA.

### F3. Cortisol cocktail / adrenal cocktail — **Score 71 · Em aceleração (busca) · MISTO**
- **Aliases:** adrenal cocktail; cortisol mocktail; "cortisol cocktail recipe for weight loss" (sufixo que denuncia SEO/anúncio).
- **Receita:** ½ xícara de suco de laranja + ½ xícara de água de coco + pitada de sal marinho (+ ¼ colher de chá de cremor tártaro ou magnésio); manhã ou meio da tarde. Variações: "sleepy girl" à noite.
- **Primeiros sinais:** Wikipedia: viral no TikTok em **2023**. Yahoo/Ro/Noom: cobertura 2025–2026.
- **Evolução:** **Google (print): +80% (7d) e "Grande aumento" (30d)** para "cortisol cocktail recipe for weight loss" — a única bebida com aceleração explícita além de gelatina/baking soda. YouTube orgânico fraco e **em queda**: Ben Azadi 1,7M e Steak and Butter Gal 1,23M (ambos 11mo), Lillie Kane 808k (5mo), Jockers 339k (4mo); no mês só 7 vídeos (mediana 78 views); Dr. Jen Caudle "Does the Viral Cortisol Cocktail ACTUALLY Work?" 3,6k (1mo). **Sinal de comercialização:** reviews de produtos prontos — Harmonia Cortisol Cocktail (11mo), **Nature Aurora Cortisol Drink (8d)**, **Loroc'e UltraCalm Cortisol Drink (1d)**.
- **INTERPRETAÇÃO:** descompasso "busca sobe, vídeo orgânico cai" + sufixo "for weight loss" + produtos novos = alguém já está comprando tráfego com esse nome (provável VSL/TSL em teste). Verificar na biblioteca de anúncios (bloqueada aqui).
- **Pesquisas relacionadas:** cortisol belly; cortisol face; adrenal fatigue drink; does the cortisol cocktail work; cortisol cocktail perimenopause.
- **Alegações:** baixa cortisol; derrete "cortisol belly"; energia; adrenais; menopausa.
- **Ciência:** **fraca.** QUOTE (clínico, Women's Fitness UK): *"Cortisol cocktails haven't been shown to lower cortisol or reduce abdominal fat."* PARAPHRASE (Keri Gans RDN): "just another way of hydrating"; Noom 2026: hidrata/eletrólitos/vitamina C, não baixa cortisol nem emagrece.
- **Riscos:** sódio (hipertensão); potássio (cremor tártaro + água de coco — doença renal, IECA, diuréticos poupadores de K); açúcar do suco. Seguro como bebida ocasional.
- **Saturação:** não está no top-20 de VSLs; "Hormone Activation Hack" (#1, 21.144 anúncios) ocupa o território "hormônio". Média.
- **Novidade:** 3/5. **40+:** 5/5 (cortisol/menopausa é a linguagem da avatar).
- **Oportunidade narrativa:** excelente como **ritual de abertura/demonstração** ("o coquetel de 3 ingredientes que as mulheres estão bebendo às 15h"), **não** como mecanismo central com alegação de cortisol. Ligar ao insight "Menopause Weight Gain Wasn't a Thing in 1945" (1,58M/7d).
- **Confiança:** MÉDIA (busca forte, orgânico fraco, suspeita de ad-driven recente).

### F4. "Natural GLP-1 foods" (frame) — **Score 70,5 · Consolidada · MISTO**
- **Aliases:** natural Ozempic; nature's Ozempic; GLP-1 foods; "99 cent food mimics Ozempic"; "foods that trigger GLP-1".
- **Ritual:** listas de alimentos (aveia, feijão, ovos, abacate, azeite, fibra solúvel, proteína) e "1 hack de $1".
- **Vídeos (DATA):** Bazgha Khalid MD "This 99 Cent Food Mimics Ozempic" **1,76M (4mo)**; Doctor Mike Diamonds 1,1M (7mo); Dr. Livingood "10 Foods UNDER $1 That Work Like Ozempic" 1,13M (6mo); Dr. Berg "Dirty Secret Behind Ozempic" 1,05M (8mo); Jockers 669k (7mo); Mindy Pelz 604k (6mo); **Nutrition Made Simple "Foods That Trigger GLP-1? What Studies Actually Show" 432k (4w)**; Henry's Health Habits/Pelz 53k (5d); Jockers "$1 Diet Hack That Activates GLP-1" 9k (11d); 17 vídeos/semana.
- **Pesquisas:** natural GLP-1; how to increase GLP-1 naturally; GLP-1 friendly; "peptides for weight loss" (Grande aumento 30d, print).
- **Ciência:** fraca para "equivalência"; moderada para "fibra/proteína aumentam GLP-1 endógeno modestamente" (GoodRx/WW).
- **Riscos:** regulatório — comparar com droga de prescrição; promessa de equivalência é falsa.
- **Saturação:** **alta** em anúncios (VSL #5 "GLP-1 Reset" 14.989 anúncios; #8 "GLP-1 Natural com Gelatina"); Amazon "GLP-1 Companion", "GLP-1 Friendly".
- **Oportunidade:** usar como **frame secundário** ("o que seu corpo já produz"), não como nome de mecanismo.
- **Confiança:** ALTA.

### F5. Cottage cheese (protein-maxxing) — **Score 70 · Consolidada (mainstream) · ORGÂNICO**
- **Aliases:** cottage cheese recipes for weight loss; cottage cheese flatbread/bread; cottage cheese ice cream; "protein maxxing".
- **Receita:** cottage cheese + ovo (flatbread "better than bread"); mousse; bowls; ~14 g proteína/porção.
- **Sinais:** Circana +20% vendas jun/24–jun/25 (MSU); AOL/NorthJersey jun/2026: falta em prateleiras, Good Culture quase quadruplicou vendas em 3 anos, categoria +~60%; **CNN 22/out/2026** "the social media cottage cheese craze we can get behind". **Google (print): "cottage cheese recipes for weight loss" Grande aumento (30d)**; "chicken salad", "egg salad", "tuna salad", "egg bites recipe" +130% (7d) — família "proteína fácil".
- **Vídeos:** Cooking With Merry 4,84M (7mo) e 1,28M (3mo); Keto Kitchen 1,29M (6mo) e **28k (3d)**; Allrecipes 1,52M (5mo); Flexible Dieting Lifestyle 1,53M; **Steak and Butter Gal "4 Cottage Cheese Recipes" 89,9k (3w)**; Grace Over Glucose 20k (2w).
- **Ciência:** moderada (proteína/saciedade; cálcio para osso durante perda de peso — CNN). PARAPHRASE (Yahoo Health): não é "bala mágica".
- **Riscos:** sódio; lactose. Segurança excelente.
- **Saturação:** zero VSL com cottage cheese; "Iogurte Bariátrico – YoBurn" (#19) é o vizinho mais próximo.
- **40+:** 4/5 (massa magra, osso, saciedade sem contar caloria). **Novidade:** 2/5. **Visual:** 4/5.
- **Oportunidade:** "o pão de 2 ingredientes" como demonstração; "bariatric cottage cheese" seria a cópia óbvia do padrão de VSL — evitar o prefixo, usar "proteína de saciedade após os 50".
- **Confiança:** ALTA.

### F6. Black seed oil (Nigella sativa) — **Score 64,5 · Em aceleração · MISTO**
- **Aliases:** kalonji; black cumin seed oil; "Resilia" (produto com canela do Ceilão + berberina semeado em canais 50+ — ver F14).
- **Ritual:** 1 colher de chá/dia ou "2 gotas no café"; cápsulas.
- **Sinais (DATA, novembro/2026):** **Dr. Eric Berg 385k em 1 dia**; Thomas DeLauer "2 Drops of This Oil in Coffee Cuts Insulin Resistance" 323k (4w); Shea Whitney "18 *Miracle* Benefits" 125k (3w); SolarGirl Homestead "Black Seed Oil and Menopause" (13d); **"real life fitness over 50": "I Tried Resilia for 6 Weeks and the Scale Said This" 85,7k (2w), "week 5 trying resilia" 71,7k (3w); Wellness With Keeta 99k (1mo)**; Dr. Bilquis (kalonji) 334k (4mo). 14 vídeos/semana; 20/mês.
- **INTERPRETAÇÃO:** padrão pré-pico clássico — médicos-influencers grandes + criadoras 50+ pequenas testando "6 semanas" + um produto sendo semeado. Ainda sem VSL no top-20.
- **Ciência:** fraca a moderada (há meta-análises de Nigella sativa com redução modesta de peso — **não verificadas nesta rodada**; marcar como a confirmar).
- **Riscos:** pode baixar glicemia e pressão (interação com antidiabéticos/anti-hipertensivos); evitar na gestação; GI leve.
- **Novidade:** 4/5. **40+:** 4/5 (menopausa, insulina, cabelo). **Visual:** 3/5 (óleo escuro no café — bom).
- **Oportunidade:** "o óleo preto das faraós" / "2 gotas no café" — narrativa cultural (Oriente Médio/Egito) ainda não queimada por VSL.
- **Confiança:** MÉDIA.

### F7. Lemon balm tea — **Score 64 · Em aceleração (UK) / Evidência insuficiente (US) · ORGÂNICO**
- **Aliases:** Melissa officinalis; lemon balm elixir; "nature's Ozempic" (TikTok UK).
- **Ritual:** chá 1–2x/dia, especialmente à noite; "elixir" com limão/mel.
- **Sinais:** **LADbible 19/nov/2025: buscas UK por lemon balm tea "+800% no último mês"**; Yahoo, Onya, Ro, Noom, Formblends (2025–26). YouTube EUA dedicado quase nulo (micro-canais "The Dark Side of Lemon Balm" 16 views); Dr. Berg "DRINK 1 CUP at Night to Burn Belly Fat FAST" 879k (10mo) ocupa o ângulo "chá noturno".
- **Ciência:** fraca. QUOTE (dietista londrina, Yahoo): *"there's no clinical evidence that supports lemon balm directly causing weight loss."* Endocrinologista: "not very potent as a weight loss agent".
- **Riscos:** **tireoide** (pode interferir em hormônio tireoidiano; cautela em hipotireoidismo — relevante na avatar 40+ com levotiroxina); sedação.
- **Saturação:** nenhuma VSL. **Novidade:** 4/5. **40+:** 4/5 (sono, ansiedade, menopausa, "cravings noturnos").
- **Oportunidade:** "a erva calmante que silencia a fome noturna" — bom veículo de história (jardim, avó), com disclaimer de tireoide. Esperar confirmação de tração nos EUA (HIPÓTESE: lag UK→US de 6–12 meses).
- **Confiança:** MÉDIA.

### F8. Clove water / "1 clove in your coffee" — **Score 63 · Em aceleração · ORGÂNICO (canais 60+)**
- **Sinais:** **Dr. Berg "1 CLOVE in Your Coffee Every Morning" 8,86M (2mo)** + follow-up "Don't Make These 4 Mistakes" 468k (12d); Senior Health Hub 3,75M (6mo) e 628k (9mo); motivationaldoc "clove under your tongue" 3,27M (4mo); Ben Azadi "Clove Water Before Bed" 1,31M (3mo); Biohealthy 99k (5d); Dr Visakh 71k (6d); "Clove and Cinnamon Water After 60" (4w). 11 vídeos/semana, mediana 5,1k — a maior velocidade orgânica entre as "águas".
- **Ciência:** nenhuma para peso (Noom; Banner Health: efeito indireto via digestão/glicemia).
- **Riscos:** eugenol — hepatotoxicidade em dose alta, risco de sangramento com anticoagulantes, hipoglicemia; público 60+ polimedicado. Dose "1 cravo" é inócua, mas a copy tende a escalar.
- **40+:** 4/5 (canais "Senior Health"). **Novidade:** 3/5. **Visual:** 4/5.
- **Oportunidade:** ritual barato e visual; usar apenas como "hábito matinal" com dose mínima e sem promessa de gordura. Saturação: zero VSL.
- **Confiança:** MÉDIA.

### F9. Protein jello / fluffy Jell-O — **Score 61 · Consolidada · ORGÂNICO**
- Ver 2.3. Vídeos: Clean & Delicious mousse 746k (11mo); Patricia 366k (11mo) e "banana + gelatin" 8,4k (3w); Steph's Stove 83,8k (9mo); Small Town Southern Wife 54k (5mo); Grace Over Glucose 20k (2w); Feelin' Fab "Homemade Botox Jello" 20k (1mo); Amanda Widener (-116 lb, GLP-1) snacks (2d).
- **Ciência:** moderada (proteína/saciedade; gelatina = proteína incompleta). **Risco:** reputacional por proximidade com o scam. **Saturação:** alta por contaminação do termo "gelatin trick".
- **Oportunidade:** reposicionar gelatina como "sobremesa proteica" e nunca como "trick".

### F10. Chia seed water / internal shower — **Score 60,5 · Consolidada (ciclos) · ORGÂNICO**
- **Sinais:** TODAY mar/2026 ("going viral once again"); Cleveland Clinic; **Google (print): "chia seed pudding recipe" Grande aumento (30d)**. Vídeos: Doctor Karthikeyan 4,56M (2w, Tamil); Doctor's Kitchen 2,58M (2mo); Dr Rohini Patil 3,06M (7mo); Livingood 2,09M (8mo); Keto Kitchen "Just Chia Seeds and Water — Better Than Bread" 25k (3w); Body Shock 22k/12k (3–4w); Patricia 7,9k (2d).
- **Ciência:** moderada para saciedade/intestino; RCT citado: chia **não** reduziu peso em adultos com sobrepeso. QUOTE (Cleveland Clinic): *"First, chia seed water made waves on social media for its alleged ability to help with weight loss."*
- **Riscos:** engasgo/obstrução com semente seca (disfagia); diverticulite.
- **Saturação:** média (VSL #13 "Chia Gelatin Trick"). **Visual:** 5/5 (gel). **Novidade:** 2/5.
- **Confiança:** ALTA.

### F11. Olive oil shot — **Score 59 · Consolidada · ORGÂNICO**
- Fox News (médico: QUOTE *"can unintentionally add several hundred extra calories a week"*; 1 vídeo TikTok >57M; ~3.000 buscas/semana); rollingout 03/jan/2026. Vídeos: Ben Azadi "30 TBSP in 10 Days" 1,95M (6mo); **Food Vs. Fact "Over 40? Mix THIS Into Olive Oil Before Bed" 803k (3mo)**; Patricia 340k (11mo); Justin Dorff "olive oil fast" 321k (10mo).
- **Ciência:** fraca para o "shot"; forte para azeite na dieta mediterrânea. **Risco:** calorias, refluxo. **Saturação:** média — o conceito "óleo em jejum" já foi queimado pela VSL #14 "Filipino Bariatric Oil Protocol" (coconut oil).
- **Oportunidade:** narrativa "Mediterrânea/Italiana" para 50+ (canais de salada "over 50" com 1,3M views) — mais como cultura alimentar que como shot.

### F12. Protein coffee (proffee) — **Score 57,5 · Consolidada (varejo) · ORGÂNICO**
- Fox News jun/2026: demanda "particularly among adults over age 40"; GlobalData abr/2026 "mainstream"; Starbucks linha proteica set/2025 (36 g); 20,2M posts TikTok; Perfect Daily Grind ago/2026 "boom won't last — fibre is next". Vídeos: Clean & Delicious 102k (5mo); Harry Mander 53,8k (4w); WION 8k (1mo); Journey To Fifty Plus (1k).
- **Ciência:** moderada (proteína). **Saturação:** commoditizado (Costco, Starbucks); VSL #16 "Glow Shakes" (colágeno, 2.578 anúncios em 11h, 12/nov) ocupa o shake. Oportunidade baixa-média.

### F13. Bone broth — **Score 51 · Consolidada/estável · ORGÂNICO**
- Noom: sem estudos de jejum de caldo; programa Kellyann incluía jejum/exercício. Vídeos: Steak and Butter Gal "1 Cup Before 10AM" 193k (10mo) e "visceral fat 14 days" 394k (9mo); Dr. Autumn Smith (glycine) 32k (6d); Emma Voysey "why I stopped" 46k (4w); 19 vídeos/mês com mediana 97 views (cauda longa fraca). Contexto 40+: UCHealth jun/2026 "perfect storm for bone loss: menopause + GLP-1". Oportunidade: ângulo "osso/colágeno na menopausa", não "emagrece".

### F14. Berberine — **Score 55 · Consolidada (2º ciclo) · MISTO — NÃO usar como central**
- **Google (print):** "does berberine help you lose weight" +110% (30d); "will metformin help me lose weight" **+3.100%** (sinal da "farmácia barata"). Amazon: Rootation berberine gummies 10K+/mês ($39,99). Vídeos: Dr. Berg "Berberine Isn't a Weight Loss Supplement" 781k (3mo); **Real Alex Clark/Josh Axe "The NATURAL Ozempic?" 20,6k (5d)**; Fit Wise Woman 5,5k (6d); Nadolsky 6,3k (4w); "berberine patch" review (11d).
- **Ciência:** fraca — meta-análise 23 RCTs (2.270 pessoas): −0,88 kg vs placebo (Examine). **Segurança:** **EFSA (jan/2026) não conseguiu estabelecer nível seguro de ingestão** e abriu consulta; interações CYP (metformina, anticoagulantes); evitar gestação/lactação/hepatopatia. Trade (NutraIngredients 31/jul/2026) teme restrição/banimento.
- **Decisão:** não eliminado para menção, **eliminado como mecanismo central** (risco regulatório + interação na avatar polimedicada).

### F15. Castor oil in belly button — **Score 46,5 · Consolidada · ELIMINADO por segurança/alegação**
- Dr. Berg Shorts 40,6k (4d); Dr. Greg Hall (1d); 20 vídeos/semana (mediana 57); Science Focus: nenhuma evidência de absorção/detox. Só funciona com alegação falsa (umbigo → fígado). Oral = laxante/gestação.

### F16. Sleepy girl mocktail / magnésio — **Score 43,5 · Em declínio (mocktail) / Consolidada (magnésio)**
- Wikipedia (Gracie Norton 2023); Healthline fev/2026 (resultados mistos); 6 vídeos/semana com 2–8 views — morreu como meme, virou "sleepmaxxing". Magnésio: **Dr. Mary Claire Haver "What I Actually Take Daily" 97k (13d)**; Elevate MD perimenopause 9k (6d). Oportunidade: magnésio como **coadjuvante** de sono/cortisol em bundle 40+.

### F17. Okra water — **Score 42 · Em declínio** (Jasmine Duke fev/2024; Noom "not supported"; MD Anderson; Dr. Jen Caudle 35,6k 5mo; "I tried okra water 7 days" 306 views 5d). Visual 5/5, ciência 0, público errado (jovem/Black vegan TikTok).

### F18. Cinnamon water — **Score 37 · Estável** (fact-check THIP ago/2026; cássia/cumarina; 0 vídeos novos/semana). Só como tempero da narrativa.

### F19. Apple cider vinegar — **Score 44 · Saturada** (Goli 299K reviews; motivationaldoc 71k 3w; Ken Berry "hype?" 23k 2w). Nota: "Sidra de maçã sem álcool +200%" no print é **bebida sazonal de outono**, não vinagre — não confundir.

### F20. Japanese Mounjaro drink — **Score 43 · Evidência insuficiente · SEO-farm**
- Receita (ACV + matcha/limão/gengibre/canela) só existe em blogs de receita; **1 vídeo (71 views, 9mo)**; busca por vídeo retorna notícias coreanas sobre o Mounjaro real (JTBC 102k). Risco legal (marca Lilly). Mesmo para Oatzempic/Ricezempic (F21: Cleveland Clinic nov/2026 ainda comenta, mas 1 vídeo/semana com 69 views; ricezempic sem cobertura há 744 dias).

### Extras (fichas curtas no CSV)
- **Collagen "burn"/Glow Shakes** (51): Amazon ELMNT 20K+/mês; **TSL Glow Shakes 2.578 anúncios em 11 h (12/nov)** — anúncio acelerando; ciência fraca para peso; 40+ 5/5 (pele/osso).
- **Cucumber salad / Mediterranean salads 50+** (52): Laka Kitchen 2,3M; "Goddess of Salads — if you're over 50+" 1,32M; "Pepino" Grande aumento (30d, print). Alimento, não truque; bom B-roll.
- **Pineapple/bromelain** (49,5): **"Abacaxi" +300% (7d, print)**; Camirra's Kitchen 444k (4mo); "pineapple + cinnamon flattens belly in 1 night" 79k. Sinal de busca sem criador novo — **Emergente de busca, evidência insuficiente** (pode ser sazonal/Thanksgiving). Monitorar.
- **Kefir/fermentados/gut reset** (49): Mel Robbins + Rajsree Nambudripad MD 1,15M (2mo).
- **Seed cycling** (45), **Spearmint** (42), **Moringa** (40,5), **Dandelion/bitter tonic** (40,5; Victor Prince 1,66M), **Sea moss** (33): nicho ou declínio; ver CSV.
- **Hormone activation hack (VSL #1, 21.144 anúncios)**: ad-driven; mas o orgânico "15 Daily Habits to Support Hormone Balance Naturally After 40" fez 90,8k em 6 dias — a narrativa "hormônios após 40" é viva; o nome "hack" é da VSL.
- **GLP-1 Reset (VSL #5)**: ad-driven; orgânico vizinho forte: "what happens when you STOP Ozempic" 56k (1d), "when Ozempic stops working" 499k (2mo), Dr. Jones "why you're NOT losing on GLP-1" 638k — **público pós-GLP-1** é um segmento novo da avatar (HIPÓTESE forte).
- **Filipino bariatric oil / Coco Burn (VSL #14)**: 0 vídeos, 0 cobertura; Mayo Clinic (jun/2026): coconut oil não reduz peso. Puro artefato de VSL.
- **Coffee loophole / ice hack / blue tonic / exotic rice / purple peel / 7-second ritual**: mortos no orgânico (2–143 views em vídeos de afiliado 2026). Históricos.

---

## 4. RANKING

### 4.1 Top 10 oportunidades (score 0–100; pesos: crescimento 20 · conversas 15 · curiosidade 15 · adequação 40+ 15 · novidade 10 · demonstração 10 · ciência/segurança 15)

| # | Ingrediente | Cresc. | Conv. | Curios. | 40+ | Novid. | Demo | Ciência | **Score** | Status | Saturação VSL |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Creatine (women 40+) | 90 | 85 | 80 | 95 | 70 | 50 | 75 | **80,2** | Em aceleração | nenhuma |
| 2 | Psyllium / fibermaxxing / GLP-1-friendly fiber | 80 | 75 | 75 | 85 | 55 | 90 | 75 | **77,0** | Em aceleração | nenhuma explícita |
| 3 | Cortisol cocktail (como ritual, não mecanismo) | 85 | 70 | 85 | 90 | 55 | 80 | 25 | **71,0** | Em aceleração (busca) | média (hormônio ocupado) |
| 4 | Natural GLP-1 foods (frame) | 75 | 80 | 85 | 80 | 45 | 60 | 55 | **70,5** | Consolidada | alta |
| 5 | Cottage cheese / protein-maxxing | 70 | 85 | 70 | 75 | 40 | 70 | 70 | **70,0** | Consolidada | nenhuma |
| 6 | Black seed oil | 75 | 55 | 75 | 70 | 70 | 65 | 40 | **64,5** | Em aceleração | nenhuma |
| 7 | Lemon balm | 75 | 55 | 80 | 80 | 80 | 60 | 20 | **64,2** | Em aceleração (UK) | nenhuma |
| 8 | Clove in coffee | 80 | 60 | 85 | 70 | 60 | 75 | 10 | **63,2** | Em aceleração | nenhuma |
| 9 | Protein jello | 55 | 60 | 65 | 70 | 50 | 85 | 50 | **61,2** | Consolidada | alta (contaminação) |
| 10 | Chia seed water | 55 | 70 | 65 | 65 | 30 | 90 | 50 | **60,5** | Consolidada | média |

**Recomendação de arquitetura (INTERPRETAÇÃO):** mecanismo central = **músculo/metabolismo após os 40 (creatina + proteína)** ou **fibra "GLP-1 do próprio corpo" (psyllium)**; ritual de abertura/demonstração = cortisol cocktail ou copo de psyllium gelificando; frame = "o que a menopausa fez com seu metabolismo"; coadjuvantes = magnésio, black seed oil. Evitar nomes "trick/hack/loophole" e qualquer celebridade.

### 4.2 Top 5 emergentes (pré-pico)
1. **Creatina para mulheres 40+** — vários criadores grandes e pequenos no mesmo tema em 7–30 dias; produto segmentado chegando ao varejo; zero VSL; imprensa datada (03/nov/2026).
2. **Psyllium "1 colher antes das refeições"** — vídeo novo com 52k em 2 dias; Amazon já rotula "GLP-1 Friendly"; TV local cobrindo "fibermaxxing"; trade prevê "fibra é a próxima proteína".
3. **Black seed oil** — salto de novembro (Berg 385k/1d, DeLauer 323k) + criadoras 50+ testando "6 semanas" + produto sendo semeado (Resilia).
4. **Cortisol cocktail "for weight loss"** — +80% (7d), Grande aumento (30d), produtos prontos aparecendo em reviews nos últimos 8 dias. (Atenção: pode já ser ad-driven.)
5. **Lemon balm** — +800% no UK em nov/2025 e cobertura "nature's Ozempic"; EUA ainda sem vídeo dedicado = janela antes do pico (ou risco de nunca cruzar).
   *Menção honrosa:* clove-in-coffee (maior velocidade entre as "águas", público 60+); pineapple (+300% busca sem criador).

### 4.3 Top 5 saturadas
1. **Gelatin Trick** (10/20 VSLs; Snopes; content farm; mutações). 2. **Baking Soda Shot** (2 VSLs ativas; fact-checks; migração para homens). 3. **Pink Salt Trick** (2025; morto). 4. **Apple cider vinegar** (Goli 299K reviews; década de uso). 5. **Nomes "natural GLP-1/Ozempic"** como mecanismo (VSLs #5 e #8; Oatzempic/Ricezempic/Japanese Mounjaro com risco de marca). *Também:* coffee loophole, ice hack, blue tonic, exotic rice, purple peel, 7-second ritual, Filipino bariatric oil — históricos, sem orgânico.

### 4.4 Eliminados por segurança (não usar como ingrediente central)
| Ingrediente | Motivo |
|---|---|
| **Baking soda** | Carga de sódio (hipertensão/IC/rim — prevalentes na avatar), alcalose metabólica, altera absorção de medicamentos, relatos de ruptura gástrica; exige alegação falsa de "queima de gordura" e endosso deepfake |
| **Pink salt** | Sódio; troca de sal iodado = risco de deficiência de iodo/tireoide (Snopes); só perda de água |
| **Castor oil no umbigo** | Mecanismo inexistente — exige alegação falsa; oral = laxante estimulante/estimulante uterino |
| **Berberine (como central)** | EFSA jan/2026: sem nível seguro; interações CYP com metformina/anticoagulantes; efeito −0,88 kg |
| **Mecanismos ad-driven copiados** (coffee loophole, ice hack, blue tonic, exotic rice, purple peel, 7-second, Filipino bariatric oil, hormone activation hack, bariatric yogurt, GLP-1 reset) | Dependem de "truque" inexistente + celebridade/deepfake; risco FTC; não são tendências de consumidoras |
| **Com restrição (usar só com dose mínima e disclaimer)** | Clove (eugenol/anticoagulantes), lemon balm (tireoide), cinnamon cassia (cumarina), cortisol cocktail com cremor tártaro (potássio/rim), chia seca (disfagia), olive oil shot (calorias) |
| **Risco legal, não sanitário** | Oatzempic, Ricezempic, Japanese Mounjaro (marcas registradas) |

---

## 5. DETECÇÃO PRÉ-PICO — sinais observados por tipo

| Sinal | Onde apareceu (DATA) |
|---|---|
| Crescimento em canais menores | Creatina: Nurse Tanya (368), Med Matrix (171), Varium (182), Elodie Beaucent 25k, Harry Mander 26k — todos ≤4 semanas; Black seed oil: "real life fitness over 50" 85k/71k; psyllium: Natureza que Cura 52k em 2d |
| Vários criadores no mesmo ingrediente em janela curta | Creatina (Pelz, Sims, Physionic, Mander, Beaucent, Fadal — 7–30d); clove (Berg, Biohealthy, Dr Visakh, Aging No Limits — 5–30d) |
| Perguntas repetidas (títulos em forma de dúvida) | "Should women over 40 take creatine?", "5g or 10g?", "Does the viral cortisol cocktail actually work?", "Is more fiber actually better?", "how much fiber is too much" |
| Novos vídeos copiando a receita | Baking soda (Trafity/Odilon/unhappier. — 4 vídeos em 2 semanas, mas views caindo = cópia tardia); gelatina (content farm BATIDÃO — cópia sem audiência = fim de ciclo) |
| Aparição em podcasts/TV | Creatina: Diary of a CEO 6,1M, Commune Podcast (Stacy Sims), Tamsen Fadal; fibermaxxing: KSTP 5 News, Fox/WION; cottage cheese: CNN 22/out; proffee: Fox jun/2026 |
| Interesse crescente sem muitos anúncios | Creatina, psyllium/fibermaxxing, cottage cheese, black seed oil, clove — zero VSL no top-20 |
| Variações novas de tendência antiga | "Korean pink gelatin for skin", "horse gelatin trick for men", "baking soda trick for men", "pink salt trick for neuropathy", "gelatin + baking soda" — todas indicam **exaustão** do original, não oportunidade |
| Produto sendo semeado antes da VSL | Resilia (black seed oil/canela/berberina) em canais 50+; Nature Aurora / Loroc'e cortisol drinks; creatine gummies "for women over 40" |
| Reddit antes da comercialização | **n/d** — reddit.com bloqueado; busca "site:reddit.com gelatin trick" negada por limite |

---

## 6. Tabela — alegação popular × evidência científica × segurança

| Ingrediente | Alegação popular (como circula) | Evidência (fonte) | Nível | Segurança |
|---|---|---|---|---|
| Gelatin trick | "enche o estômago como bariátrica", "natural GLP-1", celebridades usaram | Snopes: scam; sem ensaios do "trick"; gelatina = proteína incompleta com saciedade modesta | fraca | Gelatina segura; funil enganoso |
| Baking soda shot | alcaliniza e queima gordura; Oprah/Jastreboff recomendaram | Noom: nenhuma evidência; deepfakes confirmados (Jordan Liles) | nenhuma | Sódio, alcalose, interação medicamentosa — **eliminado** |
| Pink salt | minerais destravam metabolismo | Ro/Snopes/Yahoo: só perda de água | nenhuma | Sódio; iodo — **eliminado** |
| Cortisol cocktail | baixa cortisol, derrete "cortisol belly" | QUOTE: "haven't been shown to lower cortisol or reduce abdominal fat"; hidrata | fraca | Sódio/potássio; OK ocasional |
| Creatine 40+ | "segredo da perda de peso", músculo, cérebro | Meta-análise 2026 (7 RCTs/608 mulheres): massa magra/força **com treino**; cérebro fraco | moderada | Boa; retenção hídrica |
| Psyllium/fiber | "GLP-1 natural", saciedade, barriga | WW/GoodRx: saciedade, glicemia, GLP-1 endógeno modesto | moderada | Boa (água; separar remédios) |
| Cottage cheese | "better than bread", perdi peso rápido | CNN/dietistas: proteína+cálcio; não é bala mágica | moderada | Sódio/lactose |
| Chia water | internal shower, derrete gordura | Cleveland Clinic: intestino sim; RCT: sem perda de peso | moderada (intestino) / fraca (peso) | Disfagia/diverticulite |
| Olive oil shot | saciedade, "melts belly fat & lowers cortisol" | Noom/Fox: sem evidência do shot; +calorias | fraca | Refluxo |
| Lemon balm | "nature's Ozempic" | Dietista: sem evidência clínica; animal only | fraca | **Tireoide** |
| Berberine | natural Ozempic | 23 RCTs: −0,88 kg; sem evidência humana de ↑GLP-1 | fraca | **EFSA: sem nível seguro**; interações |
| Clove water | derrete gordura à noite | Noom/Banner: nenhuma; indireto | nenhuma | Eugenol/anticoagulantes |
| Okra water | glicemia, peso, libido | Noom "not supported"; estudo em ratos | nenhuma | Oxalato |
| Castor oil navel | detox fígado, barriga chata | Science Focus: sem absorção | nenhuma | Oral: laxante — **eliminado** |
| Oatzempic | −40 lb em 2 meses | Cleveland Clinic: saciedade, não replica GLP-1 | fraca | OK; marca |
| Bone broth | reset, colágeno, osso | Noom: sem estudos de broth-only | fraca | Sódio |
| Black seed oil | 18 benefícios, insulina, menopausa | não verificado nesta rodada (meta-análises existentes a conferir) | fraca-moderada (a confirmar) | Glicemia/pressão; gestação |
| Collagen | pele, "burn", osso | ensaio de 5 g/dia colágeno peptídeo em osso (citado); peso: nada | fraca | Boa |
| Proffee | músculo após 40 | proteína ok; "not a magic bullet" | moderada (proteína) | Açúcar/cafeína |

---

## 7. INSIGHTS ESTRATÉGICOS

### I1 — O ciclo "trick" tem ~9–12 meses e termina em fact-check indexado + mutação
- **DESCOBERTA:** Pink salt (ago/2025) → gelatina (out/2025–mai/2026) → baking soda (abr–ago/2026) seguem a mesma curva; cada um morre quando Snopes/Jordan Liles/Dr. Jen Caudle ocupam a SERP e o mecanismo migra para homens/pele/neuropatia.
- **EVIDÊNCIA:** Seção 2.1; Snopes 24/abr/2026; vídeos "for men" (sadland 12,5k 4w; Odilon 43k 3mo); content farm BATIDÃO (20–68 views).
- **INTERPRETAÇÃO:** o lado comprador (10 VSLs de gelatina) está pagando por um termo que o lado orgânico já abandonou; o +120% de busca é eco de mídia.
- **IMPLICAÇÃO PARA A VSL:** não lançar "truque" com nome de ingrediente de cozinha + celebridade; se usar ingrediente, usar com nome próprio do produto e mecanismo fisiológico (músculo, fibra), sem "trick/hack".
- **CONFIANÇA:** ALTA.

### I2 — A próxima onda é "corpo após os 40" com ingredientes de evidência moderada (creatina, fibra, proteína)
- **DESCOBERTA:** os únicos ingredientes com (a) aceleração orgânica, (b) zero VSL e (c) ciência moderada são creatina, psyllium/fibra e cottage cheese/proteína.
- **EVIDÊNCIA:** F1, F2, F5; Amazon (Metamucil 70K+, ON Creatine 40K+); CNN 22/out/2026; Stacker 03/nov/2026; Datassential via PDG ago/2026.
- **INTERPRETAÇÃO:** o mercado está migrando de "bebida mágica" para "biologia da meia-idade"; o público pós-GLP-1 (como não recuperar peso, como não perder músculo) amplia a avatar.
- **IMPLICAÇÃO:** mecanismo central "metabolismo muscular após os 40" com creatina+proteína+fibra; demonstração: copo de psyllium gelificando / teste de força da cadeira; prova: meta-análise 2026 em mulheres.
- **CONFIANÇA:** ALTA.

### I3 — Cortisol é a palavra, não o coquetel
- **DESCOBERTA:** "cortisol belly" rende milhões (Jockers 1,28M; Mitch Rice 455k em 2 semanas; Kowallik 432k), "cortisol cocktail" rende busca mas não vídeo; produtos "cortisol drink" começam a aparecer.
- **EVIDÊNCIA:** F3; print (+80% 7d); reviews Nature Aurora (8d)/Loroc'e (1d).
- **INTERPRETAÇÃO:** o termo está prestes a ser comercializado (talvez já esteja); a avatar associa cortisol a menopausa/estresse/barriga.
- **IMPLICAÇÃO:** usar "cortisol" na lead e o coquetel como ritual de 3 ingredientes (seguro), sem prometer que ele baixa cortisol; o produto deve resolver "o que o cortisol faz com o músculo/apetite".
- **CONFIANÇA:** MÉDIA.

### I4 — Menopausa é a lead mais quente do mês
- **DESCOBERTA:** "Menopause Weight Gain Wasn't a Thing in 1945 — What Changed?" 1,58M views em 7 dias; Stacy Sims 173k (11d); Livingood 381k (2w); Salako 250k (2w); "does your metabolism slow down as you get older" +200% (print).
- **IMPLICAÇÃO:** abrir com a pergunta histórica/contrafactual ("em 1945 não existia barriga de menopausa — o que mudou?") é o gancho mais validado da semana; testar como lead.
- **CONFIANÇA:** ALTA (DATA de views; interpretação do porquê é HIPÓTESE).

### I5 — Tai Chi "after 50" é o formato-surpresa
- **DESCOBERTA:** dois canais irmãos publicaram 6+ vídeos "Tai Chi After 50 — Burn Belly Fat, Lower Cortisol" com 58k–117k views cada em 30 dias.
- **IMPLICAÇÃO:** B-roll e "movimento suave que respeita joelhos" podem compor a promessa de "sem academia"; sinal de que a avatar quer exercício gentil + cortisol.
- **CONFIANÇA:** MÉDIA.

### I6 — Semeadura de produto em canais de mulheres 50+ é o novo "pré-VSL"
- **DESCOBERTA:** "Resilia" (canela/berberina/black seed) aparece em 3 canais de mulheres 50+ com testes de "6 semanas" (85k, 71k, 99k views) sem VSL no top-20.
- **IMPLICAÇÃO:** monitorar a biblioteca de anúncios para "Resilia"/"black seed" nas próximas 4–8 semanas; se aparecer VSL, o ingrediente entra no ciclo. Para nós: black seed oil como coadjuvante narrativo ("óleo dos faraós"), não central, até confirmar evidência.
- **CONFIANÇA:** MÉDIA.

### I7 — Sinais de busca sem criador (pineapple +300%, tortilla +250%, apple cider +200%) são provavelmente sazonais
- **EVIDÊNCIA:** nenhum vídeo novo relevante na semana para pineapple/tortilla; "sidra" = bebida de outono.
- **IMPLICAÇÃO:** não construir mecanismo sobre eles; usar como tempero de época na copy se houver.
- **CONFIANÇA:** BAIXA.

---

## 8. Cruzamento com as 20 VSLs do print (saturação)

| Mecanismo da VSL | Nº VSLs | Anúncios (soma) | Tendência orgânica correspondente | Status orgânico |
|---|---|---|---|---|
| Gelatina (trick/rosa/bariátrica/jelly/chia) | 10 | ~95.000 | protein jello (orgânico sobrevive) | Em declínio |
| GLP-1 (reset/natural) | 2 | ~21.700 | natural GLP-1 foods; pós-GLP-1 | Consolidada/Em aceleração |
| Hormone activation hack | 1 | 21.144 | "hormone balance after 40" (90k/6d) | Em aceleração (narrativa) |
| Baking soda shot | 2 | ~9.270 | — | Em declínio |
| Thermogenic activation | 1 | 3.930 | — | n/d |
| Filipino bariatric oil (coconut) | 1 | 3.146 | olive oil shot (vizinho) | inexistente |
| Green ritual | 1 | 2.724 | chlorophyll/moringa (fraco) | Em declínio |
| Glow Shakes (colágeno TSL) | 1 | 2.578 (11 h) | collagen/proffee | Consolidada |
| Iogurte bariátrico | 1 | 2.245 | Greek yogurt bread 1,94M | Consolidada |
| **Sem VSL:** creatina, psyllium/fibra, cottage cheese, black seed oil, lemon balm, clove, cortisol cocktail, magnésio | 0 | 0 | ver fichas | **Janela aberta** |

---

## 9. Links e métricas-chave (seleção; lista completa em `data/F3_sources.csv`)
- Snopes gelatina (24/abr/2026): https://www.snopes.com/fact-check/weight-loss-gelatin-scam/
- Snopes pink salt (ago/2025): https://www.snopes.com/fact-check/oprah-pink-salt-weight-loss/
- Jordan Liles baking soda deepfake: https://jordanliles.com/scams/baking-soda-recipe-weight-loss/ · vídeo https://www.youtube.com/watch?v=9rZ1UKl9UuU (20.965 views)
- Dr. Jen Caudle baking soda: https://www.youtube.com/watch?v=DQS51EbyOBI (105.001) · cortisol cocktail: https://www.youtube.com/watch?v=E3EqgKEzMjk (3.597)
- Creatina: DOAC https://www.youtube.com/watch?v=Jk7RAkFN4vk (6,1M) · Jaramillo https://www.youtube.com/watch?v=3C4JZ4ShhW8 (3,85M) · Berg https://www.youtube.com/watch?v=nhYPkHh7bO0 (3,66M) · Pelz 7d https://www.youtube.com/watch?v=7II20nd_gsQ · Stacker 03/nov https://abc17news.com/stacker-wellness/2026/11/03/should-women-take-creatine-during-perimenopause/
- Fibra: WW https://www.weightwatchers.com/us/blog/fibermaxxing · Abbey Sharp https://www.youtube.com/watch?v=ZBz7iHswRgI · psyllium 2d https://www.youtube.com/watch?v=aQmP-6QtQY4
- Cottage cheese: CNN https://edition.cnn.com/2026/10/22/health/cottage-cheese-protein-benefits-wellness · AOL https://www.aol.com/articles/cottage-cheese-demand-surges-amid-080256674.html
- Menopausa 1,58M/7d: https://www.youtube.com/watch?v=o7EQ8iItS1Y
- Black seed oil: Berg https://www.youtube.com/watch?v=C7NhjQBMh-I (385k/1d) · Resilia 50+ https://www.youtube.com/watch?v=-easqSqku6g
- Lemon balm UK +800%: https://www.ladbible.com/news/health/natural-ozempic-tiktok-trend-lemon-balm-tea-972718-20251119
- Berberine/EFSA: https://www.nutraingredients.com/Article/2026/07/31/safety-in-question-what-is-the-future-of-berberine/
- Clove: https://www.youtube.com/watch?v=S89Qd06Iyu8 (8,86M)
- Oatzempic (Cleveland Clinic, nov/2026): https://health.clevelandclinic.org/oatzempic
- Print do usuário: /home/user/WL-2/01-pesquisa/01-pesquisa-usuario-briefing.md

---

## 10. Limitações e bloqueios
1. **Bloqueados pela rede:** trends.google.com, reddit.com, tiktok.com, instagram.com, Meta Ad Library, Google Ads Transparency, páginas de vídeo do YouTube (sem comentários), noom.com e womensfitness.co.uk (WebFetch). Google Trends real foi substituído pelo print do usuário (7d/30d, sem 90d/180d) — por isso as colunas trend_90d/180d usam idade e views de vídeos como proxy.
2. **Orçamento de WebSearch esgotado** (limite compartilhado do turno) após 25 buscas; 3 buscas planejadas não rodaram (Reddit "gelatin trick", "protein jello" imprensa, "viral trend November 2026"). Cobertura de Reddit = zero; a frente "ceticismo no Reddit" não pôde ser verificada diretamente (apenas via fact-checkers).
3. **YouTube:** o coletor público é ruidoso em filtros `week/month` (retorna conteúdo não relacionado); datas são relativas ("7mo ago"); contagens de "novos vídeos/mês" são direcionais. Sem acesso a comentários → **0 comentários literais de público**.
4. **Idade/gênero dos criadores:** não declarados na maioria; marquei "n/d" ou "inferência incerta". Títulos "after 40/50/menopause" são a única evidência de segmentação.
5. **Ciência:** não acessei PubMed; evidências vêm de resumos de Examine, Cleveland Clinic, GoodRx, WW, Noom, Stacker/ABC17, NutraIngredients. Black seed oil e colágeno precisam de verificação primária antes de uso em copy.
6. **Fontes de baixa qualidade** (páginas SEO em subdomínios .edu invadidos, blogs de receita, sites de "review") foram usadas apenas como **sinal de existência/mutação de tendência**, nunca como evidência.
7. **Velocidade vs. causalidade:** views altas = atenção; nenhum dado aqui mede conversão.

*Fim do relatório — Frente 03.*
