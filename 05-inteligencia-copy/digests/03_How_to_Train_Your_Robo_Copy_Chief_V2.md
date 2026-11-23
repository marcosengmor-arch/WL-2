# Digest 03 — How to Train Your Robo-Copy Chief (9 prompts, CA Labs / Bond Halbert)

**Fonte:** `raw/03_How_to_Train_Your_Robo_Copy_Chief_V2.txt` (inglês).
**Tipo:** biblioteca de prompts de copy-chiefing + trechos de Bond Halbert sobre edição.

## Prefácio de Bond Halbert (regra-mãe)
"This formula can NOT make Eskimos want more ice. All the power in your sales copy comes from what you are saying and knowing your audience… market research is much more important than any creative writing ability." Edição é onde entra o profissionalismo, mas "no amount of clarity will make a bad offer better."

## Meta-regra para prompts
Adjetivos ("punchy", "conversational") não bastam. Conceber a IA como um agente: instruções claras, identidade, exemplos, contra-exemplos, restrições. Fazer UMA coisa por passada.

## Os 9 prompts (o que cada um faz)
1. **Dimensionalize pain & benefits** — listar todas as "benefit claims" e "pain claims"; sob cada uma, versão concreta/visual/social. Exemplos: "HORRIFIED by her disappearing hair" → "used to spend hours everyday combing and styling her hair to cover up her visible scalp"; "weak erections" → "started having to make excuses to his wife after date night". Social: "People at work keep saying I must have gotten veneers…"
   - Revisão cirúrgica: substituir SÓ a frase #n, sem mexer no resto.
   - Prompt adicional: o **"block"** = overarching statement + 3 descrições vívidas + 1–2 cenas "lived-in" + recap emocional ("You'll lose 48lbs effortlessly… fat will melt from your love handles… you'll see your husband watch you as you walk to the bathroom in your tight black dress… fully in love with yourself").
2. **Specific proof** — toda claim casada com prova na mesma frase ou logo após ("According to Harvard scientists, you can skyrocket your metabolism by 400%"). **Proof modalities**: Specificity (nomes + números) · Acknowledging skepticism · Credible source · Candor · The Reason Why ("because") · Technical jargon (rajada curta) · "Fake" celebrity link (lógica: se a celebridade bebe probiótico, entende a importância do intestino) · Metaphors ("Your joints dry out, which turns them into a cracked wasteland") · **Testable proof** ("gyms are busy in January and empty in July").
3. **Eliminate fluff (estrutural)** — identificar blocos de 2–3 frases removíveis sem mudar sentido/tom.
4. **Concision (frase a frase)** — voz ativa; cortar repetição (saliva dita 3x); colapsar duas frases em uma (50% das palavras); cortar detalhes irrelevantes (benefícios de cúrcuma para fígado/asma num produto de cabelo).
5. **Reading level** — ~7ª série; palavras anglo-saxãs em vez de latinas; frases de 18–22 palavras; minimizar sílabas sem perder impacto.
6. **Vague/unclear language** — 11 fontes de confusão: ambiguidade, frases longas, passiva, redundância, falta de contexto, excesso de pronomes, jargão, falta de transições, suposições não explicadas, falta de exemplos/evidência, terminologia inconsistente.
7. **Conversational style & flow** — ritmo (curtas + longas), tripletas, "conversational inflections": Okay / But check this out / You know what? / Here's the thing / Listen / Now, imagine this / But here's the kicker / And the best part? / Not only that… (sem exagero). Mínimo 20 sugestões.
8. **Power words** — listas por emoção: GREED, FEAR, ANGER, CURIOSITY, LAZY, LUST, SAFETY. Regra: só substantivos/verbos/adjetivos, nunca advérbios; **uma a cada 80–100 palavras (~10 por peça)**. Bond: faça SUA lista lendo National Enquirer (positivas: Miracle, Jaw-Dropping; negativas: Crisis, Slime Ball); "upset" → "livid", "rare" → "impossible to find".
9. **Progressive tense** — "has taken… and added" → "is taking… and adding". Sensação de movimento em curso ("a product is selling many copies right now" dispara FOMO). Usar especialmente em benefícios/promessas; não em histórias.
10. (bônus) **Remove qualifiers & adverbs** — like/some/mostly/could/may/possibly; advérbios em "-ly" (extremely, probably, clearly…). Manter só se tornar a frase mais verdadeira (defensável "in a court of law and the court of public opinion"). "There is a big difference between 'This may work' and 'This WILL work!'"

## Frase de estilo repetida em todos os prompts (nossa régua de voz)
"casual, conversational language that still paints descriptive pictures… like a friend talking to another friend… short, rhythmic language… lower reading level (fewer consonants)… NOT overly poetic."

## Aplicação direta no WL-2
Ordem de edição da VSL: dimensionalizar (lead, história, close) → provas na tese → cortar (estrutural, depois frase) → nível de leitura → fluxo conversacional → power words com parcimônia → progressivo nas promessas → caçar qualificadores (sem perder compliance: qualificador que protege juridicamente fica).
