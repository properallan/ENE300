function a=bound(a,X_max,X_min)
% for ii=1:2
% if a(ii)>X_max(ii)
%     a(ii)=X_max(ii)
% elseif a(ii)<X_min(ii)
%      a(ii)=X_min(ii)
% end
a(a>X_max)=X_max(a>X_max); 
a(a<X_min)=X_min(a<X_min);
%end
end

