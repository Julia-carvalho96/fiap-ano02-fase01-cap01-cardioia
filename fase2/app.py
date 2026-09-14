"""Front acadêmico do CardioIA — Fase 2.

Execução:
    streamlit run fase2/app.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


DIRETORIO_FASE2 = Path(__file__).resolve().parent
sys.path.insert(0, str(DIRETORIO_FASE2 / "src"))

from treinar_baselines import carregar_dados, criar_modelos  # noqa: E402


st.set_page_config(
    page_title="CardioIA",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
)


ROTULOS_VARIAVEIS = {
    "idade": "Idade",
    "sexo": "Sexo",
    "tipo_dor_peito": "Tipo de dor no peito",
    "pressao_arterial_repouso": "Pressão arterial em repouso",
    "colesterol": "Colesterol",
    "acucar_jejum_maior_120": "Glicemia de jejum acima de 120 mg/dl",
    "eletrocardiograma_repouso": "Resultado do ECG em repouso",
    "frequencia_cardiaca_maxima": "Frequência cardíaca máxima",
    "angina_induzida_exercicio": "Angina induzida por exercício",
    "depressao_st_exercicio": "Depressão do segmento ST",
    "inclinacao_st_pico_exercicio": "Inclinação do segmento ST",
    "num_vasos_principais": "Número de vasos principais",
    "resultado_thal": "Resultado do atributo thal",
}

ROTULOS_CATEGORIAS = {
    "masculino": "Masculino",
    "feminino": "Feminino",
    "angina_tipica": "Angina típica",
    "angina_atipica": "Angina atípica",
    "dor_nao_anginosa": "Dor não anginosa",
    "assintomatico": "Assintomático",
    "sim": "Sim",
    "nao": "Não",
    "normal": "Normal",
    "anormalidade_onda_st_t": "Anormalidade da onda ST-T",
    "hipertrofia_ventricular_esquerda": "Hipertrofia ventricular esquerda",
    "ascendente": "Ascendente",
    "plana": "Plana",
    "descendente": "Descendente",
    "defeito_fixo": "Defeito fixo",
    "defeito_reversivel": "Defeito reversível",
}


def aplicar_estilo() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at 92% 8%, rgba(200, 29, 119, 0.10), transparent 30rem),
                #fcfafc;
        }
        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }
        .hero {
            padding: 2rem 2.2rem;
            border-radius: 24px;
            color: white;
            background: linear-gradient(120deg, #50133f 0%, #9d145e 58%, #d92d84 100%);
            box-shadow: 0 18px 45px rgba(80, 19, 63, 0.18);
            margin-bottom: 1.4rem;
        }
        .hero h1 {
            margin: 0;
            font-size: 2.55rem;
            letter-spacing: -0.04em;
        }
        .hero p {
            margin: 0.65rem 0 0;
            max-width: 760px;
            font-size: 1.05rem;
            opacity: 0.92;
        }
        .academic-badge {
            display: inline-block;
            padding: 0.35rem 0.75rem;
            margin-bottom: 0.8rem;
            border: 1px solid rgba(255,255,255,0.45);
            border-radius: 999px;
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }
        .result-card {
            padding: 1.5rem;
            border: 1px solid #eadce5;
            border-radius: 20px;
            background: white;
            box-shadow: 0 8px 28px rgba(62, 22, 49, 0.08);
        }
        .result-number {
            color: #9d145e;
            font-size: 3rem;
            font-weight: 750;
            line-height: 1;
        }
        .muted {
            color: #6f626b;
            font-size: 0.92rem;
        }
        div[data-testid="stMetric"] {
            border: 1px solid #eadce5;
            background: white;
            padding: 1rem;
            border-radius: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_resource(show_spinner="Preparando o modelo acadêmico...")
def obter_modelo():
    """Treina o modelo selecionado usando todos os registros para demonstração."""
    atributos, alvo = carregar_dados()
    modelo = criar_modelos()["regressao_logistica"]
    modelo.fit(atributos, alvo)
    return modelo


def formatar_categoria(valor: str) -> str:
    return ROTULOS_CATEGORIAS.get(valor, valor.replace("_", " ").capitalize())


def criar_formulario() -> pd.DataFrame | None:
    st.subheader("Dados da simulação")
    st.caption(
        "Preencha valores fictícios ou de exemplo. Não insira nome, CPF, prontuário "
        "ou qualquer informação que identifique uma pessoa."
    )

    with st.form("formulario_simulacao"):
        coluna_1, coluna_2, coluna_3 = st.columns(3)

        with coluna_1:
            idade = st.number_input("Idade", min_value=18, max_value=100, value=54)
            sexo = st.selectbox(
                "Sexo biológico",
                ["feminino", "masculino"],
                format_func=formatar_categoria,
            )
            tipo_dor = st.selectbox(
                "Tipo de dor no peito",
                [
                    "angina_tipica",
                    "angina_atipica",
                    "dor_nao_anginosa",
                    "assintomatico",
                ],
                format_func=formatar_categoria,
            )
            pressao = st.number_input(
                "Pressão arterial em repouso (mm Hg)",
                min_value=70,
                max_value=250,
                value=130,
            )
            colesterol = st.number_input(
                "Colesterol sérico (mg/dl)",
                min_value=80,
                max_value=700,
                value=245,
            )

        with coluna_2:
            acucar = st.selectbox(
                "Glicemia de jejum acima de 120 mg/dl",
                ["nao", "sim"],
                format_func=formatar_categoria,
            )
            ecg = st.selectbox(
                "ECG em repouso",
                [
                    "normal",
                    "anormalidade_onda_st_t",
                    "hipertrofia_ventricular_esquerda",
                ],
                format_func=formatar_categoria,
            )
            frequencia = st.number_input(
                "Frequência cardíaca máxima (bpm)",
                min_value=50,
                max_value=230,
                value=150,
            )
            angina_exercicio = st.selectbox(
                "Angina induzida por exercício",
                ["nao", "sim"],
                format_func=formatar_categoria,
            )
            depressao_st = st.number_input(
                "Depressão do segmento ST",
                min_value=0.0,
                max_value=10.0,
                value=1.0,
                step=0.1,
            )

        with coluna_3:
            inclinacao = st.selectbox(
                "Inclinação do ST no pico do exercício",
                ["ascendente", "plana", "descendente"],
                format_func=formatar_categoria,
            )
            vasos_exibicao = st.selectbox(
                "Número de vasos principais",
                ["Não informado", "0", "1", "2", "3"],
                help="Quantidade observada por fluoroscopia na base original.",
            )
            thal_exibicao = st.selectbox(
                "Resultado do atributo thal",
                [
                    "Não informado",
                    "normal",
                    "defeito_fixo",
                    "defeito_reversivel",
                ],
                format_func=lambda valor: (
                    valor if valor == "Não informado" else formatar_categoria(valor)
                ),
                help=(
                    "A documentação original da UCI fornece os rótulos, mas não "
                    "expande o significado clínico da sigla."
                ),
            )
            st.info(
                "O modelo foi desenvolvido com uma base histórica pequena. "
                "Valores fora do perfil original aumentam a incerteza."
            )

        enviado = st.form_submit_button(
            "Executar simulação",
            type="primary",
            use_container_width=True,
        )

    if not enviado:
        return None

    vasos = np.nan if vasos_exibicao == "Não informado" else float(vasos_exibicao)
    thal = np.nan if thal_exibicao == "Não informado" else thal_exibicao

    return pd.DataFrame(
        [
            {
                "idade": int(idade),
                "pressao_arterial_repouso": float(pressao),
                "colesterol": float(colesterol),
                "frequencia_cardiaca_maxima": float(frequencia),
                "depressao_st_exercicio": float(depressao_st),
                "num_vasos_principais": vasos,
                "sexo": sexo,
                "tipo_dor_peito": tipo_dor,
                "acucar_jejum_maior_120": acucar,
                "eletrocardiograma_repouso": ecg,
                "angina_induzida_exercicio": angina_exercicio,
                "inclinacao_st_pico_exercicio": inclinacao,
                "resultado_thal": thal,
            }
        ]
    )


def explicar_predicao(modelo, registro: pd.DataFrame) -> pd.DataFrame:
    """Calcula contribuições locais da Regressão Logística."""
    preprocessador = modelo.named_steps["preprocessamento"]
    estimador = modelo.named_steps["modelo"]
    valores = preprocessador.transform(registro)[0]
    coeficientes = estimador.coef_[0]
    nomes = preprocessador.get_feature_names_out()
    contribuicoes = valores * coeficientes

    linhas = []
    for nome, contribuicao in zip(nomes, contribuicoes, strict=True):
        nome_limpo = nome.replace("numerico__", "").replace("categorico__", "")
        rotulo = nome_limpo
        for variavel, traducao in sorted(
            ROTULOS_VARIAVEIS.items(),
            key=lambda item: len(item[0]),
            reverse=True,
        ):
            if nome_limpo == variavel:
                rotulo = traducao
                break
            prefixo = f"{variavel}_"
            if nome_limpo.startswith(prefixo):
                categoria = nome_limpo[len(prefixo):]
                rotulo = f"{traducao}: {formatar_categoria(categoria)}"
                break

        linhas.append(
            {
                "Fator": rotulo,
                "Contribuição": float(contribuicao),
                "Efeito": (
                    "Aumentou a estimativa"
                    if contribuicao > 0
                    else "Reduziu a estimativa"
                ),
            }
        )

    tabela = pd.DataFrame(linhas)
    tabela["Magnitude"] = tabela["Contribuição"].abs()
    return tabela.sort_values("Magnitude", ascending=False).head(6)


def mostrar_resultado(registro: pd.DataFrame) -> None:
    modelo = obter_modelo()
    probabilidade = float(modelo.predict_proba(registro)[0, 1])
    classe = "Presença" if probabilidade >= 0.5 else "Ausência"

    st.markdown("---")
    st.subheader("Resultado da simulação")

    coluna_resultado, coluna_contexto = st.columns([1, 1.25], gap="large")
    with coluna_resultado:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="muted">Probabilidade produzida pelo modelo</div>
                <div class="result-number">{probabilidade:.1%}</div>
                <p><strong>Classe estimada:</strong> {classe}</p>
                <p class="muted">
                    O corte acadêmico usado para transformar a probabilidade em
                    classe é 50%.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(probabilidade)

    with coluna_contexto:
        st.warning(
            "Este resultado não indica diagnóstico, risco clínico real nem "
            "necessidade de tratamento. Não use a simulação para tomar decisões "
            "de saúde."
        )
        st.write(
            "O percentual mostra apenas o comportamento matemático de um modelo "
            "treinado em 303 registros históricos da Cleveland Clinic."
        )

    st.subheader("Fatores que mais influenciaram esta simulação")
    st.caption(
        "As contribuições mostram como o modelo combinou as variáveis neste "
        "registro. Associação estatística não significa causalidade."
    )
    explicacao = explicar_predicao(modelo, registro)
    st.dataframe(
        explicacao[["Fator", "Efeito", "Contribuição"]].style.format(
            {"Contribuição": "{:+.3f}"}
        ),
        use_container_width=True,
        hide_index=True,
    )


def pagina_desempenho() -> None:
    st.subheader("Desempenho observado")
    st.caption("Avaliação no conjunto de teste com 61 pacientes.")

    colunas = st.columns(4)
    colunas[0].metric("ROC AUC", "0,958")
    colunas[1].metric("Acurácia", "86,9%")
    colunas[2].metric("Sensibilidade", "92,9%")
    colunas[3].metric("F1", "86,7%")

    st.markdown("#### Avaliação descritiva por sexo")
    desempenho = pd.DataFrame(
        [
            {
                "Sexo": "Feminino",
                "n": 20,
                "Casos positivos": 7,
                "Acurácia": 0.950,
                "Precisão": 1.000,
                "Sensibilidade": 0.857,
                "F1": 0.923,
                "ROC AUC": 1.000,
            },
            {
                "Sexo": "Masculino",
                "n": 41,
                "Casos positivos": 21,
                "Acurácia": 0.829,
                "Precisão": 0.769,
                "Sensibilidade": 0.952,
                "F1": 0.851,
                "ROC AUC": 0.938,
            },
        ]
    )
    st.dataframe(
        desempenho.style.format(
            {
                "Acurácia": "{:.1%}",
                "Precisão": "{:.1%}",
                "Sensibilidade": "{:.1%}",
                "F1": "{:.1%}",
                "ROC AUC": "{:.3f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )
    st.info(
        "Os grupos são pequenos e desbalanceados. A ROC AUC de 1,000 entre "
        "mulheres pode ser consequência da amostra reduzida e não demonstra "
        "desempenho perfeito em outras populações."
    )


def pagina_sobre() -> None:
    st.subheader("Sobre o modelo")
    st.write(
        "O CardioIA compara dois classificadores supervisionados e seleciona a "
        "Regressão Logística por desempenho na validação cruzada. O front treina "
        "uma cópia desse modelo com toda a base para permitir simulações."
    )

    st.markdown(
        """
        #### Limitações principais

        - Base Cleveland com 303 registros de uma única instituição.
        - Dados coletados na década de 1980 e sem representatividade brasileira.
        - Distribuição desigual entre sexos e ausência de informação étnico-racial.
        - Variável-alvo simplificada para presença ou ausência de doença.
        - Não houve validação clínica, prospectiva ou externa.
        - As modalidades textual e visual não são combinadas com este modelo.

        #### Privacidade

        O formulário não envia informações para uma API própria nem armazena os
        valores preenchidos. Ainda assim, use apenas dados fictícios ou exemplos
        e nunca forneça identificadores pessoais.
        """
    )


def main() -> None:
    aplicar_estilo()
    st.markdown(
        """
        <div class="hero">
            <div class="academic-badge">Protótipo acadêmico • Fase 2</div>
            <h1>CardioIA</h1>
            <p>
                Uma demonstração transparente de Machine Learning aplicado a
                dados cardiovasculares tabulares.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.error(
        "Uso exclusivamente educacional. Este protótipo não realiza diagnóstico "
        "e não substitui avaliação médica."
    )

    aba_simulacao, aba_desempenho, aba_sobre = st.tabs(
        ["Simulação", "Desempenho", "Metodologia e limitações"]
    )

    with aba_simulacao:
        registro = criar_formulario()
        if registro is not None:
            mostrar_resultado(registro)

    with aba_desempenho:
        pagina_desempenho()

    with aba_sobre:
        pagina_sobre()


if __name__ == "__main__":
    main()
