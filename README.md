# Desafio Técnico LogiTrack Pro - Estágio em Qualidade

Análise de qualidade da aplicação **LogiTrack Pro**, realizada por Eduardo como parte do processo seletivo para Estágio em Qualidade da LogAp. A aplicação analisada é o sistema web de gerenciamento de veículos, viagens, manutenções e indicadores operacionais da frota.

- **Aplicação analisada:** https://logitrack.danieldiegosantana.me/
- **Período da execução:** outubro de 2026

## Resumo da análise

| Item | Resultado |
|---|---|
| Cenários de teste executados | 19 (12 aprovados e 7 reprovados) |
| Bugs registrados | 6 (1 crítico, 2 de severidade alta e 3 de severidade média) |
| Melhorias de UX propostas | 6 |
| Tipos de teste propostos na estratégia | 5 (API, segurança, integração, interface automatizada e end-to-end) |
| Diferenciais | Testes de API (Postman), análise de desempenho (validação básica), prova de conceito de automação (Playwright), análise de acessibilidade (automática, com Lighthouse) e sugestões de melhoria no processo |

**Principais achados:**

- **BUG-01 (crítico):** o login aceita qualquer senha quando o e-mail está cadastrado. O defeito foi reproduzido na interface, diretamente na API e por um teste automatizado.
- **BUG-05 (alto):** a viagem aceita quilometragem negativa e o Dashboard subtrai esse valor do total da frota.
- **BUG-02 a BUG-06:** o sistema aceita dados inválidos (ano, datas, km e viagens sobrepostas), o que indica ausência de validação nos formulários e na API. Todos foram reproduzidos também na API.

## Organização dos materiais

| Arquivo ou pasta | Conteúdo | Parte do desafio |
|---|---|---|
| [`docs/01-cenarios-de-teste.md`](docs/01-cenarios-de-teste.md) | Resumo e detalhamento dos 19 cenários de teste, com os 9 campos solicitados | A. Planejamento e execução dos cenários de teste |
| [`docs/04-bugs.md`](docs/04-bugs.md) | Relatório dos 6 bugs, com problema, impacto e condições para reproduzir | A. Comportamentos incorretos encontrados |
| [`docs/02-analise-ux.md`](docs/02-analise-ux.md) | 6 oportunidades de melhoria na experiência do usuário | B. Análise de experiência do usuário |
| [`docs/03-estrategia-de-testes.md`](docs/03-estrategia-de-testes.md) | Tipos de teste recomendados, com objetivo, parte do sistema, risco e ordem de implementação, além de sugestões de melhoria no processo | C. Estratégia de testes adicionais |
| [`docs/05-diferenciais.md`](docs/05-diferenciais.md) | Testes de API, análise de desempenho e prova de conceito de automação | Diferenciais |
| [`automacao/api/`](automacao/api) | Coleção do Postman com os testes de API | Diferenciais |
| [`automacao/ui/`](automacao/ui) | Testes automatizados de interface com Playwright (Python) | Diferenciais |
| [`evidencias/cenarios/`](evidencias/cenarios) | Prints e demais evidências dos cenários e dos bugs | Evidências |
| [`evidencias/diferenciais/`](evidencias/diferenciais) | Prints dos testes de API, de desempenho e de automação | Evidências |

Estrutura do repositório:

```
.
├── README.md
├── docs/
│   ├── 01-cenarios-de-teste.md
│   ├── 02-analise-ux.md
│   ├── 03-estrategia-de-testes.md
│   ├── 04-bugs.md
│   └── 05-diferenciais.md
├── automacao/
│   ├── api/
│   │   └── LogiTrack-Pro.postman_collection.json
│   └── ui/
│       ├── requirements.txt
│       └── tests/
│           ├── test_login.py
│           └── test_smoke.py
└── evidencias/
    ├── cenarios/
    └── diferenciais/
```

Sugestão de leitura: começar pelo resumo do `01-cenarios-de-teste.md`, seguir para o `04-bugs.md`, depois a análise de UX, a estratégia de testes e, por fim, os diferenciais.

Os nomes dos arquivos de evidência seguem o identificador do cenário ou do bug (por exemplo, `CT-VIA-02_1_forms_km_negativo.png` e `API_BUG-05_viagem_km_negativo.png`). As evidências dos bugs usam os mesmos arquivos dos cenários de origem, acrescidos dos prints da reprodução na API.

## Ferramentas utilizadas

| Ferramenta | Uso |
|---|---|
| Google Chrome com DevTools | Execução manual dos testes, captura de evidências e observação das requisições na aba Network (status e endpoints) |
| Postman | Testes de API e análise de desempenho (Collection Runner) |
| Playwright para Python (com pytest) | Prova de conceito de automação de testes de interface |
| Lighthouse (Chrome DevTools) | Avaliação automática de acessibilidade |
| Jira | Organização das etapas do desafio em quadro, com épicos |
| Google Docs | Elaboração e revisão dos textos da documentação |
| GitHub e Markdown | Versionamento e entrega da documentação |

