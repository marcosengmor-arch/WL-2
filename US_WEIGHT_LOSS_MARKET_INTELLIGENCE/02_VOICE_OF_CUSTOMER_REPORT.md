# FRENTE 01 — VOZ REAL DAS CONSUMIDORAS (mulheres EUA 40+ e emagrecimento)

Data de coleta: 2026-11-19. Mercado: EUA. Relatório em PT-BR; citações preservadas em inglês. Arquivos complementares: `data/CUSTOMER_LANGUAGE.csv` (119 linhas) e `data/F1_sources.csv` (235 fontes). Bruto do YouTube em `raw/F1_yt_*.jsonl` (423 linhas, 382 vídeos únicos).

---

## 0. METODOLOGIA E AMOSTRA EFETIVA (leia antes de usar)

**Ferramentas.** WebSearch (modo "extended" na maioria), coletor público de busca do YouTube (`tools/yt_search.py`, títulos/snippets/views, sem comentários).

**Bloqueios confirmados nesta sessão (DADO):**
- `reddit.com` é inacessível ao crawler do WebSearch (erro 400 "domains not accessible to our user agent") e o proxy de rede recusa acesso direto. `site:reddit.com` e `allowed_domains=["reddit.com"]` falharam. **Resultado: 0 threads do Reddit lidas diretamente.** O Reddit aparece apenas de forma indireta (um estudo JAMA Network Open, via UMD, sobre o que as mulheres contam ao Reddit e não ao médico).
- WebFetch não resolve hosts de fóruns/Substack (healthunlocked.com, substack.com retornaram ENOTFOUND). Nenhuma página de fórum foi lida na íntegra; todo o conteúdo veio dos resumos do WebSearch, que trazem fragmentos literais.
- Comentários do YouTube: inacessíveis (páginas de vídeo bloqueadas). Coletei 382 vídeos únicos (títulos, snippets, views, recência) como **sinal de linguagem de criadores**, não como voz de consumidora.
- TikTok/Instagram/Meta Ad Library/Google Trends diretos: bloqueados (não tentei contornar).
- **Orçamento de buscas:** a cota compartilhada de WebSearch da sessão esgotou após 35 buscas bem-sucedidas (6 falharam por domínio bloqueado, 5 foram recusadas por limite). A meta de 60–100 buscas **não foi alcançada**. Temas que ficaram sem busca dedicada: marido/atração, Thanksgiving/fotos de família, dor nas articulações como ciclo vicioso, reações a episódios da Oprah, Trustpilot de telehealth (Mochi/Henry Meds), Quora específico. Onde há evidência parcial desses temas via YouTube, marquei como tal.

**Amostra efetiva.**
| Métrica | Meta do brief | Obtido |
|---|---|---|
| Buscas WebSearch | 60–100 | 35 efetivas (46 tentadas) |
| Discussões/comentários Reddit | 150 | **0 diretos**; 1 fonte indireta |
| Interações outras redes/fóruns/reviews | 50 | 23 posts/reviews de fóruns e sites de review (MyFitnessPal Community, Cronometer, HealthUnlocked*, Mumsnet*, Gransnet*, Drugs.com, WebMD Reviews, Trustpilot, Substack comments, BBB Scam Tracker) — *UK, marcados como não-US |
| Comentários YouTube | 300 | **0** (bloqueado); 382 vídeos únicos coletados como sinal de linguagem; 46 deles registrados em CUSTOMER_LANGUAGE.csv |
| Linhas de linguagem registradas | — | 119 (73 QUOTE verbatim / 46 PARAPHRASE) |
| Fontes únicas | — | 235 (115 não-YouTube + 120 YouTube) |

**Consequência para a leitura:** a voz "espontânea e crua" (Reddit, comentários) está sub-representada; o que capturei melhor é (a) linguagem de fóruns de emagrecimento com idade declarada, (b) reviews de medicamentos GLP-1 e de suplementos, (c) notícias/BBB sobre objeções e golpes, e (d) a linguagem que criadores do YouTube usam para **espelhar** o que a audiência 40+ diz (títulos em forma de pergunta da consumidora: "I'm barely eating, but the scale keeps climbing"). Trato (d) como proxy de linguagem com confiança MÉDIA, nunca como depoimento.

Convenções: QUOTE = literal no output da ferramenta; PARAPHRASE = resumo. Idade: "declarada" / "pista contextual" / "inferência incerta". IE = intensidade emocional (1–5); Freq = nº de fontes independentes observadas; Copy = utilidade para copy (1–5). Datas "n/d" quando a ferramenta não as mostrou; conteúdo com >90 dias marcado "histórico".

---

## 1. SÍNTESE EXECUTIVA (10 descobertas)

1. **A frase-núcleo do avatar é "eu faço tudo certo e a balança não se mexe / sobe" — e ela vem acompanhada de ritual descrito em detalhe** ("1200kcal religiosamente", "parei o álcool", "4 litros de água", "ando mais"). Confiança ALTA (MFP, HealthUnlocked, Mumsnet, YouTube 68K views em 2 dias).
2. **A dor física mais específica não é "peso", é "a cintura mudou com o peso igual"**: "pants fitting everywhere except the middle", "jeans won't zip", "went up two sizes at the waist while weight stayed the same". Confiança ALTA.
3. **"Comer menos piorou"** é o insight contra-intuitivo com mais tração em 2026: "Eating Less Made My Menopause Belly Worse", "The 1,200-Calorie Trap", "Don't Eat Like a Bird", "Don't Stop Eating". Abre mecanismo de VSL ("não é o quanto você come"). Confiança MÉDIA-ALTA.
4. **GLP-1: a conversa migrou de "funciona?" para "e quando eu parar?" e "quanto custa por quilo?"**: "the food noise came back", "the weight came back lightening quick plus a few", "coupon has run out… $900", "75% of patients are quietly quitting" (267K views), Medicare $50 bridge, microdosing. Confiança ALTA.
5. **Nasce o ângulo "GLP-1 natural por $1"** ("6 Foods Under $1 That Raise Your Own GLP-1", "Forget $1,000 GLP-1 Shots", "Mimic GLP-1 for Under $1"): a palavra-chave é "your own GLP-1 / your gut makes the hormone". Emergente. Confiança MÉDIA.
6. **Objeção dominante em 2026 = golpe com deepfake de celebridade/médico**: BBB registrou 150–170 denúncias do "pink salt trick"/LipoMax com vídeo falso da Oprah; exposés no YouTube sobre "Jillian Michaels gelatin trick" (51K views), Gumitide, Thermo Ignite. **Os próprios formatos benchmark (Oprah/TODAY/Jillian) já estão associados a golpe na mente de parte do público.** Confiança ALTA.
7. **Sinal viral da semana: "Menopause Weight Gain Wasn't a Thing in 1945 — What Changed?" — 1,58M views em 7 dias**, com dois clones em dias ("1950s habits", "wasn't a thing in 1950 — a doctor explains"). Ângulo nostálgico/"o que mudou no ambiente" (não "o que há de errado com você"). Emergente, em aceleração. Confiança MÉDIA (views = atenção).
8. **Desejo 60+ não é número na balança: é energia, mobilidade e "não aceitar menos"**: "63 is too old to change…" (3,88M views em 2 semanas): "I want more than just a number on the scale. I want to wake up feeling energetic." Confiança MÉDIA-ALTA.
9. **Dor emocional de fundo: invisibilidade e "guerra com o espelho"** ("a war with my reflection", "sometimes invisible altogether", só 15% com alta confiança em qualquer área da vida). A roupa é o gatilho de retração social (estudo com 252 mulheres 38–67). Confiança MÉDIA.
10. **Metformina/berberina: o interesse (Trends +3100%) convive com decepção na prática** ("helped somewhat, but not enough for me to lose any weight"; "about 5 pounds over a few months"; "secondary benefit, not guaranteed"). Oportunidade para "o que a berberina não consegue". Confiança MÉDIA.

