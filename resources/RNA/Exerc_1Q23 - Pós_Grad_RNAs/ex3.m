% Exercício 3 (neste exercício a rna deve classificar novas entradas
% segundo uma das quatro classes existentes)

% plotando os vetores de entrada
P=[0.1 0.7 0.8 0.8 1 0.3 0 -0.3 -0.5 -1.5;
   1.2 1.8 1.6 0.6 0.8 0.5 0.2 0.8 -1.5 -1.3]
T=[1 1 1 0 0 1 1 1 0 0; 0 0 0 0 0 1 1 1 1 1]
plotpv(P,T)
grid
pause
%definindo e treinando a RNA (usando valores default)
net = newp([-2 2;-2 2],2);
net = train(net,P,T);
net.IW{1}
net.b{1}
pause
figure
plotpv(P,T) %plotando as áreas criadas durante o treinamento
plotpc(net.IW{1},net.b{1})
grid
% testando com a nova entrada P1
P1 = [-1; 2]
pause
a1 = sim(net,P1)
plotpv(P1,a1);
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1}); %plotando a classificação de P1 em Y > 1
grid
pause
% testando com nova entrada P2
P2 = [1.5; 1]
pause
a2 = sim(net,P2)
figure
plotpv(P2,a2);
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1}); %plotando a classificação de P2 em <0 X eY < 1
grid

% Neste exercício a rna classificou novas entradas segundo uma das
% quatro classes criadas durante o treinamento