## Premissas consideradas

- **Credenciais:** foram usadas as credenciais fornecidas no desafio. A senha não foi registrada nos arquivos deste repositório. Nos cenários, as demais senhas citadas são dados fictícios de teste.
- **Execução manual:** os cenários foram executados manualmente, no navegador Chrome, em visualização desktop. A melhoria de UX número 6 considera o acesso por dispositivos móveis.
- **Ausência de especificação funcional:** o desafio não traz requisitos detalhados. As regras de validação esperadas (por exemplo, ano de veículo realista, quilometragem maior que zero, data de chegada igual ou posterior à de saída) foram definidas com base em bom senso e no comportamento de sistemas desse tipo. A regra de viagens sobrepostas para o mesmo veículo (BUG-06) é uma regra de negócio assumida e deve ser confirmada com o time de produto.
- **Ambiente compartilhado:** o ambiente já continha registros criados por outros testes (por exemplo, veículos com ano negativo ou futuro, e viagens com km negativo), e outras pessoas também o utilizam. Por isso, os números do sistema variam ao longo do tempo. No início da análise, o Dashboard exibia 19.676 km no total da frota e 99 viagens no gráfico de volume por categoria, e as listas tinham 260 veículos e 82 manutenções.
- **Dados criados nos testes:** os cenários manuais criaram uma conta de usuário de teste e registros de veículo, manutenção e viagem, alguns com dados inválidos de propósito, para comprovar os bugs. Nos testes de API, cada registro criado foi excluído em seguida, e a análise de desempenho usou apenas consultas (GET).
- **Escopo da estratégia de testes:** a proposta contempla os tipos de teste relacionados ao que foi observado na execução dos cenários. O desempenho foi avaliado apenas com uma validação básica de tempo de resposta, sem teste de carga. A acessibilidade foi avaliada apenas de forma automática (Lighthouse), sem testes manuais de teclado e de leitor de tela, e a compatibilidade entre navegadores e dispositivos não foi avaliada.
- **Limite de tempo de resposta:** o valor de 2000 ms usado nos testes de API é uma premissa, pois o desafio não define requisito de desempenho.

## Diferenciais abordados

| Diferencial | Situação | Onde ver |
|---|---|---|
| Automação de testes | Prova de conceito com Playwright (Python) | [`automacao/ui`](automacao/ui) e [`docs/05-diferenciais.md`](docs/05-diferenciais.md) |
| Testes de API | Coleção do Postman com testes de status, acesso e dados inválidos | [`automacao/api`](automacao/api) e [`docs/05-diferenciais.md`](docs/05-diferenciais.md) |
| Análise de desempenho | Validação básica de tempo de resposta com 20 iterações | [`docs/05-diferenciais.md`](docs/05-diferenciais.md) |
| Sugestões de melhoria no processo | Critérios de aceite, validação no servidor, testes no pipeline, definição de pronto e ambiente de testes separado | [`docs/03-estrategia-de-testes.md`](docs/03-estrategia-de-testes.md) |
| Análise de acessibilidade | Avaliação automática com o Lighthouse em 6 telas (Login, Cadastro, Dashboard, Veículos, Manutenção e Viagens) | [`docs/05-diferenciais.md`](docs/05-diferenciais.md) |

## Execução dos testes automatizados

Os detalhes, os resultados e as evidências estão em [`docs/05-diferenciais.md`](docs/05-diferenciais.md). Em resumo:

### Testes de interface (Playwright)

Comandos para Linux (Ubuntu), a partir da raiz do repositório. É necessário ter Python 3 instalado.

```bash
cd automacao/ui
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

export LOGITRACK_EMAIL="e-mail fornecido no desafio"
read -s -p "Senha: " LOGITRACK_PASSWORD; export LOGITRACK_PASSWORD; echo

pytest -v
```

- O teste do BUG-01 está marcado como falha esperada (`xfail`). Para ver a falha real, execute `pytest -v --runxfail`.
- Para acompanhar a execução no navegador, use `pytest --headed`.
- As credenciais são lidas das variáveis de ambiente e não ficam no código. Os testes que dependem delas são ignorados se as variáveis não estiverem definidas.

### Testes de API (Postman)

1. Importar a coleção `automacao/api/LogiTrack-Pro.postman_collection.json` no Postman.
2. Criar um ambiente com as variáveis `baseUrl` (`https://api-logitrack.danieldiegosantana.me/v1`), `email` e `password` (credenciais fornecidas no desafio), marcando a senha como secret.
3. Executar primeiro a requisição de login válido da pasta Autenticação, que grava o `token` usado pelas demais.
4. Executar as requisições uma a uma. As requisições de cadastro com dado inválido criam registros quando o bug está presente, então cada uma deve ser seguida da requisição de exclusão correspondente.

Não é recomendado executar a coleção inteira de uma vez pelo Runner, porque os cadastros e as exclusões dependem da ordem. A análise de desempenho usa o Runner apenas com as requisições de consulta (GET).