---

## 2. DORES RECORRENTES (A. físicas/funcionais e B. emocionais) — 22 itens

| # | Dor | Evidência (fonte / link / tipo) | IE | Freq | Copy |
|---|---|---|---|---|---|
| D1 | **Gordura migrou para a barriga com peso igual** | QUOTE "pants fitting everywhere except the middle"; "go up two clothing sizes around the waist while their weight stays the same" — Dr. Haver Substack (US) https://drmaryclairehaver.substack.com/p/what-i-got-wrong-about-the-menopause ; QUOTE "Your weight hasn't changed, but your jeans suddenly feel tighter? You're not imagining it!" YouTube Rebbecca Hertel DO https://www.youtube.com/watch?v=1Yqe1Qi5OiA | 4 | 6 | 5 |
| D2 | **"Como pouco e engordo"** | QUOTE "'I'm barely eating, but the scale keeps climbing. Is it my hormones, my metabolism, or something else?'" (pergunta de ouvinte, Morphus) https://www.youtube.com/watch?v=bWcdLxW_FCE ; PBS "gaining weight for no apparent reason" https://www.pbs.org/video/4-ilpjcj/ | 4 | 5 | 5 |
| D3 | **Fiz tudo "certo" e nada** | QUOTE "I have religiously stuck to the recommended 1200kcal a day, stopped all alcohol, go cycling twice a…" (55 anos) MFP https://community.myfitnesspal.com/en/discussion/10856678/weight-loss-during-the-menopause ; QUOTE "You eat less, walk more, drink your 4 litres of water, throw…" (68.629 views/2 dias) https://www.youtube.com/watch?v=8VIwovYaS4k | 5 | 7 | 5 |
| D4 | **O que funcionava antes parou de funcionar** | QUOTE "I used to be able to lose weight through restriction and exercise and that is not currently doing the trick for me." MFP https://community.myfitnesspal.com/en/discussion/1410842/menopause-related-weight-gain-how-do-i-lose-weight-now ; QUOTE "the same diet, the same exercise and the same routines that held things steady in your 30s now seem to deliver the opposite result" https://thebettermenopause.com/en-us/blogs/the-better-gut-community/perimenopause-weight-gain-why-it-happens-and-what-actually-helps | 4 | 5 | 5 |
| D5 | **Ganho rápido e inexplicado em 1 ano** | PARAPHRASE 56 anos, "put on over a stone in the past year and can't seem to lose it" HealthUnlocked (UK) https://healthunlocked.com/weight-loss-support/posts/130588712/... ; QUOTE "I gained 10 pounds in the past year and trying to lose. It's been really hard." Cronometer (US, 50+) https://forums.cronometer.com/discussion/comment/15875 | 3 | 3 | 4 |
| D6 | **Barriga "dura como balão" no fim da tarde** | QUOTE "Feels like your stomach turns into a tight, hard balloon around 3 PM?" YouTube https://www.youtube.com/watch?v=qCAhplLeB5k | 3 | 1 | 4 |
| D7 | **Fome/"food noise" volta ao parar o GLP-1** | QUOTE "patients often describe the food noise coming back" Sutter Health https://www.sutterhealth.org/health/stopping-ozempic ; QUOTE "Then the food noise came back." https://www.youtube.com/watch?v=HVhwvFVArxo | 5 | 5 | 5 |
| D8 | **Reganho rápido pós-GLP-1** | QUOTE "the weight came back lightening quick plus a few" Drugs.com https://www.drugs.com/comments/semaglutide/wegovy.html?page=2 ; PARAPHRASE reganho ~4x mais rápido que pós-dieta (Oxford, jan/2026) https://www.tctmd.com/news/weight-regained-within-18-months-stopping-glp-1-drugs | 5 | 6 | 5 |
| D9 | **Efeitos colaterais do GLP-1 (fadiga, queda de cabelo, náusea)** | QUOTE "the only side effect is horrible hair loss" (72 anos) WebMD https://reviews.webmd.com/drugs/drugreview-187794-zepbound-subcutaneous ; QUOTE "side effects are too much for me" Drugs.com | 3 | 4 | 4 |
| D10 | **"Ozempic face"/pele flácida após perda rápida** | PARAPHRASE Diane, 63, facelift e enxerto de gordura https://www.yahoo.com/lifestyle/articles/women-flock-surgery-annoying-ozempic-230338860.html ; QUOTE "skin changes are one reason some people hesitate about or quit these drugs, especially women" https://glp1newsnow.substack.com/p/ozempic-face-was-just-the-beginning | 4 | 4 | 4 |
| D11 | **Articulações/impacto: precisa perder peso sem pular** | QUOTE "Want to lose weight without jumping, running, or putting stress on your joints?" (1,01M views) https://www.youtube.com/watch?v=YPSAQKhKQ6s ; cluster Tai Chi "belly fat after 50" >10M views acumulados | 3 | 5 | 4 |
| D12 | **Tireoide "normal" no exame, peso não se mexe** | QUOTE "Blood test says normal, but the weight still won't move?" https://www.youtube.com/watch?v=EKgIUEVgUo8 ; PARAPHRASE TSH 3,5–4,0 "normal" com sintomas https://thenutritiondesk.com/blog/hypothyroidism-and-weight-loss/ | 3 | 3 | 4 |
| D13 | **Sono ruim = barriga** | PARAPHRASE 6h vs 7h de sono = +1,6 lb https://hormonallyspeaking.substack.com/p/why-your-body-is-changing-shape-and ; QUOTE "Sis, your sleep and your belly are telling the same…" https://www.youtube.com/watch?v=vXHCcprg8is | 2 | 3 | 3 |
| D14 | **Custo: "$900 do próprio bolso", "$1.000/mês ou nada"** | QUOTE "the coupon has run out, and now my out-of-pocket cost with insurance is around $900" Drugs.com ; QUOTE "I've lost 56 pounds on Zepbound at 72, but how much has it actually cost me?" https://www.youtube.com/watch?v=FgaTzHs58A0 | 4 | 6 | 5 |
| **Emocionais** | | | | | |
| D15 | **Desesperança: "nunca mais vou ter um peso saudável"** | QUOTE "I feel like I'm never going to be a healthy weight now that I'm menopausal." (54, UK) https://healthunlocked.com/weight-loss-support/posts/133327270/have-i-left-it-too-late | 5 | 2 | 5 |
| D16 | **Raiva de ser dispensada pelo médico ("é a menopausa")** | QUOTE "weight gain was 5 to 7 lbs but it made me CRAZY!" + médico atribuiu à menopausa, Substack comments https://nadinearaksi.substack.com/p/the-messy-truth-about-perimenopause/comments ; estudo: mulheres contam ao Reddit, não ao médico https://today.umd.edu/women-are-telling-reddit-not-doctors-about-menopause | 4 | 3 | 5 |
| D17 | **Guerra com o espelho / não se reconhecer** | QUOTE "a war with my reflection" (50s) https://sixtyandme.com/aging-women-expectation/ | 5 | 2 | 5 |
| D18 | **Invisibilidade social** | QUOTE "Less remarked upon. Sometimes invisible altogether." https://secondseasonlife.substack.com/p/feeling-invisible-after-50-and-how ; QUOTE "talked over by sales people, ignored trying to order a drink at a bar" https://kimfoster.substack.com/p/on-fuckability | 4 | 4 | 4 |
| D19 | **Roupa que não serve → retração social** | PARAPHRASE mulheres sem roupa que dê confiança se retraem socialmente (252 mulheres 38–67) https://goddessgear.net/blogs/... | 4 | 2 | 5 |
| D20 | **Vergonha de precisar de remédio / medo de depender** | PARAPHRASE "needing ongoing treatment isn't a failure… what to do if you can't afford to continue" (Dr Sophie GP, YouTube) ; QUOTE "Weight regain after stopping a GLP-1 is not a willpower problem. It is biology." https://www.youtube.com/watch?v=I48LcDn2OEA | 3 | 3 | 4 |
| D21 | **Cansaço de recomeçar programas** | QUOTE "Tired of starting another weight loss program only to quit because the rules are too restrictive?" https://www.youtube.com/watch?v=3yDNTTUbYjs ; QUOTE "But can you live like that forever?" https://www.youtube.com/watch?v=BTyGmcGcjvk | 4 | 3 | 5 |
| D22 | **Baixa confiança generalizada após os 50** | PARAPHRASE só 15% com alta confiança em qualquer área da vida https://pcar.org/blog/invisible-woman-syndrome-can-make-aging-hard | 3 | 1 | 3 |

