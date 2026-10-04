# Análise de Experiência do Usuário (UX)

## Introdução

Este documento reúne as oportunidades de melhoria na experiência do usuário (UX) identificadas no LogiTrack Pro durante a exploração do sistema e a execução dos cenários de teste (ver `01-cenarios-de-teste.md`). As observações foram feitas por navegação manual no navegador, em visualização desktop.

Foram analisadas as telas de Login e Cadastro, o menu lateral, o Dashboard, a listagem de Veículos e as mensagens de erro das telas de Manutenção e Veículos. Os pontos observados dizem respeito à consistência e hierarquia visual, ao aproveitamento do espaço, à densidade de informação, à usabilidade de componentes e à clareza das mensagens.

Cada melhoria é apresentada com a estrutura solicitada no desafio: funcionalidade ou tela analisada, situação identificada, alteração recomendada, justificativa da melhoria e benefício esperado para o usuário. As melhorias não são defeitos funcionais, que estão registrados em `04-bugs.md`.

## Resumo das melhorias

| Nº | Melhoria | Tela analisada |
|---|---|---|
| 1 | Harmonia e Hierarquia Visual da Marca | Telas de Login, Cadastro e Menu Lateral |
| 2 | Aproveitamento do Espaço Visual no Login | Tela de Login e Cadastro (Visualização Desktop) |
| 3 | Otimização do Espaço e Densidade de Informação nos Cards | Tela principal (dashboard) |
| 4 | Otimização do Componente de Paginação | Tela de listagem de veículos |
| 5 | Padronização e Clareza nas Mensagens de Erro | Telas de Manutenção e Veículos |
| 6 | Responsividade das Tabelas e Paginação na Versão Mobile | Telas de listagem (Veículos, Viagens e Manutenção) no acesso por dispositivos móveis |

## Detalhamento das melhorias

### 1. Harmonia e Hierarquia Visual da Marca

| Campo | Descrição |
|---|---|
| **Funcionalidade ou Tela Analisada** | Telas de Login, Cadastro e Menu Lateral. |
| **Situação Identificada** | A logomarca (LogiTrack) apresenta proporções reduzidas e está posicionada de forma isolada no canto superior esquerdo da tela de login, criando um grande espaço vazio e desequilibrando a composição visual da página. |
| **Alteração Recomendada** | Aumentar a proporção da logo e centralizá-la na tela, posicionando-a logo acima do título "Bem-vindo de volta" e do formulário de autenticação. No menu lateral, ajustar o tamanho e o alinhamento para que fiquem harmônicos em relação aos itens de navegação. |
| **Justificativa da Melhoria** | O posicionamento e tamanho atuais quebram a harmonia e a hierarquia visual da interface. Centralizar a marca junto ao formulário agrupa os elementos de forma lógica e preenche melhor o espaço em branco. |
| **Benefício Esperado pelo Usuário** | Proporcionar uma interface mais simétrica, agradável e equilibrada visualmente. Isso gera uma primeira impressão muito mais positiva, transmitindo maior profissionalismo, segurança e credibilidade logo no primeiro contato do usuário com o sistema. |

### 2. Aproveitamento do Espaço Visual no Login

| Campo | Descrição |
|---|---|
| **Funcionalidade ou Tela Analisada** | Tela de Login e Cadastro (Visualização Desktop). |
| **Situação Identificada** | A metade direita da tela é preenchida inteiramente por um bloco de cor azul sólida, sem nenhum elemento visual, texto de apoio ou contexto sobre a aplicação. |
| **Alteração Recomendada** | Substituir o bloco de cor sólida por uma fotografia de alta qualidade relacionada ao setor de logística ou adicionar uma ilustração vetorial acompanhada de uma breve frase destacando o valor do LogiTrack Pro. |
| **Justificativa da Melhoria** | O padrão de layout com tela dividida é eficaz, mas manter metade da área útil do monitor vazia gera uma sensação de desequilíbrio e sistema incompleto. A utilização de recursos visuais contextuais preenche o espaço de forma inteligente e reforça a identidade do produto. |
| **Benefício Esperado pelo Usuário** | Torna o primeiro contato com o sistema mais imersivo e acolhedor. Consequentemente, aumenta a percepção de profissionalismo e confiabilidade da ferramenta logo no momento da autenticação. |

### 3. Otimização do Espaço e Densidade de Informação nos Cards

