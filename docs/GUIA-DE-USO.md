# Guia de Uso — Esquadrão Clase A

Guia prático para tirar o máximo dos esquadrões no Claude Code.

## 1. Conceito

Cada **esquadrão** é um plugin com:
- um **orquestrador** (a skill `SKILL.md`) que entende o seu pedido e decide quem resolve;
- vários **especialistas** (personas em `agents/`) que o orquestrador "veste" para trabalhar;
- **tasks** (passos executáveis em `tasks/`) e **workflows** (fluxos multi-etapa).

Você nunca precisa decorar nomes de especialistas: descreva o problema e o orquestrador roteia.

## 2. Três formas de acionar

1. **Natural (recomendado):** apenas peça. A skill ativa pelo contexto.
   > "Preciso reescrever a página de vendas do meu curso, o público é frio."
2. **Comando dedicado:** `/<esquadrão> <pedido>`.
   > `/copy-squad reescreva minha página de vendas para público frio`
3. **Especialista específico:** se você já sabe quem quer, peça pelo nome.
   > "Use a abordagem do Eugene Schwartz para diagnosticar o nível de consciência."

## 3. Exemplos por esquadrão

| Você quer… | Esquadrão | Exemplo de pedido |
|---|---|---|
| Uma headline / VSL / e-mail / carta de vendas | `copy-squad` ou `copy-master` | `/copy-squad 10 headlines para anúncio de curso de inglês` |
| Decidir algo estratégico (sócio, investimento, pivô) | `advisory-board` | `/advisory-board vale a pena pegar um sócio investidor por 30%?` |
| Visão executiva (CEO/CTO/CFO/CMO) | `c-level-squad` | `/c-level-squad como estruturar o roadmap de produto do próximo ano?` |
| Montar uma oferta irresistível | `hormozi-squad` | `/hormozi-squad transforme meu serviço em uma Grand Slam Offer` |
| Posicionar/nomear uma marca | `brand-squad` | `/brand-squad arquétipo e tom de voz para uma marca de café especial` |
| Estruturar uma narrativa | `storytelling` | `/storytelling arco de história para o vídeo de lançamento` |
| Resolver campanha de tráfego pago | `traffic-masters` | `/traffic-masters meu CPA dobrou essa semana, o que investigar?` |
| Design de produto/UX | `design-squad` | `/design-squad fluxo de onboarding para um app financeiro` |
| Análise de dados / BI | `data-squad` | `/data-squad como modelar churn com os dados que tenho?` |
| Auditoria/segurança | `cybersecurity` | `/cybersecurity checklist de hardening para minha API Laravel` |
| Construir um movimento/comunidade | `movement` | `/movement plano para lançar uma comunidade em torno da minha causa` |
| Dominar o próprio Claude Code | `claude-code-mastery` | `/claude-code-mastery crie hooks para rodar testes ao salvar` |

## 4. Fluxo típico de uma sessão

1. **Peça.** O orquestrador faz o diagnóstico e diz qual especialista vai atuar.
2. **Refine.** Responda às perguntas do diagnóstico (público, objetivo, restrições).
3. **Receba o trabalho** já passado pela checagem de qualidade do esquadrão.
4. **Itere.** Peça uma segunda opinião de outro especialista, ou rode um workflow completo.

## 5. Dicas

- **Combine esquadrões:** copy + traffic + design cobrem um lançamento inteiro.
- **Workflows** entregam projetos ponta a ponta (ex.: `copy-squad` tem
  "projeto completo de copy"): peça "rode o workflow completo".
- **Qualidade:** se quiser rigor extra, peça para "revisar contra o checklist do esquadrão".
- **KNOWN-GAPS:** alguns esquadrões têm comandos do orquestrador original sem task pronta —
  estão documentados no fim do `SKILL.md`. Peça e o especialista resolve mesmo assim.

## 6. Atualizar/reconstruir

O marketplace é reprodutível a partir da fonte (ver `README.md` › "Como o marketplace é
construído"). Para atualizar quando a fonte mudar: reclonar `xquads-squads-src/`, rodar
`scripts/classify_orphans.py` e `scripts/build_marketplace.py`, e revisar os `SKILL.md`.
