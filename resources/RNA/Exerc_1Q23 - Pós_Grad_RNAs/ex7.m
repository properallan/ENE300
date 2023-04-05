% Exercício 7 - Neste caso, a RNA deve encontrar os pesos e bias para
% aproximar uma função senoidal, cujos dados são apresentados no
% conjunto de treinamento. 

% Define a função (os pontos) de treinamento
p = [-1:.05:1];
t = sin(2*pi*p);

% Plota a função que a RNA deve aprender
figure
plot (p,t)
grid

% definições dos parêmetros e treinamento da RNA
net=newff(minmax(p),[20,1],{'tansig','purelin'},'traingd');
net.trainParam.goal = 1e-9;
net.trainParam.show = 10;
net.trainParam.epochs = 1000;
net = init(net);
[net,tr]=train(net,p,t);

% Testando a RNA frente ao vetor de treinamento
figure
plot (p,t)
a1 = sim(net,p);
hold on
plot (p,a1,'r')
grid

% Testando a RNA diante de novos pontos
p1 = [-1:.005:1];
a2 = sim(net,p1);
plot (p1,a2,'g')

% Aumentando o numero de iterações de 1000 para 20000
% o desempenho no processo de treinamento melhora bastante

%==========================================================
% NOVO CASO - treinando a rede com ruído no sinal

% definindo o sinal de entrada com ruído
p = [-1:.05:1];
t = sin(2*pi*p)+0.1*randn(size(p));

% Plotando o sinal de entrada
figure
plot (p,t)
grid

% definição dos parâmetros e treinamento da RNA
net=newff(minmax(p),[20,1],{'tansig','purelin'},'traingd');
net.trainParam.goal = 1e-9;
net.trainParam.show = 10;
net.trainParam.epochs = 1000;
net = init(net);
[net,tr]=train(net,p,t);

% Testando a RNA frente ao vetor de treinamento
a1 = sim(net,p);
figure
plot (p,t)
hold on
plot (p,a1,'r')
grid

% Testando a RNA diante de novos pontos
p1 = [-1:.0005:1];
a2 = sim(net,p1);
plot (p1,a2,'g')

% Aumentando o numero de iterações de 1000 para 50000
% o desempenho no processo de treinamento melhora bastante

%=================================================================
% Tentativa de RNA com hardlim (neste caso o matlab não inicia o
% processo de treinamento)

% treinando a rede com ruído no sinal
p = [-1:.05:1];
t = sin(2*pi*p)+0.1*randn(size(p));

% treinamento da rede
net=newff(minmax(p),[20,1],{'tansig','hardlim'},'traingd');
net.trainParam.goal = 1e-9;
net.trainParam.show = 10;
net.trainParam.epochs = 5000;
net = init(net);
[net,tr]=train(net,p,t);

%=================================================================
% Tentativa de RNA com logsig (observa-se um desempenho um pouco
% inferior ao tansig para 50000 iterações, porém uma tentativa com maior
% número de iterações poderia resolver -???- é ne cessário testar)

% treinando a rede com ruído no sinal
p = [-1:.05:1];
t = sin(2*pi*p)+0.1*randn(size(p));

% treinamento da rede
net=newff(minmax(p),[20,1],{'logsig','purelin'},'traingd');
net.trainParam.goal = 1e-9;
net.trainParam.show = 10;
net.trainParam.epochs = 1000;
net = init(net);
[net,tr]=train(net,p,t);

% Testando a RNA frente ao vetor de treinamento
a1 = sim(net,p);
figure
plot (p,t)
hold on
plot (p,a1,'r')
grid

% Testando a RNA diante de novos pontos
p1 = [-1:.0005:1];
a2 = sim(net,p1);
plot (p1,a2,'g')