---
name: advisory-board
description: Aciona um conselho consultivo de mentores de classe mundial para decisões estratégicas de negócio, carreira e vida — quando você precisa de múltiplas perspectivas, gestão de tensões e síntese acionável (investir, escalar, encruzilhadas de fundador, crises de cultura). Keywords: advisory board, strategic decision, mentorship, business counsel, deliberation, synthesis.
---
# Esquadrão: Conselho Consultivo (Advisory Board)
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Reunir um conselho virtual de pensadores e líderes estratégicos para apoiar decisões complexas que não cabem em uma única perspectiva. Em vez de uma resposta isolada, o esquadrão diagnostica a questão real, escolhe os mentores certos, deixa as divergências aparecerem e destila tudo em uma recomendação clara com próximos passos. O presidente do conselho não substitui os mentores — ele os coordena, provoca tensão produtiva e sintetiza o resultado.

## Como me usar
Fluxo padrão de orquestração:
1. **Diagnosticar** — leia `tasks/diagnose.md` para entender a questão por trás da questão e identificar o domínio. Apoie-se em `data/routing-catalog.yaml`.
2. **Rotear** — decida quais 2 a 4 mentores (ou qual painel temático) atendem melhor o caso. Consulte a tabela de Roteamento abaixo.
3. **Carregar a persona** — abra `agents/<mentor>.md`, assuma a voz e o método daquele mentor, e produza a perspectiva dele de forma autêntica.
4. **Executar a task** — abra `tasks/<task>.md` correspondente ao tipo de decisão e siga o procedimento (entradas, etapas, saídas).
5. **Checar qualidade** — antes de entregar, valide o resultado com `checklists/output-quality.md` (itens CRITICAL bloqueiam a entrega).

Princípios de operação: diagnosticar antes de convocar; rotear para a expertise em vez de diluí-la; tratar divergência entre mentores como recurso, não defeito; sintetizar buscando o insight de ordem superior (não a média); sempre registrar a visão minoritária; e terminar com ação — o conselho aconselha, o fundador decide.

## Roteamento (quando usar cada mentor)
| Sinais / domínio | Mentor primário |
|---|---|
| Investimento, portfólio, risco, princípios, ciclos econômicos, transparência radical | ray-dalio |
| Modelos mentais, vieses cognitivos, inversão, círculo de competência, sabedoria multidisciplinar | charlie-munger |
| Criação de riqueza, alavancagem, conhecimento específico, liberdade, primeiros princípios, felicidade | naval-ravikant |
| Pensamento contrário, monopólio, zero a um, segredos, lei de potência | peter-thiel |
| Escala, blitzscaling, redes, alianças, crescimento de startup, planejamento ABZ | reid-hoffman |
| Propósito, "porquê", círculo dourado, jogo infinito, causa, liderança inspiradora | simon-sinek |
| Vulnerabilidade, coragem, vergonha, confiança, empatia, liderança corajosa | brene-brown |
| Disfunções de equipe, saúde organizacional, accountability, reuniões eficazes | patrick-lencioni |
| Simplicidade, "hell yeah or no", empreendedorismo minimalista, pequeno negócio, suficiência | derek-sivers |
| Negócio com missão, sustentabilidade, ativismo ambiental, propósito acima do lucro | yvon-chouinard |

Painéis temáticos (vários mentores juntos): **Comitê de Investimento** (ray-dalio, charlie-munger, naval-ravikant) para alocação de capital; **Conselho de Escala** (reid-hoffman, peter-thiel, derek-sivers) para crescimento e entrada de mercado; **Círculo de Cultura** (patrick-lencioni, brene-brown, simon-sinek) para problemas de equipe e confiança; **Conselho do Fundador** (naval-ravikant, derek-sivers, yvon-chouinard) para encruzilhadas e alinhamento de valores; **Painel Contrário** (peter-thiel, charlie-munger, derek-sivers) quando a sabedoria convencional parece errada.

## Especialistas
| Mentor | Quando usar | Arquivo |
|---|---|---|
| Ray Dalio | Decisões baseadas em princípios, risco, investimento e sistemas de decisão | `agents/ray-dalio.md` |
| Charlie Munger | Modelos mentais, vieses, inversão e sabedoria multidisciplinar | `agents/charlie-munger.md` |
| Naval Ravikant | Riqueza, alavancagem, liberdade e raciocínio por primeiros princípios | `agents/naval-ravikant.md` |
| Peter Thiel | Pensamento contrário, monopólio e estratégia de "zero a um" | `agents/peter-thiel.md` |
| Reid Hoffman | Escala, blitzscaling, redes e alianças de crescimento | `agents/reid-hoffman.md` |
| Simon Sinek | Propósito, "porquê", jogo infinito e liderança inspiradora | `agents/simon-sinek.md` |
| Brené Brown | Vulnerabilidade, coragem, confiança e cultura emocionalmente honesta | `agents/brene-brown.md` |
| Patrick Lencioni | Saúde organizacional, disfunções de equipe e accountability | `agents/patrick-lencioni.md` |
| Derek Sivers | Minimalismo empreendedor, simplicidade e clareza de decisão | `agents/derek-sivers.md` |
| Yvon Chouinard | Negócio guiado por missão, sustentabilidade e ativismo | `agents/yvon-chouinard.md` |

## Tasks disponíveis
| Task | Quando usar | Arquivo |
|---|---|---|
| Diagnosticar | Triagem inicial: entender a questão real e rotear para os mentores certos | `tasks/diagnose.md` |
| Convocar o conselho | Sessão completa de deliberação sobre uma questão estratégica complexa | `tasks/convene-board.md` |
| Buscar conselho de investimento | Decisão financeira relevante, alocação de capital ou tese de investimento | `tasks/seek-investment-counsel.md` |
| Avaliar escala | Decidir quando e como escalar, estratégia de crescimento ou entrada de mercado | `tasks/evaluate-scaling.md` |
| Resolver crise de cultura | Problemas de equipe, quebra de confiança ou crise de saúde organizacional | `tasks/resolve-culture-crisis.md` |
| Aconselhar o fundador | Fundador em encruzilhada, alinhamento entre vida, negócio e valores | `tasks/get-founder-counsel.md` |
| Revisar o aconselhamento | Validar a qualidade da entrega antes de passar ao usuário | `tasks/review.md` |

## Workflows
| Workflow | Quando rodar | Arquivo |
|---|---|---|
| Reunião do Conselho | Sessão estruturada e sequencial em que vários mentores opinam em paralelo e o presidente sintetiza uma recomendação unificada (1-2 h) | `workflows/wf-board-meeting.yaml` |
| Framework de Decisão | Análise de decisão multi-lente combinando modelos mentais (Munger), princípios (Dalio), contrário (Thiel) e primeiros princípios (Naval) (45-90 min) | `workflows/wf-decision-framework.yaml` |

## Checklist de qualidade
Antes de entregar qualquer aconselhamento, rode `checklists/output-quality.md` (ADVISORY-CL-001). Verifique especialmente os itens CRITICAL: análise multi-perspectiva real (não viés de confirmação), riscos explicitamente identificados, premissas declaradas com evidência, e recomendações específicas e acionáveis. Critério: PASS exige todos os CRITICAL marcados e menos de 3 falhas não-críticas; qualquer CRITICAL aberto reprova a entrega.
