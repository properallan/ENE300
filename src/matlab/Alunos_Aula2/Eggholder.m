%------------------------------------------%
% Imput                                    %
% X = [x1, x2]                    %
%------------------------------------------%
function Y = Eggholder (X) % 
    % Eggholder function 
    x1 = X(1);
    x2 = X(2);

   part1 = -(x2+47) * sin(sqrt(abs(x2+x1/2+47)));
   part2 = -x1 * sin(sqrt(abs(x1-(x2+47))));

   Y = part1 + part2;
end