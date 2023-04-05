% Exercício 4 (este exercício é igual ao anterior, porém com uma
% inconsistência no conjunto de treinamento, ou seja, o seu primeiro
% elemento é -1.6 e -1.4). Ele deveria pertencer a classe 01 e não 10. 

%apresentando e plotando os vetores de treinamento
P=[-1.6 0.7 0.8 0.8 1 0.3 0 -0.3 -0.5 -1.5;
   -1.4 1.8 1.6 0.6 0.8 0.5 0.2 0.8 -1.5 -1.3]
T=[1 1 1 0 0 1 1 1 0 0; 0 0 0 0 0 1 1 1 1 1]
plotpv(P,T)
grid
pause

%definindo a treinando a RNA
net = newp([-2 2;-2 2],2);
net = train(net,P,T);
net.IW{1}
net.b{1}
pause
figure
plotpv(P,T) %plotando as retas que dividem o plano em 4 partes
plotpc(net.IW{1},net.b{1})
grid
% testando com a nova entrada P1
P1 = [-1; 2]
pause
a1 = sim(net,P1)
plotpv(P1,a1);
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1}); %plotando o resultado da classificação de P1
grid
pause
% testando com a nova entrada P2
P2 = [1.5; 1]
pause
a2 = sim(net,P2)
figure
plotpv(P2,a2);
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1}); %plotando o resultado da classificação de P2
grid

% Não houve classificação correta, pois a RNA não foi treinada devido a uma
% inconsistência no vetor de treinamento