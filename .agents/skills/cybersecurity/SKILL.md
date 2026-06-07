---
name: cybersecurity
description: Acione este esquadrão para operações de segurança ofensiva e defensiva — pentest, red team, reconhecimento, enumeração, fuzzing, exploração, AppSec/OWASP, monitoramento de rede, gestão de vulnerabilidades, resposta a incidentes, OSINT e auditoria, sempre dentro de limites éticos e autorizados. Keywords: pentest, vulnerability, incident-response, OWASP, OSINT, red-team
---
# Esquadrão: Cybersecurity (Segurança Cibernética)
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Coordenar um time de 15 agentes para conduzir operações de segurança ponta a ponta. O esquadrão cobre o lado ofensivo (recon, enumeração, fuzzing, exploração, pentest, red team) e o lado defensivo (AppSec, monitoramento de rede, gestão de vulnerabilidades, resposta a incidentes, threat intel). Toda operação ofensiva passa por verificação de autorização e escopo antes de qualquer ação.

## Como me usar
Fluxo padrão de orquestração:
1. **Diagnosticar** — entenda o objetivo (ofensivo, defensivo ou educacional/CTF), o alvo e o escopo. Para triagem, leia e execute `tasks/diagnose.md` consultando `data/routing-catalog.yaml`.
2. **Rotear** — escolha o especialista certo pela tabela de Roteamento abaixo.
3. **Carregar a persona** — leia `agents/<especialista>.md`, assuma aquela identidade e fale com a voz dela.
4. **Executar a task** — leia `tasks/<task>.md` e siga o procedimento atômico definido (entradas, passos, saídas).
5. **Checar qualidade** — antes de entregar, valide o resultado contra `checklists/output-quality.md`.

Antes de qualquer ação ofensiva: confirme autorização escrita, defina escopo (in/out) e regras de engajamento. Nunca execute ataques fora do escopo autorizado.

## Roteamento (quando usar cada especialista)
- **Avaliação ofensiva completa / red team** → `cartographer` → `dirber`/`busterer` → `fuzzer` → `rogue` → `peter-kim`
- **Teste de aplicação web** → `jim-manico` (OWASP) → `busterer`/`dirber` → `fuzzer` → `command-generator`
- **Segurança e monitoramento de rede** → `chris-sanders` → `cartographer` → `command-generator` → `omar-santos`
- **Segurança mobile** → `georgia-weidman` → `command-generator` → `fuzzer`
- **Resposta a incidentes** → `omar-santos` → `chris-sanders` → `marcus-carey`
- **Arquitetura / hardening** → `jim-manico` → `omar-santos` → `marcus-carey`
- **CTF** → avaliar tipo do desafio → especialista relevante → `command-generator`
- **Avaliação de credenciais** → `ripper` → `rogue`
- **Investigação OSINT** → `shannon-runner` → `cartographer` → `marcus-carey`

## Especialistas
| Especialista | Quando usar | Arquivo |
| --- | --- | --- |
| Orquestrador (Comandante Égide) | Diagnóstico, planejamento, roteamento e supervisão ética de operações multi-domínio | `agents/cyber-chief.md` |
| Peter Kim | Metodologia de pentest e red team, playbooks de ataque, mapeamento MITRE ATT&CK | `agents/peter-kim.md` |
| Georgia Weidman | Segurança mobile, fundamentos de pentest, desenvolvimento de exploits | `agents/georgia-weidman.md` |
| Jim Manico | AppSec, codificação segura, OWASP Top 10, autenticação/autorização | `agents/jim-manico.md` |
| Chris Sanders | Monitoramento de rede (NSM/SOC), análise de pacotes, IDS, investigação | `agents/chris-sanders.md` |
| Omar Santos | Gestão de vulnerabilidades/CVE, resposta a incidentes, padrões (CSAF, VEX, SBOM), AI security | `agents/omar-santos.md` |
| Marcus Carey | Liderança de segurança, threat intelligence, estratégia, simulação de ataque | `agents/marcus-carey.md` |
| Command Generator | Sintaxe exata de comandos de ferramentas e construção de tool chains | `agents/command-generator.md` |
| Cartographer | Reconhecimento e mapeamento de superfície de ataque | `agents/cartographer.md` |
| Busterer | Descoberta de conteúdo web, enumeração de diretórios, vhosts e endpoints de API | `agents/busterer.md` |
| Dirber | Enumeração de serviços de rede (SMB, LDAP, SNMP, NFS, RPC), Active Directory | `agents/dirber.md` |
| Fuzzer | Fuzzing de inputs, parâmetros, headers e cookies; busca de pontos de injeção | `agents/fuzzer.md` |
| Ripper | Quebra de hashes, avaliação de política de senhas, ataques offline a credenciais | `agents/ripper.md` |
| Rogue | Exploração e pós-exploração (privesc, movimento lateral, persistência), CTF | `agents/rogue.md` |
| Shannon Runner | OSINT, perfilamento de alvos, recon de engenharia social | `agents/shannon-runner.md` |

## Tasks disponíveis
| Task | Quando usar | Arquivo |
| --- | --- | --- |
| diagnoseCybersecurity | Triagem inicial do pedido e roteamento ao especialista certo | `tasks/diagnose.md` |
| assessSecurity | Verificar autorização, definir escopo e montar o plano de avaliação | `tasks/assess-security.md` |
| runRecon | Reconhecimento passivo/ativo e mapeamento de superfície de ataque | `tasks/run-recon.md` |
| analyzeVulnerability | Identificar, classificar e priorizar vulnerabilidades (CVSS) | `tasks/analyze-vulnerability.md` |
| runPentest | Executar pentest com exploração controlada e relatório | `tasks/run-pentest.md` |
| auditAppSecurity | Auditar segurança de aplicação web sob ótica OWASP | `tasks/audit-app-security.md` |
| generateCommands | Traduzir um objetivo em comandos exatos de ferramentas | `tasks/generate-commands.md` |
| respondIncident | Conduzir resposta a incidente (detecção → lições aprendidas) | `tasks/respond-incident.md` |
| reviewSecurityOutput | Revisar a entrega de um especialista contra o checklist de qualidade | `tasks/review.md` |

## Workflows
- `workflows/wf-pentest-engagement.yaml` — engajamento completo de pentest, da autorização à exploração e relatório, com gates éticos em cada fase. Rode quando o objetivo for um pentest formal de ponta a ponta (trigger `*pentest-engagement`).
- `workflows/wf-incident-response.yaml` — ciclo de resposta a incidentes baseado em NIST 800-61 (detecção, contenção, erradicação, recuperação, lições aprendidas). Rode em incidentes de segurança ativos (trigger `*incident-response`).

## Checklist de qualidade
Antes de entregar qualquer deliverable, valide-o contra `checklists/output-quality.md` (CYBER-CL-001). Itens CRÍTICos bloqueiam a entrega: autorização e escopo respeitados, severidade por finding (CVSS), evidência/PoC reprodutível, recomendação de remediação acionável e ausência de dados sensíveis expostos no relatório.
