# Roteiros dos vídeos — Fase 2 CardioIA

Os roteiros abaixo foram desenhados para manter cada demonstração abaixo de **4 minutos**. Grave a tela em 1080p, aumente o zoom do navegador para facilitar a leitura e não apresente o projeto como ferramenta diagnóstica.

## Vídeo 1 — entrega obrigatória de NLP (3min40s)

| Tempo | Tela | Fala sugerida |
|---|---|---|
| 0:00–0:20 | README da Fase 2 | “Este é o CardioIA do Grupo Aura. Nesta fase construímos uma solução de NLP para extrair sintomas de relatos e classificar risco textual simulado.” |
| 0:20–0:50 | `dados/relatos_sintomas.txt` e `mapa_conhecimento.csv` | “Criamos dez relatos completos e um mapa de conhecimento em CSV que relaciona expressões de sintomas a possíveis doenças.” |
| 0:50–1:25 | `extrair_sintomas.py` e resultado | “O extrator normaliza acentos, caixa e pontuação, encontra os termos do mapa e agrega as correspondências por relato.” |
| 1:25–2:10 | `classificacao_risco.csv` e notebook | “A base de risco tem 120 frases únicas, balanceadas entre alto e baixo risco. Usamos TF-IDF com unigramas e bigramas e Regressão Logística.” |
| 2:10–2:45 | métricas e matriz de confusão | “A divisão é estratificada e agrupada pelo cenário para impedir versões semelhantes no treino e no teste. O teste teve 24 frases e acurácia de 100%.” |
| 2:45–3:10 | análise contrafactual | “Também comparamos versões feminina e masculina dos mesmos cenários. A maior diferença de probabilidade foi de aproximadamente 0,0033.” |
| 3:10–3:40 | aba Triagem textual do Streamlit | “Na interface podemos extrair sintomas e estimar o risco textual. Como os dados são simulados e separáveis, o resultado não demonstra validade clínica nem substitui atendimento médico.” |

## Vídeo 2 — Ir Além: portal React (3min30s)

| Tempo | Tela | Fala sugerida |
|---|---|---|
| 0:00–0:20 | README do portal | “Como primeiro Ir Além, criamos um portal médico acadêmico em React e Vite.” |
| 0:20–0:50 | tela de login | “A autenticação é simulada, gera um token local e usa Context API. Credenciais de demonstração: cardioia@fiap.com e aura2026.” |
| 0:50–1:20 | rota protegida e dashboard | “Sem autenticação, as rotas internas redirecionam para o login. Após entrar, o dashboard apresenta indicadores calculados a partir dos dados simulados.” |
| 1:20–1:55 | pacientes | “A listagem de pacientes é consumida por uma camada de serviço que simula uma API.” |
| 1:55–2:35 | agendamentos | “Nos agendamentos, o estado é controlado com reducer; podemos incluir e remover registros sem backend.” |
| 2:35–3:05 | estrutura de pastas | “O código está separado em contexts, components, services e pages, com estilos modulares e rotas protegidas.” |
| 3:05–3:30 | teste/build no GitHub Actions | “Os testes verificam proteção de rota, login válido e inválido, e o workflow também executa o build de produção.” |

## Vídeo 3 — Ir Além: classificação visual de ECG (3min35s)

| Tempo | Tela | Fala sugerida |
|---|---|---|
| 0:00–0:25 | amostra de ECGs e README | “No segundo Ir Além, formulamos uma classificação binária de ECG em normal e anormal.” |
| 0:25–0:55 | inventário dos dados | “Selecionamos 60 exames: 30 normais e 30 anormais, mantendo as classes equilibradas para o experimento.” |
| 0:55–1:30 | notebook de pré-processamento | “As imagens são convertidas para tons de cinza, redimensionadas para 64 por 64, normalizadas e transformadas em vetores.” |
| 1:30–2:00 | separação e hashes | “A separação treino/teste é estratificada e validada por hash do exame, impedindo que a mesma imagem apareça nos dois conjuntos. A fonte não fornece ID de paciente.” |
| 2:00–2:35 | arquitetura MLP | “A MLP Keras usa camadas densas, normalização em lote e dropout. A escolha do limiar usa somente a validação.” |
| 2:35–3:10 | métricas | “No teste com 12 exames, a acurácia balanceada foi 41,7% e a ROC AUC 0,667. Mantivemos esse resultado baixo para relatar honestamente a limitação da amostra.” |
| 3:10–3:35 | limitações | “O modelo é apenas uma prova de conceito educacional, sem validação clínica. Um próximo passo exigiria mais dados, identificação por paciente e validação externa.” |

## Checklist antes de publicar

- deixar cada vídeo como **não listado** no YouTube;
- confirmar duração inferior a 4 minutos;
- colocar os links no README correspondente;
- evitar nomes ou dados reais de pacientes na gravação;
- mostrar o commit/branch final e uma execução bem-sucedida dos testes;
- conferir áudio e legibilidade antes do envio.
