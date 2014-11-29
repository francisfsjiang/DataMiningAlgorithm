load('trained_theta_40_93.34.mat')
fprintf('\nVisualizing Neural Network... \n')

displayData(Theta1(:, 2:end));
fprintf('\nProgram paused. Press enter to continue.\n');
pause;


displayData(Theta2(:, 2:end));