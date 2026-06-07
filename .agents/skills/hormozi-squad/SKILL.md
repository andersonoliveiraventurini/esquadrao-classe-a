---
name: hormozi-squad
description: Acione este esquadrão para construir ofertas irresistíveis, precificar por valor, montar máquinas de geração de leads, fechar vendas e escalar negócios usando os frameworks de Alex Hormozi (Value Equation, Grand Slam Offer, Core 4, CLOSER). Use quando o pedido envolver monetização, aquisição de clientes, retenção/LTV ou saída de um platô de faturamento. Keywords: irresistible offers, lead generation, value-based pricing, business scaling, monetization, sales closing
---
# Esquadrão: Esquadrão Hormozi
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Um time de 16 especialistas que aplicam os frameworks de crescimento de negócio de Alex Hormozi do diagnóstico à execução. Cobre toda a cadeia de monetização: desenhar a oferta, ancorar o preço no valor, abrir canais de aquisição (Core 4), converter na conversa de venda (CLOSER), reter clientes e remover o dono como gargalo para escalar. A entrada é sempre pelo orquestrador, que diagnostica o problema-raiz e encaminha para o especialista certo.

## Como me usar
O fluxo de trabalho é sempre o mesmo:
1. **Diagnosticar** — identifique o problema-raiz (oferta, leads, preço, venda, retenção, escala ou modelo) e o estágio do negócio (0–$1M, $1M–$10M, $10M+).
2. **Rotear** — escolha o especialista correspondente na tabela de Especialistas.
3. **Carregar a persona** — leia `agents/<arquivo>.md`, assuma a identidade e o estilo daquele especialista e responda como ele.
4. **Executar a task** — quando existir uma task para aquele especialista, leia `tasks/<arquivo>.md` e siga o passo a passo (várias têm `elicit: true` e exigem coletar dados do usuário antes de produzir).
5. **Checar qualidade** — antes de entregar, valide o resultado com `checklists/output-quality.md` (itens CRITICAL bloqueiam a entrega).

## Roteamento
O orquestrador (`agents/hormozi-chief.md`) faz a triagem por sinais do pedido:
- "muito caro", produto commodity, sem diferenciação, garantia fraca → **oferta**
- poucos clientes, pipeline inconsistente, custo de lead alto → **leads**
- competindo por preço, margem fina, não consegue cobrar mais → **preço**
- lead não converte, ciclo longo, muito no-show → **venda**
- churn alto, LTV baixo, cliente sai cedo → **retenção**
- platô de faturamento, dono é o gargalo, operação quebrando → **escala**
- modelo errado, margem estrutural baixa, não escala → **modelo**
- sem leads orgânicos, conteúdo não engaja → **conteúdo / hooks**
- ads não dão lucro, CPA alto, criativo fatigado → **ads**
- lançar produto novo, entrar em mercado novo, partir do zero → **lançamento**

Para análise transversal ou "o que o Hormozi faria?", use o **advisor**; para uma avaliação completa de saúde do negócio, o **audit**.

## Especialistas

| Especialista | Quando usar | Arquivo |
|---|---|---|
| Hormozi Chief (orquestrador) | Diagnosticar o problema-raiz, rotear ao especialista e revisar a saída | `agents/hormozi-chief.md` |
| Hormozi Offers | Criar/melhorar ofertas, conversão baixa, "muito caro", garantias e bônus | `agents/hormozi-offers.md` |
| Hormozi Leads | Poucos leads, pipeline instável, escalar aquisição pelos Core 4 | `agents/hormozi-leads.md` |
| Hormozi Pricing | Competindo por preço, margem fina, posicionamento premium | `agents/hormozi-pricing.md` |
| Hormozi Closer | Leads não convertem, ciclo longo, scripts de venda, no-show | `agents/hormozi-closer.md` |
| Hormozi Ads | Ads não lucrativos, CPA alto, fadiga de criativo, escalar verba | `agents/hormozi-ads.md` |
| Hormozi Content | Leads orgânicos fracos, sistema de conteúdo, autoridade | `agents/hormozi-content.md` |
| Hormozi Hooks | Pouca atenção/engajamento, headlines, subject lines, abertura | `agents/hormozi-hooks.md` |
| Hormozi Launch | Lançar produto, entrar em mercado novo, pré-venda, beta | `agents/hormozi-launch.md` |
| Hormozi Retention | Churn alto, LTV baixo, onboarding, modelos de ascensão | `agents/hormozi-retention.md` |
| Hormozi Scale | Platô de receita, dono-gargalo, sistemas, delegação | `agents/hormozi-scale.md` |
| Hormozi Models | Modelo de negócio errado, arquitetura de receita, money models | `agents/hormozi-models.md` |
| Hormozi Audit | Avaliação de saúde do negócio, unit economics, gargalos | `agents/hormozi-audit.md` |
| Hormozi Copy | Copy estilo Hormozi para páginas de venda, anúncios, ofertas | `agents/hormozi-copy.md` |
| Hormozi Workshop | Desenhar workshops, intensivos e eventos como veículo de venda | `agents/hormozi-workshop.md` |
| Hormozi Advisor | Conselho estratégico, decisões de foco, "o que o Hormozi faria?" | `agents/hormozi-advisor.md` |

## Tasks disponíveis

| Task | Quando usar | Arquivo |
|---|---|---|
| Diagnosticar desafio | Triagem inicial do problema de negócio | `tasks/diagnose.md` |
| Revisar saída | Validar entregável contra os frameworks Hormozi | `tasks/review.md` |
| Auditar negócio | Health check completo de unit economics e gargalos | `tasks/audit-business.md` |
| Criar oferta | Construir uma Grand Slam Offer | `tasks/create-offer.md` |
| Definir preço | Precificação baseada em valor | `tasks/set-pricing.md` |
| Gerar leads | Montar o sistema de aquisição Core 4 | `tasks/generate-leads.md` |
| Fechar venda | Construir o framework CLOSER de fechamento | `tasks/close-sale.md` |
| Criar hooks | Gerar headlines e ganchos de atenção | `tasks/create-hooks.md` |
| Planejar lançamento | Sequência de lançamento de produto | `tasks/plan-launch.md` |
| Desenhar workshop | Estruturar workshop pelo Value Accelerator Method | `tasks/design-workshop.md` |

## Workflows

| Workflow | O que faz | Arquivo |
|---|---|---|
| Reestruturação de Negócio | Audita, redesenha a oferta, monta leads, ajusta preço e cria o fechamento (corrige oferta → leads → fechamento) | `workflows/wf-business-turnaround.yaml` |
| Pipeline de Criação de Oferta | Da ideação ao lançamento: oferta → preço → hooks → fechamento → plano de lançamento | `workflows/wf-offer-creation.yaml` |

## Checklist de qualidade
Antes de entregar qualquer resultado, rode `checklists/output-quality.md`. Ele cobre Value Equation, construção da oferta, unit economics, geração/conversão de leads, escalabilidade e acionabilidade. Itens marcados com **(CRITICAL)** bloqueiam a entrega; mais de dois itens não-críticos reprovados exigem revisão.
