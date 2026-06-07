---
name: copy-master
description: Acione este esquadrão para copywriting de elite de resposta direta — quando o pedido exigir vender por escrito com 32 copywriters lendários (cartas de venda, VSL, sequências de e-mail, ofertas irresistíveis, funis, webinars e pitch decks), roteamento por meio e nível de consciência do mercado, mais uma camada obrigatória de psicologia da persuasão. Keywords: direct-response copywriting, sales letter, VSL, email sequence, irresistible offer, sales funnel
---
# Esquadrão: Copy Master
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Transformar qualquer pedido de copy em texto que vende. O esquadrão reúne 32 dos maiores copywriters e especialistas em persuasão de todos os tempos — das lendas da resposta direta aos arquitetos modernos de funis, mestres de e-mail, engenheiros de oferta e psicólogos da influência — sob um único orquestrador que diagnostica o pedido, escolhe o especialista certo pelo meio e pelo nível de consciência do mercado, e aplica uma camada de psicologia da persuasão em todo projeto. Você não recebe "um texto qualquer": recebe a metodologia certa, na mídia certa, para o estágio de consciência certo, com revisão de persuasão por cima.

## Como me usar
Fluxo de trabalho recomendado:
1. **Diagnosticar** — descreva o pedido (mídia, oferta, público, objetivo). O orquestrador identifica o meio, o nível de consciência do mercado e o objetivo antes de prescrever.
2. **Rotear** — com base no diagnóstico, escolha o especialista primário (e, se o projeto for complexo, um secundário + um revisor de psicologia da Tier 1E).
3. **Carregar a persona** — leia `agents/<especialista>.md`, assuma a voz, os princípios e o vocabulário daquele copywriter e atue como ele.
4. **Executar a task** — leia `tasks/<task>.md` e siga suas fases, entradas/saídas e condições de veto (várias têm `elicit: true` e exigem coletar dados do usuário antes de produzir).
5. **Checar qualidade** — antes de entregar, valide o resultado contra `checklists/output-quality.md` (itens CRITICAL bloqueiam a entrega; a Seção 7 de psicologia da persuasão é obrigatória).

Para projetos que cruzam várias mídias, use um **workflow** (`workflows/*.yaml`), que encadeia especialistas, revisor de psicologia e tasks em fases com checkpoints.

## Roteamento (por mídia e nível de consciência do mercado)
O orquestrador (`agents/copy-master-chief.md`) roteia cruzando três eixos:

- **Mídia:** carta de venda · VSL · sequência de e-mail · e-mail diário · anúncio pago · landing page · funil · webinar · pitch deck · página de oferta · página de SaaS/conversão · magalog/mala direta.
- **Nível de consciência do mercado (escala de Schwartz):** inconsciente → consciente do problema → consciente da solução → consciente do produto → totalmente consciente. O nível define a abordagem do headline e o especialista ideal.
- **Objetivo:** gerar leads · vender · nutrir/engajar · lançar · estruturar oferta · negociar/pitch · converter trials · contornar objeções.

Regra de ouro: diagnóstico antes de prescrição, e **todo projeto recebe um revisor de psicologia da Tier 1E** (Cialdini para gatilhos de influência, Blair Warren para ressonância de identidade, Voss para objeções/negociação, Klaff para frame/pitch). Confiança ALTA roteia direto ao primário; MÉDIA sugere primário + secundário; BAIXA permanece no orquestrador e faz perguntas de esclarecimento.

## Especialistas
33 agents no total: 1 orquestrador + 32 copywriters lendários, agrupados por tier.

### Tier 0 — Orquestrador
| Copywriter | Quando usar | Arquivo |
|---|---|---|
| Copy Master Chief (orquestrador) | Diagnosticar o pedido, rotear ao especialista, designar revisor de psicologia e aplicar o portão de qualidade de 8 pontos | `agents/copy-master-chief.md` |

