% Exercício 5 - Neste caso, alterar o número de iterações não tem efeito,
% pois não há uma única reta que pode separar as classes em duas regiões
% distintas 

%apresentando e plotando os vetores de entrada
P = [ -0.5 -0.5 +0.3 -0.1 -0.8;
      -0.5 +0.5 -0.5 +1.0 +0.0 ]
T = [1 1 0 0 0]
plotpv(P,T)
grid
pause

%definindo e treinando a RNA
net = newp([-1 1;-1 1],1);
net.trainParam.epochs = 500;
net = train(net,P,T);
net.IW{1}
net.b{1}
pause

%plotando a solução (reta) encontrada após o treinamento
figure
plotpv(P,T)
plotpc(net.IW{1},net.b{1})
grid

% alterar o numero de iteraçoes não tem efeito