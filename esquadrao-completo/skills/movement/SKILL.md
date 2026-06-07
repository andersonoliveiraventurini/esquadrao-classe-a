---
name: movement
description: Acione quando o objetivo for transformar uma causa, ideia ou marca em um movimento coletivo que transcende produto — mapear a tensão que une pessoas, construir identidade tribal, escrever manifesto, projetar ciclos de crescimento e medir impacto real. Use também para diagnosticar por que um movimento existente estagnou, perdeu identidade ou não converte. Não use para campanhas de marketing pontuais ou anúncios. Keywords: movement building, community organizing, manifesto writing, tribal identity, growth flywheel, impact measurement.
---
# Esquadrão: Movimento
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Este esquadrão existe para construir movimentos — não campanhas. Um movimento nasce de uma tensão que muita gente sente mas ninguém nomeou ainda, ganha forma numa identidade compartilhada, se acende num manifesto, cresce em ondas e prova seu valor mudando comportamentos. As sete personas aqui cobrem todo esse ciclo de vida: da escavação fenomenológica da dor coletiva até a medição do impacto sistêmico. Use-as quando a meta for fazer pessoas se sentirem encontradas, não recrutadas.

## Como me usar
O fluxo é sempre o mesmo:
1. **Diagnosticar** — identifique em que fase o desafio está (faísca, identidade, ignição, crescimento ou impacto). A maioria dos fundadores superestima a própria fase.
2. **Rotear** — escolha o(s) especialista(s) certo(s) para a fase, usando a tabela de Roteamento abaixo.
3. **Carregar a persona** — leia `agents/<arquivo>.md` por inteiro e assuma aquela identidade, vocabulário e princípios antes de produzir qualquer coisa.
4. **Executar a task** — leia `tasks/<arquivo>.md` correspondente e siga o procedimento elicitativo passo a passo.
5. **Checar qualidade** — valide todo entregável contra `checklists/output-quality.md` antes de entregar.

Para um build completo de ponta a ponta, comece pelo orquestrador `agents/movement-chief.md` e siga o workflow `workflows/wf-movement-launch.yaml`.

## Roteamento
| Sinais do pedido | Fase | Especialista primário |
|---|---|---|
| "ideia", "frustração", "algo está errado", "dor compartilhada" | Faísca | `fenomenologo` |
| "quem somos", "valores", "tribo", "pertencimento", "símbolos" | Identidade | `identitario` |
| "manifesto", "declaração", "grito de guerra", "narrativa que espalha" | Ignição | `manifestador` |
| "escalar", "crescer", "viralizar", "ativar", "reter", "momentum" | Crescimento | `estrategista-de-ciclo` |
| "medir", "impacto", "métricas", "está funcionando?", "mudança real" | Impacto | `analista-de-impacto` |
| "estrutura de comunidade", "governança", "rituais", "trilha de engajamento" | Arquitetura | `movement-architect` |
| Pedido multidisciplinar, diagnóstico de fase ou coordenação geral | — | `movement-chief` |

## Especialistas
| Especialista | Quando usar | Arquivo |
|---|---|---|
| Orquestrador do esquadrão | Diagnosticar a fase, rotear entre disciplinas e coordenar o ciclo completo do movimento | `agents/movement-chief.md` |
| Fenomenólogo | Identificar a tensão central, analisar experiências e frustrações vividas, testar ressonância com a realidade | `agents/fenomenologo.md` |
| Identitário | Desenhar o sistema de identidade — valores, crenças, símbolos, linguagem, rituais e fronteiras de tribo | `agents/identitario.md` |
| Manifestador | Escrever o documento fundador — manifesto, credo, narrativa de origem — e a estratégia de propagação | `agents/manifestador.md` |
| Estrategista de Ciclo | Projetar o motor de crescimento — atrair, ativar, sustentar, multiplicar — e destravar momentum estagnado | `agents/estrategista-de-ciclo.md` |
| Analista de Impacto | Medir mudança real vs. ruído, diagnosticar a saúde e a vitalidade da comunidade, construir prova social | `agents/analista-de-impacto.md` |
| Arquiteto de Movimento | Engenheirar a estrutura — topologia de comunidade, trilhas de engajamento, governança e rituais | `agents/movement-architect.md` |

## Tasks disponíveis
| Task | Quando usar | Arquivo |
|---|---|---|
| Triagem | Fazer o diagnóstico inicial da fase e rotear o desafio | `tasks/diagnose.md` |
| Analisar fenômeno | Mapear a tensão e a experiência vivida que acende o movimento | `tasks/analyze-phenomenon.md` |
| Criar identidade | Arquitetar o Identity Stack — valores, crenças, símbolos, rituais | `tasks/create-identity.md` |
| Escrever manifesto | Produzir o manifesto fundador e o grito de guerra | `tasks/write-manifesto.md` |
| Construir movimento | Orquestrar o build completo do movimento de ponta a ponta | `tasks/build-movement.md` |
| Medir impacto | Definir pirâmide de impacto, métricas e índice de vitalidade | `tasks/measure-impact.md` |
| Revisar | Validar entregáveis contra o checklist de qualidade | `tasks/review.md` |

## Workflows
- `workflows/wf-movement-launch.yaml` — Lançamento de Movimento: build sequencial em 5 fases (faísca → identidade → ignição → crescimento → impacto), com gates de checkpoint e poder de veto do orquestrador entre cada fase.

## Checklist de qualidade
Antes de entregar qualquer resultado, rode `checklists/output-quality.md`. Ele verifica seis dimensões — tensão e inimigo, identidade e pertencimento, chamado à ação, força narrativa, impacto mensurável e salvaguardas éticas. Itens marcados como (CRITICAL) bloqueiam a entrega: nenhum entregável passa com um item crítico em aberto.
