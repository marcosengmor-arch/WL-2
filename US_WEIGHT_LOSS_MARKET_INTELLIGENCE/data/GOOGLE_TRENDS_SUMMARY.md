# Google Trends — coleta própria (EUA, 19/11/2026)

Ferramenta: `tools/trends_collect.py` (pytrends, geo=US, `today 3-m` e `today 12-m`, related queries em 3 meses, pausas de 7–14 s, retentativas em 429). Dados brutos em `raw/TRENDS_*`; tabela consolidada em `data/GOOGLE_TRENDS.csv` (74 termos).
Leitura correta: o índice é **relativo ao termo-âncora de cada lote** (lote "ingredients" e "avatar" ancorados em "weight loss", que comprime termos de nicho para 0–4; lote "niche" ancorado em "gelatin trick", que compara os mecanismos entre si). Não há volume absoluto. Datas de pico = DADO; "por quê" = INTERPRETAÇÃO.

## 1. Lote "niche" (âncora: gelatin trick) — a comparação que importa para a VSL

| Termo | 12 meses (q1→q4, média por trimestre) | Pico 12m | 3 meses (primeiros 30d → últimos 30d → últimos 7d) | Status (busca) | Rising queries (3m) |
|---|---|---|---|---|---|
| **gelatin trick** | 63,5 → 54,2 → 17,8 → **5,1** | 04/01/2026 | 25,6 → 17,1 → 26,9 (ruído de mídia paga) | **Em declínio (−92% vs q1)** | "korean gelatin" (+810.750%), "horse soda trick", "baking soda trick for men" — mutação para pele/homens |
| **baking soda trick** | 19,0 → 11,4 → 13,5 → **23,9** | 13/09/2026 | 38,1 → 26,0 → 26,7 | Consolidada (2ª onda; já 4,7x o gelatin trick) | "baking soda trick for men step by-step" (+102.550%), "baking soda horse trick tiktok video" (+45.450%) — **migrou para homens** |
| **pink salt trick** | 6,8 → 4,0 → 1,5 → **0,1** | 16/11/2025 | 0 → 0,3 → 0,6 | Em declínio (morto) | "pink salt trick for neuropathy" (top) |
| **cortisol cocktail** | 3,0 → 3,2 → 3,0 → 1,7 | 22/03/2026 | 0 → 0,9 → **2,1** (pico 18/11/2026) | **Em aceleração (semana)** | "cortisol cocktail recipe for weight loss" (+300%); top: **"harmonia cortisol cocktail"** = marca de produto domina a busca → ad-driven |
| **creatine for women** | 44,5 → 71,8 → 65,5 → 45,4 | 12/04/2026 | 75,6 → 59,5 → 55,6 | **Consolidada em patamar alto** (≈11x gelatin trick hoje; não está acelerando na busca) | "clean nutra creatine for women reviews" (+500%) — intenção de compra; top "best creatine for women" |
| **black seed oil** | 57,4 → 73,5 → 58,7 → **64,1** | 05/04/2026 | 72,5 → 61,3 → 57,3 | Consolidada em patamar alto | "purely nutrient ethiopian black seed oil reviews" (+26.150%), "oil of oregano with black seed oil" — marca + combinação |
| **clove water** | 34,3 → 28,5 → 24,2 → 25,8 | 04/01/2026 | 22,3 → 22,2 → 21,4 | Consolidada | "can i drink clove water everyday" (+190%), "clove water benefits for women" |
| **berberine weight loss** | 18,3 → 30,8 → 26,2 → 15,2 | 05/04/2026 | 38,1 → 34,4 → 35,0 | Consolidada / passou o pico de abril | **"do berberine patches work for weight loss" (+300%)** — novo formato (adesivo) |
| **chia seed water** | 14,5 → 17,2 → 18,1 → 12,4 | 04/01/2026 | 13,0 → 8,0 → 9,4 | Em declínio leve | "does chia seed water help you lose weight" (+70%) |
| **natural GLP-1** | 8,5 → 18,5 → 14,2 → 12,7 | 12/04/2026 | pico isolado 20/09/2026 → 1,7 → 3,3 | Consolidada | "glp 1 natural supplement" (+1.000%) |
| **GLP-1 friendly** | 4,4 → 8,1 → 5,7 → 2,2 | 12/04/2026 | 1,4 → 2,7 → **3,6** | Em aceleração leve (varejo) | — |
| **cortisol belly** | 13,2 → 18,8 → 20,5 → 13,5 | 26/07/2026 | 44,0 (pico 20/09) → 17,8 → 19,0 | Consolidada | "is cortisol belly a real thing" (+60%), "is cortisol belly real" — **ceticismo já na busca** |
| **menopause belly fat** | 2,5 → 4,6 → 5,4 → 3,1 | 14/06/2026 | 1,4 → 3,4 → **4,9** (pico 24/10) | **Em aceleração** | **"how to get rid of belly fat after menopause" (+189.900%)**, "best supplements for menopause belly fat" (+70%) |
| **perimenopause weight gain** | 4,5 → 7,4 → 7,7 → 4,9 | 14/06/2026 | 9,4 → 19,0 → **26,1** (pico 27/08) | **Em aceleração** | "perimenopause sudden weight gain" (+130%) |
| **weight loss after 50** | 2,5 → 4,2 → 3,8 → 1,6 | 31/05/2026 | 0 → 7,8 → **9,9** (pico 29/10) | Em aceleração | "50 pound weight loss before and after" (+200%) |
| **hormone therapy weight loss** | 2,7 → 3,6 → 3,2 → 1,7 | 21/06/2026 | 0 → 5,7 → **10,7** (pico 03/10) | **Em aceleração** | — (coincide com estudo Menopause Society HT+GLP-1, out/2026, e fim do black box) |
| psyllium husk weight loss | 0,6 → 0,9 → 1,0 → 0,8 | — | 0,3 → 0,5 → 1,0 | Baixo volume, leve alta | "does psyllium husk help with weight loss" (+90%) |
| fibermaxxing | 0,1 → 0,5 → 0,5 → 0,2 | 04/01/2026 | pico 26/09 → 0,1 | Baixo volume | "fibermaxxing trend" (+70%) |
| cottage cheese diet | 3,1 → 3,6 → 3,3 → 2,4 | 04/01/2026 | 1,7 → 1,3 → 2,0 | Consolidada baixa | "can you have cottage cheese on carnivore diet" |
| lemon balm weight loss | 3,2 → 1,3 → 0,5 → **0,0** | 28/12/2025 | 0,3 → 0 → 0 | Em declínio (sem onda US) | — |

