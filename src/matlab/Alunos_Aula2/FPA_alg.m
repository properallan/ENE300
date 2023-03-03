function [Y,Gb, FA]=FPA_alg(FOB, Func, X_max, X_min, N, M, I_max, FA, p);    
   
% Initialize the population/solutions
for i=1:M;
  x(i,:)=X_min(:)+rand()*(X_max(:)-X_min(:));
  Fitness(i)=Func(x(i,:));
  FA=FA+1;
end
% Find the current best
[fmin,I]=min(Fitness);
Gb=x(I,:);
S=x; 
% Start the iterations -- Flower Algorithm 
for t=1:I_max;
        % Loop over all bats/solutions
        for i=1:M,
          % Pollens are carried by insects and thus can move in
          % large scale, large distance.
          % This L should replace by Levy flights  
          % Formula: x_i^{t+1}=x_i^t+ L (x_i^t-gbest)
          if rand>p;
          %% L=rand;
          L=Levy(N);
          dS=L.*(x(i,:)-Gb);
          S(i,:)=x(i,:)+dS;
          % Check if the simple limits/bounds are OK
          S(i,:)=bound(S(i,:),X_max,X_min);
                  
          % If not, then local pollenation of neighbor flowers 
          else
              epsilon=rand;
              % Find random flowers in the neighbourhood
              JK=randperm(M);
              % As they are random, the first two entries also random
              % If the flower are the same or similar species, then
              % they can be pollenated, otherwise, no action.
              % Formula: x_i^{t+1}+epsilon*(x_j^t-x_k^t)
              S(i,:)=x(i,:)+epsilon*(x(JK(1),:)-x(JK(2),:));
              % Check if the simple limits/bounds are OK
              S(i,:)=bound(S(i,:),X_max,X_min);
          end
          % Evaluate new solutions
           Fnew=Func(S(i,:));
           FA=FA+1;
          % If fitness improves (better solutions found), update then
            if (Fnew<=Fitness(i)),
                x(i,:)=S(i,:);
                Fitness(i)=Fnew;
           end
           
          % Update the current global best
          if Fnew<=fmin,
                Gb=S(i,:);
                fmin=Fnew;
          end
        end
     
    Y=Func(Gb);
    algo='FPA - The Best Fitness: %.15f';
    graf_conver(Y,t,'r.',algo);
    %fun_resp(Y,Gb,FOB) %Figure (not recommended )
          
          end
 end


% 		
