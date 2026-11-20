import docx, copy, sys
from docx.shared import Pt, Emu, RGBColor
from docx.oxml.ns import qn
SRC='/root/.claude/uploads/fa23ecdd-119f-5e9c-9135-1cd2ef9f1b17/d0d5e032-Briefing_de_Oferta_2.docx'
OUT='/home/user/WL-2/04-briefing/Briefing_de_Oferta_WL2_ChiaSoda.docx'
d=docx.Document(SRC); T=d.tables
BODY=Pt(9.5); IND=Emu(165100); IND2=Emu(330200)

def run(p,text,bold=False,italic=False,color=None):
    r=p.add_run(text); r.font.name='Calibri'; r.font.size=BODY; r.bold=bold; r.italic=italic
    r._element.rPr.rFonts.set(qn('w:eastAsia'),'Calibri')
    if color: r.font.color.rgb=RGBColor.from_string(color)
    return r
def add(cell,items,clear=True):
    """items: list of (kind,text). kinds: h=bold heading, p=paragraph, b=bullet, s=sub-bullet, i=italic note, bl=blank"""
    if clear:
        for p in list(cell.paragraphs)[1:]: p._element.getparent().remove(p._element)
        first=cell.paragraphs[0]
        for r in list(first.runs): r._element.getparent().remove(r._element)
        use_first=True
    else: use_first=False
    for kind,text in items:
        if use_first: p=first; use_first=False
        else: p=cell.add_paragraph()
        p.paragraph_format.space_after=Pt(2)
        def rich(prefix,text):
            if prefix: run(p,prefix)
            parts=text.split('**')
            for i,part in enumerate(parts):
                if part: run(p,part,bold=(i%2==1))
        if kind=='h': run(p,text,bold=True,color='1F5C43')
        elif kind=='p': rich('',text)
        elif kind=='b': p.paragraph_format.left_indent=IND; rich('•  ',text)
        elif kind=='s': p.paragraph_format.left_indent=IND2; rich('–  ',text)
        elif kind=='i': run(p,text,italic=True)
        elif kind=='bl': pass

# ---------- 0. nome do copy
add(T[1].rows[0].cells[0],[('p','**WL-2 — The Chia Soda Ritual** · VSL de emagrecimento para mulheres norte-americanas 40–75 (EUA, inglês) · Pesquisa consolidada em 19–20/11/2026 (relatórios 01–10, dissecação da VSL AlkaMelt, mecanismo V2 e decisões de formato/receita/nome) · Copywriter responsável: [preencher]')])

# ---------- 1. PREMISSAS
add(T[4].rows[0].cells[0],[
('p','**Nome de trabalho:** ChiaSoda Drops (alternativas: SodaChia, Chia Buffer, PinchPro — marca e domínio ainda não verificados).'),
('p','**O que é:** fórmula líquida em gotas (ou sachê) que substitui "a pitada" do ritual caseiro pela dose medida e tamponada, para ser tomada junto com o copo de água + chia da manhã (The Chia Soda Ritual). Hipótese de composição, a validar com o fornecedor e com compliance:'),
('b','Bicarbonato de sódio tamponado em dose medida (camada 1 — neutralizar o solo ácido e "acordar" as células L que produzem GLP-1/GIP). Dose baixa, com aviso de sódio.'),
('b','Fibra de chia/psyllium micronizada (camada 1 — o gel que forra e alimenta as células L; saciedade; evidência moderada para GLP-1 endógeno).'),
('b','Extrato de gengibre (gingerol) + magnésio glicinato (camada 2 — proteger o sinal do "ácido do estresse", digestão, sono).'),
('b','Ativador do "interruptor" (camada 3 — canela de Ceilão + cromo; berberina só em dose baixa e com disclaimer, pois a EFSA/2026 não definiu nível seguro).'),
('b','Sem glúten, sem açúcar, fabricado em instalação registrada na FDA, lote testado — exatamente o que a avatar já cobra nas reviews.'),
('p','**Formato de uso:** 5 gotas (ou 1 sachê) no copo do Chia Soda, em jejum, 10 minutos antes de beber. Ritual de 30 segundos + 10 minutos de espera (a espera é a prova visual).'),
('p','**Posicionamento:** "a versão over-45 do baking soda shot" — companion/support para quem não quer, não pode ou parou a injeção. Nunca "natural Ozempic", nunca "alternative", nunca "better than Mounjaro".'),
])
add(T[5].rows[0].cells[0],[
('p','**Promessa central (com tipicidade e prazo):** "Troque o shot de bicarbonato que te inchou pela versão over-45 — um copo, uma colher de chia, uma pitada e 10 minutos — e sinta o apetite acalmar na primeira semana, a roupa mudar em 30 dias e a cintura perder polegadas em 3 meses, sem injeção, sem dieta de 1.200 calorias e sem recomeçar do zero."'),
('p','**Números a usar (defensáveis):** "primeiras 8–10 lb em 30 dias" com "resultados típicos"; "polegadas na cintura em 3 meses"; "menos food noise até as 10 da manhã" na 1ª semana. **Não usar:** "1 lb por dia", "7 lb na 1ª semana", "43 lb em 2 meses" (números da AlkaMelt sem lastro).'),
('p','**Promessa de absolvição (a que mais retém na pesquisa):** "Não é a mesma gordura. Não é força de vontade. Você usou o manual dos 30 no corpo dos 50 — e a receita viral era a versão de 25 anos."'),
])
add(T[6].rows[0].cells[0],[
('p','**Física:** cintura que volta a caber na calça (ela mede em polegadas, não em libras: "pants fitting everywhere except the middle", "jeans won\'t zip"); barriga que não endurece às 15h; menos inchaço; energia ao acordar; sono melhor.'),
('p','**Mental:** silêncio sobre comida ("the mental food noise is gone"); comer sem contar; parar de pesar todo dia.'),
('p','**Emocional/identidade:** reconhecer-se no espelho ("a war with my reflection" acaba); não correr para o fundo da foto; ser vista de novo pelo parceiro e pelas amigas; não aceitar "menos" com a idade ("I want more than just a number on the scale. I want to wake up feeling energetic", 63 anos, 3,88M views).'),
('p','**Relacional/social:** sair, viajar, ir ao casamento/feriado sem a roupa como obstáculo; parar de evitar o marido.'),
('p','**Linha do tempo (como na AlkaMelt, com números honestos):** dia 1–7 apetite acalma e o copo vira hábito; dia 30 roupa diferente e primeiras 8–10 lb típicas; 3 meses polegadas na cintura; 6 meses "o intestino reaprendeu" e o resultado fica.'),
])
add(T[7].rows[0].cells[0],[
('p','**Quem é:** mulheres norte-americanas de 40 a 75 anos, falantes nativas de inglês, que já tentaram dieta, exercício, suplemento, truques virais e (em 1 de cada 5 no grupo 50–64) a injeção de GLP-1 — e continuam insatisfeitas com o peso. Núcleo de conversão: **50–59**; segundo núcleo: **60–69** (Medicare, renda fixa, joelhos); entrada: **40–49** (perimenopausa, "a barriga apareceu aos 40").'),
('h','Como ela fala (verbatim da pesquisa):'),
('b','"I have religiously stuck to the recommended 1200kcal a day, stopped all alcohol…" (55 anos) — o ritual que falhou é a frase-núcleo.'),
('b','"Some women go up two clothing sizes around the waist while their weight stays the same" / "Your weight hasn\'t changed, but your jeans suddenly feel tighter?"'),
('b','"I\'m barely eating, but the scale keeps climbing. Is it my hormones, my metabolism, or something else?"'),
('b','"The mental food noise is gone." → "Then the food noise came back." / "the weight came back lightening quick plus a few" / "the coupon has run out… around $900".'),
('b','"I feel like I\'m never going to be a healthy weight now that I\'m menopausal." / "weight gain was 5 to 7 lbs but it made me CRAZY!"'),
('h','O que ela acredita (crença ≠ fato):'),
('b','"É a menopausa/estrogênio: a gordura foi para a barriga" (verdadeiro na redistribuição); "meu metabolismo desabou" (contestado — é músculo/hormônio); "comer menos faz engordar" (parcial); "cortisol belly" (linguagem de rede; efeito pequeno); "o corpo produz o próprio GLP-1 e dá para ativar com comida" (verdadeiro em parte, magnitude menor que a droga).'),
('h','O que ela já tentou e falhou:'),
('b','1.200 kcal; comer ainda menos; WW; academia/cardio; keto; GLP-1 → parou → reganho; GLP-1 composto por telehealth; berberina/metformina ("about 5 pounds"); baking soda shot do TikTok ("All I got was acid reflux" é a linha que a AlkaMelt usa); gelatin trick.'),
('h','Objeções (em ordem de força):'),
('b','1) "É deepfake da Oprah/médico" (BBB: 170+ denúncias; Snopes; Yale); 2) assinatura escondida ("$39,99 → $239,99", "$60 para cancelar"); 3) "a receita nunca é revelada"; 4) "natural Ozempic é red flag"; 5) "suplemento de Amazon é marca duvidosa"; 6) "vou perder o rosto/cabelo" (GLP-1); 7) "já ouvi eat less move more mil vezes".'),
('h','Gatilhos de compra:'),
('b','Cupom/seguro acabou ($900); janeiro/2027 (fim do Medicare GLP-1 Bridge a $50; planos federais +400–500%); parou a injeção e o food noise voltou; feriados/casamento/viagem; a roupa que não fecha antes de sair; médico que disse "é a menopausa"; novo alerta de segurança da FDA (9/nov).'),
('h','Mídia e familiaridade:'),
('b','Assiste TV matinal (Today with Jenna & Sheinelle, Drew, Tamron), podcasts de mulheres 45+ (Oprah, Mel Robbins, Tamsen Fadal), médicos solo no YouTube ("If I were over 50 & 30 lbs overweight…"), vídeos de Tai Chi "after 50"; compra fibra "GLP-1 friendly" na Amazon (Metamucil 70K+/mês); pesquisa "how to lose 20 pounds in 2 months", "does your metabolism slow down as you get older" (+200%), "cortisol cocktail recipe for weight loss" (+80%).'),
])

