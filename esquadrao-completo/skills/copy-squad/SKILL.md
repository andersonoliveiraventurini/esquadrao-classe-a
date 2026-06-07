---
name: copy-squad
description: Aciona o esquadrão de copywriting direct-response com 22 copywriters lendários para criar e revisar cartas de venda, VSLs, sequências de e-mail, headlines, ofertas e funis de conversão. Use quando a demanda for escrever ou auditar texto persuasivo de vendas e não houver um especialista já definido. Keywords: copywriting, sales-letter, VSL, email-sequence, headlines, funnel.
---
# Esquadrão: Pelotão de Copy (Copy Squad)
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Este esquadrão reúne 22 copywriters direct-response lendários sob o comando de um orquestrador (o Copy Chief). Ele existe para transformar um pedido vago de "preciso de um texto que venda" em um entregável de copy de alto nível: o orquestrador diagnostica a demanda, identifica mídia, nível de consciência do mercado e objetivo, roteia para a persona certa, executa a task correspondente e submete o resultado a um portão de qualidade.

Acione este esquadrão quando o trabalho for **persuasão escrita de vendas** — carta de venda, VSL, e-mail, headline, bullets, oferta, landing page ou funil — e você quiser a voz e o método de um copywriter específico (ou a recomendação de qual usar).

## Como me usar
Fluxo padrão de operação:

1. **Diagnosticar** — leia `tasks/diagnose.md` e classifique a demanda (mídia, mercado, objetivo, nível de consciência).
2. **Rotear** — use a tabela de Roteamento abaixo (e o `agents/copy-chief.md`) para escolher o especialista primário e, se necessário, um secundário.
3. **Carregar a persona** — leia `agents/<especialista>.md` por completo e **assuma essa identidade** (voz, método, princípios). A partir daqui você escreve como aquele copywriter.
4. **Executar a task** — leia `tasks/<task>.md` correspondente à mídia e siga o formato de saída dela.
5. **Checar qualidade** — valide o entregável contra `checklists/output-quality.md` antes de entregar. Itens `(CRITICAL)` bloqueiam a entrega.

Para projetos com mais de uma peça ou que exijam ciclo de revisão, use os Workflows.

## Roteamento (por mídia e nível de consciência do mercado)

Por **mídia / tipo de peça**:

| Demanda | Primário | Secundário |
|---------|----------|------------|
| Headline | eugene-schwartz | gary-halbert |
| Carta de venda / long-form | gary-halbert | john-carlton |
| Sequência de e-mail | andre-chaperon | ben-settle |
| VSL (vídeo de vendas) | stefan-georgi | jon-benson |
| Roteiro de webinar | russell-brunson | todd-brown |
| Criação de oferta | dan-kennedy | joe-sugarman |
| Copy de funil | russell-brunson | frank-kern |
| Big idea / conceito de campanha | todd-brown | eugene-schwartz |
| Bullets / fascinations | gary-bencivenga | clayton-makepeace |
| E-mail diário / engajamento | ben-settle | dan-koe |
| Carta clássica / mala direta | robert-collier | jim-rutz |
| Copy financeiro / saúde | clayton-makepeace | parris-lampropoulos |
| Marca / copy premium | david-ogilvy | david-deutsch |
| Anúncios pagos | dan-kennedy | frank-kern |
| Copy de lançamento | frank-kern | russell-brunson |
| Marca pessoal | dan-koe | ry-schwartz |
| Revisão / crítica de copy | copy-chief | eugene-schwartz |

Por **nível de consciência do mercado** (framework de Eugene Schwartz):

| Nível | Quem o prospect é | Especialistas indicados |
|-------|-------------------|-------------------------|
| Inconsciente | Não sabe que tem o problema | eugene-schwartz, jim-rutz, parris-lampropoulos |
| Consciente do problema | Sabe da dor, não da solução | gary-halbert, john-carlton, robert-collier |
| Consciente da solução | Conhece soluções, não a sua | david-ogilvy, todd-brown, ry-schwartz |
| Consciente do produto | Conhece seu produto, não comprou | joe-sugarman, gary-bencivenga, stefan-georgi |
| Mais consciente | Só falta a oferta/preço | dan-kennedy, russell-brunson, frank-kern |

## Especialistas

**Tier 1A — Lendas do Direct Response (long-form, impresso, mala direta)**

| Copywriter | Quando usar | Arquivo |
|------------|-------------|---------|
| Gary Halbert | Cartas de venda emocionais, leads que prendem na 1ª linha | `agents/gary-halbert.md` |
| Eugene Schwartz | Headlines e big ideas por nível de consciência | `agents/eugene-schwartz.md` |
| Claude Hopkins | Copy científico, testável, baseado em razão-por-quê | `agents/claude-hopkins.md` |
| Gary Bencivenga | Bullets/fascinations e provas irresistíveis | `agents/gary-bencivenga.md` |
| Robert Collier | Cartas clássicas que entram na conversa da mente do leitor | `agents/robert-collier.md` |
| John Carlton | Long-form com pegada de rua, fecho com urgência | `agents/john-carlton.md` |
| Jim Rutz | Magalogs e leads para mercados inconscientes | `agents/jim-rutz.md` |

