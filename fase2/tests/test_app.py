"""Teste funcional do front: abre a aplicação e executa uma simulação."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


CAMINHO_APP = Path(__file__).resolve().parents[1] / "app.py"

app = AppTest.from_file(str(CAMINHO_APP))
app.run(timeout=60)

if app.exception:
    raise AssertionError(f"Erro ao abrir o front: {app.exception}")

botoes = [
    botao
    for botao in app.button
    if botao.label == "Executar simulação"
]
if len(botoes) != 1:
    raise AssertionError(
        "O botão 'Executar simulação' não foi encontrado de forma única."
    )

botoes[0].click()
app.run(timeout=120)

if app.exception:
    mensagens = [str(excecao.value) for excecao in app.exception]
    raise AssertionError(
        "A simulação gerou uma exceção: " + " | ".join(mensagens)
    )

subtitulos = [str(item.value) for item in app.subheader]
if "Resultado da simulação" not in subtitulos:
    raise AssertionError("A seção de resultado não apareceu após a simulação.")

print("Front aberto e simulação executada com sucesso.")