# ---------- Ideias (uma por formato)
add(T[9].rows[0].cells[0],[
('p','**Ângulo central (comum aos 3):** "The Over-45 Version" — o baking soda shot que você viu era a versão de 25 anos (colherada + limão + gelo). Depois dos 45 o intestino perdeu o escudo do estrogênio; a versão certa é um copo de água, uma colher de chia, uma pitada e 10 minutos: **The Chia Soda Ritual**.'),
('p','**Roupagem desta ideia — "The $1 Chia Soda Ritual" no formato MESA DA COZINHA (referência: Drew Barrymore Show, segmento com Sunny Anderson, Valerie Bertinelli e médica da Midi Health, nov/2026).** Programa de manhã em cozinha de estúdio clara (bancada, não sofá). Girl talk de 3 mulheres da idade da avatar que confessam o ritual que falhou, uma chef/nutricionista prepara o copo na bancada com cronômetro de 10 minutos correndo no canto da tela, e a médica explica o mecanismo em cima do copo. O "$1" ancora contra a injeção de $1.000/mês antes de a oferta chegar.'),
('h','Personagens (produção original, atores/porta-vozes autorizados, credenciais verdadeiras):'),
('b','**A Anfitriã (52):** ex-âncora de TV local, a "paciente" do programa; abre com a própria cintura ("same weight, two sizes bigger"). Arquétipo: a âncora que virou advocate (ref. de tom: Tamsen Fadal).'),
('b','**A Chef-Nutricionista (48):** faz os dois copos (o do TikTok que espuma vs. o over-45 que engrossa); traduz a receita em gesto de cozinha ("a pitada da avó no molho de tomate"). Arquétipo: Sunny Anderson.'),
('b','**A Convidada "sem injeção" (64):** mulher comum que perdeu peso sem GLP-1, largou a balança, mede em polegadas; traz a linha do Trends (Valerie Bertinelli +3.050%, Kay Lake). Arquétipo: a vizinha de renda fixa.'),
('b','**A Ginecologista (55):** explica o escudo que cai aos 45 e o solo ácido; tom "ninguém te contou", sem "doctors are furious". Arquétipo: ginecologista rebelde (sem look-alike de Haver/Ashton).'),
('p','**Abertura (pré-lead confessional, 0:00–1:00, anfitriã em cozinha de casa com o copo):** "If you tried the baking soda shot — the spoonful, the lemon, the ice — and all you got was bloating, it\'s because that was the 25-year-old version…"'),
])
add(T[10].rows[0].cells[0],[
('b','**É o formato que o dinheiro de telehealth está comprando agora:** Midi Health patrocinou exatamente "mesa de amigas 50+ + médica" em Drew (com Bertinelli, 9 dias) e Jennifer Hudson (out/2026); Tamron Hall HRT 463K/1 mês.'),
('b','**Único formato em que a demonstração é natural:** chef + bancada + copo + cronômetro. O mecanismo escolhido precisa de um copo engrossando em 10 minutos; num sofá isso é forçado.'),
('b','**Absolvição coletiva:** 3 mulheres dizendo "eu também" é a validação de pares que a pesquisa mostrou ser mais confiável que a autoridade ("mulheres contam ao Reddit o que não contam ao médico").'),
('b','**"$1" é a âncora que a avatar já procura:** "10 Foods UNDER $1 That Trigger Your GLP-1" (1,1M), "Forget $1,000 GLP-1 Shots"; custo real de chia + pitada fecha em ~$0,50/dia.'),
('b','**Diferencia da AlkaMelt e da VSL #1 (Gumitide, 21.144 ads):** cozinha em vez de sofá/bancada de notícia, zero logos NBC/CBS, zero pessoa real, demonstração honesta em vez de "receita nunca revelada".'),
('b','**Risco a controlar:** visual "mulheres + médica em talk show" é o mais saturado e mais vigiado por deepfake; a cozinha, a chef e o cronômetro são o que o afastam. Views orgânicas do formato no YouTube são baixas (19,6K) — ele converte na TV e em mídia paga, não em descoberta orgânica.'),
])
add(T[11].rows[0].cells[0],[
('p','**Ângulo central (comum):** "The Over-45 Version" / The Chia Soda Ritual (mesmo mecanismo e mesma receita).'),
('p','**Roupagem desta ideia — "The Over-45 Chia Soda Ritual" no formato PODCAST CONFESSIONAL (referência: The Oprah Podcast, episódio de menopausa com Dra. Haver e Dra. Mosconi, 13/10/2026, 1,91M views em 1 mês).** Estúdio de podcast (microfones de mesa, duas câmeras, fundo de sala), 45–50 min. A anfitriã é a paciente: confessa primeiro (dietas, injeção, reganho, "o manual dos 30"), depois duas médicas explicam — uma o escudo que cai (ginecologia), outra o que isso faz com apetite e cérebro (obesidade/neuro). O copo entra na mesa do podcast como "o que eu faço toda manhã desde que parei a injeção".'),
('h','Personagens:'),
('b','**A Anfitriã-Confidente (62):** autora/comunicadora de bem-estar com luta pública própria com o peso (não ícone nacional; sem semelhança com Oprah); 40 anos de dieta, usou GLP-1, parou, reganhou, "there has to be another way". Arquétipo: a confidente que admite a própria vergonha antes da solução.'),
('b','**A Ginecologista da Menopausa (56):** a voz da causa (escudo de estrogênio, solo ácido, células L); "exatamente como eu trato a minha própria menopausa".'),
('b','**A Médica de Obesidade/Neurociência (50):** a voz do "não é a mesma gordura", do food noise e de por que a injeção silencia o sinal mas não devolve o escudo; apresenta a prova (saciedade, GLP-1 endógeno com fibra) sem fMRI inventado.'),
('b','**Produtora/"Pilar" (fora de quadro ou voz):** faz as perguntas das ouvintes ("Baking soda, really?", "Can I do this at home?").'),
('p','**Abertura:** anfitriã, close, sem música: "I\'m 62. I did 40 years of diets, two years of injections and one winter of gaining it all back. Then a gynecologist told me the one thing nobody had said in four decades: it\'s not the same fat after 45 — and the shot I\'d seen online was the 25-year-old version."'),
])
add(T[12].rows[0].cells[0],[
('b','**Maior atenção observada no nicho entre os 3 formatos:** 1,91M views em ~1 mês (2,3x a mediana do canal); "menopausa" é hoje o guarda-chuva socialmente aceito para falar de peso depois dos 45 — dá permissão para assistir 45 minutos.'),
('b','**A estrutura "anfitriã-paciente + médica que explica" transfere o papel da autoridade:** a apresentadora é a compradora, não a vendedora; é a arquitetura da Oprah sem a Oprah.'),
('b','**Longo o suficiente para as 3 camadas do mecanismo** (produzir → proteger → queimar), cada uma com uma pergunta "burra" da anfitriã e uma metáfora (jardim, rádio com chiado, interruptor).'),
('b','**Encaixa a sub-avatar 60+ e a pós-GLP-1** (quem parou a injeção; "after the shot"), que têm calendário próprio em dezembro/janeiro (Medicare Bridge, FEHB).'),
('b','**Risco a controlar:** é o formato mais associado a golpe quando usa ícone (AlkaMelt usa avatar da Oprah; Snopes/BBB/Yale marcaram) — por isso anfitriã original, sem semelhança; e a demonstração do copo é menos natural (resolver com o copo na mesa + inserto de bancada de 60 s).'),
])
add(T[13].rows[0].cells[0],[
('p','**Ângulo central (comum):** "The Over-45 Version" / The Chia Soda Ritual (mesmo mecanismo e mesma receita).'),
('p','**Roupagem desta ideia — "The 10-Minute Chia Soda Ritual" no formato PAINEL DE EXPERTS / MASTERCLASS (referência: Oprah Daily "The State of Weight — The Life You Want Class", 465K views; formato validado internamente em campanha há ~1 ano).** Sala de aula/auditório íntimo, mesa com 3 médicas e uma moderadora, plateia pequena de mulheres 45+, um copo de Chia Soda na mesa desde o minuto 1 com o cronômetro de 10 minutos visível. Cada expert é dona de UMA camada do mecanismo; a moderadora costura com as perguntas da plateia. Os "10 minutos" são o fio: "a espera que o TikTok pulou".'),
('h','Personagens:'),
('b','**A Moderadora (58):** jornalista de saúde, faz as perguntas da plateia e mantém o cronômetro; confessa a própria cintura no primeiro minuto.'),
('b','**Expert 1 — Ginecologista/menopausa (camada 1, acordar):** o escudo que cai aos 45, o solo ácido, as células L; metáfora do jardim.'),
('b','**Expert 2 — Gastroenterologista/nutricionista clínica (camada 2, proteger):** estômago vazio + estresse = mais ácido e menos sinal ("comer menos piorou"); gengibre e magnésio; o ritual das 15h como linguagem (sem alegação de cortisol).'),
('b','**Expert 3 — Médica de obesidade/metabolismo (camada 3, queimar):** o interruptor que trava, "não é a mesma gordura", por que a injeção não devolve o escudo; linha do tempo de 30/90/180 dias.'),
('b','**2–3 mulheres da plateia (54, 61, 68):** fazem a pergunta-objeção ("Can I just buy baking soda at Walmart?", "I\'ve been burned before") e dão o depoimento com número e tipicidade.'),
('p','**Abertura:** plano do copo sendo mexido, cronômetro zera; moderadora: "In ten minutes this glass will be something the baking soda shot never was. In the same ten minutes, three doctors will show you why everything you did after 45 stopped working — and why it wasn\'t you."'),
])
add(T[14].rows[0].cells[0],[
('b','**Validação comercial real:** o formato "várias experts" foi validado pelo usuário em campanha há um ano — dado de conversão que pesa mais que views.'),
('b','**Autoridade em camadas é o único elemento que nenhuma das 20 VSLs escaladas usa:** o mercado tem um médico (deepfake) ou duas apresentadoras; um painel de 3 experts reais com credenciais verdadeiras é novo e difícil de clonar rápido.'),
('b','**Cada camada ganha uma dona:** a avatar lembra "a ginecologista do escudo", "a gastro do estômago vazio", "a médica do interruptor" — e o mecanismo fica memorizável.'),
('b','**O cronômetro de 10 minutos é um open loop físico** que atravessa o painel inteiro e termina na demonstração (a colher desliza devagar; fita métrica).'),
('b','**Tom mais clínico protege de compliance** (claims qualificados, "resultados típicos") e fala com a 60+ que quer "ser levada a sério pelo médico".'),
('b','**Risco a controlar:** painel pode virar aula (menos emoção) — por isso a moderadora confessa no minuto 1 e a plateia traz os depoimentos; views históricas (1 ano) → a prova de que ainda funciona é a conversão interna, não o YouTube.'),
])