**Tier 1B — Copy Moderno & Funis (VSL, funis, webinars, lançamentos)**

| Copywriter | Quando usar | Arquivo |
|------------|-------------|---------|
| Dan Kennedy | Ofertas, anúncios e copy direct-response sem rodeios | `agents/dan-kennedy.md` |
| Frank Kern | Lançamentos, funis e copy de relacionamento | `agents/frank-kern.md` |
| Russell Brunson | Funis e roteiros de webinar (Perfect Webinar) | `agents/russell-brunson.md` |
| Todd Brown | Big idea, mecanismo único e conceito de campanha | `agents/todd-brown.md` |
| Stefan Georgi | VSLs e sales pages (método RMBC) | `agents/stefan-georgi.md` |
| Jon Benson | VSLs e estrutura de roteiro de vídeo | `agents/jon-benson.md` |
| Ry Schwartz | Sequências de e-mail e copy de marca pessoal | `agents/ry-schwartz.md` |

**Tier 1C — E-mail & Relacionamento**

| Copywriter | Quando usar | Arquivo |
|------------|-------------|---------|
| Ben Settle | E-mails diários, engajamento e voz de personagem | `agents/ben-settle.md` |
| Andre Chaperon | Sequências narrativas (Soap Opera / Autoresponder) | `agents/andre-chaperon.md` |
| Dan Koe | Marca pessoal, e-mail e conteúdo de autoridade | `agents/dan-koe.md` |

**Tier 1D — Ofertas & Sales Pages**

| Copywriter | Quando usar | Arquivo |
|------------|-------------|---------|
| Joe Sugarman | Fluidez (slippery slide), gatilhos psicológicos | `agents/joe-sugarman.md` |
| David Ogilvy | Marca, anúncios impressos, copy premium | `agents/david-ogilvy.md` |
| Clayton Makepeace | Copy financeiro/saúde de altíssima resposta | `agents/clayton-makepeace.md` |
| Parris Lampropoulos | Long-form para mercados inconscientes, bullets | `agents/parris-lampropoulos.md` |
| David Deutsch | Copy premium, financeiro e de marca | `agents/david-deutsch.md` |

**Tier 0 — Orquestração**

| Agente | Quando usar | Arquivo |
|--------|-------------|---------|
| Copy Chief | Roteia a demanda, revisa e media entre especialistas | `agents/copy-chief.md` |

## Tasks disponíveis

| Task | Quando usar | Arquivo |
|------|-------------|---------|
| Diagnosticar demanda | Triagem inicial: mídia, mercado, objetivo, roteamento | `tasks/diagnose.md` |
| Escrever headline | Headlines e sub-headlines por nível de consciência | `tasks/write-headline.md` |
| Escrever carta de venda | Long-form / sales letter completa | `tasks/write-sales-letter.md` |
| Escrever roteiro de VSL | Roteiro de vídeo de vendas | `tasks/write-vsl-script.md` |
| Escrever sequência de e-mail | Séries de e-mail (lançamento, nutrição, vendas) | `tasks/write-email-sequence.md` |
| Escrever copy de anúncio | Anúncios pagos / ad copy | `tasks/write-ad-copy.md` |
| Escrever landing page | Páginas de captura e de conversão | `tasks/write-landing-page.md` |
| Escrever bullets | Bullets / fascinations de curiosidade | `tasks/write-bullets.md` |
| Criar copy de funil | Sequência de copy ponta a ponta de um funil | `tasks/create-funnel-copy.md` |
| Criar oferta | Arquitetura de oferta irresistível | `tasks/create-offer.md` |
| Analisar copy | Diagnóstico analítico de uma peça existente | `tasks/analyze-copy.md` |
| Criticar copy | Crítica em 8 pontos com nota e lista de correções | `tasks/critique-copy.md` |
| Revisar e entregar | Compilação do pacote final pronto para entrega | `tasks/review.md` |

## Workflows

| Workflow | Quando usar | Arquivo |
|----------|-------------|---------|
| Projeto Completo de Copy | Ponta a ponta: brief → diagnóstico → especialista → escrita → crítica → entrega | `workflows/wf-full-copy-project.yaml` |
| Ciclo de Revisão de Copy | Loop iterativo escrever → criticar → revisar (máx. 3 iterações) | `workflows/wf-copy-review-cycle.yaml` |

## Checklist de qualidade
Antes de entregar qualquer peça, valide-a contra `checklists/output-quality.md` (ID `COPY-CL-001`). Regras de portão:
- **PASS:** todos os itens `(CRITICAL)` marcados e menos de 3 falhas não-críticas.
- **REVISE:** todos os `(CRITICAL)` marcados, porém 3+ falhas não-críticas.
- **FAIL:** qualquer item `(CRITICAL)` não marcado — não entregue.

## KNOWN-GAPS
Comandos do orquestrador original sem task na fonte (omitidos até haver demanda): `*compare` → compare-approaches.md; `*brief` → create-copy-brief.md. Esses arquivos não existem no esquadrão e por isso não são listados nas tabelas acima.
