# Wave Encoder

### Esse código roda uma interface em python, que faz codificações de sequencias de bits em ondas, com métodos de comunicação de dados

## Como rodar

### Dependências
!sudo apt install python3 

!sudo apt-get install python-pip

%pip3 install numpy

%pip3 install matplotlib

%pip3 install pygame

### Código principal
!python3 main.py

## Tipos de Codificação de Ondas implementadas

### NRZ-L
O nível da voltagem representa o valor do bit, um nível é selecionado para representar bits zero,
enquanto outro é selecionado para representar bits 1.

Lei de Formação: A lei de formação do NRZ-L é simples - o bit "1" é representado por uma tensão positiva
e o bit "0" é representado por uma tensão negativa. O nível de tensão é mantido constante durante a duração do bit.

Sincronismo: O NRZ-L não usa uma técnica de sincronismo, o que significa que não há informações adicionais (como um 
clock ou um sinal de início/fim) no sinal codificado que indiquem o início ou o fim de um byte ou quadro de dados.
Isso pode levar a problemas de sincronização se ocorrerem erros de transmissão, o que pode resultar em dados corrompidos.

Componente DC: O NRZ-L tem uma componente DC (corrente contínua) significativa, o que significa que há uma quantidade
substancial de energia de baixa frequência presente no sinal. Isso pode causar problemas para o receptor, como a
saturação do amplificador ou a polarização do sinal.

Imunidade a ruídos: O NRZ-L não é muito imune a ruídos, pois a presença de uma única transição de bit incorreta pode
causar erros em vários bits subsequentes. Isso significa que o NRZ-L pode ser mais suscetível a erros de transmissão
em comparação com outras técnicas de codificação de linha.

Aplicação prática: O NRZ-L é usado em várias aplicações práticas, incluindo transmissão de dados em redes Ethernet,
em unidades de disco rígido e em transmissão de sinais de vídeo digital. No entanto, ele é frequentemente usado em
conjunto com outras técnicas de codificação de linha (como Manchester ou AMI) para melhorar a integridade dos dados transmitidos.