# ---------- Mecanismo 1 (único)
add(T[16].rows[0].cells[0],[
('p','**"Menopause Acid Belly"** (a barriga que o ácido da menopausa guarda) — vilão único com três consequências. Nome alternativo/metáfora de causa: "The Estrogen Shield" (o escudo que cai aos 45). Nome da solução: **The Chia Soda Ritual / "the over-45 version"**.'),
('i','Decisão de 20/11/2026: este é o único mecanismo para os três ângulos/formatos; os campos "Mecanismo 2" e "Mecanismo 3" ficam reservados (não se aplicam).'),
])
add(T[17].rows[0].cells[0],[
('p','Por 30 anos o estrogênio foi o **escudo** do sistema digestivo: mantinha o ambiente do intestino equilibrado, protegia o revestimento e mantinha acordadas as células L — as que produzem GLP-1 e GIP, os hormônios que dizem ao cérebro "já chega, pode queimar". Entre 40 e 55 o escudo cai, e três coisas acontecem ao mesmo tempo (por isso ela sente que "tudo mudou de uma vez"):'),
('b','**Camada 1 — o solo azeda e as células L dormem.** Sem o escudo, anos de café, açúcar, ultraprocessado, remédio e estresse viram um intestino inflamado e ácido. Nesse solo as células L param de produzir GLP-1/GIP; o cérebro nunca recebe o "já chega": food noise, doce às 15h, fome fora de hora. (Metáfora: o jardim com solo ácido onde a semente não brota.)'),
('b','**Camada 2 — o ácido do estresse destrói o pouco que sobra.** A perimenopausa derruba o sono e sobe o estresse (a palavra dela: cortisol). Estômago vazio + estresse = mais ácido e uma enzima (DPP-4) mais ativa, que destrói o hormônio em minutos. Aqui "comer menos piorou" vira mecanismo: 1.200 kcal e refeições puladas deixam o intestino ácido por mais horas e tiram das células L a chance de acordar. (Metáfora: o rádio com chiado — o sinal sai, o ruído come a mensagem.)'),
('b','**Camada 3 — o interruptor trava e a gordura muda de endereço.** O estrogênio mantinha ligado o interruptor queimar/guardar (AMPK) e mandava a gordura para o quadril. Sem ele, o interruptor trava em "guardar" e a gordura vai para dentro da barriga: por isso a cintura cresce com o peso igual e **não é a mesma gordura** (visceral, hormonalmente ativa, que ignora dieta, caminhada e 4 litros de água). (Metáfora: o porão onde o corpo guarda carvão.)'),
('p','**Por que o que ela tentou falhou:** dieta e caminhada não devolvem o escudo; a injeção substitui o sinal, mas não acorda as células L — ao parar, "the food noise came back". E o baking soda shot viral era a **versão de 25 anos**: colherada + limão + gelo, ácido em cima de ácido, explodindo no estômago (inchaço, refluxo) em vez de chegar ao intestino.'),
('p','**Causa raiz em uma frase:** "It isn\'t the bread. It isn\'t your willpower. It\'s that the shield that kept your gut calm for 30 years quietly came down around 45 — and nobody gave you the over-45 version of the recipe."'),
('i','Nível de evidência (para o copy): redistribuição visceral e perda muscular na menopausa = FORTE; menopausa altera microbiota/barreira intestinal = MODERADA; "ácido desliga GLP-1" e DPP-4/AMPK ligados ao estrogênio = ângulo plausível (FRACA-MODERADA), não alegar números; cortisol = linguagem, nunca alegação.'),
])
add(T[18].rows[0].cells[0],[
('p','**O ritual (a parte caseira, revelada na VSL):** 1 copo de água morna/ambiente (8 oz) + 1 colher de sopa de chia + **uma pitada** de bicarbonato puro; mexer, esperar **10 minutos** até engrossar, beber em jejum 20–30 min antes do café. Sem limão, sem gelo.'),
('b','**A chia** vira o gel que forra e "alimenta" as células L (fibra solúvel → saciedade → o próprio GLP-1/GIP, de forma modesta e natural).'),
('b','**A pitada** tampona o ácido para que o gel trabalhe no intestino, não no estômago (por isso a versão com limão inchava).'),
('b','**Os 10 minutos** são "a espera que o TikTok pulou": o copo engrossa na sua frente.'),
('p','**O produto (ChiaSoda Drops) substitui a pitada pela dose certa e cobre as camadas 2 e 3:**'),
('b','**Camada 1 — Neutralizar e acordar:** bicarbonato **tamponado e medido** (não a colherada; dose baixa e constante; o que "não dá para fazer em casa" não é a pureza, é a dose por peso e o tampão).'),
('b','**Camada 2 — Proteger o sinal:** gingerol (gengibre, o remédio de digestão em que a mulher 45+ já confia) + magnésio glicinato (o mineral da menopausa: sono, cãibra, ansiedade) para que o pouco sinal produzido não seja destruído pelo "ácido do estresse".'),
('b','**Camada 3 — Destravar o interruptor:** ativador de baixo risco (canela de Ceilão + cromo; berberina só em dose baixa com disclaimer) para o corpo voltar a "queimar" em vez de "guardar na barriga".'),
('b','**(Opcional) Camada 4 — Reparar o escudo:** zinco-carnosina/glutamina para o revestimento — reforça a tese do escudo sem prometer efeito hormonal.'),
('p','**Resultado esperado em sequência:** 1ª semana o apetite acalma e o copo vira hábito → 30 dias roupa diferente (8–10 lb típicas) → 3 meses polegadas na cintura → 6 meses o intestino "reaprendeu" e o resultado fica, sem injeção.'),
])
add(T[19].rows[0].cells[0],[
('p','**Explicação por A + B (a lógica que a VSL repete):** A) depois dos 45 o escudo cai e o intestino azeda; B) em solo ácido as células L dormem e o sinal "já chega" some → logo a barriga não é disciplina, é o ácido da menopausa. A\') a chia + pitada neutralizam e acordam; B\') gengibre/magnésio protegem e o ativador destrava → logo o próprio corpo volta a produzir o sinal e a queimar, sem agulha.'),
('h','Provas a usar (reais, com nível de evidência):'),
('b','**Demonstração dos dois copos (prova demonstrativa, a mais forte):** colherada + limão espuma e transborda ("isso foi no seu estômago") vs. pitada + chia engrossa em 10 min e a colher desliza devagar ("isso é o que chega ao intestino"). Fecha com fita métrica: "medimos em polegadas, não em espuma".'),
('b','**Ciência do esporte (superestrutura real):** o "sodium bicarbonate loading" é suplemento com evidência reconhecida para atletas — só funciona tamponado, dosado por peso e no horário certo. Justifica "a dose, não a colherada" sem inventar laboratório.'),
('b','**Menopausa e gordura visceral (FORTE):** Mayo/Harvard/Cleveland Clinic: a gordura muda para a barriga na transição; ganho total ~1,5 lb/ano, mas a cintura muda mais que o peso.'),
('b','**Menopausa e intestino (MODERADA):** a queda do estrogênio altera a microbiota e a barreira intestinal (literatura do "estroboloma") — usar como "o escudo", sem pH medido.'),
('b','**Fibra solúvel e saciedade/GLP-1 endógeno (MODERADA):** psyllium/chia aumentam saciedade e achatam a glicemia; a Amazon já rotula fibra como "GLP-1 Friendly" (Metamucil 70K+/mês) — prova cultural de que a avatar aceita a ideia.'),
('b','**Reganho pós-GLP-1 (MODERADA):** Oxford jan/2026: reganho mais rápido que pós-dieta; Menopause Society out/2026: mulheres 50–64 são o maior grupo de usuárias. Sustenta "a injeção silencia o sinal, não devolve o escudo".'),
('b','**Prova cultural:** a caixa de bicarbonato na cozinha americana há gerações; "sua avó usava para azia"; a pitada no molho de tomate.'),
('b','**Depoimentos:** mulheres reais 50+, com idade, número, prazo e "resultados típicos"; nunca atores de Craigslist (FTC x NextMed, $150K).'),
('h','O que NÃO alegar:'),
('b','"alcaliniza o sangue", "queima gordura", "baixa cortisol", "trata menopausa", "93%/3x/5x harder/10x faster" (números da AlkaMelt sem fonte), "1 lb por dia".'),
])
NA=[('i','Não se aplica — decisão de 20/11/2026: mecanismo único ("Menopause Acid Belly" / The Chia Soda Ritual) para os três ângulos e formatos. Ver Mecanismo 1.')]
for i in (20,21,22,23,24,25,26,27): add(T[i].rows[0].cells[0],NA)

