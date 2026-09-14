# Fase 2 — Machine Learning

Esta pasta reúne a etapa de Machine Learning do CardioIA, construída exclusivamente com a modalidade numérica da base Heart Disease — Cleveland preparada na Fase 1.

> **Uso exclusivamente educacional.** O projeto não realiza diagnóstico, não estima risco clínico real e não substitui avaliação médica.

## Aplicação publicada

- **CardioIA:** https://cardioia-fiap.streamlit.app/
- **Arquivo principal:** `fase2/app.py`
- **Branch:** `fase-2-machine-learning`

A aplicação possui três áreas:

1. **Simulação:** formulário com as 13 variáveis e estimativa produzida pelo modelo.
2. **Desempenho:** métricas gerais e avaliação descritiva separada por sexo.
3. **Metodologia e limitações:** origem dos dados, decisões experimentais e cuidados de interpretação.

A tela informa o desfecho específico da base, diferencia classe matemática de interpretação clínica, mostra os fatores que aumentaram ou reduziram cada estimativa e alerta quando valores ausentes foram preenchidos automaticamente.

## Objetivo

Construir e comparar classificadores supervisionados para estimar a presença do desfecho registrado na base Cleveland: estreitamento angiográfico superior a 50%. O resultado é acadêmico e exploratório.

## Estado da entrega

- pipeline de pré-processamento e treinamento concluído;
- comparação entre Regressão Logística e Random Forest concluída;
- validação cruzada e seleção do modelo concluídas;
- avaliação geral e separada por sexo concluída;
- intervalos de confiança por bootstrap concluídos;
- matriz de confusão, curvas ROC e precisão-recall concluídas;
- análise de calibração e interpretação das variáveis concluídas;
- notebook narrado e executável concluído;
- front acadêmico publicado em Streamlit;
- testes funcionais e auditoria de cenários automatizados;
- workflow de validação executado com sucesso.

Não fazem parte do escopo desta fase: API independente, autenticação, armazenamento de simulações e fusão com as modalidades textual ou visual.

## Resultados principais

O conjunto de teste estratificado contém 61 pacientes, sendo 28 com desfecho positivo.

| Métrica | Resultado |
|---|---:|
| Acurácia | 86,9% |
| Precisão | 81,3% |
| Sensibilidade/recall | 92,9% |
| F1 | 86,7% |
| ROC AUC | 0,958 |

A Regressão Logística foi selecionada pela maior ROC AUC média na validação cruzada do conjunto de treino. A diferença em relação ao Random Forest foi pequena e não demonstra superioridade universal.

### Avaliação descritiva por sexo

| Sexo | n | Positivos | Acurácia | Precisão | Sensibilidade | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| Feminino | 20 | 7 | 95,0% | 100,0% | 85,7% | 92,3% | 1,000 |
| Masculino | 41 | 21 | 82,9% | 76,9% | 95,2% | 85,1% | 0,938 |

Os grupos são pequenos e desbalanceados. As diferenças são apenas descritivas e não sustentam conclusões de equidade ou desempenho clínico.

## Protocolo experimental

1. Carregar `assets/dados/processed/heart_disease_cleveland.csv`.
2. Separar atributos e alvo antes de ajustar qualquer transformação.
3. Fazer divisão estratificada de 80% para treino e 20% para teste, com semente 42.
4. Ajustar imputação, codificação e padronização somente dentro do treino por meio de `Pipeline`.
5. Comparar Regressão Logística e Random Forest com validação cruzada estratificada em cinco folds.
6. Selecionar o modelo pela ROC AUC média da validação, sem consultar o teste.
7. Avaliar uma única vez no teste com acurácia, precisão, recall, F1 e ROC AUC.
8. Avaliar as mesmas métricas separadamente para os grupos feminino e masculino.
9. Estimar intervalos de confiança de 95% com 2.000 reamostragens bootstrap.
10. Examinar discriminação, calibração e influência das variáveis.
11. Treinar uma cópia da Regressão Logística com toda a base exclusivamente para o front.

## Pré-processamento

- Campos numéricos ausentes: imputação pela mediana do conjunto de treino.
- Campos categóricos ausentes: imputação pela categoria mais frequente no treino.
- Campos categóricos: codificação one-hot.
- Campos numéricos: padronização.
- Todas as transformações ficam dentro do pipeline para evitar vazamento de dados.

## Decisões relacionadas ao feedback da Fase 1

- **Avaliação demográfica:** desempenho reportado separadamente por sexo e interpretado com cautela.
- **Separação por indivíduo:** a base tabular possui uma linha por paciente, permitindo divisão no nível do paciente.
- **Prevalência:** a amostra visual balanceada da Fase 1 não é usada para inferir prevalência.
- **Modalidades independentes:** somente os dados numéricos são utilizados nesta fase.
- **Reprodutibilidade:** sementes, configurações, métricas e previsões são registradas durante a execução.

## Estrutura

```text
fase2/
├── app.py
├── README.md
├── requirements.txt
├── notebooks/
│   └── analise_baseline.ipynb
├── src/
│   ├── analisar_modelo.py
│   └── treinar_baselines.py
├── tests/
│   ├── auditar_cenarios.py
│   └── test_app.py
└── resultados/
    └── README.md
```

Os scripts geram métricas, previsões, gráficos, modelo serializado e uma cópia executada do notebook dentro de `fase2/resultados/`.

## Como executar

Pré-requisito: Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r fase2/requirements.txt
python fase2/src/treinar_baselines.py
python fase2/src/analisar_modelo.py
streamlit run fase2/app.py
```

No Windows, use `.venv\Scripts\activate` para ativar o ambiente.

Para executar o notebook integralmente:

```bash
jupyter nbconvert --to notebook --execute fase2/notebooks/analise_baseline.ipynb --output-dir fase2/resultados --output analise_baseline_executada.ipynb
```

## Validação automática

O workflow `.github/workflows/fase2-baseline.yml`:

- verifica a sintaxe;
- testa a inicialização do Streamlit;
- executa uma simulação completa;
- audita cenários sintéticos;
- treina e avalia os modelos;
- executa as análises e o notebook;
- confere todas as saídas obrigatórias.

## Limitações

- apenas 303 registros de uma única instituição;
- dados coletados nos Estados Unidos na década de 1980;
- ausência de representatividade brasileira;
- distribuição desigual entre os sexos;
- avaliação por sexo baseada em subgrupos pequenos;
- ausência de validação clínica, prospectiva e externa;
- probabilidades não devem ser interpretadas como risco individual;
- valores ausentes imputados adicionam incerteza;
- associações aprendidas pelo modelo não demonstram causalidade.

## Privacidade

O front não utiliza API própria nem banco de dados e não armazena os valores preenchidos. A interface orienta o uso exclusivo de dados fictícios e proíbe informações identificáveis.
