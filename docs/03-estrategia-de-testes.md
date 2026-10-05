# Estratégia de Testes Adicionais

## Introdução

Esta proposta apresenta os tipos de teste que podem ser incorporados ao processo de qualidade do LogiTrack Pro, além dos testes manuais executados neste desafio (ver `01-cenarios-de-teste.md` e `04-bugs.md`). Para cada tipo são indicados o objetivo, a parte do sistema a ser validada, o risco que o teste ajuda a reduzir e a ordem sugerida para sua implementação.

## Escopo

A proposta se limita aos tipos de teste que se relacionam diretamente com o que foi observado na execução dos cenários: cinco dos seis bugs (BUG-02 a BUG-06) são falhas de **validação de dados**, o BUG-01 é uma falha de **autenticação** e o BUG-05 mostra um dado inválido **contaminando um indicador do Dashboard**. Por isso, a estratégia se concentra em testes de API, segurança, integração, interface automatizada e end-to-end. Os demais tipos citados no desafio não foram incluídos como recomendação porque não houve achados relacionados a eles: a compatibilidade entre navegadores e dispositivos não foi avaliada, a acessibilidade foi avaliada apenas de forma automática com o Lighthouse (ver `05-diferenciais.md`), e o desempenho foi tratado apenas por uma validação básica de tempo de resposta (ver `05-diferenciais.md`), sem teste de carga.

## Resumo

| Ordem | Tipo de teste | Principal ligação com os achados |
|---|---|---|
| 1º | Testes de API | BUG-01 a BUG-06: validações ausentes no servidor |
| 2º | Testes de segurança | BUG-01: autenticação aceita qualquer senha |
| 3º | Testes de integração | BUG-05: dado inválido em Viagens contamina o Dashboard |
| 4º | Testes automatizados de interface | Regressão de login e das validações de formulário |
| 5º | Testes end-to-end | Fluxos completos entre Viagens, Manutenção e Dashboard |

## Detalhamento por tipo de teste

### 1. Testes de API

| Campo | Descrição |
|---|---|
| **Objetivo** | Validar endpoints, contratos, códigos de resposta e tratamento de dados inválidos diretamente na API, sem passar pela interface |
| **Parte do sistema** | Endpoints observados na aba Network do navegador: login, me, veiculos, total-km, volume-por-categoria, cronograma-manutencao, ranking-utilizacao e projecao-financeira, além dos endpoints de cadastro, edição e exclusão de veículos, viagens e manutenções |
| **Risco reduzido** | Regras de negócio que existem só na tela ou que não existem. Uma API sem validação aceita dados inválidos mesmo que o formulário os bloqueie, e permite login com senha incorreta |
| **Ordem de implementação** | **1º.** Todos os bugs encontrados são de validação, e a API é o ponto em que essa regra precisa ser garantida. É também o tipo de teste mais rápido de montar |
| **Ligação com os achados** | BUG-01 a BUG-06. No BUG-01, a requisição de login retornou status 200 com senha incorreta, o que indica que a falha está no servidor. Uma prova de conceito desses testes foi feita no Postman e está descrita em `05-diferenciais.md` |
| **Casos sugeridos** | Login com senha incorreta deve retornar erro de autenticação (401)<br>Cadastro de veículo com ano inválido deve ser rejeitado (BUG-02)<br>Cadastro de manutenção com data de ano inválido deve ser rejeitado (BUG-03)<br>Cadastro de viagem com chegada anterior à saída deve ser rejeitado (BUG-04)<br>Cadastro de viagem com km negativo deve ser rejeitado (BUG-05)<br>Cadastro de viagem sobreposta para o mesmo veículo deve ser rejeitado ou sinalizado, conforme a regra definida pelo time de produto (BUG-06)<br>Verificação dos códigos de status e do formato das respostas dos endpoints observados |
| **Ferramentas sugeridas** | Postman (coleções com testes automáticos) e Newman para executar a coleção no pipeline |

### 2. Testes de segurança

| Campo | Descrição |
|---|---|
| **Objetivo** | Verificar se o sistema protege o acesso e os dados: autenticação, autorização e tratamento das respostas de erro |
| **Parte do sistema** | Login, cadastro de usuário e os endpoints que retornam dados da frota |
| **Risco reduzido** | Acesso indevido a informações operacionais e financeiras da empresa |
| **Ordem de implementação** | **2º.** O BUG-01 é uma falha crítica de autenticação e deve ser tratado antes de qualquer liberação aos usuários |
| **Ligação com os achados** | BUG-01 (senha incorreta aceita, com os dados da frota carregados após o acesso indevido). No cadastro, a mensagem de e-mail já existente (CT-CAD-01) confirma que o e-mail está cadastrado, enquanto o login usa uma mensagem genérica. Não é um defeito, mas é um ponto a ser avaliado (descoberta de e-mails cadastrados) |
| **Casos sugeridos** | Login com e-mail correto e senha incorreta, e com e-mail inexistente (CT-LOG-02 e CT-LOG-03)<br>Acesso às APIs de dados da frota sem autenticação ou com token inválido, para confirmar que retornam erro de acesso<br>Revisão das mensagens de erro de login e de cadastro quanto à informação que revelam |
| **Ferramentas sugeridas** | Postman para as chamadas sem token ou com token inválido, e testes manuais na interface. Executar apenas em ambiente autorizado para testes |

### 3. Testes de integração

