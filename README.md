# Firewall_Analysis

` Análise de Malware por crivo de um Firewall`

Projeto 2 - Ciência de Dados 

A Base de dados utilizada pode ser encontrada [aqui](https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data), tratando-se de uma plataforma da Universidade da Califórnia com grande quantidade de repositórios de Ciência dos Dados e Machine Learning open source.

### Autores
 - Letícia Coêlho Barbosa
 - Matheus Silva Melo de Oliveira

 Atualmente, navegar no meio cibernético tornou-se uma comunalidade, ficou mais fácil para os usuários navegarem, se comunicarem, compartilharem informações. Entretanto, essa nova realidade também trás ameaças. A disseminação de vírus, os ataques de hackers a todo tipo de máquina, seja pessoal ou corporativa, estão maiores do que nunca.

Para defender os nossos queridos celulares/tablets/computadores existem diversos programas e ferramentas que se propõem a defender o seu sistema, uma dessas técnicas utilizadas com esse objetivo é conhecida como Firewall.

De acordo com o tamanho da rede, a quantidade de dados produzidos pelos usuários na rede pode ser muito grande.
Dispositivos de firewall em uma rede podem permitir ou impedir tráfego de acordo com a política usada examinando o
dados. A configuração de firewalls é vital para a comunicaçãoredes funcionem de forma adequada e segura.Firewalls agem como controle portas para redes de computadores.

Entendendo a sua importância como "barreira" para o fluxo de dados, o Firewall é o responsável pelo controle dos dados transferidos de e para o seu computador através da internet, além de prevenir que informações pessoais ou confidenciais sejam transmitidas pelo seu computador para a internet e impedir a invasão da máquina por software malicioso.

Portanto, **o objetivo desse projeto é classificar e tentar prever, atraves das características da transação (Portas destino e cliente , Número de bytes total, entre outros), se determinada transação de dados será aceita ou negada/impedida pelo computador (Allow, deny or drop).**

### Divisão de tarefas

A divisão de tarefas feita de forma conjunta na maior parte do projeto , todavia os integrantes dividiram seu foco em algumas partes , conforme elucidado abaixo:

Leticia : Refinamento dos dados , outliers , valores nulos. Na parte de analise exploratória ficou responsável pela visualização de dados categóricos assim como pela maior parte das bibliotecas utilizadas no trabalho. Na seção de predição ficou responsável por parte da  introdução ao machine learning e da biblioteca utilizada, além dos modelos Logistic Regression e Random Florest.

Matheus :  Refinamento dos dados , outliers , valores nulos. Na parte de analise exploratória ficou responsável pela visualização de dados numéricos assim como pela maior parte das bibliotecas iterativas (Ipywidgets) para predição utilizadas no trabalho. Na seção de predição ficou responsável por parte da introdução ao machine learning e conclusão geral,  além dos modelos KNN e Decision Tree.

De toda forma , resalta-se que o trabalho em conjunto foi fundamental para a realização do projeto.

### Para melhor Leitura e Interatividade

Para melhor leitura e compreensão do arquivo, assim como ter contato com inteirações e detalhes, clone o repositório utilizando: 

` git clone https://github.com/leticiacb1/Firewall_Analysis`

Clique em Aplicação Prática e veja você mesmo o funcionamento do modelo para diferentes parâmetros de acordo com os atributos do Dataset.

**Ressalta-se que para a melhor analise e utilização do projeto é recomendado que seja feita a clonagem do repositorio**
 
### Bibliotecas Necessárias

 Para o funcionamento adequado será necessária a instalação das seguintes bibliotecas, caso não as possua:

 
 - sklearn
 - scipy
 - matplotlib
 - seaborn 
 - time
 - pandas
 - numpy
 - yellowbrick
 - graphviz
 - ipywidgets
 

### Bibliografias Principais

Muller,Andreas e Guido,Sarah  ; **Introduction to Machine Learning with Python** , 1° Edição , editora O'Reilly Media , 2016.

[Towards Data Science](https://towardsdatascience.com/)

[Saed](http://www.saedsayad.com/)

 - <em>Projeto Finalizado</em>
 <center><img src="firewall_assets/giphy.gif" width=600 style="float: center; margin: 0px 0px 10px 10px"></center>