---

## 3. DESEJOS (E) — 20 itens (14 com evidência direta; 6 marcados INTERPRETAÇÃO, derivados das dores)

| # | Desejo | Evidência | IE | Freq | Copy |
|---|---|---|---|---|---|
| E1 | **Silêncio mental sobre comida** ("food noise gone") | QUOTE "The mental food noise is gone." Drugs.com https://www.drugs.com/comments/tirzepatide/zepbound.html | 5 | 5 | 5 |
| E2 | **Energia ao acordar e mover-se sem dor — mais que número** | QUOTE "I want more than just a number on the scale. I want to wake up feeling energetic. I want to move without feeling…" (63 anos, 3,88M views) https://www.youtube.com/watch?v=UgMoMFLCuKQ | 5 | 2 | 5 |
| E3 | **Não aceitar "menos" com a idade** | QUOTE "I used to think getting older meant accepting less. Less energy. Less strength. Less confidence in my own body." https://www.youtube.com/watch?v=-aHyS4ofKVw | 5 | 1 | 5 |
| E4 | **Resultado sem receita médica e sem abrir mão de comida** | QUOTE "I lost 5 inches of menopause belly fat in three months. At 58. Without a prescription. And without giving up food I love." (232K views) https://www.youtube.com/watch?v=d6j7zcmcIok | 4 | 3 | 5 |
| E5 | **Perder cintura/barriga especificamente (polegadas, não libras)** | mesmo acima ("5 inches"); "How I Lost 15 Lbs of Belly Fat At 64!" (274K) https://www.youtube.com/watch?v=4tPbPS5dKaU | 4 | 5 | 5 |
| E6 | **Alternativa barata ao GLP-1 que use "o próprio GLP-1"** | QUOTE "Your gut makes the hormone it…" / "6 Foods Under $1 That Raise Your Own GLP-1" https://www.youtube.com/watch?v=JqvpwXcT_XY ; "Forget $1,000 GLP-1 Shots!" https://www.youtube.com/watch?v=NKbTapyRdIQ | 4 | 5 | 5 |
| E7 | **Simplicidade: sem horas de exercício** | QUOTE "I was 54 when i finally realized i didn't need to do hours of exercise to lose weight i was making it far more complicated than it…" https://www.youtube.com/watch?v=FpEIuD7xqPs | 3 | 3 | 4 |
| E8 | **Sem dieta miserável / regras restritivas** | QUOTE "Fat Loss After 50 Without Miserable Diets" https://www.youtube.com/watch?v=3yDNTTUbYjs ; "No Dieting, No Cardio" (WarriorBabe, 98K views) | 4 | 4 | 5 |
| E9 | **Manter o que perdeu (keep it off)** | QUOTE "Losing Weight in Menopause Is Hard. Keeping It Off Is Harder." https://www.youtube.com/watch?v=BTyGmcGcjvk ; "I Lost 95 Lbs in Menopause and Kept it Off" (Nurse Julie) | 4 | 4 | 4 |
| E10 | **Liberdade (não "controle")** | QUOTE "Oprah Winfrey on How She Found 'New Freedom' After Weight Loss" TODAY (341K) https://www.youtube.com/watch?v=2AKX0dGq_x8 | 4 | 2 | 4 |
| E11 | **Parar de se pesar / paz com o corpo** | PARAPHRASE Valerie Bertinelli (65) "focuses less on the scale", Trends +3050% https://www.thelist.com/2132185/valerie-bertinelli-thoughts-ozempic-glp-1-never-taking-them | 3 | 2 | 3 |
| E12 | **Validação: "não é falta de força de vontade"** | "The Menopause Belly Is Real — And It's Not About Willpower" https://drmaryclairehaver.substack.com/p/the-menopause-belly-is-real-and-its ; "Why 'eat less, move more' is wrong" https://www.youtube.com/watch?v=48JcS2dsOTo | 4 | 5 | 5 |
| E13 | **Perder peso antes de um evento/feriado** | QUOTE "Lose menopausal belly fat before Christmas" https://www.youtube.com/watch?v=EpVIEPo738s ; Forbes tester 50+ usaria Noom "to get ready for a special event, like a wedding or vacation" https://www.forbes.com/health/weight-loss/best-weight-loss-program-women-over-50/ | 3 | 3 | 4 |
| E14 | **Entender "o que mudou" (causa), não só "o que fazer"** | 1,58M views em 7d "Menopause Weight Gain Wasn't a Thing in 1945 — What Changed?" https://www.youtube.com/watch?v=o7EQ8iItS1Y | 4 | 3 | 5 |
| E15 | Vestir a roupa antiga / fechar o jeans | INTERPRETAÇÃO a partir de D1/D19 ("jeans won't zip") | 4 | — | 5 |
| E16 | Voltar a ser vista (fim da invisibilidade) | INTERPRETAÇÃO a partir de D17/D18 | 4 | — | 4 |
| E17 | Ser levada a sério pelo médico / ter uma explicação | INTERPRETAÇÃO a partir de D16 | 4 | — | 4 |
| E18 | Não depender de injeção para sempre | INTERPRETAÇÃO a partir de D7/D8/D14/D20 | 4 | — | 5 |
| E19 | Resultado que não deixe o rosto "velho" (sem Ozempic face) | INTERPRETAÇÃO a partir de D10 | 3 | — | 4 |
| E20 | Movimento gentil, sem impacto | evidência indireta D11 (Tai Chi 50+ >10M views) | 3 | — | 3 |

