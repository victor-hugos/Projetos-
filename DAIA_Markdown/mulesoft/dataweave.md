# DataWeave


:::info
<https://dataweave.mulesoft.com/learn/dataweave>

:::

# O que é DataWeave

É uma linguagem de programação com foco em Transformação de Dados. Utilizando DataWeave você pode facilmente ler, manipular e escrever dados em quaisquer formatos aceitos.

É principalmente usada dentro da MuleSoft e seus sistemas, mas também possui uma CLI (Comand line Interface) que pode ser executada em qualquer ambiente.

O principal objetivo da DataWeave é facilitar a transformação de data, sem precisar se preocupar com a melhor forma, ou a forma mais eficiente, uma vez que a DataWeave possui uma forma canônica de resolver essas transformações.

 ![](/api/attachments.redirect?id=505a3feb-c59c-494a-b08f-b50ae38aa489)

\
# Tutorial de uso do DataWeave

<https://dataweave.mulesoft.com/learn/tutorial>

Também é possível consultar mais detalhes em: <https://github.com/mulesoft/data-weave-tutorial/tree/master>

\
## DataWeave

Ao criar um script DataWeave, a linguagem executa algumas ações “por baixo dos panos", sendo elas:

* Quando DataWave recebe algum dado, primeiro passa o dado por um processo conhecido como “*Reader*" , que transforma esse dado para o formato canônico;
* Em seguida envia o dado para o script que executa as ações definidas seguindo outro modelo canônico
* Por fim o script envia os dados transformados para outro processo conhecido como “*Writer*" que tem como responsabilidade transformar o dado do modelo canônico para o formato definido para o “output" da operação.

\
## MIME Types

