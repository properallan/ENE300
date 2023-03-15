%**************************************************************************
%          Inteligência Computacional
% Programa que resolve o seguinte problema unidimensional utilizando 
% Método de Newton:   min  f1=8*x1^3-2*x1^2-7*x1+3 ( no intervalo (0,2))
% Edmarcio Belati - 2022.1
%**************************************************************************
clc,clear; % Comandos para Limpar a Memória
%  entradas de dados
a=0; b=2; % Intervalo de busca (verificar a solução final)
% syms x
f=inline('8*x.^3-2*x.^2-7*x+3');
x=0:0.01:2.0;
hold;
plot(x,f(x));
% erro para entrar no while
erro=1;
it=0;
x=1.9; % O ponto inical precisa estar próximo da região de solução.
xa=8*x^3-2*x^2-7*x+3;  #utilizado para avaliar a convergência
%Derivadas utilziadas
% f'=24*x^2-4*x-7
% f''=48*x-4
while erro>0.00001;  % 0.0001 precisão escolhida
deltax=-(24*x^2-4*x-7)/(48*x-4);
x=x+deltax;
xb=8*x^3-2*x^2-7*x+3;
erro=abs(xa-xb);
xa=xb;
it=it+1;
resp(it,:)=[ it x xb erro];
end
disp('          IT                x           valor da FOB         erro       ')
disp(resp)

plot(x, xb, 'o');