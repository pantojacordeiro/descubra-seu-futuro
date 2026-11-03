import streamlit as st

st.set_page_config(
    page_title="Descubra seu Futuro",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family: Inter, sans-serif;}
.stApp {background: #f4f6fc;}
.block-container {max-width: 850px; padding-top: 2rem; padding-bottom: 3rem;}
.hero {
 background: radial-gradient(circle at 88% 15%, #3c77d8 0, transparent 30%),
             linear-gradient(125deg,#101a35,#1b3264 75%,#214d77);
 color: white; padding: 3.2rem; border-radius: 26px; margin-bottom: 1.2rem;
}
.eyebrow {color:#9deaf0;font-size:.75rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;}
.hero h1 {font-size: clamp(2.2rem,6vw,3.8rem);line-height:1.05;letter-spacing:-2px;margin:.9rem 0;}
.hero p {color:#d4def3;line-height:1.7;font-size:1.05rem;}
.info-card {background:white;color:#20283a;border:1px solid #e5e9f2;border-radius:16px;padding:1rem 1.2rem;height:100%;}
.info-card b {color:#20283a;}
.result-card {background:linear-gradient(125deg,#101a35,#1c3970);color:white;padding:1.7rem;border-radius:20px;}
.result-card p {color:#d3def1;line-height:1.6;}
.small-muted {color:#69748c;font-size:.9rem;}
div.stButton > button[kind="primary"] {background:linear-gradient(100deg,#5b78ff,#39c6d8);border:0;color:white;border-radius:12px;font-weight:800;min-height:3rem;}
div.stButton > button {border-radius:12px;}
</style>
""", unsafe_allow_html=True)

COURSES = {
    "log": {
        "name": "Técnico em Logística",
        "desc": "Organização e movimentação de materiais, estoques, compras, armazenagem, transporte e distribuição.",
        "fit": "Você pode gostar de organizar recursos, acompanhar prazos, resolver imprevistos e fazer as coisas chegarem ao lugar certo.",
        "areas": "Estoques, centros de distribuição, transportadoras, compras, almoxarifados e operações.",
        "traits": "Organização, comunicação, atenção a prazos e visão do processo como um todo.",
    },
    "pcp": {
        "name": "Técnico em PCP",
        "desc": "Planejamento e controle da produção: programação de atividades, acompanhamento de processos, materiais, prazos e produtividade.",
        "fit": "Você pode se identificar com planejar etapas, acompanhar indicadores e encontrar maneiras de tornar o trabalho mais eficiente.",
        "areas": "Indústrias, planejamento da produção, programação, controle de materiais e acompanhamento de processos.",
        "traits": "Raciocínio lógico, organização, análise, atenção a detalhes e planejamento.",
    },
    "auto": {
        "name": "Técnico em Automação Industrial",
        "desc": "Sistemas de controle, sensores, comandos, equipamentos automatizados, instrumentação e tecnologias industriais.",
        "fit": "Você pode gostar de tecnologia aplicada, descobrir como sistemas funcionam e integrar equipamentos para executar tarefas automaticamente.",
        "areas": "Indústrias, integração de sistemas, instrumentação, manutenção e processos automatizados.",
        "traits": "Curiosidade tecnológica, lógica, investigação e interesse por eletrônica e controle.",
    },
    "eletro": {
        "name": "Técnico em Eletromecânica",
        "desc": "Integra conhecimentos elétricos e mecânicos para instalação, operação e manutenção de máquinas e equipamentos.",
        "fit": "Você pode se interessar por entender máquinas por dentro, identificar falhas e trabalhar com componentes elétricos e mecânicos.",
        "areas": "Manutenção industrial, máquinas, equipamentos, montagem e assistência técnica.",
        "traits": "Habilidade prática, observação, raciocínio técnico e interesse por mecanismos.",
    },
    "eletrotec": {
        "name": "Técnico em Eletrotécnica",
        "desc": "Instalações e sistemas elétricos, circuitos, comandos, máquinas elétricas, geração, distribuição e uso da energia.",
        "fit": "Você pode gostar de trabalhar com circuitos, instalações, energia e encontrar soluções para sistemas elétricos.",
        "areas": "Instalações prediais e industriais, energia, manutenção elétrica e projetos.",
        "traits": "Atenção, responsabilidade, raciocínio lógico e interesse por eletricidade.",
    },
    "tst": {
        "name": "Técnico em Segurança do Trabalho",
        "desc": "Prevenção de acidentes e doenças ocupacionais, identificação de riscos, inspeções, treinamentos e aplicação de normas.",
        "fit": "Você pode gostar de orientar pessoas, observar ambientes, prevenir problemas e contribuir para um trabalho mais seguro.",
        "areas": "Construção civil, indústrias, empresas, inspeções, treinamentos e gestão de segurança.",
        "traits": "Comunicação, observação, responsabilidade, organização e cuidado com pessoas.",
    },
}

QUESTIONS = [
    ("Em um projeto em grupo, qual tarefa você teria mais vontade de assumir?", [
        ("log", "Organizar materiais, entregas e recursos."),
        ("pcp", "Montar o cronograma e acompanhar cada etapa."),
        ("tst", "Verificar riscos e garantir que todos trabalhem com segurança."),
        ("auto", "Pensar em uma solução tecnológica para facilitar o trabalho."),
    ]),
    ("Qual situação parece mais interessante para você?", [
        ("eletro", "Descobrir por que uma máquina parou de funcionar."),
        ("eletrotec", "Entender e resolver um problema em uma instalação elétrica."),
        ("log", "Organizar o caminho de um produto até o cliente."),
        ("pcp", "Ajustar o planejamento para cumprir a produção no prazo."),
    ]),
    ("Quando algo não sai como planejado, o que você tende a fazer?", [
        ("pcp", "Reorganizar as etapas e definir novas prioridades."),
        ("tst", "Identificar o risco e evitar que o problema se repita."),
        ("eletro", "Investigar a causa técnica do defeito."),
        ("log", "Reorganizar materiais, transporte ou entregas."),
    ]),
    ("Qual atividade prática mais desperta sua curiosidade?", [
        ("auto", "Montar ou testar sensores e sistemas automatizados."),
        ("eletrotec", "Montar e testar circuitos elétricos."),
        ("eletro", "Desmontar, entender e ajustar mecanismos."),
        ("tst", "Inspecionar um local e propor melhorias de segurança."),
    ]),
    ("Em um ambiente de trabalho, o que mais chama sua atenção?", [
        ("log", "O fluxo de produtos, materiais e entregas."),
        ("pcp", "O andamento das tarefas e os resultados da produção."),
        ("auto", "As máquinas, os painéis e os sistemas de controle."),
        ("tst", "As condições do ambiente e o comportamento seguro."),
    ]),
    ("Qual problema você gostaria mais de resolver?", [
        ("eletrotec", "Uma falha em um circuito ou sistema de energia."),
        ("log", "Atrasos e desorganização no estoque ou transporte."),
        ("tst", "Uma situação que pode causar acidente ou lesão."),
        ("auto", "Um processo que poderia funcionar automaticamente."),
    ]),
    ("Que tipo de resultado dá mais satisfação a você?", [
        ("pcp", "Ver um plano funcionar e as metas serem cumpridas."),
        ("eletro", "Ver uma máquina voltar a funcionar corretamente."),
        ("log", "Ver tudo chegar no lugar certo e no prazo."),
        ("tst", "Perceber que uma prevenção evitou um acidente."),
    ]),
    ("Se pudesse fazer uma visita técnica, qual setor escolheria?", [
        ("auto", "Uma linha industrial com robôs e sensores."),
        ("log", "Um centro de distribuição e armazenagem."),
        ("eletrotec", "Uma instalação elétrica ou subestação."),
        ("pcp", "Uma sala de planejamento da produção."),
    ]),
    ("Qual dessas tarefas combina mais com seu jeito?", [
        ("tst", "Conversar com equipes e orientar sobre procedimentos."),
        ("eletro", "Usar ferramentas para avaliar e ajustar equipamentos."),
        ("pcp", "Analisar informações e organizar prioridades."),
        ("log", "Conferir materiais e coordenar movimentações."),
    ]),
    ("Diante de uma máquina moderna, o que você teria vontade de descobrir?", [
        ("auto", "Como sensores e comandos fazem tudo funcionar."),
        ("eletro", "Como as partes mecânicas e elétricas trabalham juntas."),
        ("eletrotec", "Como a energia alimenta os componentes."),
        ("pcp", "Como a máquina se encaixa no ritmo da produção."),
    ]),
    ("Qual assunto você teria mais vontade de estudar?", [
        ("log", "Estoques, transporte, compras e distribuição."),
        ("tst", "Riscos ocupacionais, prevenção e normas."),
        ("eletrotec", "Eletricidade, circuitos e instalações."),
        ("pcp", "Processos, indicadores e planejamento."),
    ]),
    ("Quando precisa aprender algo novo, qual abordagem prefere?", [
        ("eletro", "Aprender mexendo em equipamentos e componentes."),
        ("pcp", "Entender o processo e montar um passo a passo."),
        ("auto", "Testar tecnologias e descobrir como se conectam."),
        ("tst", "Observar situações reais e aprender a prevenir riscos."),
    ]),
    ("Qual desafio parece mais estimulante?", [
        ("pcp", "Fazer uma produção render melhor sem perder qualidade."),
        ("log", "Reduzir atrasos e melhorar a circulação de materiais."),
        ("eletrotec", "Planejar uma solução segura para uma instalação elétrica."),
        ("tst", "Criar ações para reduzir acidentes em uma empresa."),
    ]),
    ("Em qual atividade você se imagina trabalhando com mais interesse?", [
        ("auto", "Programando ou ajustando sistemas automatizados."),
        ("tst", "Acompanhando ambientes e orientando trabalhadores."),
        ("eletro", "Realizando manutenção em máquinas e equipamentos."),
        ("log", "Acompanhando estoques e operações de transporte."),
    ]),
    ("O que mais gostaria de desenvolver em sua formação?", [
        ("eletrotec", "Conhecimento técnico sobre sistemas elétricos."),
        ("log", "Capacidade de coordenar operações e materiais."),
        ("pcp", "Habilidade para planejar e controlar processos."),
        ("auto", "Conhecimento sobre controle e automação industrial."),
    ]),
]

def reset_quiz():
    st.session_state.started = False
    st.session_state.step = 0
    st.session_state.answers = [None] * len(QUESTIONS)
    st.session_state.finished = False

if "step" not in st.session_state:
    reset_quiz()
if "started" not in st.session_state:
    st.session_state.started = False

st.markdown("""
<div class="hero">
 <div class="eyebrow">✦ TESTE VOCACIONAL • CURSOS TÉCNICOS</div>
 <h1>Descubra o caminho que combina com você.</h1>
 <p>Responda a perguntas sobre seus interesses, seu jeito de trabalhar e as atividades que despertam sua curiosidade. No final, veja quais cursos técnicos têm mais afinidade com seu perfil.</p>
</div>
""", unsafe_allow_html=True)

if not st.session_state.finished and not st.session_state.started:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="info-card">🧭<br><b>Conheça seu perfil</b><br><span class="small-muted">Reflita sobre atividades e ambientes que combinam com você.</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="info-card">📊<br><b>Veja seu resultado</b><br><span class="small-muted">Compare a afinidade com seis áreas técnicas.</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="info-card">💡<br><b>Explore possibilidades</b><br><span class="small-muted">Entenda o que cada formação envolve.</span></div>', unsafe_allow_html=True)
    st.write("")
    if st.button("Começar meu teste →", type="primary", use_container_width=True):
        st.session_state.started = True
        st.rerun()
    st.caption("15 perguntas · cerca de 4 minutos · sem respostas certas ou erradas")

elif not st.session_state.finished:
    i = st.session_state.step
    question, options = QUESTIONS[i]
    st.progress(i / len(QUESTIONS), text=f"Pergunta {i+1} de {len(QUESTIONS)}")
    st.subheader(question)
    st.caption("Escolha a alternativa que mais se aproxima de você.")
    labels = [label for _, label in options]
    current = st.session_state.answers[i]
    default_index = next((j for j, (key, _) in enumerate(options) if key == current), None)
    selected = st.radio(
        "Selecione uma opção:",
        labels,
        index=default_index,
        key=f"answer_{i}",
        label_visibility="collapsed",
    )
    # O rádio pode retornar None enquanto o usuário ainda não escolheu uma opção.
    # Só convertemos para a chave quando houver uma seleção válida.
    if selected is not None and selected in labels:
        selected_key = options[labels.index(selected)][0]
        st.session_state.answers[i] = selected_key

    left, right = st.columns([1, 1])
    with left:
        if i > 0 and st.button("← Voltar", use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
    with right:
        button_label = "Ver meu resultado →" if i == len(QUESTIONS)-1 else "Próxima →"
        if st.button(button_label, type="primary", use_container_width=True):
            if not st.session_state.answers[i]:
                st.warning("Escolha uma alternativa antes de continuar.")
            elif i < len(QUESTIONS)-1:
                st.session_state.step += 1
                st.rerun()
            else:
                st.session_state.finished = True
                st.rerun()
    st.caption("Suas respostas são usadas para calcular o resultado nesta página. Este teste é uma ferramenta de reflexão, não substitui orientação profissional.")

else:
    counts = {key: 0 for key in COURSES}
    for answer in st.session_state.answers:
        if answer:
            counts[answer] += 1
    total = sum(counts.values())
    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    winner_key, winner_count = ranked[0]
    winner = COURSES[winner_key]
    winner_pct = round(winner_count / total * 100) if total else 0

    st.markdown(f"""
    <div class="result-card">
      <div class="eyebrow">✦ SEU RESULTADO</div>
      <h1>{winner['name']} tem mais afinidade com você!</h1>
      <p>{winner['fit']} Isso é um ponto de partida para explorar essa formação e conhecer sua rotina profissional.</p>
      <b>{winner_pct}% das suas escolhas</b>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Seu ranking de afinidade")
    st.caption("A porcentagem indica a participação de cada curso nas suas escolhas.")
    for position, (key, count) in enumerate(ranked, start=1):
        course = COURSES[key]
        pct = round(count / total * 100) if total else 0
        st.markdown(f"**{position}. {course['name']} — {pct}%**")
        st.progress(pct / 100)
        st.caption(course["desc"])

    st.subheader("Conheça melhor sua primeira opção")
    d1, d2 = st.columns(2)
    with d1:
        st.markdown("**📘 O que você estuda**")
        st.write(winner["desc"])
        st.markdown("**🧰 Onde pode atuar**")
        st.write(winner["areas"])
    with d2:
        st.markdown("**✨ Por que pode combinar**")
        st.write(winner["fit"])
        st.markdown("**🎯 Habilidades úteis**")
        st.write(winner["traits"])

    st.info("As porcentagens representam uma estimativa de afinidade com base nas respostas escolhidas, não uma garantia de desempenho ou sucesso profissional. Pesquise a grade curricular, converse com profissionais e visite instituições antes de decidir.")
    if st.button("Refazer teste ↻", type="primary"):
        reset_quiz()
        st.rerun()

st.markdown("---")
st.caption("Descubra seu Futuro · Orientação vocacional para cursos técnicos")
