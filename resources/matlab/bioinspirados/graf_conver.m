function graf_conver(Y,t,cor,algo)

% Plot, just for look
figure(1);
%plot(t,Y,'r.');
plot(t,Y,cor);
pause(0.0001)% Necessário para acompanhar o processo de busca. Pode comentar
xlabel('Iteration');
ylabel('Fitness');
title(sprintf(algo,Y));
% title(sprintf('The Best Fitness: %.15f',Y));
% title('The Best Fitness: %.15f',Y);
grid on;
hold on;
end