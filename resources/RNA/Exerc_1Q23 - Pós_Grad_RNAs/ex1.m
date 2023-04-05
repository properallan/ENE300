
% Exercício (neste exercício a rna aprende que quando x é negativo
% a saída está abaixo da reta) 

P=[-0.5 -0.5 0.3 0; -0.5 0.5 -0.5 1.0] %vetor de treinamento - entrada
T=[1 1 0 0] %vetor de treinamento - saída 
plotpv(P,T) %plota os vetores de entrada e saída no plano
grid
pause
net = newp([-1 1;-1 1],1); %um neurônio com duas entradas (de -1 a 1)
net.trainParam.epochs = 500; %se comentar, usa valores default (não muda)
net.trainParam.goal = 1e-9; %se comentar, usa valores default (não muda)
net = train(net,P,T);%treina rna segundo P e T
net.IW{1} %mostra pesos utilizados
net.b{1} %mostra bias utilizado
pause
figure
plotpv(P,T)
plotpc(net.IW{1},net.b{1}) %plota a linha de classificação da rna
grid
% testando com nova entrada
P1 = [0.7; 1.2]
pause
a1 = sim(net,P1);
plotpv(P1,a1);
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1}); %plota resposta de P1 acima da linha da rna
grid
pause
% testando com nova entrada
P2 = [-0.2; 0.7]
pause
a2 = sim(net,P2);
figure
plotpv(P2,a2);
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1}); %plota resposta de P2 abaixo da linha da rna
grid

% neste exercício a rna aprende que quando x é negativo
% a saída está abaixo da reta