% Exercício 2 (neste exercício a rna aprende que quando a entrada 3 é
%positiva a saída é 1 e quando a entrada 3 é negativa a saída é 0)

% definindo e plotando os vetores de treinamento
P=[-0.5 0.2 -0.3 0.8; 0.5 0.1 -0.8 -0.9;
    0.9 0.8 -0.8 -0.9]
T=[1 1 0 0]
plotpv(P,T)
grid
pause

% definindo e treinando a rna (com valores default)
net = newp([-1 1;-1 1;-1 1],1);%defini numero de neurônios e entradas
net = train(net,P,T);%treina a rna segundo P e T
net.IW{1}
net.b{1}
pause

% plotando o plano que divide/classifica os vetores de entrada
figure
plotpv(P,T)
plotpc(net.IW{1},net.b{1})
grid

% testando com nova entrada P1
P1 = [0.7; 0.9; 0.6]
pause
a1 = sim(net,P1);
v=[-1 1 -1 1];
plotpv(P1,a1,v);% plota a resposta de P1 acima do plano
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1});
grid
pause
% testando com nova entrada P2
P2 = [-0.2; 0.7; -0.9]
pause
a2 = sim(net,P2);
figure
plotpv(P2,a2,v); % plota a resposta de P2 abaixo do plano
hold on
plotpv(P,T)
plotpc(net.IW{1},net.b{1});
grid
%A rna aprendeu que quando a entrada 3 é positiva a saída é 1 e
%quando a entrada 3 é negativa a saída é 0. Entrada 3 positiva = 1 e
%entrada 3 negativa = 0
% entrada 3 positiva = 1 e entrada 3 negativa = 0