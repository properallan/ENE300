function PlotG(FOB)
if FOB==1
    
    [X,Y] = meshgrid(-10:.1:10,-10:.1:10);
N = size(X,1);

for i = 1:N
    for j = 1:N
        z = [X(i,j),Y(i,j)];
        Z(i,j) = Shubert(z);
    end
end

mesh(X,Y,Z);
title('Shubert Function in 2 dimension');
    
elseif FOB==2
    
    [X,Y] = meshgrid(-100:100,-100:100);
    N = size(X,1);

    for i = 1:N
        for j = 1:N
            z = [X(i,j),Y(i,j)];
            Z(i,j) = Griewank (z);
        end
    end

mesh(X,Y,Z);
title('Griewangk Function in 2 dimension');
   



%elseif FOB==3
    
%

%elseif FOB==4
    

%elseif FOB==5
    

end
end