function [Y,Gb, FA]=POS_alg(FOB,Func, X_max, X_min, N, M, I_max, FA, V_max, V_min, c1, c2, W_max, W_min );

    for i=1:M % Personal best initialize
        x(i,:)=X_min+rand(1,N).*(X_max-X_min);
        v(i,:)=V_min+rand(1,N).*(V_max-V_min);
        Fit(i,:)=Func(x(i,:));
        FA=FA+1;
    end
    
    Pb(i,:)=x(i,:); % solution
    [bestFit,idx]=min(Fit);
    Gb=x(idx,:); % The best solution corrente
    
for t=1:I_max
    
    for i=1:M
        % Update the velocity
		% Calculate the weighting function
		w=W_max-(W_max-W_min)*t/I_max;
		v(i,:)=w*v(i,:)+c1*rand*(Pb(i,:)-x(i,:))+c2*rand*(Gb-x(i,:));
		% Check the velocity
        v(i,:)=bound(v(i,:),V_max,V_min);
 
		% Update the position
		x(i,:)=x(i,:)+v(i,:);
                
        % Check the velocity
        x(i,:)=bound(x(i,:),X_max,X_min);

        Fit_i=Func(x(i,:));
        FA=FA+1; % Increase the number of function evaluation counter
        
     if Fit_i<Fit(i)
        Fit(i)=Fit_i;
			  Pb(i,:)=x(i,:);
		 end
		% Update the Gb
		 if bestFit>Fit(i)       
			  Gb=Pb(i,:);
              bestFit=Fit(i);
		 end
  end
	Y=Func(Gb);
    algo='POS - The Best Fitness: %.15f';
    graf_conver(Y,t,'b.',algo);
    %fun_resp(Y,Gb,FOB) %Figure (not recommended )
    end
end

