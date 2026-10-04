# Desafio Técnico LogiTrack Pro - Estágio em Qualidade

Análise de qualidade da aplicação **LogiTrack Pro**, realizada por Eduardo como parte do processo seletivo para Estágio em Qualidade da LogAp. A aplicação analisada é o sistema web de gerenciamento de veículos, viagens, manutenções e indicadores operacionais da frota.

- **Aplicação analisada:** https://logitrack.danieldiegosantana.me/
- **Período da execução:** outubro de 2026

## Resumo da análise

| Item | Resultado |
|---|---|
| Cenários de teste executados | 19 (12 aprovados e 7 reprovados) |
| Bugs registrados | 6 (1 crítico, 2 de severidade alta e 3 de severidade média) |
| Melhorias de UX propostas | 5 |
| Tipos de teste propostos na estratégia | 5 (API, segurança, integração, interface automatizada e end-to-end) |

**Principais achados:**

- **BUG-01 (crítico):** o login aceita qualquer senha quando o e-mail está cadastrado.
- **BUG-05 (alto):** a viagem aceita quilometragem negativa e o Dashboard subtrai esse valor do total da frota.
- **BUG-02 a BUG-06:** o sistema aceita dados inválidos (ano, datas, km e viagens sobrepostas), o que indica ausência de validação nos formulários e na API.

## Organização dos materiais

| Arquivo | Conteúdo | Parte do desafio |
|---|---|---|
| [`docs/01-cenarios-de-teste.md`](docs/01-cenarios-de-teste.md) | Resumo e detalhamento dos 19 cenários de teste, com os 9 campos solicitados | A. Planejamento e execução dos cenários de teste |
| [`docs/04-bugs.md`](docs/04-bugs.md) | Relatório dos 6 bugs, com problema, impacto e condições para reproduzir | A. Comportamentos incorretos encontrados |
| [`docs/02-analise-ux.md`](docs/02-analise-ux.md) | 5 oportunidades de melhoria na experiência do usuário | B. Análise de experiência do usuário |
| [`docs/03-estrategia-de-testes.md`](docs/03-estrategia-de-testes.md) | Tipos de teste recomendados, com objetivo, parte do sistema, risco e ordem de implementação, além de sugestões de melhoria no processo | C. Estratégia de testes adicionais |
| [`evidencias/cenarios/`](evidencias/cenarios) | Prints e demais evidências referenciados nos cenários e nos bugs | Evidências |
| [`automacao/`](automacao) | Pasta reservada para provas de conceito de automação | Diferenciais |

Estrutura do repositório:

```
.
├── README.md
├── docs/
│   ├── 01-cenarios-de-teste.md
│   ├── 02-analise-ux.md
│   ├── 03-estrategia-de-testes.md
│   └── 04-bugs.md
├── evidencias/
│   └── cenarios/
└── automacao/
```

Sugestão de leitura: começar pelo resumo do `01-cenarios-de-teste.md`, seguir para o `04-bugs.md` e depois ler a análise de UX e a estratégia de testes.

As evidências dos bugs usam os mesmos arquivos dos cenários de origem, que ficam em `evidencias/cenarios/`. Os nomes dos arquivos seguem o identificador do cenário (por exemplo, `CT-VIA-02_1_forms_km_negativo.png`).

## Ferramentas utilizadas

| Ferramenta | Uso |
|---|---|
| Google Chrome com DevTools | Execução manual dos testes, captura de evidências e observação das requisições na aba Network (status e endpoints) |
| Jira | Organização das etapas do desafio em quadro, com épicos |
| Google Docs | Elaboração e revisão dos textos da documentação |
| GitHub e Markdown | Versionamento e entrega da documentação |

## Premissas consideradas

- **Credenciais:** foram usadas as credenciais fornecidas no desafio. A senha não foi registrada nos arquivos deste repositório. Nos cenários, as demais senhas citadas são dados fictícios de teste.
- **Execução manual:** todos os cenários foram executados manualmente, no navegador Chrome, em visualização desktop.
- **Ausência de especificação funcional:** o desafio não traz requisitos detalhados. As regras de validação esperadas (por exemplo, ano de veículo realista, quilometragem maior que zero, data de chegada igual ou posterior à de saída) foram definidas com base em bom senso e no comportamento de sistemas desse tipo. A regra de viagens sobrepostas para o mesmo veículo (BUG-06) é uma regra de negócio assumida e deve ser confirmada com o time de produto.
- **Ambiente compartilhado:** o ambiente já continha registros criados por outros testes (por exemplo, veículos com ano negativo ou futuro, e viagens com km negativo). Por isso, os números do sistema variam ao longo do tempo. No início da análise, o Dashboard exibia 19.676 km no total da frota e 99 viagens no gráfico de volume por categoria, e as listas tinham 260 veículos e 82 manutenções.
- **Dados criados nos testes:** os cenários criaram uma conta de usuário de teste e registros de veículo, manutenção e viagem, alguns com dados inválidos de propósito, para comprovar os bugs.
- **Escopo da estratégia de testes:** a proposta contempla os tipos de teste relacionados ao que foi observado na execução dos cenários. Carga, acessibilidade e compatibilidade entre navegadores e dispositivos não foram avaliados nesta análise.

## Execução de testes automatizados

Nesta entrega não foram implementados testes automatizados: todos os cenários foram executados manualmente. A pasta `automacao/` está reservada para provas de conceito.

A estratégia para incorporar testes automatizados ao processo de qualidade (API, interface e end-to-end) está descrita em [`docs/03-estrategia-de-testes.md`](docs/03-estrategia-de-testes.md), que também inclui as sugestões de melhoria no processo.