# ---------- Nomes chiclete
add(T[29].rows[0].cells[0],[
('p','**Nome 1: "The $1 Chia Soda Ritual"** (falado: "the one-dollar Chia Soda"). Ângulo-irmão: formato Mesa da Cozinha (Ideia 1).'),
('b','Leva ingredientes, custo e rotina no nome: "Chia" e "Soda" (lê como baking soda e como bebida) + "$1" + "Ritual".'),
('b','Ancora contra a injeção de $1.000/mês antes de a oferta chegar; conversa com o orgânico que a avatar já assiste ("10 Foods UNDER $1 That Trigger Your GLP-1", 1,1M; "Forget $1,000 GLP-1 Shots").'),
('b','Custo real por dose (chia 1 colher + pitada) fecha em ~$0,50 — a promessa é verificável.'),
('b','Evita "trick/hack/loophole" (marcadores de golpe) e "shot" (degrau saturado); "ritual" sustenta a repetição diária e o kit de 6 meses.'),
])
add(T[30].rows[0].cells[0],[
('p','**Nome 2: "The Over-45 Chia Soda Ritual"** (variação: "The After-45 Glass" para criativos de 15 s). Ângulo-irmão: Podcast Confessional (Ideia 2).'),
('b','Carrega a correção pela década no próprio nome: "a receita viral era a versão de 25 anos; esta é a over-45" — absolve sem culpar a receita nem a mulher.'),
('b','Segmenta na primeira palavra (como "weight loss specialist for women over 40" faz na AlkaMelt) e dá permissão de assistir para quem já desistiu de "truques".'),
('b','Casa com a busca que mais cresce no trimestre ("perimenopause weight gain" 9 → 26; "how to get rid of belly fat after menopause" +189.900%) sem usar "menopause" no nome, o que protege o claim.'),
])
add(T[31].rows[0].cells[0],[
('p','**Nome 3: "The 10-Minute Chia Soda Ritual"** (variação: "The 10-Minute Glass"). Ângulo-irmão: Painel de Experts (Ideia 3).'),
('b','Leva o mecanismo e a prova visual no nome: os 10 minutos em que o copo engrossa são "a espera que o TikTok pulou" — o número vira demonstração e open loop (cronômetro na tela).'),
('b','Dimensão nova na escada da receita (cru → +limão → shot → +gelo → **+tempo**), com a mesma lógica dos vídeos que mais retêm no nicho ("If I only had 14 days…", "First 30 minutes after waking", 2,6M).'),
('b','Curto, falável por uma apresentadora de 55 anos e fácil de encurtar na fala corrente para "the Chia Soda".'),
('p','**Produto que "substitui a pitada":** ChiaSoda Drops, SodaChia, Chia Buffer, PinchPro — evitar sufixos "-tide/-melt" (famílias já expostas). Marca e domínio não verificados nesta pesquisa.'),
])

