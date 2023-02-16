%------------------------------------------%
% Imput                                    %
% X = [x1, x2, ..., xd]                    %
%------------------------------------------%
function Y = Griewank (X) % 
    % Griewank's function in 2 dimensions
    m = length(X); % Dimension
 	d=0;
	f=1;
	for i=1:m
        d=d+X(i)^2/4000;
		f=f*cos(X(i)/(i^0.5));
    end
	Y=d-f+1;
end