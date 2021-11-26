clc
clear all
close all
Nx=200;
CFL=0.5;
dt = CFL*(1/Nx)/1;
time=0:dt:1;
x=0:1/Nx:1;

for i=1:length(x)
    if (x(i) >= 0.125 && x(i) <= 0.375)
        exact(i) = 0.5*(1-cos(8*pi*(x(i)-0.125)));
    else
        exact(i) = 0;
    end
end

%Nx200, CFL0.25
figure
plot(x,exact,'-b','LineWidth',2)
ylim([-0.2 1.2])
Array = csvread('Nx200_CFL0.25.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');
ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=200 and CFL=0.25')

%Nx200, CFL0.8
figure
plot(x,exact,'-b','LineWidth',2)
ylim([-0.2 1.2])
Array = csvread('Nx200_CFL0.8.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');
ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=200 and CFL=0.8')

%Nx200, CFL1
figure
plot(x,exact,'-b','LineWidth',2)
ylim([-0.2 1.2])
Array = csvread('Nx200_CFL1.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');
ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=200 and CFL=1')

%Nx100, CFL0.25
figure
plot(x,exact,'-b','LineWidth',2)
ylim([-0.2 1.2])
Array = csvread('Nx100_CFL0.25.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');
ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=100 and CFL=0.25')


%Nx100, CFL0.8
figure
plot(x,exact,'-b','LineWidth',2)
ylim([-0.2 1.2])
Array = csvread('Nx100_CFL0.8.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');
ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=100 and CFL=0.8')

%Nx100, CFL1
figure
plot(x,exact,'-b','LineWidth',2)
ylim([-0.2 1.2])
Array = csvread('Nx100_CFL1.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');
ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=100 and CFL=1')

%Nx200, CFL1.002
figure
plot(x,exact,'-b','LineWidth',2)
Array = csvread('Nx200_CFL1.002.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
hold on
plot(col1, col2,'-x','color','r');ylabel('\phi')
xlabel('x')
legend('Exact Solution', 'Simulated Solution')
title('Advection Simulation with Nx=200 and CFL=1.002')