# ---------- 2. PESQUISA DE MERCADO (substitui o exemplo pelo nosso)
cell=T[33].rows[0].cells[0]
nested=cell.tables  # [box, element table]
box_tbl=copy.deepcopy(nested[0]._tbl); el_tbl=copy.deepcopy(nested[1]._tbl)
# clear cell
for child in list(cell._tc):
    if child.tag.endswith('}p') or child.tag.endswith('}tbl'): cell._tc.remove(child)
# rebuild: box title
cell._tc.append(box_tbl)
from docx.table import Table
bt=Table(box_tbl,cell)
bc=bt.rows[0].cells[0]
for p in list(bc.paragraphs)[1:]: p._element.getparent().remove(p._element)
for r in list(bc.paragraphs[0].runs): r._element.getparent().remove(r._element)
run(bc.paragraphs[0],'PESQUISA WL-2 — THE CHIA SODA RITUAL (EUA, mulheres 40–75) · coleta 19–20/11/2026 · fontes completas em US_WEIGHT_LOSS_MARKET_INTELLIGENCE/ (646 fontes, dashboard) e 02-dissecacoes/ALKAMELT_dissecacao.docx',bold=True)
items=[
('bl',''),
('h','Tendências de Conteúdo (YouTube público; TikTok/Instagram não acessíveis nesta coleta — só sinais indiretos)'),
('p','Google (Trends, EUA, prints do usuário 19/11 + coleta própria):'),
('b','"cortisol cocktail recipe for weight loss": +80% (7d), Grande aumento (30d), +300% rising; pico em 18/11/2026 — busca já dominada pela marca "Harmonia" (ad-driven).'),
('b','"bariatric gelatin recipe for weight loss" +120% (7d) — eco de mídia paga: a série de 12 meses de "gelatin trick" caiu 92% (q1 → q4) e as rising queries mutaram para "korean gelatin for skin" e "horse soda trick".'),
('b','"baking soda recipe for weight loss": nº 1 em "recipe for weight loss" (30d, +20%), mas 7d em -6%/-10%; rising "baking soda trick for men step by-step" +102.550% (migrou para homens). 2ª onda ainda ativa em anúncios (Sodatide, Slim Metrix, SodaFit, Thermo Ignite).'),
('b','"perimenopause weight gain" 9 → 26 no trimestre; "hormone therapy weight loss" 0 → 11; "weight loss after 50" 0 → 10; "how to get rid of belly fat after menopause" +189.900%; "how to speed up metabolism after 40" +665.500%; "does your metabolism slow down as you get older" +200%.'),
('b','"chia seed pudding recipe", "cottage cheese recipes for weight loss", "healthy overnight oats recipe for weight loss": Grande aumento (30d); "overnight oats recipe for weight loss" +30% (7d); "chia seed water" 12m estável (12–18 na escala do lote).'),
('b','GLP-1: "metformin weight loss" +3.100%, "berberine" +110% (mas berberina passou o pico em abr/2026 e decepciona: "about 5 pounds"); "here\'s what happens when you stop taking ozempic and wegovy" +100.050%; "what does ozempic do to your face" +45.550%; "glp 1 natural supplement" +1.000%.'),
('p','YouTube (views públicas, coletor próprio):'),
('b','"Menopause Weight Gain Wasn\'t a Thing in 1945 — What Changed?": 1,58M em 7 dias (38x a mediana do canal), 2 clones em dias.'),
('b','"First 30 Minutes After Waking Decides Whether You BURN or STORE Fat" (Leonid Kim MD): 2,61M/2 sem; "If I Only Had 14 days to Kill Cortisol Belly": 932K/4 sem; cardiologista brasileiro replica o gancho em inglês: 1,56M/9 dias.'),
('b','"If I Were Over 50 & 30 Lbs Overweight, This Is Exactly What I\'d Do" (Rachel Felber MD): 515K; "The Only 7 Things That Actually Move Menopause Belly Fat After 50": 623K.'),
('b','"I Was Over 50 And 95 Lbs Overweight. This Is Exactly What I Did." (Nurse Julie): 783K/1 mês (440x a mediana); "I\'m 58. This Is the Exact Walking Routine That Took Off 50 Lbs": 368K/2 sem.'),
('b','"10 Foods UNDER $1 That NATURALLY Trigger Your GLP-1" (Mindy Pelz): 1,12M; "This 99 Cent Food Mimics Ozempic" (Bazgha Khalid MD): 1,76M; "Nighttime Cortisol… (Take This Before Bed)": 300K/2 sem.'),
('b','"It\'s Boring, But It Kills Cortisol Belly Fat in 48 Hours": 455K/2 sem; "It\'s Boring, But You\'ll Lose Belly Fat Guaranteed": 350K.'),
('b','Oprah Podcast menopausa (Haver + Mosconi, 13/10/2026): 1,91M/1 mês; Oprah + Serena GLP-1: 3,69M; Oprah Daily "State of Weight": 465K; Tamron Hall "Truth About HRT": 463K/1 mês; Drew + Bertinelli + Midi: 19,6K/9 dias (TV, não YouTube).'),
('b','Chia/baking soda no orgânico: "chia seed water" consolidada (ciclos; Cleveland Clinic cobre); baking soda em zona de desmonte (Dra. Jen Caudle 105K; Jordan Liles; canais-receita admitindo que "a ordem muda dependendo de quem você assiste").'),
('b','Tai Chi "After 50 — Burn Belly Fat, Lower Cortisol": 6+ vídeos com 30–117K cada em 30 dias (movimento sem impacto para 50+).'),
('p','Amazon (print do usuário):'),
('b','Metamucil 70K+/mês (36K reviews); Vitafusion "GLP-1 Friendly" 40K+/mês; Physician\'s Choice "Fiber Gummies for GLP-1 Support" 50K+/mês ($8,53); Nature Made "GLP-1 Companion" 20K+/mês; Optimum Nutrition Creatine 40K+/mês; Goli ACV 299K reviews (saturado); Rootation berberine gummies $39,99.'),
('bl',''),
('h','Tendências de Marketing'),
('b','19 das 20 VSLs mais escaladas (biblioteca do usuário) seguem o mesmo template: anúncio → página falsa do TODAY → VSL longa com deepfake/look-alike (Jillian Michaels, Oprah, Dr. Oz, Dra. Ashton, Hoda & Jenna / Jenna & Sheinelle, Jastreboff) → gummies/drops de ACV+BHB. Zero médico real autorizado; em ≥80% o ingrediente do gancho não está na fórmula.'),
('b','Sequência de mecanismos: pink salt (pico ago/2025) → gelatina/pink gelatin (dez/2025–; 10/20 VSLs) → baking soda shot (abr/2026–; 3/20 + clones) → "GLP-1 reset"/"hormone activation" (mai/2026–). AlkaMelt (set/2026, ativa) = baking soda + gengibre + berberina + NAD+, com lead de CORREÇÃO do próprio truque e invalidação nominal de gelatina/pink salt/ACV.'),
('b','Exposição pública massiva em 2026: Snopes (abr/mai), TODAY/NBC (Kathy Hilton, 67: "It has messed up my whole entire system"), Yale (aviso oficial contra deepfakes da Dra. Jastreboff), BBB (170+ denúncias LipoMax em 35 estados), Medscape/McGill ("gelatin is not nature\'s Ozempic"). O avatar 60+ está sendo alertada contra "receita + celebridade + TODAY".'),
('b','Regulatório: FDA 30+25 warning letters a compounders de GLP-1 (mar/jun 2026); FTC x NextMed ($150K: atores de Craigslist); class actions Lemme (3ª, jul/2026) e Veracity "Nature\'s Ozempic" (jun/2026); ASA x Arrae "Faux-Zempic"; NAD x Midi Health; Meta celeb-bait (mar/2026) e política Health & Wellness (jul/2026). "Ozempic alternative" é passivo; "GLP-1 companion/support" está normalizado (Noom grátis, WW Med+, Amazon).'),
('b','Legítimos comunicam anti-estigma e acesso (Ro/Serena "never about willpower"; Midi/Amy Schumer; Nutrisystem "belly fat by 8% in your first month" — único com oferta nomeada para 50+). Lacuna: nenhuma VSL nutra top-20 nomeia menopausa, cortisol ou "40+"; nenhuma usa demonstração honesta; todas têm receita "nunca revelada" e subscription trap.'),
('b','Objeções reais coletadas de VSLs concorrentes: "charged over $400", "lost zero pounds", "gained 8 pounds", "hidden recurring charges after 30 days", "the recipe is never revealed", "$39.99 → $239.99", "$60 fee to cancel" → a nossa oferta responde a cada uma na copy (sem assinatura obrigatória, reembolso visível, receita revelada no minuto 1).'),
('b','Oferta de referência (AlkaMelt): $185 → $98 → $49/frasco no kit de 6 (6 pelo preço de 3), 3 bônus (treino "Runway Waist", masterclass de pele, Zoom com a médica para 50), app + 2 consultas/mês + comunidade, garantia 60 dias, 300 kits, botão verde/vermelho. Para nós: manter a escada e os bônus de serviço; trocar a escassez fabricada por verdadeira (ou nenhuma); bônus codificados para 45+ ("The Over-45 Kitchen", "The 10-Minute Morning", consulta de 20 min).'),
('b','Apresentadores: look-alikes de Jillian/Oz/Ashton já são marcadores de golpe; o orgânico de 30 dias é dominado por mulheres 50+ com história própria (Nurse Julie, MWS, Felber) e por "doutor(a) solo com relógio". Lacunas: médica/enfermeira real 50+ com transformação; apresentadora 60–75 "renda fixa"; mulher negra 45–55 como host; painel de várias experts.'),
('bl',''),
('h','Explicação das VSLs'),
('p','**Mecanismo do exemplo (referência que escala hoje): AlkaMelt — "The real baking soda water shot" (Today with Jenna & Sheinelle com avatares de IA; 51:36; dissecação completa em 02-dissecacoes/).**'),
]
add(cell,items,clear=False)
cell._tc.append(el_tbl)
et=Table(el_tbl,cell)
rows=[
('Resumo do Mecanismo Único do Problema','O peso depois dos 40 não é disciplina: estresse crônico, ultraprocessados e "the hormonal crash that happens after 40" desligam a produção de GLP-1 e GIP (os hormônios que dizem "stop eating, start burning"). O corpo entra em pânico e guarda tudo como gordura. As injeções "replace them with synthetic versions" em vez de ativar — o corpo "shuts down" e, ao parar, perder peso fica "up to 5 times harder". A receita viral de bicarbonato (sem os 2 ingredientes, na dose errada) "shuts down the cells responsible for producing GLP-1 and GIP".'),
('Explicação Técnica/Científica do Mecanismo','Três camadas, cada uma com estudo e metáfora: (1) intestino ácido adormece as células L — "think of your digestive system like a garden… if the soil is too acidic, nothing grows"; prova: fMRI "2023 study in the Journal of Clinical Endocrinology" (sinais de fome "fading away"); (2) a enzima DPP-4 destrói GLP-1/GIP "within minutes" — por isso pink salt, gelatina e ACV falham; gingerol "inhibits DPP-4 activity by up to 93%" (Journal of Medicinal Food); (3) o "metabolic switch" AMPK trava após os 40 — berberina "flip your metabolic switch"; "12-week trial at Yale… up to 3 times more body fat". Números sem fonte verificável — não reutilizar.'),
('Resumo do Mecanismo Único da Solução','"The real baking soda shot": bicarbonato puro + 2 ingredientes (gengibre e berberina), "less than a dollar a day", 1 copo por manhã → "cleans your intestine from the inside out, waking up your fat-burning hormones"; "Your own hormones produced by your own body. Not synthetic, not from a needle." "Purity problem" + "mixing ratio" fecham o faça-em-casa; nasce a fórmula líquida (BioActive Naturals, "FDA registered"): gotas "absorb… up to 10 times faster and deliver 6 times more bioactive compound". + NAD+ para a pele ("you actually look younger").'),
('Produto e Composição','Produto: AlkaMelt (gotas sublinguais, 5 gotas em jejum, "takes about 10 seconds"); dose "personalizada" por perfil de saúde (quiz de 5 passos). Composição declarada na VSL: sodium bicarbonate + concentrated gingerol extract + bioactive berberine + NAD+; "100% natural. No gluten, no sugar, no artificial anything"; "recommended for women dealing with thyroid imbalances, prediabetes, or high cholesterol". Inclui app (consultas 1 clique, 2 grátis/mês), AlkaMelt Academy ("Netflix for your health"), Inner Circle ("sisterhood" com Gayle/Kelly/Whoopi).'),
('Oferta (Desconto, brindes etc.)','– "Not in pharmacies… not on Amazon or eBay" (markup 6x, falsificações). – Lançamento $185 → "$98 per bottle" (demanda após a Oprah) → "Today and only today… 6-month supply for the price of just 3 bottles" = $49/frasco, "saving you over $300"; 3 frascos $69; 2 meses $79 ("almost nobody picks that one"). – 3 presentes só no kit de 6: Runway Waist Formula ($247; "nutritionist who preps Victoria\'s Secret models"), Youth Glow Masterclass ($150; dermatologista "A-list"; Oprah "paid $7,000 each time"), Zoom de 45 min com a médica ($10.000; só as 50 primeiras). – App "normally $27 a month", lifetime. – Garantia: "Try AlkaMelt for 60 days. If it doesn\'t work for you, you don\'t pay a single cent." – Entrega 3–5 dias; checkout "less than 60 seconds".'),
('Close (Pressão final e aumento de ticket médio)','– Pressão: "Our last batch was gone in 48 hours"; "every AlkaMelt formula is personalized, so we can only prepare so many each month"; "300 kits for this audience… they won\'t last until tomorrow"; "I\'m Oprah Winfrey, and I still had to wait 3 weeks"; botão verde = estoque / vermelho = "you missed it"; "less than 300 bottles left… months before the next batch". – Ticket médio: "90% of our customers go with the 6-bottle kit, because that\'s what it takes to reset your body for good"; "Once you start seeing results after 30 days, the last thing you want is to run out"; bônus condicionados ao kit de 6; recap com value stack ($27/mês + $247 + $150 + $10.000) "All of this for just $49 per bottle". – Fechamento emocional (Oprah): "It\'s not your fault. It never was… It\'s biology. And biology can be fixed." + future pacing ("Your jeans zip up. Someone takes a photo and you don\'t run to the back").'),
]
for i,(k,v) in enumerate(rows):
    r=et.rows[i+1]
    for ci,txt in enumerate((k,v)):
        c=r.cells[ci]
        for p in list(c.paragraphs)[1:]: p._element.getparent().remove(p._element)
        for rr in list(c.paragraphs[0].runs): rr._element.getparent().remove(rr._element)
        run(c.paragraphs[0],txt,bold=(ci==0))

