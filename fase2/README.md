# Fase 2 — Machine Learning

Esta pasta reúne a etapa de Machine Learning do CardioIA usando exclusivamente a modalidade numérica da base Cleveland preparada na Fase 1.

## Estado atual

Já existem:

- pipeline de pré-processamento e treinamento;
- comparação entre Regressão Logística e Random Forest;
- avaliação geral e separada por sexo;
- intervalos de confiança por bootstrap;
- matriz de confusão, curvas ROC e precisão-recall;
- análise de calibração;
- interpretação das variáveis;
- notebook narrado e validação automática.

Ainda não existem:

- front-end ou formulário para entrada de dados;
- API para servir o modelo;
- implantação pública;
- integração com as modalidades textual e visual.

## Objetivo inicial

Construir e comparar classificadores supervisionados para estimar a presença de doença cardíaca a partir das 13 variáveis clínicas. O resultado é acadêmico e exploratório e não deve ser usado para diagnóstico ou decisão clínica.

## Protocolo experimental

1. Carregar o arquivo `assets/dados/processed/heart_disease_cleveland.csv`.
2. Separar atributos e variável-alvo antes de qualquer ajuste de pré-processamento.
3. Fazer divisão estratificada de 80% para treino e 20% para teste, com `random_state=42`.
4. Ajustar imputação, codificação e padronização somente com os dados de treino por meio de `Pipeline`, evitando vazamento de dados.
5. Comparar Regressão Logística e Random Forest com validação cruzada estratificada no treino.
6. Selecionar o modelo pela maior ROC AUC média na validação cruzada, sem consultar o teste.
7. Avaliar uma única vez no teste com acurácia, precisão, recall, F1 e ROC AUC.
8. Calcular as mesmas métricas separadamente para os grupos feminino e masculino.
9. Estimar intervalos de confiança de 95% com 2.000 reamostragens bootstrap.
10. Avaliar discriminação, calibração e influência das variáveis.

## Decisões relacionadas ao feedback da Fase 1

- **Avaliação demográfica:** o desempenho é reportado separadamente por sexo, além das métricas gerais. Diferenças são descritas com cautela porque a base Cleveland é pequena e demograficamente limitada.
- **Separação por indivíduo:** a base tabular contém uma linha por paciente, portanto a divisão é feita no nível do paciente. Caso outra fonte traga múltiplos exames por indivíduo, a divisão deverá ser feita por identificador de paciente com grupos exclusivos entre treino e teste.
- **Prevalência:** a amostra visual balanceada da Fase 1 não é usada para inferir prevalência.
- **Modalidades independentes:** dados numéricos, textuais e visuais permanecem independentes. Este experimento usa somente dados numéricos e não realiza fusão multimodal.
- **Reprodutibilidade:** sementes aleatórias, configuração dos modelos, métricas e previsões ficam registradas durante a execução.

## Estrutura

```text
fase2/
├── README.md
├── requirements.txt
├── notebooks/
│   └── analise_baseline.ipynb
├── src/
│   ├── treinar_baselines.py
│   └── analisar_modelo.py
└── resultados/
    └── README.md
```

Os demais arquivos de `resultados/` são gerados ao executar o projeto e não precisam existir previamente.

## Como executar

Na raiz do repositório:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r fase2/requirements.txt
python fase2/src/treinar_baselines.py
python fase2/src/analisar_modelo.py
```

No Windows, a ativação do ambiente virtual pode ser feita com:

```powershell
.venv\Scripts\activate
```

O notebook pode ser aberto no Jupyter ou executado integralmente:

```bash
jupyter nbconvert --to notebook --execute fase2/notebooks/analise_baseline.ipynb
```

## Saídas geradas

- métricas de validação cruzada e teste;
- métricas gerais e por sexo;
- intervalos de confiança por bootstrap;
- previsões do conjunto de teste;
- modelo treinado;
- tabela de importância das variáveis;
- matriz de confusão;
- curvas ROC, precisão-recall e calibração;
- distribuição do alvo por sexo.

A inclusão de um front-end deve ser tratada como uma camada posterior de demonstração. Antes disso, é necessário confirmar os requisitos completos do enunciado e fechar a análise metodológica do modelo.
