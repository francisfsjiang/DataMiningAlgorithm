
% karate 34x78
clear;

xs =load('karate2.txt');
W = zeros(34,34);
for k=1:1:78
   W(xs(k,1),xs(k,2))=1;
   W(xs(k,2),xs(k,1))=1;
end
k=3;
result=SpectralClustering(W, k);
disp('Karate result');
disp(result);

% football 115x616
xs =load('football1.txt');
W = zeros(115,115);
for k=1:1:616
   W(xs(k,1),xs(k,2))=1;
   W(xs(k,2),xs(k,1))=1;
end
k=3;
result=SpectralClustering(W, k);
disp('Football result');
disp(result);