## 2. Lotes "ingredients" e "avatar" (âncora: weight loss) — o que o volume grande mostra
- **"weight loss"** 12m: pico 07/06/2026; 4º trimestre 52 (baixa sazonal pré-feriados; sobe em janeiro). Rising: **"trisha yearwood weight loss" (+21.700%)**, "richard satin unexplained weight loss", **"medvi quad reviews" / "medvi tirzepatide cost"** (telehealth), "em glp 1", "elixamd". Top: "glp 1" (100), "medvi" (70).
- **"Zepbound"** 3m: pico 10/11/2026 (alerta FDA/preços). **"Wegovy pill"** estável 2–4.
- **"berberine"** 12m: pico 05/04/2026 (13) → 4,4. **"protein coffee"**: pico 12/04/2026 (11) → 2,2. **"food noise"**: pico 05/04/2026 (5) → 1,0; rising "how to get rid of food noise", "how to quiet food noise". **"Ozempic face"**: rising "what does ozempic do to your face" (+45.550%), "ozempic droopy face" (+16.700%).
- **"stop taking Ozempic"**: rising **"here's what happens when you stop taking ozempic and wegovy" (+100.050%)** — confirma a sub-avatar "after the shot".
- **"metabolism after 40"**: rising **"how to speed up metabolism after 40" (+665.500%)**.
- **"GLP-1 supplement"**: top "embody glp-1" (marca), "best glp-1 supplement"; rising "embody" (+4.682.250%), "medvi" — a categoria "GLP-1 supplement" já tem marcas donas da busca.
- **"walking for weight loss"**: top inclui **"tai chi walking for weight loss" (53)** e "tai chi walking" (53) — confirma o formato-surpresa Tai Chi 50+.
- **"Jenna and Sheinelle"**: rising "today with jenna and sheinelle television show" (+317.400%), "jenna and sheinelle tension". **"Mary Claire Haver"**: rising "dr mary claire haver age" (+56.200%); top "mary claire haver supplements". **"Jillian Michaels"**: rising "jillian michaels collagen powder" (+22.300%), "jillian michaels andy cohen"; top dominado por vida pessoal — não por saúde.
- **"Valerie Bertinelli weight loss"**: pico 15/11/2026 (confirma print do usuário). **"Oprah menopause"**: top "oprah menopause special".
- Termos de nicho ancorados em "weight loss" ficam em 0–2 (compressão de escala) — usar o lote "niche" para compará-los.

## 3. O que isso muda nas conclusões (INTERPRETAÇÃO)
1. **Confirma**: gelatina (−92%), pink salt (morto), baking soda migrando para homens; cortisol cocktail acelerando **agora** (pico ontem) e já dominado por uma marca (Harmonia) → ad-driven; "natural GLP-1 supplement" com marcas donas da busca (Embody); Tai Chi walking como veículo 50+.
2. **Ajusta**: creatina para mulheres está em **patamar alto e estável** na busca (pico abr/2026), não "em aceleração" — a aceleração é no YouTube (vídeos novos) e no varejo. Continua a melhor oportunidade por ser 11x o gelatin trick em busca com zero VSL, mas a copy deve tratá-la como "o que todo mundo está pesquisando" (consolidada), não como novidade.
3. **Adiciona**: as buscas que mais crescem no trimestre são **"perimenopause weight gain"** (9 → 26), **"hormone therapy weight loss"** (0 → 11), **"weight loss after 50"** (0 → 10) e **"menopause belly fat"** (rising "how to get rid of belly fat after menopause" +189.900%) — a conversa de menopausa/HRT está em aceleração explícita na busca, alinhada com o black box removido e o estudo HT+GLP-1. Reforça BI-01/BI-02 e a lead "menopausa" nos primeiros 30 segundos.
4. **Alerta**: "is cortisol belly a real thing" subindo = ceticismo já na busca → cortisol como linguagem, nunca como mecanismo (como já recomendado).
5. **Novo formato de produto no radar**: "berberine patches" (+300%) — adesivos; não recomendado (berberina eliminada como central), mas sinal de que o mercado testa formatos novos para ingredientes velhos.