---

## 4. FRACASSOS ANTERIORES (C) — 16 itens

| # | O que tentou e falhou | Evidência | IE | Freq | Copy |
|---|---|---|---|---|---|
| C1 | 1.200 kcal/dia religiosamente | QUOTE MFP (55 anos) acima; Mumsnet (50, UK) "not losing on 1200 cals" https://www.mumsnet.com/talk/calorie_counting/4502931-Why-am-I-not-losing-weight-on-1200-cals | 4 | 5 | 5 |
| C2 | Comer ainda menos (1.100 kcal, "comer como passarinho") | PARAPHRASE trainer: mulheres a ~1.100 kcal sem perder https://29againfitness.com/timonium-personal-training-blog/menopause-weight-gain-exercise/ ; "Don't Eat Like a Bird to Lose Weight After 60" (YouTube) | 4 | 5 | 5 |
| C3 | Parar de comer quando a balança sobe | QUOTE "A patient in her 60s stopped eating because the scale went up. Here's why that backfires" https://www.youtube.com/watch?v=8jqiYqWfe0Y | 4 | 1 | 4 |
| C4 | Weight Watchers (funcionou, não sustentou) | PARAPHRASE 54 anos, HealthUnlocked (UK) | 3 | 1 | 3 |
| C5 | Restrição + exercício (o método de sempre) | QUOTE "that is not currently doing the trick for me" MFP | 4 | 3 | 5 |
| C6 | Academia/cardio longo | PARAPHRASE "gain weight quickly even though I still go to the gym" HealthUnlocked (UK) https://healthunlocked.com/weight-loss-support/posts/139711035/menopause ; crença cardio↑cortisol https://www.spotyellow.com/blog/menopause-weight-gain/ | 3 | 3 | 4 |
| C7 | Low carb/keto extremo (não dá para viver assim) | QUOTE "Very low carb and 1100-calorie days… But can you live like that forever?" | 3 | 2 | 4 |
| C8 | GLP-1 → parou → reganho | QUOTE "lightening quick plus a few" Drugs.com; CNN: +40 lb após negativa do seguro https://www.cnn.com/2024/01/08/health/weight-loss-drug-insurance-denials/index.html ; "I Quit Mounjaro… Now I've Gained 2 Stone" (UK, YouTube) | 5 | 6 | 5 |
| C9 | GLP-1 → efeitos colaterais insuportáveis | QUOTE "side effects are too much for me" Drugs.com | 3 | 3 | 4 |
| C10 | GLP-1 composto por telehealth (barato) → overdose/hospital | QUOTE "just the most affordable option" (Karleigh McClain) https://www.usnews.com/news/health-news/articles/2026-06-03/... ; chamadas ao centro de intoxicação na Geórgia +1600% https://www.youtube.com/watch?v=iCtlzWUtOMo | 4 | 3 | 4 |
| C11 | Berberina ("Ozempic natural") | PARAPHRASE "helped somewhat, but not enough for me to lose any weight" https://www.everywomanover29.com/blog/berberine-in-perimenopause-and-menopause-... ; ~5 lb em meses https://www.joinmidi.com/post/best-berberine-supplement | 3 | 4 | 5 |
| C12 | Metformina off-label | PARAPHRASE 2–5 kg/6 meses só com resistência à insulina; "secondary benefit rather than a guaranteed outcome" https://pmos-pcos.com/metformin-pcos/ | 2 | 3 | 4 |
| C13 | Baking soda trick | PARAPHRASE 21 dias → 2,8 lb "mostly because I simply ate less" https://www.noom.com/blog/weight-management/viral-weight-loss-drinks/ | 3 | 3 | 4 |
| C14 | Gelatin trick | PARAPHRASE 30 dias → 4,6 lb, "didn't melt belly fat by itself" https://www.noglubread.com/gelatin-trick-with-baking-soda/ ; QUOTE "the gelatin trick will not burn fat, as some claim" TODAY https://www.today.com/health/diet-fitness/gelatin-trick-work-weight-loss-dietitians-explain-rcna346540 | 3 | 4 | 4 |
| C15 | Cortisol cocktail | PARAPHRASE Noom: "not supported" | 2 | 2 | 3 |
| C16 | Remédio de tireoide com dose subindo e peso igual | QUOTE "Her dose had gone up from 12.5 mcg → 25 mcg → 50 mcg → 75 mcg" https://www.youtube.com/watch?v=g5Mf84auxLA | 3 | 2 | 4 |

Não encontrado nas buscas (limitadas): ACV gummies, pink salt (só como golpe), desafios de 30 dias, jejum intermitente como fracasso.

---

## 5. CRENÇAS SOBRE A CAUSA (D) — 17 itens (crença ≠ fato)

