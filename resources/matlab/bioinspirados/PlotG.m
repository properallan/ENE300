function PlotG(FOB)
if FOB==1 %Shubert Function
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
   
elseif FOB==3
  [X,Y] = meshgrid(-10:.1:10,-10:.1:10); % limites alterado para melhorar a fig.
  N = size(X,1);
    for i = 1:N
      for j = 1:N
        z = [X(i,j),Y(i,j)];
        Z(i,j) = Easom(z);
      end
    end
  mesh(X,Y,Z);
  title('Easom Function in 2 dimension');
   
elseif FOB==4
  [X,Y] = meshgrid(-3:0.1:3,-3:0.1:3);
   N = size(X,1);
     for i = 1:N
       for j = 1:N
        z = [X(i,j),Y(i,j)];
        Z(i,j) = Sixhump(z);
       end
     end
    mesh(X,Y,Z);
    title('Sixhump Function in 2 dimension');

elseif FOB==5
  [X,Y] = meshgrid(-512:5:512,-512:5:512);
  N = size(X,1);
    for i = 1:N
      for j = 1:N
        z = [X(i,j),Y(i,j)];
        Z(i,j) = Eggholder(z);
      end
    end
   mesh(X,Y,Z);
   title('Eggholder Function in 2 dimension');

%    elseif FOB==6
%   [X,Y] = meshgrid(-512:5:512,-512:5:512);
%   N = size(X,1);
%     for i = 1:N
%       for j = 1:N
%         z = [X(i,j),Y(i,j)];
%         Z(i,j) = Termoeletricas(z);
%       end
%     end
%    mesh(X,Y,Z);
    title('Termoeletricas Function in 2 dimension'); 

end
end