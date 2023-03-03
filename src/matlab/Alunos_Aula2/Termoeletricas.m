  function Y = Termoeletricas (X)
    % Griewangk's function in 2 dimensions
   alfa=0; 
   a=[26.97,1.865,39.79];
   b=[-0.3975,-0.03988, -0.3116];
   c=[0.002176,0.001138, 0.001457];
    e=[2.18, -2.40, -2.95];
    f=[-2.500, 2.400, 2.300];
    Pmim=[100, 50, 200];


  % PG=[X(1), X(2), X(3)]; 
    m=3;  % Dimension
    F=0;
	for i=1:m
		F=F+a(i)+b(i)*X(i)+c(i)*X(i)^2+alfa*abs(e(i)*sin(f(i)*(Pmim(i)-X(i))     ))%   *);
	end
	
	Y=F+(50)*((X(1)+X(2)+X(3))-550)^2; % O valor 50 corresponde ao custo por não
                                       % atender a restrição de
                                       % desigualdade (pode ser alterado).
   %solução esperada para o problema
   %X1 = 186.678
   %X2 = 114
   %X3 = 249.322
   %FOB = 93.3749
                                      

end