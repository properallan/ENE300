function [] = fun_resp(Y,Gb,FOB)
figure(2);
    %Y=Func(Gb);
    PlotG(FOB);
    hold on;
    scatter3(Gb(1),Gb(2),Y,'fill','ro');
    hold off;
end