# ---------- 3. BRIEF DE OFERTA
add(T[36].rows[0].cells[0],[
('h','Elenco comum aos 3 formatos (decisão 20/11: a protagonista da Emotional Story é Valerie Bertinelli):'),
('b','**A Protagonista — Valerie Bertinelli (66):** a mulher 60+ que "tentou tudo" em público por 40 anos e emagreceu sem injeção. Arco documentado (fontes na pesquisa, Frente 04 e Trends do usuário): porta-voz da Jenny Craig em 2007–2009 (perdeu ~40 lb, capa de biquíni aos 48) e reganhou; luta pública com comer emocional ("unconscious eating"), livro "Enough Already" (2022) sobre comida e autoestima; divórcio em 2022; disse publicamente que não usa e "nunca vai usar" GLP-1 (People, mar/2026); parou de se pesar e passou a medir o bem-estar, não o número; QUOTE (TODAY): "Unless you do the emotional and mental work, weight is not going to stay off."; QUOTE (2024, via Yahoo): "stop with the lose ten pounds in a week"; apareceu no Drew Barrymore Show em nov/2026 em segmento de menopausa (patrocinado pela Midi Health); "valerie bertinelli weight loss" +3.050% e "how did valerie bertinelli lose weight" +550% no Google Trends (7d, 19/11/2026). Função narrativa: conta o ciclo dieta → perda → reganho → vergonha pública → "largar a balança"; é quem demonstra o copo. Função psicológica: a prova de elite que a avatar 60+ já procura ("how did she do it without Ozempic") e a absolvição de quem passou 40 anos "at war with my body". Dramatização (não documentado — a roteirizar como tal): o Chia Soda Ritual, a cintura em polegadas e a correção "25-year-old version" entram como a descoberta dela na história.'),
('i','Nota de uso: a história pública acima é dado; qualquer fala, uso do ritual ou endosso do produto atribuídos a Valerie Bertinelli exigem autorização formal de imagem/voz/nome (referência criativa ≠ endosso). Sem autorização, o papel vira uma personagem original com o mesmo arco (mulher 60+, décadas de dieta pública, sem injeção, largou a balança). A pesquisa registrou que deepfakes de celebridades são a objeção nº 1 do mercado (BBB 170+ denúncias; Snopes; Meta celeb-bait).'),
('b','**A Anfitriã (varia por formato):** Ideia 1 ex-âncora local de 52 anos; Ideia 2 confidente/autora de 62 anos com luta pública própria; Ideia 3 jornalista de saúde de 58 anos como moderadora. Em todos: ela é a paciente, confessa a própria cintura no primeiro minuto — e recebe Valerie como a convidada que "fez sem injeção".'),
('b','**A Ginecologista da Menopausa (55–56):** dona da camada 1 (o escudo que cai aos 45, o solo ácido, as células L). Tom "ninguém te contou", sem "doctors are furious".'),
('b','**A Gastro/Nutricionista Clínica (48–50):** dona da camada 2 (estômago vazio + estresse; "comer menos piorou"; gengibre/magnésio); na Ideia 1 é também a chef que prepara os dois copos com Valerie (que é apresentadora de culinária — a bancada é o território dela).'),
('b','**A Médica de Obesidade/Metabolismo (50):** dona da camada 3 (o interruptor; "não é a mesma gordura"; por que a injeção não devolve o escudo); traz a linha do tempo 30/90/180.'),
('b','**Depoentes (3):** 47 (perimenopausa, "a barriga apareceu aos 40"), 58 ("5 polegadas em 3 meses, sem receita, sem abrir mão de comida"), 69 (parou o composto quando o provedor fechou; "the pharmacy said it didn\'t go through"). Sempre com idade, número, prazo e "resultados típicos".'),
('b','**A Avó (1945, fotografia):** passou pela menopausa com uma caixa de bicarbonato ao lado do fogão e a cintura não mudou — âncora da lead histórica.'),
])
add(T[37].rows[0].cells[0],[
('i','Fonte da história: peça validada "Oat Trick / LipoLess" (Drew Barrymore Show com Valerie Bertinelli). Mantidos os beats emocionais, as tentativas, o fundo do poço e os números da peça; trocados apenas o gatilho (menopausa em vez do bebê), o truque (Chia Soda em vez da aveia) e o médico (a ginecologista do painel em vez do Dr. Barnard).'),
('p','**Antes (da peça):** "Nem sempre foi assim." Valerie não tinha pavor da balança, não evitava espelhos, não desprezava o próprio corpo. Sentia-se enérgica, magra e jovem. Não era magra como uma angel da Victoria\'s Secret, mas ninguém olhava para ela e dizia que tinha se descuidado.'),
('p','**A traição do corpo (gatilho ajustado: depois dos 45, com a menopausa):** foi muito difícil ver o corpo traí-la. O cansaço era esmagador, os desejos a torturavam e o peso subia "como se meu corpo tivesse esquecido como queimar calorias". O pescoço foi desaparecendo, a gordura saltava dos braços e a barriga ficou impossível de esconder, por mais criativa que fosse com as roupas. E isso desencadeou algo mais profundo do que vergonha: raiva. "Raiva pura do meu próprio corpo por me trair." Honestamente, nojo do próprio corpo.'),
('p','**As tentativas (da peça):** fez o que qualquer mulher faria: dieta e exercício. Primeiro ioga com dieta cetogênica, perdeu cerca de 3 kg em um mês. Depois uma refeição fora da dieta, um fim de semana de folga, e tudo voltou, normalmente com 1 kg extra "como um bônus cruel". O mesmo efeito ioiô com o Weight Watchers, com as caminhadas, com o CrossFit e com todas as soluções de emagrecimento que existem. "Vocês, meninas, sabem exatamente do que estou falando, não é?" A frustração, a vergonha e a raiva.'),
('p','**O pior momento (da peça):** no pior momento ela pesava 190 lb (86 kg). Sentia-se derrotada cada vez que subia na balança, escondia-se das fotos e até evitava a intimidade. (Dramatização nossa, encaixada aqui: viu o baking soda shot que todo mundo estava fazendo, colherada, limão, gelo, fez por semanas e só ganhou refluxo e inchaço. Mais uma prova, na cabeça dela, de que o problema era ela.)'),
])
add(T[38].rows[0].cells[0],[
('p','**O fundo do poço (da peça):** derrotada na balança, escondida das fotos, evitando o marido. Foi nesse momento que uma paciente a indicou para a ginecologista (na peça original, o Dr. Barnard), e ela entrou no consultório sem esperar nada.'),
('p','**A virada (nosso mecanismo, no beat da peça):** a médica diz a frase que ninguém tinha dito em 40 anos: **"Não é a mesma gordura depois dos 45. E você não falhou no shot. Te deram a versão de 25 anos."** Explica o escudo que caiu, o solo ácido, as células L que dormem e por que a colherada com limão explodiu no estômago em vez de chegar ao intestino. Pela primeira vez a explicação não passa por força de vontade.'),
('p','**O primeiro gesto e o resultado (estrutura da peça, receita nossa):** "Vou ser sincera, até eu achei isso loucura no começo." Um copo de água, uma colher de chia, uma pitada de bicarbonato, dez minutos. "No momento em que comecei, meus desejos por junk food simplesmente desapareceram." Sem dieta, sem pisar na academia, sem injeção cara e perigosa, sem cirurgia. Em 55 dias, 48 lb (22 kg) a menos e cinco tamanhos de vestido. "Eu exagerei e tive que recuar quando os quilos começaram a cair muito rápido."'),
('p','**O que a virada ensina (fecho da peça adaptado):** não depende de virar escrava da dieta, porque ela pode comer boa comida quando quiser. Não depende de academia cinco vezes por semana. A única coisa que precisa fazer é o copo de manhã. E, como na peça, ela decide compartilhar: foi ao programa e revelou a receita completa. "Então assista à entrevista e anote o passo a passo. Antes que perceba, estará recebendo elogios em todos os lugares que for."'),
('i','Nota: os números (48 lb em 55 dias; 190 lb no pior momento) são os da peça validada. Versão com tipicidade, se preferida: "polegadas na cintura em 3 meses; primeiras 8–10 lb em 30 dias".'),
])
add(T[40].rows[0].cells[0],[
('p','**A)** Entre 40 e 55 o estrogênio cai — e ele era o escudo do seu intestino: mantinha o ambiente equilibrado, protegia o revestimento e mantinha acordadas as células L, que produzem GLP-1 e GIP (o "já chega, pode queimar").'),
('p','**B)** Sem o escudo, anos de café, açúcar, ultraprocessado, remédio e estresse azedam o solo; as células L dormem; o sinal some. O cérebro acha que a comida é escassa e manda guardar tudo — na barriga, porque o estrogênio também era quem mandava guardar no quadril.'),
('p','**Logo:** a cintura cresce com o peso igual (não é a mesma gordura), o food noise aparece, e cada tentativa de "comer menos" deixa o intestino vazio e ácido por mais horas — piorando o que tentava resolver. Não é disciplina: é a Menopause Acid Belly, e o manual dos 30 (e a receita de 25 anos do TikTok, ácido em cima de ácido) não serve para o corpo dos 50.'),
('p','**Por que a injeção não resolveu:** ela substitui o sinal enquanto está no corpo, mas não devolve o escudo nem acorda as células L; ao parar, o solo continua ácido e o sinal some de novo — "the food noise came back", e o peso volta com juros.'),
])
add(T[41].rows[0].cells[0],[
('p','**A\')** Se o problema é o solo ácido que adormeceu as células L, a primeira coisa a fazer é neutralizar o solo onde elas vivem — no intestino, não no estômago. Uma pitada de bicarbonato tamponada e levada pelo gel de chia chega onde deve chegar; a colherada com limão explode antes (por isso inchou). Os dez minutos de espera são o que o TikTok pulou: o gel se forma e carrega o tampão.'),
('p','**B\')** Com o solo neutro, as células L acordam e o próprio corpo volta a produzir o sinal "já chega" — de forma modesta e natural, sem agulha e sem dependência (a fibra solúvel aumenta a saciedade e o GLP-1 endógeno; a Amazon já chama isso de "GLP-1 friendly"). Para o sinal não ser destruído pelo "ácido do estresse", o produto acrescenta gengibre (digestão em que ela já confia) e magnésio (sono, cãibra, ansiedade da menopausa); para o corpo voltar a queimar em vez de guardar, um ativador de baixo risco destrava o interruptor.'),
('p','**Por que é a única que funciona:** dieta e caminhada não devolvem o escudo; a injeção substitui o sinal e cria dependência; gelatina, pink salt e a colherada com limão nunca chegaram ao intestino. Só o que neutraliza o solo, acorda as células L, protege o sinal e destrava o interruptor — na dose da década certa — ataca a causa em vez do sintoma. E por que não dá para fazer só em casa: a pitada é o início; a dose por peso, tamponada, constante e combinada com as camadas 2 e 3 é o que o produto entrega todo dia.'),
])
add(T[42].rows[0].cells[0],[
('b','**Demonstração dos dois copos** (bancada, 30 s, cronômetro): colherada + limão espuma e transborda vs. pitada + chia engrossa em 10 min; a colher desliza devagar. Fecha com a fita métrica ("polegadas, não espuma"). É a prova que nenhuma das 20 VSLs faz.'),
('b','**Ciência do esporte:** "sodium bicarbonate loading" com evidência reconhecida em atletas — só funciona tamponado, dosado por peso e no horário; justifica "a dose, não a colherada".'),
('b','**Menopausa e gordura visceral (Mayo/Harvard/Cleveland Clinic):** a gordura muda para a barriga na transição; "Some women go up two clothing sizes around the waist while their weight stays the same" (Dra. Haver, verbatim na pesquisa).'),
('b','**Menopausa e intestino:** queda do estrogênio altera microbiota e barreira intestinal (estroboloma) — "o escudo" tem base, sem prometer pH.'),
('b','**Fibra solúvel e saciedade/GLP-1 endógeno:** psyllium/chia; WW/GoodRx chamam psyllium de "the cheapest, best-evidence intervention"; Metamucil "GLP-1 Friendly" 70K+/mês = prova cultural.'),
('b','**Reganho pós-GLP-1:** Oxford (jan/2026) reganho mais rápido que pós-dieta; Menopause Society (out/2026): mulheres 50–64 são o maior grupo de usuárias; "the weight came back lightening quick plus a few" (Drugs.com).'),
('b','**Prova cultural e histórica:** a caixa de bicarbonato na cozinha americana há gerações; "your grandmother used it for heartburn"; a pitada no molho de tomate; fotos de 1945 (com fonte).'),
('b','**Depoimentos reais** (47, 58, 69) com idade, número, prazo, "resultados típicos" e consentimento; antes/depois autorizados e datados; nada de atores (FTC x NextMed).'),
('b','**Prova por contraste honesto:** a VSL nomeia o que não funciona e por quê (gelatin trick, pink salt, a colherada com limão, 1.200 kcal, a injeção sem devolver o escudo) — e mostra a BBB/Snopes como aliados ("por isso não tem celebridade neste vídeo").'),
('b','**Compliance como prova:** "sem celebridade, sem receita secreta, sem assinatura escondida; reembolso de 60 dias visível" — responde às 3 objeções nº 1 do mercado na própria estrutura da oferta.'),
('i','Nunca usar: fMRI "2023 JCEM", "93%", "3x em Yale", "5x harder", "10x faster", "12.000 mulheres" (a menos que seja número real), "1 lb por dia", "alcaliniza o sangue", "baixa cortisol", "trata menopausa", "natural Ozempic".'),
])

d.save(OUT); print('saved',OUT)
