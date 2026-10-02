# Execução Cenários de Testes

### CT-LOG-01 - Login com credenciais válidas

| Campo | Descrição |
|---|---|
| **Objetivo** | Validar que um usuário com credenciais válidas consegue autenticar-se e acessar a tela principal do sistema |
| **Pré-condições** | Usuário previamente cadastrado (credenciais fornecidas no desafio); sistema acessível pela URL do desafio |
| **Dados utilizados** | E-mail: logap@teste.com<br>Senha: a informada no documento do desafio |
| **Passos** | 1. Abrir a URL da aplicação<br>2. Verificar que a tela de login é exibida<br>3. Preencher o campo "E-mail" com o e-mail informado<br>4. Preencher o campo "Senha" com a senha informada<br>5. Clicar no botão "Entrar" |
| **Resultado esperado** | O sistema autentica o usuário e redireciona para o Dashboard, exibindo o nome e o e-mail do usuário no cabeçalho e os indicadores carregados, sem mensagens de erro |
| **Resultado obtido** | O sistema autenticou o usuário e redirecionou para o Dashboard. O cabeçalho exibiu o usuário logado e os cards (Total de KM, Volume por Categoria, Cronograma de Manutenção, Ranking de Utilização e Projeção Financeira) foram carregados, sem mensagens de erro |
| **Status** | Aprovado |
| **Evidências** | 1. ![Formulário preenchido](../evidencias/cenarios/CT-LOG-01_1_formulario_preenchido.png)<br>2. ![Dashboard após login](../evidencias/cenarios/CT-LOG-01_2_dashboard.png) |

### CT-LOG-02 - Login com e-mail correto e senha inválida

| Campo | Descrição |
|---|---|
| **Objetivo** | Validar que um usuário com senha inválida não consegue autenticar-se e acessar a tela principal do sistema |
| **Pré-condições** | Usuário previamente cadastrado (credenciais fornecidas no desafio); sistema acessível pela URL do desafio |
| **Dados utilizados** | E-mail: logap@teste.com<br>Senha: 123456 |
| **Passos** | 1. Abrir a URL da aplicação<br>2. Verificar que a tela de login é exibida<br>3. Preencher o campo "E-mail" com o e-mail informado<br>4. Preencher o campo "Senha" com a senha inválida<br>5. Clicar no botão "Entrar" |
| **Resultado esperado** | O sistema não autentica o usuário e e aparece uma mensagem de erro informando ao usuário que uma das suas credenciais estão incorretas |
| **Resultado obtido** | O sistema autenticou o usuário e redirecionou para o Dashboard. Não apareceu nenhuma mensagem de erro. A requisição de login retornou status 200 |
| **Status** | Reprovado |
| **Evidências** | 1. ![Formulário preenchido](../evidencias/cenarios/CT-LOG-02_1_formulario_preenchido_senha_incorreta.png)<br>2. ![Dashboard após login](../evidencias/cenarios/CT-LOG-01_2_dashboard.png) |

### CT-LOG-03 - Login com e-mail inexistente

| Campo | Descrição |
|---|---|
| **Objetivo** | Validar que um usuário com e-mail não cadastrado não consegue autenticar-se nem acessar a tela principal do sistema |
| **Pré-condições** | E-mail utilizado sem cadastro no sistema; sistema acessível pela URL do desafio |
| **Dados utilizados** | E-mail: teste@gmail.com<br>Senha: abcdef |
| **Passos** | 1. Abrir a URL da aplicação<br>2. Verificar que a tela de login é exibida<br>3. Preencher o campo “E-mail” com algum e-mail não cadastrado no sistema<br>4. Preencher o campo "Senha" com a senha informada<br>5. Clicar no botão "Entrar" |
| **Resultado esperado** | O sistema não autentica o usuário, permanece na tela de login e exibe uma mensagem informando que uma das credenciais está incorreta. O Dashboard não é exibido |
| **Resultado obtido** | O sistema não autenticou o usuário e exibiu a mensagem "Invalid email or password". O usuário permaneceu na tela de login |
| **Status** | Aprovado |
| **Evidências** | 1. ![Formulário com e-mail inexistente](../evidencias/cenarios/CT-LOG-03_1_formulario_preenchido_email_inexistente.png)<br>2. ![Mensagem de erro](../evidencias/cenarios/CT-LOG-03_1_mensagem_de_erro.png) |
