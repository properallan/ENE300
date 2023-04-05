% Exercício 6 - Neste caso, a RNA deve encontrar os pesos e bias para
% aproximar uma função, cujos dados são apresentados no conjunto de
% treinamento. Treinando um neurônio linear p/ função y = -0.2273.x+0.7273

% Apresentando o conjunto de treinamento
P = [1.0 -1.2]
T = [0.5 1.0]

% Plotando a superfície de erro
w_range = -1:0.2:1;  b_range = -1:0.2:1;
ES = errsurf(P,T,w_range,b_range,'purelin');
plotes(w_range,b_range,ES);

% Criando e treinando a RNA
net = newlin([-2 2],1);% neurônio linear com entradas de -2 a 2
net.trainParam.goal = .00001;% erro objetivo
net.trainParam.epochs = 100; % máximo número de iterações
[net,tr] = train(net,P,T);% treinando a RNA

%parâmetros encontrados com 100 iterações
net.IW{1}
net.b{1}

% Testando a RNA com o segundo ponto do vetor de treinamento
p = -1.2
a = sim(net, p)
pause

%melhorando a resposta passando de 100 para 500 iterações (reduz erro)
net.trainParam.goal = .00001;
net.trainParam.epochs = 500;
[net,tr] = train(net,P,T);

% parâmetros encontrados com 500 iterações
net.IW{1}
net.b{1}

% Novamente, testando a RNA com o segundo ponto do vetor de treinamento
p = -1.2
a = sim(net, p)
pause

% Testando a RNA com uma nova entrada
p = 1.8
a = sim(net, p)

% equaçao y = -0.2273.x+0.7273
% se 1.8 for substituido na equação, y será aprox. a (0.3138) 