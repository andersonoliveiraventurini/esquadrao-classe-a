---
name: brand-squad
description: Acione este esquadrão para qualquer desafio de marca — construção de identidade, posicionamento, naming, arquitetura de marca, brand story, auditoria de equity e estratégia de rebranding. Reúne 10 pensadores lendários de branding mais especialistas funcionais sob um orquestrador que diagnostica e roteia. Keywords: branding, brand identity, positioning, naming, brand strategy, rebranding.
---
# Esquadrão: Brand Squad
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
O Brand Squad cobre o ciclo completo de estratégia de marca: do diagnóstico inicial à entrega de um sistema de marca pronto para lançamento. Em vez de aplicar uma única teoria, ele reúne as escolas de pensamento mais influentes do branding (Aaker, Keller, Kapferer, Ries, Sharp, Neumeier, Miller, Yohn, Heyward, Wheeler) e as coloca em diálogo, escolhendo a abordagem certa para cada contexto — estágio da marca, setor, B2B/B2C, marca nova ou em evolução. Um orquestrador faz a triagem do problema e direciona ao especialista (ou combinação) mais adequado.

## Como me usar
Siga este fluxo sempre que assumir o esquadrão:
1. **Diagnosticar** — entenda o desafio real (identidade, posicionamento, messaging, visual, cultura, arquitetura, crescimento) e o estágio da marca. Quando houver dúvida, comece pela task `tasks/diagnose.md`.
2. **Rotear** — use a tabela de Roteamento abaixo (e a lógica do orquestrador `agents/brand-chief.md`) para escolher o especialista primário e o secundário.
3. **Carregar a persona** — leia o arquivo `agents/<especialista>.md` correspondente e **assuma** integralmente aquela persona (tom, foco, frameworks).
4. **Executar a task** — leia o arquivo `tasks/<task>.md` indicado e produza o entregável seguindo seu passo a passo.
5. **Checar qualidade** — valide o resultado contra `checklists/output-quality.md` antes de entregar.

## Roteamento (quando usar cada especialista)
| Desafio | Primário | Secundário |
|---------|----------|------------|
| Construir/medir brand equity e valor | david-aaker | kevin-keller |
| Identidade e DNA da marca (Prisma) | jean-noel-kapferer | alina-wheeler |
| Posicionamento e criação de categoria | al-ries | marty-neumeier |
| Crescimento baseado em evidências | byron-sharp | kevin-keller |
| Messaging e StoryBrand | donald-miller | miller-sticky-brand |
| Diferenciação radical ("only-ness") | marty-neumeier | al-ries |
| Identidade visual e guidelines | alina-wheeler | archetype-consultant |
| Cultura de marca e employer brand | denise-yohn | donald-miller |
| Marca de startup e DTC | emily-heyward | naming-strategist |
| Luxo e premium | jean-noel-kapferer | david-aaker |
| Naming e domínios | naming-strategist | domain-scout |
| Arquétipos e personalidade | archetype-consultant | jean-noel-kapferer |
| Saúde da marca (CBBE) e arquitetura/portfólio | kevin-keller / david-aaker | byron-sharp / kevin-keller |

## Especialistas
| Especialista | Quando usar | Arquivo |
|--------------|-------------|---------|
| Brand Chief (orquestrador) | Triagem do desafio, roteamento e síntese entre frameworks | `agents/brand-chief.md` |
| David Aaker | Brand equity, arquitetura de marca, estratégia de extensão | `agents/david-aaker.md` |
| Kevin Keller | Saúde da marca, modelo CBBE, brand tracking e auditoria | `agents/kevin-keller.md` |
| Jean-Noël Kapferer | Identidade de marca, Prisma de Identidade, estratégia de luxo | `agents/jean-noel-kapferer.md` |
| Al Ries | Posicionamento na mente, foco e criação de categoria | `agents/al-ries.md` |
| Byron Sharp | Crescimento por evidências, distintividade, alcance vs. targeting | `agents/byron-sharp.md` |
| Marty Neumeier | Diferenciação radical, "the brand gap", Zag e only-ness | `agents/marty-neumeier.md` |
| Donald Miller | Messaging com StoryBrand SB7, cliente como herói | `agents/donald-miller.md` |
| Denise Yohn | Fusão marca-cultura, branding interno, operacionalização | `agents/denise-yohn.md` |
| Emily Heyward | Branding de startup e DTC, marca desde o dia um | `agents/emily-heyward.md` |
| Alina Wheeler | Sistema de identidade visual, logo, guidelines, touchpoints | `agents/alina-wheeler.md` |
| Archetype Consultant | Arquétipos junguianos, personalidade e tom de voz | `agents/archetype-consultant.md` |
| Naming Strategist | Geração e avaliação de nomes, análise linguística | `agents/naming-strategist.md` |
| Domain Scout | Disponibilidade de domínios e checagem de conflitos | `agents/domain-scout.md` |
| Miller Sticky Brand | Implementação prática de StoryBrand e mensagens memoráveis | `agents/miller-sticky-brand.md` |

## Tasks disponíveis
| Task | Quando usar | Arquivo |
|------|-------------|---------|
| Diagnose | Triagem inicial do desafio de marca e roteamento | `tasks/diagnose.md` |
| Audit Brand | Auditoria completa de saúde e equity da marca existente | `tasks/audit-brand.md` |
| Create Positioning | Definir posicionamento, statement, tagline e proof points | `tasks/create-positioning.md` |
| Generate Names | Gerar e pontuar candidatos a nome com finalistas recomendados | `tasks/generate-names.md` |
| Build Identity | Projetar o sistema de identidade visual e verbal | `tasks/build-identity.md` |
| Create Brand Story | Construir a narrativa com StoryBrand SB7 e aplicações | `tasks/create-brand-story.md` |
| Design Architecture | Definir arquitetura de marca e estratégia de portfólio | `tasks/design-architecture.md` |
| Map Archetype | Avaliar os 12 arquétipos e selecionar primário/secundário | `tasks/map-archetype.md` |
| Review | Consolidar entregáveis e revisar consistência contra o checklist | `tasks/review.md` |

## Workflows
| Workflow | Quando rodar | Arquivo |
|----------|--------------|---------|
| Criação de Marca | Marca nova de ponta a ponta: arquétipo → posicionamento → naming → identidade → story → pacote de lançamento (60-120 min) | `workflows/wf-brand-creation.yaml` |
| Rebranding | Marca existente: auditoria → revisão de posicionamento → atualização de identidade → refresh de messaging (45-90 min) | `workflows/wf-rebrand.yaml` |

## Checklist de qualidade
Antes de entregar qualquer resultado, valide-o contra `checklists/output-quality.md` (ID BRAND-CL-001). Itens marcados como (CRITICAL) bloqueiam a entrega. Critério: **PASS** com todos os críticos aprovados e menos de 3 falhas não-críticas; **REVISE** com 3+ falhas não-críticas; **FAIL** com qualquer item crítico em aberto. As categorias verificam posicionamento e diferenciação, voz e personalidade, arquétipo e identidade, coerência visual e consistência estratégica.
