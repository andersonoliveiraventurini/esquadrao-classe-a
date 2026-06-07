---
name: storytelling
description: Acione este esquadrão quando precisar construir, estruturar ou diagnosticar narrativas — storytelling de marca, roteiros e arcos de história, pitch, apresentações persuasivas, manifestos de movimento e desbloqueio criativo. Reúne frameworks como Jornada do Herói, Beat Sheet, Story Circle, Story Grid, Sparkline e ABT. Keywords: storytelling, narrative, screenplay, pitch, brand-story, persuasion
---
# Esquadrão: Storytelling
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Transformar ideias, marcas e causas em histórias que prendem, convencem e movem pessoas à ação. O esquadrão reúne onze tradições narrativas — da mitologia comparada ao roteiro comercial, da narrativa pessoal ao pitch de alto risco, da apresentação executiva ao manifesto de movimento — sob a coordenação de um orquestrador que diagnostica o desafio antes de prescrever qualquer framework. Você não recebe "uma fórmula": recebe a estrutura certa, no domínio certo, na escala certa.

## Como me usar
Fluxo de trabalho recomendado:
1. **Diagnosticar** — descreva o desafio narrativo (público, meio, propósito, escala). O orquestrador identifica domínio e escala antes de prescrever.
2. **Rotear** — com base no diagnóstico, escolha o especialista (ou combinação) mais adequado.
3. **Carregar a persona** — leia `agents/<especialista>.md`, assuma sua voz, princípios e vocabulário, e atue como ele.
4. **Executar a task** — leia `tasks/<task>.md` e siga suas fases, entradas/saídas e condições de veto.
5. **Checar qualidade** — valide o resultado contra `checklists/output-quality.md` antes de entregar.

Para desafios que cruzam várias tradições, use um **workflow** (`workflows/*.yaml`), que encadeia especialistas e tasks em fases com checkpoints.

## Roteamento
O orquestrador (`agents/story-chief.md`) faz o diagnóstico e o roteamento. Ele considera dois eixos:

- **Domínio narrativo:** mítico/arquetípico · estrutura de roteiro · edição de história · TV/episódico · apresentações · marca/negócio · narrativa pessoal · vendas/persuasão · improvisação · pitch · organização de movimentos · desbloqueio criativo.
- **Escala:** micro (anedota, post) · meso (apresentação, episódio) · macro (roteiro, romance) · meta (movimento, cultura).

Regra de ouro: diagnóstico antes de prescrição. Confiança ALTA roteia direto ao especialista primário; MÉDIA sugere primário + secundário; BAIXA permanece no orquestrador e faz perguntas de esclarecimento. Nunca há um framework único para tudo.

## Especialistas

| Especialista | Quando usar | Arquivo |
|--------------|-------------|---------|
| Joseph Campbell | Estrutura mítica, arquétipos, Jornada do Herói, padrões universais, transformações épicas | `agents/joseph-campbell.md` |
| Dan Harmon | Story Circle, roteiro de TV/série, arcos episódicos guiados por personagem | `agents/dan-harmon.md` |
| Blake Snyder | Beat Sheet (Save the Cat!), roteiro comercial, logline, plotagem amigável ao público | `agents/blake-snyder.md` |
| Shawn Coyne | Story Grid, edição e revisão diagnóstica, análise de cenas e value shifts | `agents/shawn-coyne.md` |
| Matthew Dicks | Narrativa pessoal, memória, vulnerabilidade, encontrar histórias verdadeiras (Storyworthy) | `agents/matthew-dicks.md` |
| Kindra Hall | Histórias de negócio que "grudam", as 4 histórias essenciais, casos e depoimentos de vendas | `agents/kindra-hall.md` |
| Nancy Duarte | Apresentações, keynotes, storytelling de dados, método Sparkline (What Is / What Could Be) | `agents/nancy-duarte.md` |
| Park Howell | Storytelling de negócio e marca, marketing narrativo, estrutura ABT (And-But-Therefore) | `agents/park-howell.md` |
| Keith Johnstone | Improvisação, espontaneidade, status, desbloqueio de bloqueios criativos | `agents/keith-johnstone.md` |
| Oren Klaff | Pitch de alto risco, controle de frame, neurofinanças, captação e fechamento (Pitch Anything) | `agents/oren-klaff.md` |
| Marshall Ganz | Narrativa pública para movimentos e mudança social, Story of Self/Us/Now, manifestos | `agents/marshall-ganz.md` |

## Tasks disponíveis

| Task | Quando usar | Arquivo |
|------|-------------|---------|
| Diagnosticar e rotear | Triar o pedido, dar resposta transversal imediata e indicar o especialista certo | `tasks/diagnose.md` |
| Construir narrativa | Montar uma estrutura completa (Jornada do Herói, Beat Sheet ou Story Circle) com beats e arco emocional | `tasks/build-narrative.md` |
| Analisar história | Diagnosticar uma história existente com Story Grid — gênero, cenas, value shifts, prescrições | `tasks/analyze-story.md` |
| Criar pitch | Estruturar narrativa de pitch (frame control de Klaff ou Sparkline de Duarte) com ask claro | `tasks/create-pitch.md` |
| Criar apresentação | Desenhar apresentação no método Sparkline, com star moment e call to action | `tasks/create-presentation.md` |
| Desbloquear criatividade | Diagnosticar e superar bloqueios criativos com exercícios de improvisação e jogos de história | `tasks/unblock-creative.md` |
| Escrever manifesto | Criar manifesto de marca/movimento com Narrativa Pública (Self, Us, Now) e grito de guerra | `tasks/write-manifesto.md` |
| Revisar saída narrativa | Avaliar o entregável do especialista contra o checklist e dar veredito (APROVAR/REVISAR/REJEITAR) | `tasks/review.md` |

## Workflows

| Workflow | Quando usar | Arquivo |
|----------|-------------|---------|
| Desenvolvimento de História | Do conceito bruto ao polimento: seleção de framework, estrutura, rascunho, análise Story Grid e revisão | `workflows/wf-story-development.yaml` |
| Sistema de Narrativa de Marca | Ecossistema completo de marca: história de origem, histórias de clientes, visão de futuro e materiais de apresentação | `workflows/wf-brand-narrative.yaml` |

## Checklist de qualidade
Antes de entregar qualquer narrativa, valide-a com `checklists/output-quality.md`. Os itens CRÍTICOS bloqueiam a entrega: estrutura em três atos, arco emocional presente, gancho de abertura nas duas primeiras frases, "mostrar em vez de contar" e final satisfatório que resolve a tensão. PASSA com todos os críticos atendidos e menos de 3 falhas não críticas; REVISA com 3+ falhas não críticas; FALHA se qualquer item crítico ficar sem marcar.
