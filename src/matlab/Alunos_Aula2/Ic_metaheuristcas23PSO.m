clear all;
clc;
  
% Escolha do Algoritmo
ALG=2 % PSO=1; FPA=2; SOS=3; GWO=4 (aluno)
% Escolha da Função
FOB=3% Shubert=1; % Griewank=2; Easom=3; Six-hump=4; Eggholder=5; Termoeletricas=6;
    
% Dados Globais
I_max=80;			% Maximum iteration
M=80;				% Number of Particle/population/ecosize
Run=1;              % The number of test time

% Parâmetros do Algoritmo
    c1=1.0;				% Learning factor 1        - PSO
    c2=1.5;				% Golbal Learning factor 2 - PSO
    W_max=0.9;			% Maximum weight           - PSO
    W_min=0.4;			% Minimum weight           - PSO
    p=0.75;             % chava                    - FPA

% Parâmetros das Funções
if FOB==1 %SHUBERT FUNCTION
    N=2; % Numer of dimension
    X_max= [ 10, 10];     % Boundary     - ALL
	X_min= [-10,-10];     % Boundary     - ALL
    V_max= (X_max-X_min)/10;     % Boundary       - PSO
    V_min=-(X_max-X_min)/10;     % Boundary       - PSO  
    Func=@Shubert; % Function 
elseif FOB==2 %GRIEWANK FUNCTION
    N=2; % Numer of dimension
    X_max= [ 600, 600];     % Boundary   - ALL
	X_min= [-600,-600];     % Boundary   - All
    V_max= X_max/5;     % Boundary       - PSO
	V_min= X_min/5;     % Boundary       - PSO 
    Func=@Griewank; % Function   

elseif FOB==3 %EASOM FUNCTION    
    N=2; % Numer of dimension
    X_max= [ 100, 100];     % Boundary   - ALL
	X_min= [-100,-100];     % Boundary   - All
    V_max= (X_max-X_min)/10;     % Boundary       - PSO
    V_min=-(X_max-X_min)/10;     % Boundary       - PSO 
    Func=@Easom; % Function   
       
elseif FOB==4 %SIX-HUMP FUNCTION    
    N=2; % Numer of dimension
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
    FA=0;
    if ALG==1 % PSO
        
        [Y,Gb, FA]=POS_alg(FOB,Func, X_max, X_min, N, M, I_max, FA, V_max, V_min, c1, c2, W_max, W_min);
         
    elseif ALG==2 % FPA
       % Apresentado na aula 3  
        [Y,Gb, FA]=FPA_alg(FOB,Func, X_max, X_min, N, M, I_max, FA, p);  
 
    elseif ALG==3 % SOS
       % Apresentado na aula 3 
        
    elseif ALG==4 % GWO   
        % Desenvolvido pelo aluno - parte do trabalho
    end
     fun_resp(Y,Gb,FOB)
     resp(r,:)=[ Y, Gb];
     resp1(r,:)=[ FA];
end 
disp('      *************************************************     ')
disp('          FOB               X1               X2            ')
disp(resp)
disp('            Avalições     ')
disp(resp1)
disp('      *************************************************     ')


 