| # | Crença (como ela diz) | Evidência | Status médico (DADO) | IE | Freq | Copy |
|---|---|---|---|---|---|---|
| B1 | "É a menopausa/estrogênio: a gordura foi para a barriga" | Mayo, Harvard, Haver; 1,58M views "what changed" | Redistribuição real; ganho total é ~1,5 lb/ano (Mayo) | 4 | 8 | 5 |
| B2 | "Meu metabolismo desabou depois dos 40" | Trends "does your metabolism slow down as you get older" +200% (print do usuário); QUOTE contrária: "A study of 6421 people found it barely changes between ages 20 and 60" https://www.youtube.com/watch?v=_Ifk5C7Cw0w | Contestada (estudo Pontzer); perda muscular é o fator | 4 | 6 | 5 |
| B3 | "Cortisol belly" (estresse engorda a barriga) | QUOTE "chronic cortisol elevation does redirect fat to your midsection" https://hacks4wellness.com/cortisol-and-weight-gain-after-40/ ; QUOTE WebMD "there are no proven supplements to reduce 'cortisol belly'" | Termo de rede social; efeito real pequeno; Cushing é raro | 4 | 6 | 4 |
| B4 | "Comer menos faz engordar / 1200 kcal é armadilha" | cluster YouTube "Eating Less Made My Menopause Belly Worse", "The 1,200-Calorie Trap"; HealthUnlocked "upped calories and lost weight" | Parcial: subnotificação de ingestão + perda muscular | 4 | 6 | 5 |
| B5 | "Resistência à insulina trava tudo" | Trends metformina +3100%; "Insulin Resistance? 7 Ways to Finally Lose Stubborn Belly Fat After 40" | Plausível em subgrupo (PCOS, pré-diabetes) | 3 | 5 | 4 |
| B6 | "É a tireoide, mesmo com exame normal" | D12 | Hipotireoidismo tratado perde peso como as demais (Sci Reports 2024) | 3 | 4 | 4 |
| B7 | "Gordura hormonal é diferente da gordura normal" | QUOTE "The belly fat you're fighting isn't regular fat—it's hormonal fat" (180K views) https://www.youtube.com/watch?v=n3ztVUhC4a0 | Visceral ≠ subcutânea, mas não "hormonal" como categoria | 3 | 4 | 5 |
| B8 | "Dormir mal engorda a barriga" | D13 | Suporte razoável | 2 | 3 | 3 |
| B9 | "Cardio intenso aumenta cortisol e piora" | Spotyellow; Jay Shetty/Dr. Shannon Ritchey (468K) "Hard workouts might be why your body isn't changing" | Fraco | 3 | 3 | 4 |
| B10 | "Médico não leva a sério / diz que é idade" | D16 | — | 4 | 3 | 5 |
| B11 | "GLP-1 é para sempre; se parar, volta tudo" | D8; "You'll Regain All The Weight" (Valuetainment 210K); "16 Celebs Who QUIT Ozempic and Gained It ALL Back" (141K) | Reganho médio ~2/3 em 1 ano; não universal | 4 | 7 | 5 |
| B12 | "Berberina é o Ozempic da natureza" | 10+ vídeos "Is berberine nature's Ozempic?" (maioria desmente) | Efeito modesto | 3 | 6 | 4 |
| B13 | "O corpo produz seu próprio GLP-1 e dá para ativá-lo com comida" | E6 cluster | Verdadeiro em parte; magnitude muito menor que droga | 4 | 5 | 5 |
| B14 | "Algo mudou no ambiente/alimentação desde 1945/1950" | 1,58M views + clones | Hipótese de criador | 4 | 3 | 5 |
| B15 | "Microdose resolve custo e efeitos colaterais" | AARP, SciFri, ThePrint (11,8K), Jen Ashton; QUOTE "Smallest dose possible. Every other week." (48 anos) https://www.youtube.com/watch?v=WxKDpsIn2Uk | Sem evidência; alertas de risco | 3 | 5 | 4 |
| B16 | "Perda rápida envelhece o rosto" | D10 | Real (perda de gordura facial) | 4 | 4 | 4 |
| B17 | "Creatina após os 50 encolhe gordura/segura músculo" | Berg 3,66M views (1 mês); Azadi 3,95M; Amazon ON Creatine 40K+/mês (print do usuário) | Creatina ajuda força/músculo; "shrinks fat cells 30%" não comprovado | 3 | 3 | 4 |

---

## 6. OBJEÇÕES (F) — 17 itens

| # | Objeção | Evidência | IE | Freq | Copy |
|---|---|---|---|---|---|
| O1 | **"É deepfake da Oprah/médico"** | BBB: 170+ denúncias LipoMax/"pink salt trick" em 2 meses, consumidora de Illinois perdeu $400+ https://www.bbb.org/article/scams/32431-bbb-scam-alert-use-caution-when-searching-for-weight-loss-products-online ; WGEM ago/2026 https://www.wgem.com/2026/08/03/deepfake-ai-scam-uses-celebrity-likenesses-push-fake-supplements-bbb-warns/ | 5 | 5 | 5 |
| O2 | **"Jillian Michaels gelatin trick é golpe"** | QUOTE "Seen the Jillian Michaels 'gelatin trick recipe' ad on Facebook, YouTube… I clicked through the whole thing" (51K views) https://www.youtube.com/watch?v=hmur2hAeJnw ; Gumitide "Is Jillian Michaels Involved?"; Thermo Ignite "Oprah, Kelly Clarkson, Dr. Oz Baking Soda Scam" https://www.youtube.com/watch?v=4qH0OQZ4snQ | 5 | 4 | 5 |
| O3 | **Armadilha de assinatura / cobrança recorrente** | PARAPHRASE $32 "membership" → tentativas de cobrar $670 https://www.bbb.org/article/news-releases/16895-bbb-tip-misleading-ads-and-subscription-traps-for-weight-loss-products | 5 | 2 | 5 |
| O4 | **"Reembolso prometido nunca vem"** | Trustpilot Sugar Control Keto Gummies 2,5/5 https://ca.trustpilot.com/review/sugarcontrol.trashlify.com | 4 | 1 | 4 |
| O5 | **"Natural Ozempic" = red flag (FTC)** | FTC warning letters; "claims 'natural Ozempic' or costs under $50 a month" como alerta https://www.glp1clinics.org/blog/glp1-supplements-truth | 4 | 3 | 5 |
| O6 | "Nenhuma gummy chega perto de 15–22% de perda" | mesmo acima; theglpspot | 3 | 3 | 4 |
| O7 | "Suplemento de Amazon é de marca duvidosa" | QUOTE "Did you try a reputable BRAND bought from a reputable SELLER, not the internet, including Amazon?" WebMD https://reviews.webmd.com/vitamins-supplements/ingredientreview-1126-BERBERINE | 3 | 1 | 4 |
| O8 | "Não posso pagar $1.000/mês; cupom acabou" | D14 | 5 | 6 | 5 |
| O9 | "Composto por telehealth é inseguro/ilegal agora" | Fortune out/2026 (FDA enforcement) https://fortune.com/2026/10/03/fda-compounded-glp1-telehealth-enforcement/ ; 4 provedores fecharam no Q1 2026 https://telehealthally.com/guides/glp1-telehealth-pricing-report-q2-2026 | 4 | 4 | 4 |
| O10 | "Vou perder o rosto/pele" | D10 | 4 | 4 | 4 |
| O11 | "Cai cabelo / enjoo / cansaço" | D9; 7,1% mulheres vs <1% homens com queda https://asktia.com/article/zepbound-for-women/ | 3 | 4 | 4 |
| O12 | "Perde músculo após os 60" | "GLP-1 Muscle Loss After 60: What the 2026 Studies Show"; Nature Medicine 9/nov/2026 (YouTube Veeff Gym) | 3 | 3 | 4 |
| O13 | "Novo alerta da FDA (olhos) em 9/nov/2026" | https://www.youtube.com/watch?v=-JKRHaJoecI | 3 | 1 | 3 |
| O14 | "Já ouvi 'eat less move more' mil vezes" | B10, E12 | 4 | 4 | 5 |
| O15 | "Drinks virais não funcionam (dietistas)" | TODAY gelatin; Noom | 3 | 4 | 4 |
| O16 | "Promessa 'sem dieta e sem exercício' é sempre falsa" (FTC via BBB) | BBB tip acima | 4 | 2 | 4 |
| O17 | "Engordar na menopausa é normal, por que patologizar?" (contra-voz anti-dieta) | QUOTE "we shouldn't be pathologizing that at baseline" https://virginiasolesmith.substack.com/p/dr-mara-will-not-sell-you-a-weighted ; Jillian Michaels vs 20 body-positivity (Jubilee), 326K views "She's Fat." (Greg Doucette) | 3 | 3 | 3 |

