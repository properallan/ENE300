function [Y,Gb,FA] = SOS_alg(FOB,Func, X_max, X_min, N, M, I_max, FA)

    for i=1:M % Personal best initialize
        x(i,:)=X_min+rand(1,N).*(X_max-X_min);
        Fit(i,:)=Func(x(i,:));
        FA=FA+1; % Increase the number of function evaluation counter
    end
     
    for t=1:I_max
        
        for i=1:M
             [bestFit,idx]=min(Fit);
             Gb=x(idx,:); % The best solution corrente
             
            % *** MUTUALISM PHASE *****************************************
            
            % Choose organism j randomly other than organism i           
            j=i;
            while i==j
                seed=randperm(M); 
                j=seed(1);                  
            end
            
            % Determine Mutual Vector & Beneficial Factor
            mutualVector=mean([x(i,:);
            x(j,:)]);
            BF1=round(1+rand);
            BF2=round(1+rand);
            
            % Calculate new solution after Mutualism Phase
            ecoNew1=x(i,:)+rand(1,N).*(Gb-BF1.*mutualVector); 
            ecoNew2=x(j,:)+rand(1,N).*(Gb-BF2.*mutualVector);
            ecoNew1=bound(ecoNew1,X_max,X_min); 
            ecoNew2=bound(ecoNew2,X_max,X_min);
                
            % Evaluate the fitness of the new solution
            fitnessNew1=Func(ecoNew1);
            FA=FA+1; % Increase the number of function evaluation counter
            fitnessNew2=Func(ecoNew2);
            FA=FA+1; % Increase the number of function evaluation counter
          
            % Accept the new solution if the fitness is better
            if fitnessNew1<Fit(i)
                Fit(i)=fitnessNew1;
                x(i,:)=ecoNew1;
            end
            if fitnessNew2<Fit(j)
               Fit(j)=fitnessNew2;
               x(j,:)=ecoNew2;
            end
           
            % End of Mutualism Phase 
        
            % *** COMMENSIALISM  PHASE ************************************    
       
            % Choose organism j randomly other than organism i
            j=i;
            while i==j
                seed=randperm(M); 
                j=seed(1);                  
            end
            
            % Calculate new solution after Commensalism Phase    
            ecoNew1=x(i,:)+(rand(1,N)*2-1).*(Gb-x(j,:));
            ecoNew1=bound(ecoNew1,X_max,X_min);

            % Evaluate the fitness of the new solution
            fitnessNew1=Func(ecoNew1);
            FA=FA+1; % Increase the number of function evaluation counter
           
            % Accept the new solution if the fitness is better
            if fitnessNew1<Fit(i)
                Fit(i)=fitnessNew1;
                x(i,:)=ecoNew1;
            end
            
            % End of Commensalism Phase
            
            % *** PARASITISM PHASE ****************************************
    
            % Choose organism j randomly other than organism i 
            j=i;
            while i==j
                seed=randperm(M);
                j=seed(1);
            end
            
            % Determine Parasite Vector & Calculate the fitness
            parasiteVector=x(i,:);
            seed=randperm(N);           
            pick=seed(1:ceil(rand*N));  % select random dimension
            parasiteVector(:,pick)=rand(1,length(pick)).*(X_max(pick)-X_min(pick))+X_min(pick);
            fitnessParasite=Func(parasiteVector);
            FA=FA+1; % Increase the number of function evaluation counter
            
            % Kill organism j and replace it with the parasite if the
            % fitness is lower than the parasite
            if fitnessParasite < Fit(j)
                Fit(j)=fitnessParasite;
                x(j,:)=parasiteVector;
            end
            
            % End of Parasitism Phase
                         
       end % End of Organisms' Looping
          
       % Plot the convergence process     
       
       %Y=Func(Gb);
       Y=bestFit;
       algo='SOS - The Best Fitness: %.15f';
       graf_conver(Y,t,'g.',algo);
       %fun_resp(Y,Gb,FOB) %Figure (not recommended )
    end
end

