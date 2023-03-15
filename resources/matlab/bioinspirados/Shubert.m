function [Y] = Shubert(X)
x1 = X(1);
x2 = X(2);
sum1 = 0;
sum2 = 0;

for i = 1:5
	new1 = i * cos((i+1)*x1+i);
	new2 = i * cos((i+1)*x2+i);
	sum1 = sum1 + new1;
	sum2 = sum2 + new2;
end

Y = sum1 * sum2;    

end