---

## 7. ≥30 EXPRESSÕES ORIGINAIS (verbatim, com link) — 34 selecionadas das 73 QUOTES do CSV

1. "I have religiously stuck to the recommended 1200kcal a day, stopped all alcohol, go cycling twice a…" — MFP, 55 anos (declarada) — https://community.myfitnesspal.com/en/discussion/10856678/weight-loss-during-the-menopause — frustração — rel. 5
2. "I used to be able to lose weight through restriction and exercise and that is not currently doing the trick for me." — MFP — https://community.myfitnesspal.com/en/discussion/1410842/menopause-related-weight-gain-how-do-i-lose-weight-now — confusão — 5
3. "Hi, I'm new. I'm a 60 year old woman and I'm having trouble losing weight." — MFP, 60 (declarada) — https://community.myfitnesspal.com/en/discussion/10930123/60-year-old-woman-weight-loss — 3
4. "I feel like I'm never going to be a healthy weight now that I'm menopausal." — HealthUnlocked (UK), 54 — https://healthunlocked.com/weight-loss-support/posts/133327270/have-i-left-it-too-late — desesperança — 5
5. "Hi - I gained 10 pounds in the past year and trying to lose. It's been really hard." — Cronometer (US), 50+ — https://forums.cronometer.com/discussion/comment/15875 — 3
6. "pants fitting everywhere except the middle" — Dr. Haver Substack — https://drmaryclairehaver.substack.com/p/what-i-got-wrong-about-the-menopause — 5
7. "Some women go up two clothing sizes around the waist while their weight stays the same" — idem — 5
8. "weight gain was 5 to 7 lbs but it made me CRAZY!" — Substack comments — https://nadinearaksi.substack.com/p/the-messy-truth-about-perimenopause/comments — raiva — 5
9. "The mental food noise is gone." — Drugs.com Zepbound — https://www.drugs.com/comments/tirzepatide/zepbound.html — alívio — 5
10. "side effects are too much for me" — Drugs.com Zepbound — idem — 4
11. "the only side effect is horrible hair loss" — WebMD, 72 (declarada) — https://reviews.webmd.com/drugs/drugreview-187794-zepbound-subcutaneous — 4
12. "the coupon has run out, and now my out-of-pocket cost with insurance is around $900" — Drugs.com Wegovy — https://www.drugs.com/comments/semaglutide/wegovy.html — ansiedade — 5
13. "the weight came back lightening quick plus a few" — Drugs.com Wegovy — https://www.drugs.com/comments/semaglutide/wegovy.html?page=2 — desespero — 5
14. "patients often describe the food noise coming back" — Sutter Health — https://www.sutterhealth.org/health/stopping-ozempic — 5
15. "just the most affordable option" — paciente (US News) — https://www.usnews.com/news/health-news/articles/2026-06-03/telehealth-booms-as-demand-for-glp-1s-surges-and-questions-mount-about-safety-oversight — 4
16. "skin changes are one reason some people hesitate about or quit these drugs, especially women" — GLP1 News Now — https://glp1newsnow.substack.com/p/ozempic-face-was-just-the-beginning — 4
17. "a war with my reflection" — SixtyAndMe, 50s — https://sixtyandme.com/aging-women-expectation/ — luto — 5
18. "Less remarked upon. Sometimes invisible altogether." — Substack — https://secondseasonlife.substack.com/p/feeling-invisible-after-50-and-how — 4
19. "stopped auditioning for rooms that weren't interested" — Art in Aging — https://www.artinaging.com/blogs/art-in-aging-blog/invisible-woman-after-50 — 3
20. "Did you try a reputable BRAND bought from a reputable SELLER, not the internet, including Amazon?" — WebMD reviews — https://reviews.webmd.com/vitamins-supplements/ingredientreview-1126-BERBERINE — 3
21. "the gelatin trick will not burn fat, as some claim" — TODAY — https://www.today.com/health/diet-fitness/gelatin-trick-work-weight-loss-dietitians-explain-rcna346540 — 4
22. "there are no proven supplements to reduce 'cortisol belly'" — WebMD — https://www.webmd.com/diet/cortisol-belly — 3
23. "the same diet, the same exercise and the same routines that held things steady in your 30s now seem to deliver the opposite result" — The Better Menopause — https://thebettermenopause.com/en-us/blogs/the-better-gut-community/perimenopause-weight-gain-why-it-happens-and-what-actually-helps — 5
24. "we shouldn't be pathologizing that at baseline" — Burnt Toast — https://virginiasolesmith.substack.com/p/dr-mara-will-not-sell-you-a-weighted — 3
25. "At this stage of life, I want more than just a number on the scale. I want to wake up feeling energetic." — YouTube, 63 (declarada), 3,88M views — https://www.youtube.com/watch?v=UgMoMFLCuKQ — 5
26. "I used to think getting older meant accepting less. Less energy. Less strength. Less confidence in my own body." — YouTube — https://www.youtube.com/watch?v=-aHyS4ofKVw — 5
27. "You eat less, walk more, drink your 4 litres of water, throw …" — YouTube, 68.629 views/2d — https://www.youtube.com/watch?v=8VIwovYaS4k — 5
28. "'I'm barely eating, but the scale keeps climbing. Is it my hormones, my metabolism, or something else?'" — YouTube (pergunta de ouvinte) — https://www.youtube.com/watch?v=bWcdLxW_FCE — 5
29. "'Why does my waist look different from my mother's at the same age, even when I don't eat that much?'" — YouTube — https://www.youtube.com/watch?v=LjK8nkZz6ao — 4
30. "Feels like your stomach turns into a tight, hard balloon around 3 PM?" — YouTube — https://www.youtube.com/watch?v=qCAhplLeB5k — 4
31. "Your weight hasn't changed, but your jeans suddenly feel tighter? You're not imagining it!" — YouTube — https://www.youtube.com/watch?v=1Yqe1Qi5OiA — 5
32. "I thought reaching my goal weight meant I was ready to stop Zepbound. Then the food noise came back." — YouTube (homem) — https://www.youtube.com/watch?v=HVhwvFVArxo — 4
33. "I've lost 56 pounds on Zepbound at 72, but how much has it actually cost me?" — YouTube, 72 (declarada) — https://www.youtube.com/watch?v=FgaTzHs58A0 — 5
34. "I lost 5 inches of menopause belly fat in three months. At 58. Without a prescription. And without giving up food I love." — YouTube, 58 (declarada), 232K views — https://www.youtube.com/watch?v=d6j7zcmcIok — 5

