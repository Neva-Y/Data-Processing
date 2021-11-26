close all
clear all
clc
Array = csvread('lindata.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
figure(1)
plot(col1, col2,'-o');
ylabel('f(x)')
xlabel('x')
title('Raw Data Points')

interprange1=4.56686291000841:-0.0001:0.046257359125315395;
interprange2=0.046257359125315395:0.0001:4.56686291000841;
coeffs_array = csvread('spline_coeff.csv');
x = coeffs_array(:, 1);
a=coeffs_array(:, 2);
b=coeffs_array(:, 3);
c=coeffs_array(:, 4);
d=coeffs_array(:, 5);

fileID = fopen('spline_plot_points1.csv','w');
for j = 1:length(interprange1)
    for i = 1:28
        if (x(i) < interprange1(j) && x(i+1) > interprange1(j) || x(i) > interprange1(j) && x(i+1) < interprange1(j) || x(i) == interprange1(j));
            fx = (a(i)+b(i)*(interprange1(j)-x(i))+c(i)*(interprange1(j)-x(i))^2+d(i)*(interprange1(j)-x(i))^3);
            fprintf(fileID,'%.6f,%.6f\n',interprange1(j),fx);
        end
    end
end
fclose(fileID);
fileID = fopen('spline_plot_points2.csv','w');
for j = 1:length(interprange2)
    for i = 29:51
        if (x(i) < interprange2(j) && x(i+1) > interprange2(j) || x(i) > interprange2(j) && x(i+1) < interprange2(j) || x(i) == interprange2(j));
            fx = (a(i)+b(i)*(interprange2(j)-x(i))+c(i)*(interprange2(j)-x(i))^2+d(i)*(interprange2(j)-x(i))^3);
            fprintf(fileID,'%.6f,%.6f\n',interprange2(j),fx);
        end
    end
end
fclose(fileID);


plot_points = csvread('spline_plot_points1.csv');
xpts = plot_points(:,1);
ypts = plot_points(:,2);
figure(2)
plot(xpts,ypts,'r','LineWidth',1)
hold on

plot_points = csvread('spline_plot_points2.csv');
xpts = plot_points(:,1);
ypts = plot_points(:,2);
plot(xpts,ypts,'r','LineWidth',1)
ylabel('f(x)')
xlabel('x')
title('Cublic Spline Interpolation')




figure(3)
plot_points = csvread('spline_plot_points1.csv');
xpts = plot_points(:,1);
ypts = plot_points(:,2);
plot(xpts,ypts,'b','LineWidth',1)
hold on
plot(col1, col2,'o');

plot_points = csvread('spline_plot_points2.csv');
xpts = plot_points(:,1);
ypts = plot_points(:,2);
plot(xpts,ypts,'b','LineWidth',1)

ylabel('f(x)')
xlabel('x')
title('Cublic Spline Interpolation vs Raw Data points')
legend('Cubic Spline','Raw Data')