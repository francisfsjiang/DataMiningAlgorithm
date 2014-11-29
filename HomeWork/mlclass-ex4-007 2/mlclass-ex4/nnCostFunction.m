function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

J =  lambda*( (sum(sum((Theta1(:,2:end)).^2)))  +  (sum(sum(Theta2(:,2:end).^2))) )/(2*m);

for i = 1:m
    %forword
    a1 = X(i,:)';
    a1 = [1;a1];%401x1
    z2 = Theta1*a1;
    a2 = sigmoid(z2);
    a2 = [1;a2];%26x1
    z3 = Theta2*a2;
    a3 = sigmoid(z3);%10x1
    out_put = a3;
    tmp_y = zeros(num_labels,1);
    tmp_y(y(i,1),1) = 1;
    J = J + sum(  -tmp_y.*log(out_put)-(1-tmp_y).*log(1-out_put) )/m;
    
    %backword
    tmp_delta3 = a3-tmp_y;
    tmp_delta2 = ((Theta2(:,2:end))'*tmp_delta3).*sigmoidGradient(z2  );
    
    Theta1_grad = Theta1_grad + tmp_delta2*a1';
    Theta2_grad = Theta2_grad + tmp_delta3*a2';
end

Theta1_grad_reg = lambda*Theta1/m;
Theta1_grad_reg(:,1) = 0;

Theta1_grad = Theta1_grad/m + Theta1_grad_reg;

Theta2_grad_reg = lambda*Theta2/m;
Theta2_grad_reg(:,1) = 0;

Theta2_grad = Theta2_grad/m + Theta2_grad_reg;


grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
