### BUG-01 - Login aceita qualquer senha para e-mail cadastrado

- **Severidade:** Crítica
- **Cenário de origem:** CT02
- **Descrição:** Ao informar um e-mail cadastrado com uma senha incorreta, o sistema concede acesso à conta sem exibir erro. Com e-mail inexistente, o bloqueio funciona normalmente (CT03).
- **Passos para reproduzir:**
  1. Abrir a tela de login
  2. Informar e-mail cadastrado: logap@teste.com
  3. Informar senha incorreta (ex.: 12345)
  4. Clicar em "Entrar"
- **Resultado esperado:** Acesso negado, com mensagem de credenciais inválidas.
- **Resultado obtido:** Acesso concedido; a requisição de login retornou status 200 e o dashboard foi carregado com os dados.
- **Impacto:** Falha de autenticação. Qualquer pessoa que conheça um e-mail cadastrado acessa dados de veículos, viagens, manutenções e indicadores financeiros.
- **Observação:** O comportamento foi reproduzido com senhas diferentes.
- **Evidência:** ![BUG-01](../evidencias/bugs/BUG01.png)