| Campo | Descrição |
|---|---|
| **Objetivo** | Verificar se os módulos funcionam corretamente juntos e se os dados são consistentes entre eles |
| **Parte do sistema** | Relação entre Viagens, Manutenção e Veículos e os cálculos do Dashboard (Total de KM, Volume por Categoria, Cronograma de Manutenção, Ranking de Utilização e Projeção Financeira) |
| **Risco reduzido** | Indicadores de gestão incorretos por causa de dados inconsistentes |
| **Ordem de implementação** | **3º.** O Dashboard é a visão gerencial do sistema e depende de todos os outros módulos. Os testes de integração se apoiam nos testes de API, por isso vêm depois deles |
| **Ligação com os achados** | BUG-05: no CT-INT-02, uma viagem com km negativo subtraiu 500 km do Total de KM Percorrido. O CT-INT-03 mostra, de forma manual, como uma manutenção cadastrada se reflete no Dashboard |
| **Casos sugeridos** | Viagem com km inválido não deve alterar o Total de KM (CT-INT-02)<br>Manutenção criada reflete no Cronograma de Manutenção e na Projeção Financeira do mês correto (CT-INT-03)<br>A soma de km das viagens de cada veículo confere com o Ranking de Utilização (conferência feita manualmente na análise: as viagens do ADF-1565, de 286 km e 297,5 km, somam os 583,5 km exibidos no Ranking) |
| **Ferramentas sugeridas** | Testes de API encadeados (criar dado, consultar indicador e conferir o valor), com banco de dados de teste |

### 4. Testes automatizados de interface

| Campo | Descrição |
|---|---|
| **Objetivo** | Automatizar na tela as verificações que hoje são feitas manualmente, para detectar regressões a cada alteração do sistema |
| **Parte do sistema** | Login e formulários de cadastro de veículos, viagens e manutenção |
| **Risco reduzido** | Falhas reintroduzidas por novas alterações (regressão) e dependência de testes manuais repetitivos a cada versão |
| **Ordem de implementação** | **4º.** Traz mais valor depois que as validações forem corrigidas e a API estiver coberta. O login e os formulários principais já podem ser automatizados |
| **Ligação com os achados** | Os cenários reprovados (CT-LOG-02, CT-VEI-03, CT-MAN-01, CT-VIA-01, CT-VIA-02 e CT-VIA-03) podem virar testes automatizados que falham hoje e passam depois da correção, servindo de comprovação. O teste do BUG-01 já foi automatizado em uma prova de conceito com Playwright, descrita em `05-diferenciais.md` |
| **Casos sugeridos** | Login com credenciais válidas, com senha incorreta e com e-mail inexistente (CT-LOG-01, CT-LOG-02 e CT-LOG-03)<br>Validações dos formulários de veículo, manutenção e viagem com os dados inválidos dos cenários reprovados |
| **Ferramentas sugeridas** | Playwright (com Python), usado na prova de conceito, ou Cypress |

### 5. Testes end-to-end

| Campo | Descrição |
|---|---|
| **Objetivo** | Validar jornadas completas do usuário, do início ao resultado final, como ele usaria o sistema no dia a dia |
| **Parte do sistema** | Fluxos que atravessam várias telas e módulos |
| **Risco reduzido** | Defeitos que só aparecem quando as partes trabalham juntas e que testes isolados não pegam |
| **Ordem de implementação** | **5º.** É um teste mais lento e mais caro de manter, por isso deve cobrir poucos fluxos críticos e vir depois dos demais |
| **Ligação com os achados** | CT-INT-02 e CT-INT-03 são exemplos manuais desse tipo de jornada |
| **Casos sugeridos** | Login, cadastro de viagem e conferência do Total de KM no Dashboard, com remoção do dado criado ao final (CT-INT-02)<br>Cadastro de manutenção e conferência no Cronograma de Manutenção e na Projeção Financeira (CT-INT-03)<br>Cadastro de usuário e autenticação em seguida (CT-CAD-02) |
| **Ferramentas sugeridas** | Playwright ou Cypress, com dados de teste criados e removidos pelo próprio teste |

## Ordem sugerida de implementação

| Fase | Tipos de teste | Motivo |
|---|---|---|
| Fase 1 | API, segurança e integração | Cobrem os bugs de maior impacto e são os mais rápidos de montar |
| Fase 2 | Interface automatizada e end-to-end | Protegem contra regressões depois que as validações estiverem corrigidas |

## Sugestões de melhoria no processo

- **Critérios de aceite com regras explícitas.** Cada funcionalidade deve ter as regras de validação escritas antes do desenvolvimento (por exemplo: ano do veículo dentro de um intervalo definido, quilometragem maior que zero, data de chegada igual ou posterior à de saída, viagens do mesmo veículo sem sobreposição). Isso evitaria os bugs BUG-02 a BUG-06 e deixaria claro o que é defeito.
- **Validação no servidor e na tela.** A regra deve existir na API e ser refletida no formulário. A tela melhora a experiência, mas só a API protege os dados.
- **Testes no pipeline de entrega.** Testes de API e de interface executados automaticamente a cada alteração de código, com bloqueio da liberação se algum falhar.
- **Definição de pronto.** Uma funcionalidade só é considerada concluída com critérios de aceite validados, testes automatizados criados e os cenários negativos (dados inválidos) cobertos, e não só o caminho feliz.
- **Ambiente de testes separado e com dados controlados.** Durante a análise foram encontrados no ambiente muitos registros criados por testes anteriores (por exemplo, veículos com ano negativo). Um ambiente dedicado, com carga inicial de dados e limpeza após os testes, torna os resultados reproduzíveis e evita que dados de teste distorçam os indicadores.
- **Gestão dos defeitos.** Registrar cada bug com severidade, impacto e passos de reprodução (como em `04-bugs.md`) e revisar a lista periodicamente.
- **Revisão dos requisitos com a participação de QA.** Envolver a qualidade desde a definição das funcionalidades para identificar regras ausentes antes da implementação.
