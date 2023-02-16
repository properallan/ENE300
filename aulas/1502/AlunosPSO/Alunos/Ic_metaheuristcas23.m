clear all;
clc;
  
% Escolha do Algoritmo
ALG=1 % PSO=1; FPA=2; SOS=3; GWO=4 . (Estudaremso três algoritmos)
% Escolha da Função
FOB=1% Shubert=1; % Griewank=2; Easom=3; Six-hump=4; Eggholder=5; Termoeletricas=6;
    
% Dados Globais
I_max=100;			% Maximum iteration
M=100;				% Number of Particle/population/ecosize
N=2;				% Numer of dimension    
Run=5;              % The number of test time

% Parâmetros do Algoritmo
    c1=1.0;				% Learning factor 1        - PSO
    c2=1.5;				% Golbal Learning factor 2 - PSO
    W_max=0.9;			% Maximum weight           - PSO
    W_min=0.4;			% Minimum weight           - PSO
    %p=0.75;             % chava                    - FPA

% Parâmetros das Funções
if FOB==1 %SHUBERT FUNCTION
    N=2;
    X_max= [ 10, 10];     % Boundary     - ALL
	X_min= [-10,-10];     % Boundary     - ALL
    V_max= (X_max-X_min)/10;     % Boundary       - PSO
    V_min=-(X_max-X_min)/10;     % Boundary       - PSO  
    Func=@Shubert; % Function 
elseif FOB==2 %GRIEWANK FUNCTION
    N=2;
    X_max= [ 600, 600];     % Boundary   - ALL
	X_min= [-600,-600];     % Boundary   - All
    V_max= X_max/5;     % Boundary       - PSO
	V_min= X_min/5;     % Boundary       - PSO 
    Func=@Griewank; % Function   

elseif FOB==3 %EASOM FUNCTION    
    N=2;
    X_max= [ 100, 100];     % Boundary   - ALL
	X_min= [-100,-100];     % Boundary   - All
    V_max= (X_max-X_min)/10;     % Boundary       - PSO
    V_min=-(X_max-X_min)/10;     % Boundary       - PSO 
    Func=@Easom; % Function   
       
elseif FOB==4 %SIX-HUMP FUNCTION    
    X_max= [ 3, 2];     % Boundary   - ALL
	X_min= [-3,-2];     % Boundary   - All
    V_max= (X_max-X_min)/10;     % Boundary       - PSO
    V_min=-(X_max-X_min)/10;     % Boundary       - PSO 
    Func=@Sixhump; % Function   
   
elseif FOB==5 %SIX-HUMP FUNCTION    
    N=2;
    X_max= [512, 512];          % Boundary   - ALL
	X_min= [-512,-512];         % Boundary   - All
    V_max= (X_max-X_min)/10;     % Boundary       - PSO
    V_min=-(X_max-X_min)/10;     % Boundary       - PSO 
    Func=@Eggholder; % Function   
    
elseif FOB==6 %TERMOELÉTRICAS
   N=3; 
   X_max= [226, 114, 332];     % Boundary
   X_min= [100, 50, 200];      % Boundary
   V_max= (X_max-X_min)/5;     % Boundary       - PSO
   V_min=-(X_max-X_min)/5;     % Boundary       - PSO 
   Func=@Termoeletricas; % Function   
  
end

FA=0 % Funções avalidas
    
for r=1:Run 
    
%     if r==1
%         ALG=1
%     elseif r==2
%         ALG=2
%     elseif r==3
%         ALG=3
%     elseif r==4
%         ALG=4
%     end
    FA=0;
    if ALG==1
        
        [Y,Gb, FA]=POS_alg(FOB,Func, X_max, X_min, N, M, I_max, FA, V_max, V_min, c1, c2, W_max, W_min);
         
    elseif ALG==2
%        [Y,Gb, FA]=FPA_alg(FOB, Func, X_max, X_min, N, M, I_max, FA, p);    
 
    elseif ALG==3
     %   I_max=I_max/3 % Em cada iteração são realizadas três avaliações
        
     %   [Y,Gb, FA]=SOS_alg(FOB,Func, X_max, X_min, N, M, I_max, FA);
        
    elseif ALG==4    
        %[Y,Gb, FA]=GWO_alg(FOB, Func, X_max, X_min, N, M, I_max, FA); 
    end
    
	fun_resp(Y,Gb,FOB)
	resp=[Y,Gb];
	resp1=FA;
	
    disp('      *************************************************     ')
	disp('          FOB               X1               X2            ')
    disp(resp)
    disp('            Avalições     ')
    disp(resp1)
    disp('      *************************************************     ')
end 


 