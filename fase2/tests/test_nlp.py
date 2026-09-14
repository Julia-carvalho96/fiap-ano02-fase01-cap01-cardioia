"""Testes funcionais dos entregáveis obrigatórios de NLP da Fase 2."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


DIRETORIO_FASE2 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DIRETORIO_FASE2 / "src"))

from classificar_risco_texto import (  # noqa: E402
    analisar_vies_contrafactual,
    carregar_dataset,
    dividir_por_cenario,
    treinar_e_avaliar,
)
from extrair_sintomas import (  # noqa: E402
    analisar_arquivo,
    analisar_relato,
    carregar_mapa,
    carregar_relatos,
    normalizar_texto,
)


def testar_dados_extracao() -> None:
    relatos = carregar_relatos()
    mapa = carregar_mapa()
    assert len(relatos) == 10, "O arquivo deve conter exatamente 10 relatos."
    assert len(mapa) >= 20, "O mapa de conhecimento deve ter pelo menos 20 linhas."
    assert len(set(relatos)) == 10, "Os relatos devem ser únicos."
    assert all(len(relato.split()) >= 12 for relato in relatos), (
        "Os relatos precisam trazer contexto suficiente."
    )

    resultados = analisar_arquivo()
    assert len(resultados) == 10
    assert all(item["encontrou_correspondencia"] for item in resultados), (
        "Todos os relatos demonstrativos devem produzir alguma associação."
    )
    assert all(item["sintomas_identificados"] for item in resultados)

    normalizado = normalizar_texto("DOR no TÓRAX!!!")
    assert normalizado == "dor no torax"
    exemplo = analisar_relato(
        "Desde ontem sinto APERTO no TÓRAX e suor frio.",
        mapa,
    )
    assert exemplo["encontrou_correspondencia"]
    assert any(
        item["doenca_associada"] == "Síndrome coronariana aguda"
        for item in exemplo["hipoteses_associadas"]
    )
    sem_correspondencia = analisar_relato(
        "Estou com uma pequena coceira no dedo.",
        mapa,
    )
    assert not sem_correspondencia["encontrou_correspondencia"]


def testar_dataset_textual() -> pd.DataFrame:
    dados = carregar_dataset()
    assert len(dados) >= 100, "A base textual deve ter pelo menos 100 frases."
    assert dados["id_cenario"].nunique() >= 50
    assert dados["frase"].nunique() == len(dados)
    assert not dados.isna().any().any()
    assert set(dados["sexo_referencia"]) == {"feminino", "masculino"}

    contagem = dados["situacao"].value_counts()
    assert contagem["alto risco"] == contagem["baixo risco"], (
        "As classes simuladas devem estar balanceadas."
    )
    tamanhos_pares = dados.groupby("id_cenario")["sexo_referencia"].nunique()
    assert tamanhos_pares.eq(2).all(), (
        "Cada cenário deve ter versões feminina e masculina."
    )

    treino, teste = dividir_por_cenario(dados)
    assert not set(treino["id_cenario"]).intersection(teste["id_cenario"])
    assert len(treino) + len(teste) == len(dados)
    return dados


def testar_classificador() -> None:
    (
        modelo,
        treino,
        teste,
        metricas,
        previsoes,
        vies,
        pares,
    ) = treinar_e_avaliar()

    assert metricas["n_treino"] == len(treino)
    assert metricas["n_teste"] == len(teste)
    assert metricas["acuracia"] >= 0.75
    assert metricas["recall_alto_risco"] >= 0.75
    assert metricas["f1_alto_risco"] >= 0.75
    assert 0.0 <= metricas["roc_auc"] <= 1.0
    assert len(previsoes) == len(teste)
    assert set(modelo.named_steps) == {"tfidf", "modelo"}

    resumo_recalculado, pares_recalculados = analisar_vies_contrafactual(
        modelo,
        teste,
    )
    assert resumo_recalculado == vies
    assert len(pares_recalculados) == len(pares)
    assert vies["maior_diferenca_absoluta"] <= 0.10, (
        "O marcador de sexo alterou excessivamente relatos equivalentes."
    )


def main() -> None:
    testar_dados_extracao()
    testar_dataset_textual()
    testar_classificador()
    print("Entregáveis de NLP, classificador e teste de viés validados.")


if __name__ == "__main__":
    main()