![image](https://user-images.githubusercontent.com/85199336/234344464-5ee74aa7-fc6d-4d9f-a8c2-4bcf2da693eb.png)

### NRZ-I
O nível da voltagem muda para representar um bit 1 e permanece o mesmo para representar um bit 0.

Lei de Formação: A lei de formação do NRZ-I é semelhante à do NRZ-L - o bit "1" é representado por
uma mudança de polaridade (ou transição) na tensão e o bit "0" é representado por uma ausência de
transição na tensão. A diferença é que, no NRZ-I, a polaridade da transição depende do valor do bit
anterior. Se o bit anterior for "1", a polaridade da transição será invertida e, se o bit anterior 
for "0", a polaridade da transição será mantida.

Sincronismo: O NRZ-I também não usa uma técnica de sincronismo, o que significa que pode ocorrer 
deslocamento de bit ou erros de sincronização em caso de perda de bits ou devido a ruídos.

Componente DC: O NRZ-I tem uma componente DC muito menor em comparação com o NRZ-L, pois as 
transições no sinal resultam em uma média de tensão próxima a zero.

Imunidade a ruídos: O NRZ-I é mais imune a ruídos em comparação com o NRZ-L, pois as transições 
no sinal reduzem a sensibilidade a erros devido a ruídos. No entanto, se ocorrerem muitas transições, 
isso pode resultar em uma alta taxa de erro.

Aplicação prática: O NRZ-I é amplamente utilizado em aplicações de transmissão de dados de alta 
velocidade, como em redes de computadores, telefonia e equipamentos de comunicação óptica. 
No entanto, como mencionado anteriormente, o NRZ-I pode sofrer problemas de sincronização e 
não é tão imune a ruídos quanto outras técnicas de codificação de linha.


![image](https://user-images.githubusercontent.com/85199336/234344818-84350f7b-11e0-4502-bdfa-d3532ca97f03.png)

### AMI
Bit 0 é representado por 0, enquanto um bit 1 é representado por um nível de tensão positivo ou negativo alternado.

Lei de Formação: A lei de formação do AMI é semelhante à do NRZ-L, onde o bit "1" é representado por uma mudança
de polaridade e o bit "0" é representado por ausência de transição. No entanto, a polaridade da transição é
alternada a cada bit "1". Por exemplo, o primeiro bit "1" é representado por uma tensão positiva, o segundo bit "1"
é representado por uma tensão negativa e assim por diante.

Sincronismo: O AMI não usa uma técnica de sincronismo, o que significa que pode ocorrer deslocamento de bit ou
erros de sincronização em caso de perda de bits ou devido a ruídos.

Componente DC: O AMI tem uma componente DC muito menor em comparação com o NRZ-L, pois as transições no sinal
resultam em uma média de tensão próxima a zero.

Imunidade a ruídos: O AMI é mais imune a ruídos em comparação com o NRZ-L, pois as transições no sinal reduzem a
sensibilidade a erros devido a ruídos. No entanto, se ocorrerem muitas transições, isso pode resultar em uma
alta taxa de erro.

Aplicação prática: O AMI é amplamente utilizado em aplicações de transmissão de dados de alta velocidade, 
como em redes de computadores, telefonia e equipamentos de comunicação óptica. O AMI é considerado uma 
técnica de codificação de linha eficiente em termos de largura de banda e é frequentemente usado em conjunto 
com outras técnicas de codificação de linha, como o Manchester, para aumentar a confiabilidade da transmissão de dados.


![image](https://user-images.githubusercontent.com/85199336/234345007-9d206552-6bdf-4bc7-b09f-5686ae6ea6b8.png)

### PSEUDOTERNARIO
Bit 1 é representado por 0, enquanto um bit 0 é representado por um nível de tensão positivo ou negativo alternado

Lei de Formação: A lei de formação do pseudoternário é diferente do NRZ-L e AMI. Nessa técnica, o bit "0" é representado
por uma transição e o bit "1" é representado pela ausência de transição. O pseudoternário é chamado assim porque, ao contrário
do método AMI, não há alternância de polaridade para os bits "1", o que o torna "pseudo" em vez de "verdadeiro" ternário.

Sincronismo: O pseudoternário não usa uma técnica de sincronismo, o que significa que pode ocorrer deslocamento de bit ou erros
de sincronização em caso de perda de bits ou devido a ruídos.

Componente DC: O pseudoternário tem uma componente DC muito menor em comparação com o NRZ-L, pois as transições no sinal resultam
em uma média de tensão próxima a zero.

Imunidade a ruídos: O pseudoternário é mais imune a ruídos em comparação com o NRZ-L, pois as transições no sinal reduzem a
sensibilidade a erros devido a ruídos. No entanto, se ocorrerem muitas transições, isso pode resultar em uma alta taxa de erro.

Aplicação prática: O pseudoternário é usado em algumas aplicações de comunicação de dados, como em alguns sistemas de
telecomunicações e equipamentos de rede. No entanto, o pseudoternário é menos comum do que outras técnicas de codificação de linha,
como o NRZ-L e AMI, devido às suas características de codificação não convencionais.

![image](https://user-images.githubusercontent.com/85199336/234347078-691b00a8-e4ba-46b6-a43f-b969cadad13b.png)


### MANCHESTER
Duracao de um bit é dividida pela metade, na primeira metade o bit permanece em um nivel, depois desloca-se,
bit 0 é representado por uma transição de descida na voltagem, enquanto um bit 1 é representado por uma subida na
voltagem.

Lei de Formação: A lei de formação do Manchester é diferente das outras técnicas de codificação de linha. 
Nessa técnica, um bit "0" é representado pela transição do sinal de um nível para o outro no meio do intervalo de 
tempo do bit, enquanto um bit "1" é representado por uma transição no início do intervalo de tempo do bit. Isso significa 
que cada bit é dividido em dois intervalos de tempo iguais, onde a transição ocorre em cada um desses intervalos.

Sincronismo: O Manchester usa uma técnica de sincronismo chamada codificação de bits de início e fim. Isso significa 
que, no início de cada quadro de dados, é enviado um conjunto de bits especiais que servem como um sinal de sincronização 
para o receptor. O receptor usa esses bits para sincronizar o relógio com o transmissor e reconhecer o início e o fim de 
cada quadro de dados.

Componente DC: O Manchester não tem uma componente DC constante, pois há transições frequentes no sinal.

Imunidade a ruídos: O Manchester é mais imune a ruídos em comparação com outras técnicas de codificação de linha, 
pois cada bit é dividido em dois intervalos de tempo iguais, o que reduz a sensibilidade a erros devido a ruídos.
No entanto, o Manchester exige uma largura de banda maior do que outras técnicas de codificação de linha.

Aplicação prática: O Manchester é amplamente utilizado em aplicações de transmissão de dados de alta velocidade, 
como em redes de computadores, sistemas de automação industrial, equipamentos de comunicação óptica, entre outros. 
O Manchester é uma técnica de codificação de linha eficiente em termos de largura de banda e é frequentemente usado 
em conjunto com outras técnicas de codificação de linha, como o AMI, para aumentar a confiabilidade da transmissão de dados.

![image](https://user-images.githubusercontent.com/85199336/234347672-eef4b586-1ce1-4c8c-844b-0ea19907737b.png)

### MANCHESTER DIFERENCIAL
Existe sempre uma transição no meio do elemento, mas o valor é determinado no início. Se for 0, começa diferente da última voltagem e termina numa voltagem igual,
enquanto o bit 1 começa na última voltagem e termina numa voltagem diferente.
Manchester diferencial (também conhecido como Manchester diferencial bipolar) é uma variação do Manchester que tem algumas diferenças em 
relação à técnica original. As características do método Manchester diferencial são as seguintes:

Lei de Formação: A lei de formação do Manchester diferencial é similar ao Manchester. No entanto, em vez de codificar os dados 
diretamente com transições de nível, a técnica codifica a mudança de fase no início do intervalo de bit. O bit "1" é representado 
por uma mudança de fase, enquanto o bit "0" é representado pela ausência de mudança de fase. Além disso, a técnica Manchester 
diferencial codifica a polaridade da transição em vez do valor do bit.

Sincronismo: O Manchester diferencial usa a mesma técnica de sincronismo que o Manchester, ou seja, a codificação de bits de início e fim.

Componente DC: O Manchester diferencial não tem uma componente DC constante, pois as transições de fase são feitas com polaridades alternadas, 
gerando uma média de tensão zero.

Imunidade a ruídos: O Manchester diferencial é mais imune a ruídos em comparação com o Manchester e outras técnicas de codificação 
de linha, pois as transições de fase garantem que a polaridade das transições seja invertida a cada bit, reduzindo a sensibilidade 
a erros devido a ruídos.

Aplicação prática: O Manchester diferencial é amplamente utilizado em aplicações de transmissão de dados de alta velocidade, 
especialmente em redes de comunicação óptica e em alguns sistemas de automação industrial. Como outras técnicas de codificação 
de linha, o Manchester diferencial é usado para garantir a integridade dos dados durante a transmissão, minimizando os erros de transmissão.

![image](https://user-images.githubusercontent.com/85199336/234345807-667c6a47-4317-4056-b91e-3309ff563d46.png)

### MLT3
MLT-3 (Modified Lullabye Transmission Level 3) é uma técnica de codificação de linha usada em sistemas de telecomunicações para transmitir sinais digitais por meio 
de um meio físico, como um fio de cobre. Na codificação MLT-3, cada bit é representado por um sinal de três níveis. Os três níveis de sinal são tipicamente -1, 0 e +1. 
A lógica de codificação de MLT-3 é baseada no princípio de reduzir o número de zeros consecutivos no sinal transmitido. Isso ocorre porque sequências longas de zeros 
podem causar erros de sincronização e de temporização no receptor. Em MLT-3, um bit "0" é representado pela ausência de mudança no nível do sinal (ou seja, o sinal 
permanece no seu nível atual). Um bit "1" é representado por uma transição para o próximo nível de sinal. No entanto, em vez de transitar para o nível mais alto ou mais 
baixo do sinal, como em outras técnicas de codificação de linha, MLT-3 transita para o nível médio do sinal. Por exemplo, se o nível atual do sinal for 0 e o próximo bit 
a ser transmitido for um "1", o nível do sinal fará uma transição para +1. Se o próximo bit a ser transmitido for um "0", o nível do sinal permanecerá em +1. Se o próximo 
bit também for um "0", o nível do sinal fará uma transição para 0 (ou seja, o nível médio do sinal). O uso do nível médio do sinal para bits "1" reduz o número de zeros 
consecutivos no sinal transmitido, o que melhora a sincronização e a temporização no receptor. Além disso, a codificação MLT-3 tem um componente DC (corrente contínua) 
menor do que outras técnicas de codificação de linha, o que reduz o consumo de energia e a interferência eletromagnética. No entanto, a codificação MLT-3 tem uma taxa de 
dados menor do que outras técnicas que usam mais níveis de sinal, como a codificação 4B/5B.

Sincronismo: O MLT-3 usa a mesma técnica de sincronismo que o Manchester e o Manchester diferencial, ou seja, a codificação de bits de início e fim.

Componente DC: O MLT-3 tem uma componente DC limitada, pois as transições de nível são controladas para evitar grandes deslocamentos de tensão.

Imunidade a ruídos: O MLT-3 é mais imune a ruídos do que outras técnicas de codificação de linha, pois a transmissão de três níveis permite uma maior tolerância a erros de transmissão. Além disso, o MLT-3 é menos suscetível a interferência eletromagnética (EMI) do que outras técnicas de codificação de linha, porque as transições de nível são mais suaves.

Aplicação prática: O MLT-3 é amplamente utilizado em redes de computadores, sistemas de telecomunicações e outras aplicações de transmissão de dados de alta velocidade. O MLT-3 é uma técnica de codificação de linha eficiente em termos de largura de banda e é frequentemente usado em conjunto com outras técnicas de codificação de linha para garantir a integridade dos dados durante a transmissão.

![image](https://user-images.githubusercontent.com/85199336/234346512-e9b673e5-4565-443c-a63f-61ea6dfbabf9.png)


### DIFFERENTIAL BINARY
Nessa técnica, cada bit é codificado como a diferença entre o nível de sinal atual e o nível de sinal anterior. Um bit "1" é representado por uma diferença positiva, enquanto um bit "0" é representado por uma diferença negativa.

Lei de Formação: A lei de formação do Differential Binary é baseada em transições de nível, em que o valor do bit é determinado pela mudança de polaridade em relação ao bit anterior. Se o bit anterior for "0", o bit atual é representado por uma transição de nível de polaridade oposta. Se o bit anterior for "1", o bit atual é representado por uma transição de nível com a mesma polaridade. Por exemplo, se o bit anterior for "0", o bit "1" é representado por uma transição de nível positivo para negativo, enquanto o bit "0" é representado por uma transição de nível negativo para positivo.

Sincronismo: O Differential Binary não utiliza bits de sincronismo para marcar o início e o fim dos dados, mas sim a transição de nível para marcar o início de cada bit. Isso pode tornar o Differential Binary mais suscetível a erros de transmissão.

Componente DC: O Differential Binary tem uma componente DC limitada, pois as transições de nível ocorrem com polaridades alternadas.

Imunidade a ruídos: O Differential Binary é suscetível a erros de transmissão causados por ruídos, pois a transmissão de dados depende da polaridade das transições de nível. Além disso, o Differential Binary pode ser afetado por interferência eletromagnética (EMI).

Aplicação prática: O Differential Binary é utilizado em algumas aplicações de transmissão de dados de alta velocidade, como em algumas interfaces de comunicação serial e em algumas redes de comunicação. No entanto, a técnica é menos comum do que outras técnicas de codificação de linha, devido à sua maior suscetibilidade a erros de transmissão e a interferência eletromagnética.

![image](https://user-images.githubusercontent.com/85199336/234346185-4033c1d2-09fe-44df-a691-9bcd5bfff1d3.png)