| Campo | Descrição |
|---|---|
| **Funcionalidade ou Tela Analisada** | Tela principal (dashboard). |
| **Situação Identificada** | Os cards de indicadores, especialmente "Volume por Categoria" e "Projeção Financeira", possuem dimensões exageradas em proporção à pequena quantidade de dados que exibem, resultando em um grande espaço em branco. O card "Total de KM Percorrido" ocupa toda a largura da tela superior apenas para exibir um único valor numérico e um filtro. |
| **Alteração Recomendada** | Reduzir o tamanho físico dos cards para um layout mais compacto, permitindo agrupar mais indicadores na mesma linha horizontal. Caso o tamanho grande seja mantido, recomenda-se preencher o espaço ocioso com recursos visuais úteis, como gráficos. |
| **Justificativa da melhoria** | Dashboards eficientes devem priorizar a exibição consolidada de métricas relevantes na primeira área visível da tela. O layout atual dispersa informações simples em blocos muito grandes, obrigando o usuário a rolar a página para conseguir visualizar o panorama completo da operação. |
| **Benefício esperado para o usuário** | Proporciona uma visão gerencial mais ágil e rica. Aumenta a velocidade de leitura dos dados, permitindo que o gestor analise o desempenho da frota e tome decisões rapidamente, sem precisar navegar excessivamente pela interface. |

### 4. Otimização do Componente de Paginação

| Campo | Descrição |
|---|---|
| **Funcionalidade ou Tela Analisada** | Tela de listagem de veículos. |
| **Situação identificada** | O controle de paginação exibe simultaneamente todos os números de páginas disponíveis (atualmente de 1 a 26), o que cria uma longa fila de números e gera poluição visual no rodapé da tabela. |
| **Alteração recomendada** | Implementar um limite de exibição para os botões de página. Por exemplo, exibir apenas 5 a 10 botões visíveis de uma vez e atualizar a numeração dinamicamente à medida que o usuário avança para as páginas seguintes. |
| **Justificativa da melhoria** | Exibir dezenas de números lado a lado sobrecarrega a interface e foge das boas práticas de UI para listas extensas. Limitar os números visíveis economiza espaço horizontal e mantém o layout organizado mesmo quando o volume de dados cresce consideravelmente. |
| **Benefício esperado para o usuário** | Reduz a carga cognitiva e a poluição visual da tela. A navegação torna-se mais clara, objetiva e alinhada aos padrões modernos de sistemas web, melhorando a experiência ao consultar grandes volumes de registros. |

### 5. Padronização e Clareza nas Mensagens de Erro

| Campo | Descrição |
|---|---|
| **Funcionalidade ou tela analisada** | Telas de "Manutenção" e "Veículos" - Mensagens de Erro. |
| **Situação identificada** | Ao acionar validações do sistema, como tentar salvar um custo zerado ou negativo na manutenção, ou cadastrar uma placa de veículo duplicada, o sistema retorna mensagens de erro técnicas e em inglês (ex: "Validation failed" e "Veiculo with placa 'ADF-1565' already exists"). |
| **Alteração recomendada** | Traduzir todas as mensagens de retorno para o português e torná-las mais descritivas. Por exemplo, substituir "Validation failed" por "O custo estimado deve ser maior que zero" e alterar o erro de duplicidade para "Esta placa já está cadastrada no sistema". |
| **Justificativa da melhoria** | O sistema possui sua interface totalmente em português, mas expõe retornos brutos do banco de dados/backend em inglês, isso quebra a consistência do sistema. |
| **Benefício esperado para o usuário** | Permite que o usuário compreenda instantaneamente o motivo do erro sem precisar de conhecimentos em inglês ou termos técnicos. |

### 6. Responsividade das Tabelas e Paginação na Versão Mobile

| Campo | Descrição |
|---|---|
| **Funcionalidade ou tela analisada** | Telas de listagem (Veículos, Viagens e Manutenção) no acesso por dispositivos móveis. |
| **Situação identificada** | O layout das tabelas não se adapta corretamente a telas menores. As colunas ficam espremidas, gerando rolagem horizontal ou empilhamento confuso de texto. Além disso, o componente de paginação quebra completamente, empurrando a numeração das páginas para uma linha isolada abaixo dos controles principais, ficando totalmente desalinhado. |
| **Alteração recomendada** | Para a versão mobile, substituir a visualização em formato de "Tabela" por uma lista de "Cards", onde cada registro (ex: um veículo ou uma viagem) seja um bloco com os dados empilhados verticalmente. Em relação à paginação, em telas pequenas deve-se ocultar a numeração extensa e exibir apenas os botões de "Anterior" (<) e "Próximo" (>), ou um botão de "Carregar mais". |
| **Justificativa da melhoria** | Tabelas complexas perdem usabilidade em smartphones devido à restrição de espaço horizontal, forçando rolagens desconfortáveis e quebra de componentes. Converter tabelas em cards no mobile é a principal boa prática de design responsivo. |
| **Benefício esperado para o usuário** | Permite que os usuários utilizem o sistema em campo, pelo celular, com facilidade e conforto. Uma interface verdadeiramente responsiva evita toques acidentais e facilita a leitura das informações. |
