# Resultados iniciais

Execução de referência do baseline tabular em 14/09/2026, com Python 3.12 e semente aleatória 42.

- Workflow: [Validar baseline da Fase 2 — execução 2](https://github.com/murilosalla-blip/fiap-ano02-fase01-cap01-cardioia/actions/runs/34859060589)
- Critério de escolha: maior ROC AUC média na validação cruzada estratificada do conjunto de treino.
- Modelo selecionado: Regressão Logística.

## Validação cruzada no treino

| Modelo | Acurácia | Precisão | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Regressão Logística | 0,847 ± 0,025 | 0,848 ± 0,062 | 0,819 ± 0,057 | 0,831 ± 0,025 | 0,907 ± 0,020 |
| Random Forest | 0,801 ± 0,029 | 0,786 ± 0,064 | 0,792 ± 0,090 | 0,784 ± 0,036 | 0,900 ± 0,034 |

Os valores representam média ± desvio-padrão em cinco folds. A diferença de ROC AUC entre os modelos é pequena e não deve ser interpretada, isoladamente, como evidência de superioridade definitiva.

## Avaliação no teste

O conjunto de teste contém 61 pacientes, dos quais 28 têm o diagnóstico classificado como presente.

| Métrica | Resultado |
|---|---:|
| Acurácia | 0,869 |
| Precisão | 0,813 |
| Recall/sensibilidade | 0,929 |
| F1 | 0,867 |
| ROC AUC | 0,958 |
| Taxa de falso positivo | 0,182 |
| Taxa de falso negativo | 0,071 |

O recall elevado indica que o baseline identificou a maior parte dos casos positivos deste teste. Como o conjunto contém apenas 61 pacientes, as métricas ainda têm incerteza relevante e não sustentam uso clínico.

## Avaliação por sexo

| Sexo | n | Positivos | Acurácia | Precisão | Recall | F1 | ROC AUC | Falso positivo | Falso negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Feminino | 20 | 7 | 0,950 | 1,000 | 0,857 | 0,923 | 1,000 | 0,000 | 0,143 |
| Masculino | 41 | 21 | 0,829 | 0,769 | 0,952 | 0,851 | 0,938 | 0,300 | 0,048 |

Essas diferenças são descritivas. O subgrupo feminino tem somente 20 pessoas e 7 casos positivos; portanto, valores extremos como ROC AUC igual a 1,000 podem refletir a pequena amostra. Antes de afirmar desempenho desigual ou equidade, será necessário calcular intervalos de confiança e avaliar a estabilidade em reamostragens.

## Próximas análises

1. Adicionar intervalos de confiança por bootstrap para as métricas gerais e por sexo.
2. Examinar matriz de confusão, curva ROC e curva precisão-recall.
3. Avaliar calibração das probabilidades.
4. Interpretar os coeficientes da Regressão Logística e conferir estabilidade das variáveis.
5. Confrontar este baseline com os requisitos completos do enunciado antes de ampliar a busca de hiperparâmetros.
