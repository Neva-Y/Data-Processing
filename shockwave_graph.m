close all
Array = csvread('6.5M_shock.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
col3 = Array(:, 3);
plot(col1, col2,'-o');
hold on
plot(col1,col3,'-o');
title('\theta-\beta-M diagram for M=7.5')
ylabel('\beta')
ylim([0 90])
xlim([0 45])
xlabel('\theta')