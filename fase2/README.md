# Fase 2 — Machine Learning

Esta pasta inicia a etapa de Machine Learning do CardioIA usando exclusivamente a modalidade numérica da base Cleveland preparada na Fase 1.

## Objetivo inicial

Construir e comparar classificadores supervisionados para estimar a presença de doença cardíaca a partir das 13 variáveis clínicas. O resultado é acadêmico e exploratório e não deve ser usado para diagnóstico ou decisão clínica.

## Protocolo experimental

1. Carregar o arquivo `assets/dados/processed/heart_disease_cleveland.csv`.
2. Separar atributos e variável-alvo antes de qualquer ajuste de pré-processamento.
3. Fazer divisão estratificada de 80% para treino e 20% para teste, com `random_state=42`.
4. Ajustar imputação, codificação e padronização somente com os dados de treino por meio de `Pipeline`, evitando vazamento de dados.
5. Comparar Regressão Logística e Random Forest com validação cruzada estratificada no treino.
6. Avaliar uma única vez no teste com acurácia, precisão, recall, F1 e ROC AUC.
7. Calcular as mesmas métricas separadamente para os grupos feminino e masculino, registrando também o tamanho de cada subgrupo.
8. Salvar métricas e previsões em `fase2/resultados/` para permitir auditoria.

## Decisões relacionadas ao feedback da Fase 1

- **Avaliação demográfica:** o desempenho será reportado separadamente por sexo, além das métricas gerais. Diferenças serão descritas com cautela porque a base Cleveland é pequena e demograficamente limitada.
- **Separação por indivíduo:** a base tabular contém uma linha por paciente, portanto a divisão é feita no nível do paciente. Caso outra fonte traga múltiplos exames por indivíduo, a divisão deverá ser feita por identificador de paciente com grupos exclusivos entre treino e teste.
- **Prevalência:** a amostra visual balanceada da Fase 1 não será usada para inferir prevalência.
- **Modalidades independentes:** dados numéricos, textuais e visuais permanecem independentes. Este primeiro experimento usa somente os dados numéricos e não realiza fusão multimodal.
- **Reprodutibilidade:** sementes aleatórias, configuração dos modelos, métricas e previsões ficam registradas.

## Estrutura inicial

```text
fase2/
├── README.md
├── requirements.txt
├── src/
│   └── treinar_baselines.py
└── resultados/              # criada automaticamente ao executar
```

## Como executar

Na raiz do repositório:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r fase2/requirements.txt
python fase2/src/treinar_baselines.py
```

No Windows, a ativação do ambiente virtual pode ser feita com:

```powershell
.venv\Scripts\activate
```

## Saídas esperadas

- `fase2/resultados/metricas_validacao_cruzada.csv`
- `fase2/resultados/metricas_teste.csv`
- `fase2/resultados/metricas_por_sexo.csv`
- `fase2/resultados/previsoes_teste.csv`

A próxima etapa é executar o pipeline, interpretar os resultados e então refinar o modelo conforme os requisitos completos do enunciado da Fase 2.
