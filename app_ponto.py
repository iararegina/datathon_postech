import streamlit as st
import pickle

def main():
    st.title('Ponto de Virada - ONG Passos Mágicos')
    st.write('O objetivo é prever se o aluno ou aluna atingirá ou não o Ponto de Virada se baseando nos principais índices de acompanhamento da ONG.')

    # Adicionando um formulário para as entradas
    with st.form(key='my_form'):
        # Adicionando as entradas
        st.write('Preencha os valores nos campos abaixo: ')
        opcoes = ['Ametista', 'Ágata', 'Quartzo', 'Topázio']
        pedra = st.selectbox('PEDRA', options=opcoes)
        INDE = st.slider('INDE', min_value=0.0, max_value=10.0, step=0.1)  # Barra deslizante para INDE
        IAA = st.slider('IAA', min_value=0.0, max_value=10.0, step=0.1)    # Barra deslizante para IAA
        IEG = st.slider('IEG', min_value=0.0, max_value=10.0, step=0.1)    # Barra deslizante para IEG
        IPS = st.slider('IPS', min_value=0.0, max_value=10.0, step=0.1)    # Barra deslizante para IPS
        IDA = st.slider('IDA', min_value=0.0, max_value=10.0, step=0.1)    # Barra deslizante para IDA
        IPP = st.slider('IPP', min_value=0.0, max_value=10.0, step=0.1)    # Barra deslizante para IPP

        # Adicionando um botão de submit
        submit_button = st.form_submit_button(label='Gerar Resultado')

    # Processar os dados quando o botão de submit for pressionado
    if submit_button:
        st.write('pedra:', pedra)
        st.write('INDE:', INDE)
        st.write('IAA:', IAA)
        st.write('IEG:', IEG)
        st.write('IPS:', IPS)
        st.write('IDA:', IDA)
        st.write('IPP:', IPP)

        if pedra == "Quartzo" or pedra == "Ágata":
            st.write("NÃO ATINGIRÁ O PONTO DE VIRADA")
        if float(INDE) < 5:
            st.write("NÃO ATINGIRÁ O PONTO DE VIRADA")
        if pedra == "Ametista" and float(INDE) > 7.5 and float(IAA) > 7:
            st.write("ATINGIRÁ O PONTO DE VIRADA")
        if pedra == "Topázio" and float(INDE) > 7.5 and float(IAA) > 7:
            st.write("ATINGIRÁ O PONTO DE VIRADA")

if __name__ == '__main__':
    main()




    