---

## 8. CONTRADIÇÕES E INSIGHTS INESPERADOS — 12 itens (formato DESCOBERTA / EVIDÊNCIA / INTERPRETAÇÃO / IMPLICAÇÃO / CONFIANÇA)

**I1. "Comer menos piora" virou tese mainstream.**
- DESCOBERTA: a reversão da regra "coma menos" é agora um gancho padrão para 40+.
- EVIDÊNCIA: "Eating Less Made My Menopause Belly Worse" (https://www.youtube.com/watch?v=tJw3NOOpk2s); "The 1,200-Calorie Trap"; "Don't Eat Like a Bird… After 60"; "Gaining Weight in Menopause? Don't Stop Eating"; HealthUnlocked "upped calories and lost weight".
- INTERPRETAÇÃO: a consumidora já aceita que o problema não é quantidade; ela quer saber "o que então".
- IMPLICAÇÃO VSL: lead pode começar validando o ritual ("você já comeu 1.200 calorias e andou todos os dias") e depois desmontá-lo como causa da perda muscular/platô; o mecanismo deve explicar por que "menos" falhou.
- CONFIANÇA: MÉDIA-ALTA.

**I2. O avatar quer entender "o que mudou" mais do que "o que fazer".**
- EVIDÊNCIA: 1.585.702 views em 7 dias para "Menopause Weight Gain Wasn't a Thing in 1945 — What Changed?" (https://www.youtube.com/watch?v=o7EQ8iItS1Y); clones em <7 dias.
- INTERPRETAÇÃO: narrativa de causa externa (ambiente, comida moderna) alivia a culpa. Formato "comparação geracional" (mãe/avó) ressoa: "Why does my waist look different from my mother's at the same age".
- IMPLICAÇÃO: ângulo de lead "o que as mulheres de 1950 tinham e você não tem"; cuidado: tendência emergente e já copiada — provável saturação em semanas.
- CONFIANÇA: MÉDIA (views ≠ conversão).

**I3. Os benchmarks internos (Oprah, TODAY/Jenna & Sheinelle, Jillian Michaels) continuam ativos — e simultaneamente viraram sinônimo de golpe.**
- EVIDÊNCIA: TODAY with Jenna & Sheinelle entrevistou Oprah (341K) e Valerie Bertinelli (2x) em 2026; mas BBB/WGEM documentam deepfakes da Oprah; exposés "Jillian Michaels gelatin trick… Scam Breakdown" (51K), Gumitide, Thermo Ignite (Oprah/Kelly Clarkson/Dr. Oz baking soda).
- INTERPRETAÇÃO: o formato "talk show matinal + truque de cozinha" já foi queimado para uma fatia cética; a VSL #1 escalada (Gumitide, "duas mulheres estilo TV matinal", print do usuário) tem vídeo de denúncia nominal.
- IMPLICAÇÃO: evitar likeness de celebridade real; se usar formato talk-show, investir em prova verificável e em "por que isso não é o gelatin trick".
- CONFIANÇA: ALTA.

**I4. "Sem receita" virou argumento de venda — mas a consumidora 60+ já está no GLP-1 e preocupada com custo, não com estigma.**
- EVIDÊNCIA: "At 58. Without a prescription." (232K); vs "I've lost 56 pounds on Zepbound at 72… how much has it actually cost me?"; Medicare $50 GLP-1 bridge (prazo 7/dez).
- INTERPRETAÇÃO: há dois públicos: (a) 45–60 que resiste ao remédio; (b) 60+ no Medicare que já usa e teme perder acesso em janeiro/2027.
- IMPLICAÇÃO: duas leads: "alternativa à injeção" e "o que fazer quando a farmácia disser que não passou".
- CONFIANÇA: MÉDIA.

**I5. A perda de peso "de verdade" no 50+ é lenta e as criadoras honestas dizem isso — contradizendo o Trends "lose 40 pounds in 1 month".**
- EVIDÊNCIA: "I lost 20 pounds over one year and four months but that was only part of the story" (https://www.youtube.com/watch?v=5H3y29E9Eho); Forbes: 0,5–1 lb/semana após 50; vs. Trends 7d "how to lose 40 pounds in 1 month" (grande aumento, print do usuário).
- INTERPRETAÇÃO: busca = desejo impaciente; voz madura = aceitação de lentidão. Tensão entre o que ela pesquisa e o que acredita ser possível.
- IMPLICAÇÃO: promessa numérica com prazo, mas ancorada em polegadas/cintura e em "3 meses" (como o vídeo de 232K), não em "1 mês".
- CONFIANÇA: MÉDIA.

**I6. Metformina/berberina em alta nas buscas, mas a experiência relatada é decepção.**
- EVIDÊNCIA: Trends +3100%/+110% (print do usuário); "not enough for me to lose any weight"; "about 5 pounds over a few months"; "secondary benefit, not guaranteed".
- IMPLICAÇÃO: posicionar o produto contra a berberina ("por que a berberina para em 5 libras") é mais crível do que imitá-la.
- CONFIANÇA: MÉDIA.

**I7. Mulheres relatam ao Reddit o que não relatam ao médico.**
- EVIDÊNCIA: JAMA Network Open via UMD: mudança de peso "several times more likely to be discussed" no Reddit do que em prontuários (https://today.umd.edu/women-are-telling-reddit-not-doctors-about-menopause).
- INTERPRETAÇÃO: o médico é percebido como quem dispensa ("é a menopausa"); a validação de pares é o canal de confiança.
- IMPLICAÇÃO: VSL com "o que seu médico não vai te dizer" continua válida, mas a prova social deve soar de par para par, não de autoridade.
- CONFIANÇA: MÉDIA (uma fonte).

**I8. "Cortisol belly" é simultaneamente a crença da consumidora e o alvo de desmentido.**
- EVIDÊNCIA: múltiplos vídeos "Is cortisol belly real?", WebMD "no proven supplements"; porém "cortisol cocktail recipe" sobe +80% (print).
- IMPLICAÇÃO: usar "cortisol" como linguagem de reconhecimento, não como mecanismo único (vulnerável a desmentido).
- CONFIANÇA: MÉDIA.

**I9. Microdosing de GLP-1 como "terceira via" (custo + efeitos) — emergente.**
- EVIDÊNCIA: "I take tirzepatide. Smallest dose possible. Every other week." (48 anos); AARP, SciFri, Dr. Jen Ashton, ThePrint.
- IMPLICAÇÃO: a consumidora já aceita "menos dose, mais tempo"; um suplemento "companion/bridge" pode se encaixar (Amazon já vende "GLP-1 Companion", print do usuário).
- CONFIANÇA: MÉDIA.

**I10. Movimento sem impacto (Tai Chi, standing abs, "no jumping") domina views 50+.**
- EVIDÊNCIA: cluster Tai Chi belly fat 50+ com >10M views; "4 Standing Moves… No Jumping"; "Skip the Crunches After 50".
- IMPLICAÇÃO: qualquer protocolo de exercício na VSL deve ser explicitamente "sem pular, sem chão, sem joelho".
- CONFIANÇA: MÉDIA-ALTA (atenção, não conversão).

**I11. Contra-voz anti-dieta ganha palco (Jillian Michaels vs 20 body-positivity; "pathologizing").**
- IMPLICAÇÃO: parte do público reage mal a "você precisa emagrecer"; enquadrar como saúde/energia/mobilidade reduz atrito (converge com E2/E3).
- CONFIANÇA: BAIXA-MÉDIA.

**I12. Creatina após 50 é o ingrediente "surpresa" com maior atenção (3,66M + 3,95M views) — fora do radar das VSLs escaladas (gelatina/bicarbonato).**
- IMPLICAÇÃO: possível mecanismo adjacente ("músculo que queima"), coerente com a crença B2/B4 (perda muscular, não metabolismo).
- CONFIANÇA: MÉDIA.

---

## 9. ANÁLISE POR FAIXA ETÁRIA (onde há evidência)

**40–49 (perimenopausa).** Linguagem: "perimenopause showed up", "belly showed up somewhere around 40", "jeans won't zip", "hormonal belly pooch after 40", "same food, same walks". Dor central: a mudança súbita de formato com peso estável; raiva da dispensa médica (D16). Já experimenta GLP-1 em microdose (48 anos). Crenças: cortisol, insulina/PCOS, sono. Desejo: explicação + manter o que era. Evidência: moderada (YouTube forte, fórum fraco).

**50–59 (menopausa/pós).** A faixa com mais voz direta nos fóruns (54, 55, 56, 58, 59). Linguagem: "religiously stuck to 1200kcal", "put on over a stone in the past year", "never going to be a healthy weight now that I'm menopausal", "without a prescription", "at 58". Dor: platô apesar do ritual; medo de "ter deixado tarde demais" ("Have I left it too late?"). Fracassos: WW, 1.200 kcal, academia. Desejo: polegadas de cintura em 3 meses sem receita e sem abrir mão de comida; não depender de injeção. É o núcleo do avatar e o mais sensível a "o que mudou".

**60+.** Linguagem: "63 is too old to change…", "I want more than just a number on the scale", "I'm 60 and lost 95 lbs", "at 64", "at 72 on Zepbound… what I paid", "Medicare… pharmacy says it didn't go through". Dor: energia, mobilidade, joelhos (Tai Chi, "no floor work"), custo/Medicare, queda de cabelo (72), rosto (60, 63). Desejo: não aceitar menos; movimento sem dor; manter acesso ao remédio ou substituí-lo. Objeção: já usa GLP-1 (não precisa ser convencida do mecanismo) e teme perder; ou nunca usou e teme "Ozempic face".

---

## 10. MOMENTO EMOCIONAL DE COMPRA (G) — gatilhos observados

| Gatilho | Evidência | Status | Copy |
|---|---|---|---|
| **Fim do cupom/seguro → "$900 do bolso"** | Drugs.com; CNN | Consolidado | 5 |
| **Janeiro/2027: Medicare GLP-1 bridge ($50) e Part D — prazo 7/dez** | YouTube Ardenwell, Retirement Rules | Emergente (novo, 60+) | 4 |
| **Provedor de composto fechou / FDA enforcement (out/2026)** | Fortune; telehealthally (4 provedores fecharam Q1) | Em aceleração | 4 |
| **Parou o GLP-1 e o "food noise" voltou (semanas)** | Sutter; YouTube | Consolidado | 5 |
| **Christmas/holidays como deadline** | "Lose menopausal belly fat before Christmas" | Sazonal (agora) | 4 |
| **Evento (casamento, viagem)** | Forbes tester 50+ | Consolidado, evidência fraca nesta coleta | 3 |
| **A roupa que não fecha antes de sair / fotos** | D1, D19 (retração social) | Consolidado | 5 |
| **Ver uma celebridade 60+ "sem Ozempic" (Valerie Bertinelli, 65)** | Trends +3050% 7d; "never taking them" | Em aceleração (semana) | 4 |
| **Médico dispensou ("é a menopausa")** | Substack comments | Consolidado | 5 |
| **Novo alerta de segurança (FDA olhos 9/nov; poison calls +1600%)** | YouTube news | Emergente | 3 |

Hipótese (não validada): o momento de maior propensão é a confluência "parei/não posso pagar o GLP-1 + feriados chegando + roupa de festa não fecha". Faltou busca dedicada a Thanksgiving/fotos (cota esgotada).

---

## 11. O QUE NÃO FOI CONFIRMADO (honestidade de amostra)

- Linguagem espontânea do Reddit (r/Menopause, r/loseit, r/Zepbound etc.): **não observada**. Toda a Frente precisa de um canal alternativo (ex.: exportação manual do usuário, ou API/aggregador permitido).
- Comentários de YouTube/TikTok/Instagram: não observados.
- Marido/atração, Thanksgiving/fotos, articulações como "ciclo vicioso", Quora, Trustpilot de Mochi/Henry Meds/Noom: buscas não executadas (cota).
- Diferença 70–75 vs 60–69: evidência insuficiente (apenas 1 voz de 72 anos).
- 10 das 119 linhas de linguagem são de fóruns UK (HealthUnlocked, Mumsnet, Gransnet) — marcadas "non-US"; usadas apenas como linguagem, não como mercado.

---

## 12. RESUMO PARA A COPY (uma linha cada)

- Abra com o ritual, não com o peso: "1,200 calories, no alcohol, 4 litres of water — and the scale went UP."
- A dor é a cintura com peso igual: "same weight, two sizes bigger at the waist".
- Valide: "it's not willpower; eating less made it worse".
- Explique "what changed" (1945/mãe/avó) antes de "what to do".
- Posicione contra: gelatin trick/baking soda (queimados), berberina (para em 5 lb), GLP-1 (custo, food noise volta, rosto, cabelo).
- Promessa: polegadas em 3 meses, sem receita, sem abrir mão de comida, sem pular.
- 60+: energia e mobilidade > número; e o que fazer quando a farmácia disser "didn't go through".
- Nunca: likeness de Oprah/Jillian/Dr. Oz; "natural Ozempic"; "<$50/mês"; "sem dieta e sem exercício".
