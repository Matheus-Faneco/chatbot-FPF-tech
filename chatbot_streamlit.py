import streamlit as st
import re

respostas = {
    'Olá': 'Olá! Como posso te ajudar?',
    'Oi': 'Olá! Como posso te ajudar?',
    'Bom dia': 'Bom dia! Como posso te ajudar?',
    'Boa tarde': 'Boa tarde! Como posso te ajudar?',
    'Boa noite': 'Boa noite! Como posso te ajudar?',
    'Quem é você?': 'Eu sou o Bit! Seu assistente virtual. Fique à vontade para me perguntar qualquer coisa sobre a FPF Tech!',
    'Qual sua função?': 'Eu sou o bit! Seu assistente virtual, fique à vontade para me perguntar qualquer coisa sobre a FPF Tech!',
    'Fundação da FPF Tech?': 'A FPF Tech foi fundada em 1998.',
    'Redes sociais':  'Nosso Instagram: @fpf.tech\n'
                      'Facebook: FPF Tech\n'
                      'linkedIn: FPFtech\n'
                      'Youtube: @FPFtech',
    'Contato': 'Nossos contatos são: (92) 2123-9797 e fpf@fpf.br',
    'Como está você?': 'Olá! eu estou ótimo, como posso te ajudar?',
    'Qual seu nome?': 'Eu sou o bit! Seu assistente virtual, fique à vontade para me perguntar qualquer coisa sobre a FPF Tech!',
    'Explicar missão': 'A missão da FPF Tech é criar soluções inovadoras entregando valor aos seus clientes e à sociedade, com a colaboração de pessoas notáveis.',
    'Conte mais sobre a fundação': 'A FPF Tech foi fundada em 1998 com o objetivo de ser um centro de excelência em tecnologia.',
    'Saudação': 'Olá! Como posso te ajudar?',
    'O que é a FPF Tech?': 'A FPF Tech é um centro tecnológico premiado em software e hardware, reconhecido por cinco anos como uma das melhores empresas em TI & Telecom no Brasil. Destaca-se por investir em treinamentos e ter uma equipe jovem.',
    'Quando a FPF Tech foi fundada?': 'A FPF Tech foi fundada em 1998.',
    'O que a FPF Tech faz?': 'A FPF Tech é uma instituição de pesquisa e desenvolvimento, sem fins lucrativos, focada na geração de soluções inovadoras, serviços e cases de sucesso globais nas áreas de automação industrial, tecnologias móveis e assistivas, internet, qualidade de software e capacitação tecnológica.',
    'Qual é a missão da FPF Tech?': 'A missão da FPF Tech é criar soluções inovadoras, entregando valor aos seus clientes e à sociedade, com a colaboração de pessoas notáveis.',
    'Como posso te chamar?': 'Pode me chamar de Bit, seu assistente virtual!',
    'Me ajude': 'Claro, estou aqui para ajudar. O que você precisa?',
    'Qual é a visão da Fundação Paulo Feitosa?': 'Ser uma empresa inspiradora, independente e sustentável no ecossistema tecnológico global',
    'Missão': 'A missão da FPF Tech é criar soluções inovadoras entregando valor aos seus clientes e à sociedade, com a colaboração de pessoas notáveis.',
    'FPF Tech faz?': 'A FPF Tech é uma instituição de Pesquisa e Desenvolvimento, sem fins lucrativos, focada na geração de soluções inovadoras, serviços e cases de sucesso globais nas áreas de Automação Industrial, Tecnologias Móveis e Assistivas, Internet, Qualidade de Software e Capacitação Tecnológica.',
    'Qual é o seu objetivo?': 'Meu objetivo é ajudar e fornecer informações sobre a FPF Tech. Como posso ajudar você hoje?',
    'Onde está localizada a Fundação Paulo Feitosa?': 'Avenida Governador Danilo Areosa, 169 lt 1 Distrito Industrial - Manaus - AM',
    'Quais são os valores da Fundação Paulo Feitosa?': 'Experimentação, atitude vencedora, colaboração, responsabilidade Social e compromisso com os parceiros!',

}


def encontrar_melhorResposta(msg,respostas):

    """
    a função 'encontrar_melhorResposta' encontrará a melhor resposta para a mensagem do usuário;
    'melhor_resposta' foi criada e será inicializada com a mensaagem padrão 'Desculpa, não entendi sua pergunta!';

    """
    melhor_resposta = 'Desculpa, não entendi sua pergunta!'
    melhor_pontuacao = 0

    #O for irá iterar cada par em pergunta-resposta no dicionário 'respostas';
    for pergunta, resposta in respostas.items():
        palavras_pergunta = set(re.findall(r'\b\w+\b', pergunta.lower()))

        palavras_msg = set(re.findall(r'\b\w+\b', msg.lower()))

        pontuacao = len(palavras_pergunta.intersection(palavras_msg))

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_resposta = resposta

    return melhor_resposta


st.title("ChatBot FPF teste")

mensagem = st.text_input("Digite aqui:")

resposta = encontrar_melhorResposta(mensagem,respostas)

st.write("Você: ", mensagem)

st.write("Bit: ", resposta)