### Tier 1A — Lendas da Resposta Direta (9)
| Copywriter | Quando usar | Arquivo |
|---|---|---|
| Gary Halbert | Cartas de venda longas, mala direta, leads com storytelling | `agents/gary-halbert.md` |
| Eugene Schwartz | Headlines, breakthrough advertising, níveis de consciência | `agents/eugene-schwartz.md` |
| Claude Hopkins | Propaganda científica, métodos testados, reason-why | `agents/claude-hopkins.md` |
| Gary Bencivenga | Prova, bullets de fascinação, vantagens competitivas | `agents/gary-bencivenga.md` |
| Robert Collier | Cartas, entrar na conversa que já existe na mente do leitor | `agents/robert-collier.md` |
| John Carlton | Copy agressiva, método SWS, fechamento | `agents/john-carlton.md` |
| Jim Rutz | Magalogs, mala direta multipágina, aberturas | `agents/jim-rutz.md` |
| John Caples | Teste de headlines, métodos de propaganda testados | `agents/john-caples.md` |
| Rosser Reeves | USP (Proposta Única de Venda), reality in advertising | `agents/rosser-reeves.md` |

### Tier 1B — Copy Moderna & Funis (9)
| Copywriter | Quando usar | Arquivo |
|---|---|---|
| Dan Kennedy | Marketing de resposta direta, No B.S., ofertas | `agents/dan-kennedy.md` |
| Frank Kern | Mass control, lançamentos, funis de internet marketing | `agents/frank-kern.md` |
| Russell Brunson | Perfect Webinar, funis, DotCom Secrets | `agents/russell-brunson.md` |
| Todd Brown | E5 Method, big ideas, mecanismos únicos | `agents/todd-brown.md` |
| Stefan Georgi | Método RMBC, VSLs, video sales letters longas | `agents/stefan-georgi.md` |
| Jon Benson | Video sales letters, Sellerator, VSL conversacional | `agents/jon-benson.md` |
| Ry Schwartz | Copy baseada em consciência, sequências de e-mail dinâmicas | `agents/ry-schwartz.md` |
| Sabri Suby | Sell Like Crazy, Halo Strategy, geração de leads | `agents/sabri-suby.md` |
| Evaldo Albuquerque | Mecanismo único, carta de venda de 16 palavras, origin story | `agents/evaldo-albuquerque.md` |

### Tier 1C — E-mail & Relacionamento (3)
| Copywriter | Quando usar | Arquivo |
|---|---|---|
| Ben Settle | E-mails diários, anti-fragile selling, Email Players | `agents/ben-settle.md` |
| Andre Chaperon | Soap Opera Sequence, autoresponder, e-mail baseado em história | `agents/andre-chaperon.md` |
| Dan Koe | Marca pessoal, one-person business, construção de audiência | `agents/dan-koe.md` |

### Tier 1D — Ofertas, Páginas de Venda & Conversão (7)
| Copywriter | Quando usar | Arquivo |
|---|---|---|
| Joe Sugarman | Gatilhos psicológicos, slippery slide, anúncios impressos | `agents/joe-sugarman.md` |
| David Ogilvy | Propaganda de marca, anúncios longos, base em pesquisa | `agents/david-ogilvy.md` |
| Clayton Makepeace | Copy financeira/saúde, power words, agitação | `agents/clayton-makepeace.md` |
| Parris Lampropoulos | Magalogs financeiros/saúde, leads movidos a curiosidade | `agents/parris-lampropoulos.md` |
| David Deutsch | Anúncios impressos, copy de boardroom, info marketing | `agents/david-deutsch.md` |
| Alex Hormozi | Grand Slam Offers, value equation, metodologia $100M | `agents/alex-hormozi.md` |
| Joanna Wiebe | Conversion copywriting, A/B testing, copy de SaaS, CTA | `agents/joanna-wiebe.md` |

### Tier 1E — Persuasão & Psicologia (4)
| Copywriter | Quando usar | Arquivo |
|---|---|---|
| Robert Cialdini | 6 princípios da influência, pré-suasão, persuasão ética | `agents/robert-cialdini.md` |
| Blair Warren | Persuasão em uma frase, validação de identidade, ressonância emocional | `agents/blair-warren.md` |
| Chris Voss | Empatia tática, negociação, labeling, contorno de objeções | `agents/chris-voss.md` |
| Oren Klaff | Pitch Anything, controle de frame, alinhamento de status, neurofinanças | `agents/oren-klaff.md` |