Um Tipo MIME (**Multipurpose Internet Mail Extensions)** é um padrão conhecido e muito utilizado na web, e sendo assim são usados como base para definir os formatos de Entrada (input) e saída (output) dos scripts DataWeave. Existe uma grande quantidade de tipos MIME disponíveis, e por isso DataWeave trabalha com um [conjunto menor deles](https://docs.mulesoft.com/dataweave/latest/dataweave-formats), de forma que seja abrangente e mais fácil de trabalhar.

Desde a versão 2.3 para definir qual MIME type será usado na operação podemos utilizar um ID simples como por exemplo: json, xml, csv e etc.

\
### Exemplo de Transformação de formatos

A seguir um exemplo de uma transformação onde os dados chegam em formato JSON e são transformados para CSV

#### INPUT

```javascript
[
  {
      "firstName": "John",
      "lastName": "Smith",
      "age": 45
  },
  {
      "firstName": "Jane",
      "lastName": "Doe",
      "age": 34
  }
]
```

#### SCRIPT DW

```yaml
%dw 2.0
input payload json
output csv header=false
---
payload
```

#### OUTPUT

```javascript
John,Smith,45
Jane,Doe,34
```

> Para incluir os nomes dos campos, basta alterar output csv header=false para true

\
## Anatomia de um script DataWeave

```javascript
%dw 2.0
input payload json
output csv header=false
---
payload
```

Esse script simples é o mesmo que usamos acima, e converte um input json em um output csv, mas vamos analisar linha por linha o que está acontecendo

> No caso desse scripts as três primeiras linhas detalham as diretivas (directives)


1. É a diretiva para todos os arquivos DataWeave e determina qual versão o script está usando
2. É a diretiva de input que permite nomear o input, definir como será lido 

   
   1. O input segue o seguinte padrão: `input <var_name> <mime_type> [<reader_properties>]`
3. É a diretiva de output que permite definir qual formato será escrito e as propriedades associadas a esse "writer"

   
   1. O output segue o seguinte padrão: `output <mime_type> [<writer_properties>]`
4. É uma linha usada para separar as diretivas e a lógica de output, numa ideia parecida com a separação de Headers e Body
5. Aqui começa a lógica de output do script

   
   1. No caso apenas apresenta o payload, após a transformação, mas aqui que deve ficar a lógica de execução e output do script.


:::tip
O seu script pode contar mais diretivas como a declaração de funções e/ou variáveis que podem ser reutilizadas no seu script.

:::

\
# Criando Dados

DataWeave trabalha com um grande conjunto de tipos que podem ser encontrados em: <https://docs.mulesoft.com/dataweave/2.4/dataweave-type-system>

Para esse tutorial usaremos os seguintes tipos:

* Number
* String
* Boolean
* Array
  * Para um Array o seu tipo sempre será Array<T>, onde T é um tipo que é utilizado dentro do array
* Object or { }
  * Na declaração de objetos, os pareces de Chave-Valor (Key-value) podem definir seus próprios tipos. Por exemplo um objecto que contém apenas uma chave “nome" com um valor do tipo "string" seria: `{name : String}` . Porém o resultado da função typeOf retornaria apenas "objeto"

\
## Strings

São definidas ao utilizar “Aspas".

> DataWeave permite a utilização de aspas simples ‘ ‘ ou aspas duplas “ “, o detalhe é que uma aspa simples só pode ser “fechada" por outra aspa simples e da mesma forma para aspas duplas

\
## Numbers

O tipo Number suporta tanto números inteiros como números "Ponto-flutuante". Sendo assim tanto números inteiros como `1,2,3,4,5` como números “com vírgula" (Importante lembrar que nesse caso utilizamos o ponto ( . ) para separar o número das casas decimais) `3.1415 , 2.71828` são considerados do tipo: Number

\
## Booleans

O tipo Booleano possui apenas dois valores possíveis:

* true
  * ou sim ou 1
* false
  * ou não ou 0

O tipo booleano é muito utilizado para lidar com lógica condicional, por exemplo ao utilizar um if.

\
## Arrays

Arrays são uma série ordenada de valores que podem ser de qualquer tipo, permitindo inclusive que você tenha tipos diferentes dentro de um mesmo array, como por exemplo:

```javascript
%dw 2.0
output json
---
[false, "1", 2, "3", 4, "five"]
```

\
## Objects

Objetos são uma série de mapeamentos entre uma chave e um valor, sendo que o último pode ser de qualquer tipo (incluindo outro objeto)

```javascript
%dw 2.0
output json
---
{
  one: [1],
  two: "2",
  three: {
      A: "AAA"
  }
}
```


:::tip
DataWeave permite chaves repetidas em um objeto! 

:::

Pode soar um pouco estranho, mas como o código é convertido em XML isso passa a fazer mais sentido. Por exemplo o objeto a seguir:

```json
{
    titles: {
        title: "Titanic",
        title: "Avatar"
    }
}
```

Ao ser convertido para xml, se torna:

```markup
<?xml version='1.0' encoding='UTF-8'?>
<titles>
  <title>Titanic</title>
  <title>Avatar</title>
</titles>
```

\
# Lendo dados

DataWeave oferece uma lista de seletores ("[selectors](https://docs.mulesoft.com/dataweave/latest/dataweave-selectors)") que permitem navegar qualquer combinação de objetos e arrays para pegar o dado que você precisa. Nesse tutorial vamos focar em:

* Single-value selector: .
* Index selector: \[n\]
* Range selector: \[n to m\]
* Multi-value selector: .\*
* Descendants selector: ..

Podemos também pensar em selectors como uma forma de buscar (query) nos seus dados.

\
## Seletor de valor único (Single Value Selector)


:::info
.

:::

O seletor de valor único ( . ) permite buscar os valores de um objeto utilizando sua chave. Por exemplo:

INPUT

```javascript
{
  "name": "Ana",
  "age": 29
}
```

DW SCRIPT

```javascript
%dw 2.0
output json
---
payload.age
```

OUTPUT

```javascript
29
```

Também é possível utilizar colchetes \[ \] ao invés de usar o ponto. Isso permite fazer algumas coisas úteis, como usar uma chave dinâmica:

INPUT

```javascript
{
  "name": "Ana",
  "age": 29,
  "dynamicKey": "age"
}
```

DW Script:

```javascript
%dw 2.0
output json
---
{
  fixed: payload.age,
  dynamic: payload[payload.dynamicKey]
}
```

Output:

```javascript
{
  "fixed": 29,
  "dynamic": 29
}
```

## Seletor de índice (Index Selector)


:::info
\[ n \]

:::

O seletor de índice é utilizado em Arrays, e permite buscar o valor armazenado na posição que foi solicitada, por exemplo Array\[0\] retorna o primeiro valor no Array.

Input:

```javascript
["prod", "qa", "dev"]
```

DW Script:

```javascript
%dw 2.0
output json
---
payload[1]
```

Output:

```javascript
"qa"
```


:::warning
DataWeave utiliza 0-based arrays, ou seja a primeira posição do array começa em 0, a segunda em 1 e assim por diante.

:::

E assim como em Python também é possível utilizar índices negativos, onde -1 busca pelo último elemento do array, -2 pelo penúltimo e etc

## Seletor de  Amplitude (Range Selector)


:::info
\[ n to m \]

:::

Se você precisa selecionar múltiplos valores sequenciais em um array você pode usar o Range Selector ( \[ n to m \] ). Dessa forma o retorno é um array do tamanho do range especificado.

Input:

```javascript
["prod", "qa", "dev"]
```

DW Script:

```javascript
%dw 2.0
output json
---
payload[0 to 1]
```

Output:

```javascript
["prod", "qa"]
```


:::tip
Aqui também é possível utilizar indices negativos

:::

Ao utilizar índices negativos em um range, podemos inverter a ordem de um array, por exemplo:

Input:

```javascript
["prod", "qa", "dev"]
```

DW Script:

```javascript
%dw 2.0
output json
---
payload[-1 to -3]
```

Output:

```javascript
[ "dev", "qa", "prod" ]
```

## Seletor de múltiplos valores (Multi Value Selector)


:::info
\[ .\* \]

:::

O seletor de múltiplos valores retorna um array com todos os valores que correspondem a chave utilizada.

Apesar de funcionar tanto para Arrays como para Objetos o comportamento do MVS é diferente para cada um dos tipos

### Objeto

O MVS busca o valor de todas as chaves que combinam com o que foi solicitado e retorna um array com essas informações. É muito útil quando estamos trabalhando com um objeto com chaves repetidas.

Input:

```javascript
{
  "name": "Emilia",
  "name": "Isobel",
  "name": "Euphemia",
  "name": "Rose",
  "surname": "Clarke"
}
```

DW Script:

```javascript
%dw 2.0
output json
---
payload.*name
```

Output:

```javascript
["Emilia", "Isobel", "Euphemia", "Rose"]
```

### Array

No caso do uso em um array, ele vai buscar todos os elementos do array que sejam do tipo Objeto e aplicar a busca dentro de cada um dos objetos.

Input:

```javascript
[
  {
    "price": 1,
    "price": 2
  },
  {
    "price": 3,
    "price": 4
  },
  {
    "price": 5,
    "price": 6
  },
  {
    "name": "Starburst",
    "category": "Candy"
  }
]
```

DW Script:

```javascript
%dw 2.0
output json
---
payload.*price
```

Output:

```javascript
[1, 2, 3, 4, 5, 6]
```

## Seletor "Descendente“ (Descendants Selector)


:::info
( . . )

:::

O Seletor descendente é a ferramenta perfeita para quando você quer selecionar os valores de uma chave não importando onde ela apareça.

Input:

```javascript
{
  "echo": {"value": "Hello there!"},
  "sequence": [
    {
      "echo": "Getting details...",
      "try": {
        "curl": "somelocation.com",
        "echo": "Success!"
      }
    },
    {
      "grep": "Success"
    }
  ]
}
```

DW Script:

```javascript
%dw 2.0
output json
---
payload..echo
```

Output:

```javascript
[{ "value": "Hello there!"}, "Getting details...", "Success!"]
```

> Esse seletor pode ser usado em conjunto com o MVS para buscar também as chaves repetidas.

\
# Variáveis

Variáveis são uma forma de armazenar valores com um determinado nome para ser reutilizado em diferentes partes do seu código.

## Acessando uma variável

Para criar a variável usamos a seguinte syntax:

`var <nome_da_variavel> = <expressão>`

A expressão é algo que retorna um valor, ou o valor em si.

#### DW Script:

```javascript
%dw 2.0
output json
var mascot = "Max the Mule"
---
mascot
```

#### Output:

```javascript
"Max the Mule"
```

> As variáveis são quase sempre declaradas no "Header”(diretivas) do script.

# Operadores lógicos

[Operadores](https://docs.mulesoft.com/dataweave/latest/dw-operators) permitem comparar valores e te oferecer a base para começar a tomada de decisões.

Os operadores lógicos permite resolver expressões do tipo verdadeiro ou falso ( `true/false` ).

| Expressão | Descrição |
|----|----|
| A > B | Maior que (Greater than) |
| A < B | Menor que (Less than) |
| A >= B | Maior ou igual (Greater than or equal to) |
| A <= B | Menor ou igual (Less than or equal to) |
| A == B | Igual (Equal to) |
| A != B | Não Igual (Not equal to) |
| A \~= B | Similar ou parecido (Similar to) |
| not A | Negação Lógica (Logical negation) |
| !A | Negação Lógica (Logical negation) |
| A and B | E (Logical and) |
| A or B | Ou (Logical or) |

\
# Controle de Fluxo

Controle de fluxo é usado quando você deseja executar algumas partes do seu código em algumas situações e não executar outras. Em outras palavras é a forma de adicionar lógica ao seu script.

## If/else

Expressões de if/else são usadas para decidir qual pedaço de código será executado a partir de operadores lógicos. Segue a seguinte sintaxe:

```javascript
if (<critério>) <código se verdadeiro> 
else <código se falso>
```

Input:

```javascript
{
  "price": 120.00
}
```

DW Script:

```javascript
%dw 2.0
output json
var action = if (payload.price < 100) "buy" else "hold"
---
{
  price  : payload.price,
  action : action
}
```

Output:

```javascript
{
  "price": 120.00,
  "action": "hold"
}
```

Outra possibilidade é encadear expressões de `if/ else if/ … / else.`

```javascript
if (<criteria_expression1>)
  <return_if_true>
else if (<criteria_expression2>)
  <return_if_true>
else
  <return_if_no_other_match>
```

## Correspondência de Padrões com Valores Literais (Literal Pattern Matching)


:::tip
Parecido com a lógica de "Switch" em *C* ou "*Case When"* em SQL

:::

Outra forma de controlar o fluxo do script é através do uso de Correspondência de Padrões com Valores Literais (ou [LPM](https://docs.mulesoft.com/dataweave/latest/dataweave-pattern-matching)).

Assim como If/else LPM retorna um único valor porém executa outros processos e possui uma sintaxe um pouco mais complexa:

```javascript
<expressão de input> match {
  case <condição> -> <executar se a condição passar>
  case <condição> -> <executar se a condição passar>
  else -> <executar se nenhuma condição passar>
}
```

Input:

```javascript
{
  "action": "buy"
}
```

DW Script:

```javascript
%dw 2.0
output json
---
payload.action match {
  case "buy"  -> “Buy at market price"
  case "sell" -> "Sell at market price"
  case "hold" -> “Hold asset"
  else   -> "Invalid input"
}
```

Output:

```javascript
"Buy at market price"
```

\
# Functions

## Funções Nomeadas (Named Functions)


:::info
fun <function_name>(<arg1>, <arg2>, …, <argN>) = <body>

:::

As funções devem ser declaradas na área de Declarações ("Header") utilizando a palavra-chave fun seguindo a seguinte sintaxe:

```typescript
fun <function_name>(<arg1>, <arg2>, …, <argN>) = <body>
```

E para chamar a função usamos a seguinte sintaxe:

```javascript
<function_name>(<arg1>, <arg2>, …, <argN>)
```

#### DW Script:

```javascript
%dw 2.0
output json

fun add(n, m) =
  n + m
---
add(1,2)
```

#### Output:

```javascript
3
```

> Note que funções DataWeave não precisam usar a palavra-chave
>
> ```javascript
> return
> ```
>
>  visto que praticamente tudo em DataWeave é uma expressão e todas as expressões retornam algum tipo de dado

## Escopo da Função (Function Scope)

É muito comum criar um escopo para as funções, onde nós declaramos variáveis e até mesmo outras funções. O escopo é criado utilizando a palavra-chave do e funciona permitindo que tudo que está definido em seu cabeçalho(Área de declarações ou Header) disponível para o Body da função mas não após isso.

#### DW Script:

```javascript
%dw 2.0
output json

fun diff(n) = do {
  var start = n[0]
  var end = n[-1]
  ---
  end - start
}

---
diff([1990, 1995, 2002, 2008, 2021])
```

#### Output:

```javascript
31
```

## Lambdas


:::info
(<arg1>, <arg2>, …, <argN>) -> body

:::

Assim como as funções nomeadas, temos também as funções sem nomes, chamadas de Lambda.

Lambdas é um valor no DataWeave, assim como uma String, um Objeto ou um booleano, e segue a sintaxe:

```javascript
(<arg1>, <arg2>, …, <argN>) -> body
```

#### DW Script

```javascript
%dw 2.0
output json
---
() -> 2 + 3
```

#### Output

```javascript
<ERROR>
```

Você pode estar se perguntando, o porque o output foi um erro e não o resultado: 5. Lembre-se que toda função precisa ser chamada. Da forma como foi escrito a função nunca é chamada, e por isso não pode ser executada. Sendo assim para que ela seja executada precisamos adicionar um ( ) ao final para indicar que a função está sendo chamada e precisamos também colocar a lambda dentro de ( ) para indicar que aquela expressão inteira é uma Lambda.

#### DW Script

```javascript
%dw 2.0
output json
---
(() -> 2 + 3)()
```

#### Output

```javascript
5
```

> A sintaxe parece estranha pois essa não é a forma que uma lambda deveria ser usada. Lambdas são valores, assim como Strings, sendo assim nós podemos atribuir o valor a uma variável o que daria um nome para a função sem nome e permitiria usa-la como uma função normal.

#### DW Script

```javascript
%dw 2.0
output json

var add = (n, m) -> n + m
---
add(2, 3)
```

#### Output

```javascript
5
```

Mesmo assim, continua não sendo muito útil, uma vez que já possuímos uma sintaxe com o uso de fun.

A utilidade das Lambdas fica mais clara quando combinamos duas ideias:


1. Lambdas são valores, assim como strings, Objetos e Booleanos
2. Valores podem ser passado para funções como argumento, assim como retornados por funções

Em outras palavras, Lambdas se tornam úteis quando você precisa passar funções como argumento para outras funções, ou retornar uma função a partir de outra.

Uma função que faz isso é referida como high-order-function (HOF).

Vamos usar o exemplo a seguir para explicar melhor, nele utilizamos a HOF \`filter\` para garantir que o Array contenha apenas números ímpares.

#### DW Script:

```javascript
%dw 2.0
output json

fun isOddNum(n) =
  (n mod 2) == 1

// Generate [1, 2, ..., 5]
var numbers = (1 to 5)
---
filter(numbers, (n, idx) -> isOddNum(n))
```

#### Output:

```javascript
[1,3,5]
```

A função filter recebe dois argumentos, um Array e uma Lambda. Nesses casos é importante especificar o que a função Lambda faz, nesse caso ela deve pegar dois argumentos:


1. Um item de um array
2. O indice desse item

E deve retornar um valor booleano, que determina se o valor deveria ser retornado no Array ou não.

#### DW Script:

```javascript
%dw 2.0
output json

var numbers = (1 to 5)
---
filter(numbers, (n, idx) -> (n mod 2) == 1)
```

#### Output:

```javascript
[1,3,5]
```

## Infix Notation


:::info
<arg1> <function_name> <arg2>

:::

Até agora nós chamamos a função filter usando a notação prefix, que significa colocar o nome da função antes dos argumentos. Porém, caso a função receba 2 argumentos, DataWeave permite que você chame utilizando a notação infix, que segue a seguinte sintaxe:

```javascript
<arg1> <function_name> <arg2>
```

Essa é a sintaxe preferida para praticamente todas as funções que recebem um lambda como o segundo parâmetro . Aqui um exemplo de como o código anterior fica, utilizando a notação Infix.

#### DW Script:

```javascript
%dw 2.0
output json

var numbers = (1 to 5)
---
numbers filter ((n, idx) -> (n mod 2) == 1)
```

#### Output:

```javascript
[1,3,5]
```

> Isso pode não parecer muito vantajoso, mas permite facilmente encadear várias funções juntas. Por exemplo, podemos utilizar duas funções filter dessa forma de uma maneira mais fácil de ler e entender

#### DW Script:

```javascript
%dw 2.0
output json

var numbers = (1 to 5)
---
numbers
  filter ((n, idx) -> (n mod 2) == 1)
  filter ((n, idx) -> (n > 3))
```

#### Output:

```javascript
[5]
```

> Repare nos parenteses adicionais ao redor da primeira lambda, eles foram colocados para ajudar DataWeave a determinar onde a Lambda começa e acaba.

# Sintaxe $, $$ e $$$


:::info
func(a,b,c) → $.filter => a.filter

:::

HOFs são muito utilizadas na biblioteca DataWeave e por isso possui algumas sintaxes adicionais para facilitar seu uso. Para as funções que DataWeave oferece você pode representar o primeiro, segundo e terceiro argumentos utilizando $, $$ e $$$ respectivamente.

Dessa forma você não precisa especificar os argumentos da lambda quando você a passa para uma função. Por exemplo:

#### DW Script:

```javascript
%dw 2.0
output json

var numbers = (1 to 5)
---
numbers filter (($ mod 2) == 1)
```

#### Output:

```javascript
[1,3,5]
```

A sintaxe dollar nos dá as mesmas funcionalidades de quando passamos algo pelo nome. O que significa que podemos encadear seletores e índices diretamente no símbolo dollar para permitir buscar nos dados:

#### Input:

```javascript
[
  {
    "id": 1,
    "item": "cheese",
    "price": 4.00  
  },
  {
    "id": 2,
    "item": "steak",
    "price": 15.00  
  },
  {
    "id": 3,
    "item": "cereal",
    "price": 5.00  
  },
  {
    "id": 4,
    "item": "apples",
    "price": 2.00  
  }
]
```

#### DW Script:

```javascript
%dw 2.0
output json
---
payload filter $.price > 5
```

#### Output:

```javascript
[
  {
    "id": 2,
    "item": "steak",
    "price": 15.00  
  }
]
```

\
