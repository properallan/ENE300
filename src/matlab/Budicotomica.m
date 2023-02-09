%**************************************************************************
%                  Inteligência Computacional
% Programa que resolve o seguinte problema unidimensional utilizando 
% Busca Dicotômica: min  f1=8*x1^3-2*x1^2-7*x1+3 ( no intervalo (0,2)
%                               Edmarcio Belati - 2022.1
%**************************************************************************
%
clc,clear;
%  entradas de dados
eps= 0.00001;% valor de epsilon
a=0; b=2; % Intervalo de busca
f=inline('8*x.^3-2*x.^2-7*x+3');% Funcão a ser minimizada
%f=inline('0.112*x.^2-0.152*x+0.292')
x=0:0.01:2;
hold;
plot(x,f(x));
erro=1; % erro para entrar no while
it=0; % contador de iterções

while erro>=0.0001; % precisão do valor (deve estar de acordo com o epsilon) 
c=(a+b)/2  ;
x1=c-eps;
x2=c+eps;
    f1=8*x1^3-2*x1^2-7*x1+3;
    f2=8*x2^3-2*x2^2-7*x2+3;
if f1>f2 ;
   a=x1;
   b=b;
else
   a=a;
   b=x2;
end
erro=abs(a-b);
it=it+1;
resp(it,:)=[ it a b erro x1 x2 f1 f2]; % vetor utilizado para saída
end
disp('       IT         a          b     intervalo    x1          x2         f1          f2')
disp(resp)

plot(x1, f1, 'o');