## Tasks disponíveis

| Task | Quando usar | Arquivo |
|---|---|---|
| Diagnosticar pedido | Triar o pedido, dar resposta rápida e rotear ao especialista certo | `tasks/diagnose.md` |
| Escrever headline | Criar headlines pelos níveis de consciência (Schwartz) e teste de Caples | `tasks/write-headline.md` |
| Escrever carta de venda | Carta de resposta direta longa (metodologia Halbert/Carlton) | `tasks/write-sales-letter.md` |
| Escrever roteiro de VSL | Roteiro de video sales letter (RMBC/Sellerator) | `tasks/write-vsl-script.md` |
| Escrever sequência de e-mail | Sequências (Soap Opera, diária, lançamento, nutrição) | `tasks/write-email-sequence.md` |
| Escrever anúncio | Copy de mídia paga (Facebook, Google, YouTube, Instagram) | `tasks/write-ad-copy.md` |
| Escrever landing page | Copy de landing page otimizada para conversão | `tasks/write-landing-page.md` |
| Escrever bullets | Bullets e fascinações carregadas de curiosidade | `tasks/write-bullets.md` |
| Criar copy de funil | Todos os ativos de copy de um funil completo | `tasks/create-funnel-copy.md` |
| Criar oferta | Estruturar oferta irresistível (Grand Slam + value equation) | `tasks/create-offer.md` |
| Escrever roteiro de webinar | Roteiro de webinar/apresentação (Perfect Webinar) | `tasks/write-webinar-script.md` |
| Escrever pitch deck | Narrativa de pitch deck com controle de frame (Klaff) | `tasks/write-pitch-deck.md` |
| Analisar copy | Analisar copy existente: forças, fraquezas e oportunidades | `tasks/analyze-copy.md` |
| Criticar copy | Crítica completa pelos 8 critérios de qualidade | `tasks/critique-copy.md` |
| Revisar entrega | Portão final de qualidade antes da entrega | `tasks/review.md` |

## Workflows

| Workflow | O que faz | Arquivo |
|---|---|---|
| Projeto Completo de Copy | Ponta a ponta: brief → diagnóstico → especialista + revisor de psicologia → escrita → revisão → entrega | `workflows/wf-full-copy-project.yaml` |
| Ciclo de Revisão de Copy | Loop iterativo escrever-criticar-revisar com auditoria de persuasão (máx. 3 iterações) | `workflows/wf-copy-review-cycle.yaml` |
| Produção de VSL Completa | Fluxo de VSL: big idea → mecanismo → roteiro → revisão → auditoria de psicologia | `workflows/wf-vsl-production.yaml` |
| Sequência Completa de Lançamento | Lançamento full: big idea → webinar → página de venda → e-mails → anúncios → camada de psicologia | `workflows/wf-launch-sequence.yaml` |

## Checklist de qualidade
Antes de entregar qualquer copy, valide-a com `checklists/output-quality.md`. Itens marcados como **(CRITICAL)** bloqueiam a entrega (headline que para o leitor, lead que fisga nas duas primeiras frases, oferta cristalina, CTA específico e urgente, e "você compraria com base nessa copy?"). A **Seção 7 — Psicologia da Persuasão** é obrigatória neste esquadrão: exige no mínimo 3 dos princípios de Cialdini e 2 das alavancas de Blair Warren aplicados de forma natural. A **Seção 8 — Arquitetura da Oferta** (value equation de Hormozi) se aplica sempre que houver oferta. Veredito: PASSA com todos os críticos atendidos e a Seção 7 satisfeita; REVISA se a Seção 7 falhar ou houver 2+ falhas não críticas; FALHA se qualquer item crítico ficar sem marcar.

## KNOWN-GAPS
Comandos do orquestrador original sem task correspondente na fonte (omitidos das tabelas acima até haver demanda):
- `*compare` → `compare-approaches.md` (task inexistente)
- `*brief` → `create-copy-brief.md` (task inexistente)

Esses comandos permanecem descritos no agente orquestrador, mas não há arquivo de task que os implemente. Não os utilize até que a task seja criada.
