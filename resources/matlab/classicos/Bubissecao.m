%**************************************************************************
%          Inteligência conputacional
% Programa que resolve o seguinte problema unidimensional utilizando 
% Método da Bisseção:   min  f1=8*x1^3-2*x1^2-7*x1+3 ( no intervalo (0,2.5))
% Edmarcio Belati - 2022.1
%**************************************************************************
clc,clear; % Comandos para Limpar a Memória
%  entradas de dados
a=0; b=2.5; % Intervalo de busca (verificar a solução final)
% syms x
f=inline('8*x.^3-2*x.^2-7*x+3');
x=0:0.01:2.5;
hold;
plot(x,f(x));
% erro para entrar no while
erro=1;
it=0;
x=(a+b)/2 ;% O ponto inical.
%Derivadas utilziadas
% f'=24*x^2-4*x-7
while erro>0.0001;  % 0.001 precisão escolhida
df= (24*x^2-4*x-7);
if df>0
  a=a;
  b=x;
elseif df<=0
  b=b;
  a=x;
elseif df=0
  erro=0.000;
end
x=(a+b)/2;
xb=8*x^3-2*x^2-7*x+3;
erro=abs(a-b);
%xa=xb;
it=it+1;
resp(it,:)=[ it a b x erro  xb];
end
disp('      IT       a          b       x     erro     Valor da FOB    ')
disp(resp)

plot(x, xb, 'o');

