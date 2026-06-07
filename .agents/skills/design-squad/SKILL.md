---
name: design-squad
description: Acione quando o pedido envolver design de produto, UX/UI, criação ou evolução de design systems, especificação de componentes, fluxos de usuário, handoff design-dev ou operações de design (DesignOps). Não use para implementação backend, infraestrutura ou conteúdo sem dimensão de interface. Keywords: design system, UX research, UI components, design tokens, accessibility, handoff.
---
# Esquadrão: Design Squad
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Reunir, sob um único ponto de entrada, especialistas em design de sistemas, pesquisa de UX, produção visual e implementação de UI. O esquadrão cobre o ciclo completo: do diagnóstico do desafio à entrega pronta para desenvolvimento, sempre com qualidade e acessibilidade como critérios não negociáveis.

## Como me usar
O fluxo de trabalho tem quatro movimentos encadeados:

1. **Diagnosticar** — entenda o desafio antes de agir. Quem é o usuário, qual o problema, quais as restrições e em que fase estamos (pesquisa, sistema, produção visual, implementação ou processo).
2. **Rotear** — escolha o especialista certo para a fase, usando a tabela de Roteamento e a de Especialistas abaixo.
3. **Carregar a persona** — abra o arquivo `agents/<especialista>.md`, leia a definição completa e **assuma** aquela persona (tom, princípios e foco) antes de produzir qualquer coisa.
4. **Executar a task** — abra `tasks/<task>.md`, siga as entradas/saídas declaradas e gere o entregável.

Ao final, valide o resultado contra `checklists/output-quality.md` antes de entregar.

## Roteamento
| Situação do pedido | Para onde rotear |
| --- | --- |
| Não está claro qual a fase ou o especialista | `agents/design-chief.md` → task `tasks/diagnose.md` |
| Criar um design system do zero | `agents/brad-frost.md` → `tasks/create-design-system.md` |
| Escalar/governar design system existente | `agents/dan-mall.md` |
| Auditar maturidade ou prática de design | `agents/dave-malouf.md` → `tasks/audit-design.md` |
| Estruturar processos e DesignOps | `agents/dave-malouf.md` → `tasks/setup-design-ops.md` |
| Pesquisa de usuário, IA, wireframes e fluxos | `agents/ux-designer.md` → `tasks/design-ux-flow.md` |
| Especificar um componente (tokens + API) | `agents/design-system-architect.md` → `tasks/create-component-spec.md` |
| Conceitos visuais, identidade e prompts de imagem | `agents/visual-generator.md` |
| Implementar a UI em código de produção | `agents/ui-engineer.md` → `tasks/generate-handoff.md` |
| Revisar qualidade de um entregável | `agents/design-chief.md` → `tasks/review.md` |

## Especialistas
| Especialista | Quando usar | Arquivo |
| --- | --- | --- |
| Design Chief (orquestrador) | Diagnóstico, roteamento, revisão e síntese de entregáveis | `agents/design-chief.md` |
| Brad Frost | Atomic design, criação de design systems e pattern labs | `agents/brad-frost.md` |
| Dan Mall | Escala, adoção e governança de design systems entre times | `agents/dan-mall.md` |
| Dave Malouf | DesignOps, maturidade de design e liderança de processos | `agents/dave-malouf.md` |
| UX Designer | Pesquisa, arquitetura de informação, wireframes e jornadas | `agents/ux-designer.md` |
| Design System Architect | Tokens, bibliotecas de componentes e APIs de componente | `agents/design-system-architect.md` |
| Visual Generator | Identidade visual, conceitos, ícones e prompts de imagem | `agents/visual-generator.md` |
| UI Engineer | Implementação de UI, responsividade, animação e a11y em código | `agents/ui-engineer.md` |

## Tasks disponíveis
| Task | Quando usar | Arquivo |
| --- | --- | --- |
| Diagnosticar desafio | Triagem inicial e definição de rota | `tasks/diagnose.md` |
| Criar design system | Construir um sistema do zero pela metodologia atomic | `tasks/create-design-system.md` |
| Especificar componente | Definir tokens, estados e API de um componente | `tasks/create-component-spec.md` |
| Desenhar fluxo de UX | Mapear pesquisa, IA e wireframes de uma feature/produto | `tasks/design-ux-flow.md` |
| Auditar design | Avaliar prática e maturidade de design da organização | `tasks/audit-design.md` |
| Estruturar DesignOps | Definir processos, papéis e ferramentas de design | `tasks/setup-design-ops.md` |
| Gerar handoff | Preparar a documentação de entrega para desenvolvimento | `tasks/generate-handoff.md` |
| Revisar entregável | Checar qualidade do output de um especialista | `tasks/review.md` |

## Workflows
| Workflow | Trigger | Quando usar | Arquivo |
| --- | --- | --- | --- |
| Criação de Design System | `*design-system-creation` | Da auditoria à governança e lançamento do sistema | `workflows/wf-design-system-creation.yaml` |
| Design de Funcionalidade | `*feature-design` | Da pesquisa de usuário ao handoff de implementação | `workflows/wf-feature-design.yaml` |

## Checklist de qualidade
Antes de entregar qualquer resultado, rode `checklists/output-quality.md`. Os itens marcados como CRITICAL (contraste WCAG, estados de foco visíveis, etc.) bloqueiam a entrega; os demais são consultivos. A task `tasks/review.md` referencia este checklist diretamente.
