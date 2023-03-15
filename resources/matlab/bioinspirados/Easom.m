function Y = Easom (X)

x1 = X(1);
x2 = X(2);
    
  m=2;  % Dimension
  
   Y=-cos(x1)*cos(x2)*exp(-(x1-pi)^2-(x2-pi)^2); 
    
end