# Resultados da Fase 2

Execução de referência do baseline tabular em 14/09/2026, com Python 3.12 e semente aleatória 42.

- **Workflow validado:** https://github.com/murilosalla-blip/fiap-ano02-fase01-cap01-cardioia/actions/runs/34884026533
- **Critério de escolha:** maior ROC AUC média na validação cruzada estratificada do treino.
- **Modelo selecionado:** Regressão Logística.
- **Aplicação publicada:** https://cardioia-fiap.streamlit.app/

## Validação cruzada no treino

| Modelo | Acurácia | Precisão | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Regressão Logística | 0,847 ± 0,025 | 0,848 ± 0,062 | 0,819 ± 0,057 | 0,831 ± 0,025 | 0,907 ± 0,020 |
| Random Forest | 0,801 ± 0,029 | 0,786 ± 0,064 | 0,792 ± 0,090 | 0,784 ± 0,036 | 0,900 ± 0,034 |

Os valores representam média ± desvio-padrão em cinco folds. A diferença de ROC AUC é pequena e não deve ser interpretada isoladamente como superioridade definitiva.

## Avaliação no teste

O conjunto de teste contém 61 pacientes, dos quais 28 têm o desfecho classificado como presente.

| Métrica | Resultado |
|---|---:|
| Acurácia | 0,869 |
| Precisão | 0,813 |
| Recall/sensibilidade | 0,929 |
| F1 | 0,867 |
| ROC AUC | 0,958 |
| Taxa de falso positivo | 0,182 |
| Taxa de falso negativo | 0,071 |

O recall elevado indica que o baseline identificou a maior parte dos casos positivos deste teste. A amostra de teste é pequena e não sustenta uso clínico.

## Avaliação por sexo

| Sexo | n | Positivos | Acurácia | Precisão | Recall | F1 | ROC AUC | Falso positivo | Falso negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Feminino | 20 | 7 | 0,950 | 1,000 | 0,857 | 0,923 | 1,000 | 0,000 | 0,143 |
| Masculino | 41 | 21 | 0,829 | 0,769 | 0,952 | 0,851 | 0,938 | 0,300 | 0,048 |

Essas diferenças são descritivas. O subgrupo feminino tem somente 20 pessoas e 7 casos positivos; valores extremos podem refletir a amostra reduzida.

## Análises complementares concluídas

O script `fase2/src/analisar_modelo.py` produz:

- intervalos de confiança de 95% por bootstrap, com 2.000 reamostragens;
- matriz de confusão;
- curva ROC;
- curva precisão-recall;
- curva de calibração;
- distribuição do alvo por sexo;
- importância das variáveis da Regressão Logística;
- tabelas de métricas gerais e por sexo.

As saídas são recriadas em `fase2/resultados/` pelo workflow e pela execução local. O workflow verifica automaticamente se cada arquivo obrigatório foi produzido.

## Auditoria das simulações

Foi incluído um teste específico para resultados aparentemente contraintuitivos no front. Em um perfil aproximado ao preenchimento discutido durante a validação, foram observadas as seguintes estimativas:

| Cenário sintético | Estimativa |
|---|---:|
| Angina típica e alterações iniciais | 1,79% |
| Com angina induzida por exercício | 3,65% |
| Com maior alteração de ST e inclinação plana | 14,36% |
| Com dois vasos e defeito reversível no thal | 85,95% |
| Mesmo cenário com categoria assintomática da UCI | 97,20% |

A auditoria confirmou que o cálculo estava correto, mas evidenciou a necessidade de melhorar sua interpretação. O front agora apresenta o desfecho específico, os fatores que aumentaram ou reduziram a estimativa e os avisos de imputação.

Na amostra histórica, o desfecho positivo ocorreu em 30,4% dos 23 registros com angina típica e em 72,9% dos 144 registros classificados como assintomáticos. Essa associação da base não representa uma regra clínica ou relação causal.

## Arquivos gerados

- `metricas_validacao_cruzada.csv`;
- `metricas_teste.csv`;
- `metricas_por_sexo.csv`;
- `intervalos_confianca_bootstrap.csv`;
- `previsoes_teste.csv`;
- `importancia_variaveis.csv`;
- `metadados_execucao.json`;
- `melhor_modelo.joblib`;
- `analise_baseline_executada.ipynb`;
- gráficos de confusão, ROC, precisão-recall, calibração, distribuição por sexo e importância.

## Interpretação responsável

O percentual exibido pelo protótipo corresponde ao desfecho binário definido na base Cleveland. Ele não representa risco cardiovascular geral, risco de infarto ou diagnóstico individual. O projeto não possui validação clínica, prospectiva ou externa.
