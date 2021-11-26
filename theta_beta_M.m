clc
clear all
close all
syms M beta gamma theta

thetaval=[3,16,26,37,44,23]*(pi/180);



eqn = (2*(1/tan(beta))*((M*M*(sin(beta))*(sin(beta))-1)/(M*M*(gamma + cos(2*beta))+2))-tan(theta))




for i=1:length(thetaval)
    thetaeqn = subs(eqn, [theta, M, gamma], [thetaval(i), 2, 1.4]);
    betaval=deg2rad(thetaval(i)):0.001:pi/2;
    hold on
    plot(rad2deg(betaval), eval(subs(thetaeqn, beta, betaval)),'LineWidth',2);
    xlim([0 90])
    ylim([-1 0.6])
end
title('f(\beta) vs \beta for M=2')
ylabel('f(\beta)')
xlabel('\beta in degrees')
yline(0,'--');
legend('\theta=3','\theta=16','\theta=26','\theta=37','\theta=44','\theta_{max}\approx23','y=0')
eqn_prime = diff(eqn,beta)
% eqn_prime = (4*M*M*cos(beta)*sin(beta))/(tan(beta)*((gamma + cos(2*beta))*M*M + 2)) - (2*(tan(beta)*tan(beta) + 1)*(M*M*sin(beta)*sin(beta) - 1))/(tan(beta)*tan(beta)*((gamma + cos(2*beta))*M*M + 2)) + (4*M*M*sin(2*beta)*(M*M*sin(beta)*sin(beta) - 1))/(tan(beta)*(M*M*(gamma + cos(2*beta)) + 2)*(M*M*(gamma + cos(2*beta)) + 2))
% 
% for i=1:length(thetaval)
%     thetaeqn = subs(eqn_prime, [theta, M, gamma], [thetaval(i), 4, 1.4]);
%     betaval=thetaval(i):0.001:pi/2;
%     hold on
%     plot(rad2deg(betaval), eval(subs(thetaeqn, beta, betaval)),'LineWidth',2);
% end