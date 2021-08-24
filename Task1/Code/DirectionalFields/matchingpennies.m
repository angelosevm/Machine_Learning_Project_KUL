%{
 Payoff matrices : A = [1 -1; -1 1] and B = [-1 1; 1 -1], Asymmetric game
%}

solution = @(t,z) [z(1).*(1-z(1)).*((-2)*z(2) - (-2)*(1-z(2))), z(2).*(1-z(2)).*(2*z(1) - 2*(1-z(1)))]';

[T,Z] = ode45(solution,[0 10],[0.1 0.5]);
[T2,Z2] = ode45(solution,[0 10],[0.25 0.5]);
[T3,Z3] = ode45(solution,[0 10],[0.4 0.5]);

plot(T,Z(:,1),'-',T,Z(:,2),'-.')  
%title('Matching Pennies');
xlabel('t');
ylabel('x & y');
set(findobj(gca,'Type','line'),'LineWidth',2);
axis([0 10 -.5 1.5]);

figure
plot(Z(:,1),Z(:,2),'-')
hold on
plot(Z2(:,1),Z2(:,2),'-')
hold on
plot(Z3(:,1),Z3(:,2),'-')

set(findobj(gca,'Type','line'),'Color','r','LineWidth',2);
%title('Matching Pennies');
xlabel('Player 1, probability of playing Heads');    
ylabel('Player 2, probability of playing Heads');     

hold on
[X,Y] = meshgrid(0:0.05:1);
V = Y.*(1-Y).*(2*X - 2*(1-X));
U = X.*(1-X).*((-2)*Y - (-2)*(1-Y));
quiver(X,Y,U,V,0.6,'b');
axis tight;
hold off

figure
[X,Y] = meshgrid(0:0.05:1);
V = Y.*(1-Y).*(2*X - 2*(1-X));
U = X.*(1-X).*((-2)*Y - (-2)*(1-Y));
quiver(X,Y,U,V,0.6,'b');
axis tight;
hold on

Array=csvread('pennies_QLearnerA4_QLearnerB41.csv');
line1 = Array(2, :);
line2 = Array(3, :);
%line1filtered = line1(1, 10:1:5000);
%line2filtered = line2(1, 10:1:5000);
line1filtered = cat(2, line1(1, 1:10:150), line1(1, 170:500:5000));
line2filtered = cat(2, line2(1, 1:10:150), line2(1, 70:500:5000));
plot(line2filtered, line1filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('pennies_QLearnerA4_QLearnerB42.csv');
line3 = Array(2, :);
line4 = Array(3, :);
line3filtered = cat(2, line3(1, 1:10:150), line3(1, 170:500:5000));
line4filtered = cat(2, line4(1, 1:10:150), line4(1, 70:500:5000));
plot(line4filtered, line3filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('pennies_QLearnerA4_QLearnerB43.csv');
line5 = Array(2, :);
line6 = Array(3, :);
line5filtered = cat(2, line5(1, 1:10:150), line5(1, 170:500:5000));
line6filtered = cat(2, line6(1, 1:10:150), line6(1, 170:500:5000));
plot(line6filtered, line5filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('pennies_QLearnerA4_QLearnerB44.csv');
line7 = Array(2, :);
line8 = Array(3, :);
line7filtered = cat(2, line7(1, 1:10:150), line7(1, 170:500:5000));
line8filtered = cat(2, line8(1, 1:10:150), line8(1, 170:500:5000));
plot(line8filtered, line7filtered, 'r', 'LineWidth',2)
hold on



xlabel('Player 1, probability of playing Heads');    
ylabel('Player 2, probability of playing Heads');  

hold off



figure
[X,Y] = meshgrid(0:0.05:1);
V = Y.*(1-Y).*(2*X - 2*(1-X));
U = X.*(1-X).*((-2)*Y - (-2)*(1-Y));
quiver(X,Y,U,V,0.6,'b');
axis tight;
hold on

Array=csvread('pennies_MCILearnerA4_MCILearnerB41.csv');
line1 = Array(2, :);
line2 = Array(3, :);
%line1filtered = line1(1, 10:1:5000);
%line2filtered = line2(1, 10:1:5000);
line1filtered = cat(2, line1(1, 1:10:150), line1(1, 170:200:2000));
line2filtered = cat(2, line2(1, 1:10:150), line2(1, 70:200:2000));
plot(line2filtered, line1filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('pennies_MCILearnerA4_MCILearnerB42.csv');
line3 = Array(2, :);
line4 = Array(3, :);
line3filtered = cat(2, line3(1, 1:10:150), line3(1, 170:200:2000));
line4filtered = cat(2, line4(1, 1:10:150), line4(1, 70:200:2000));
plot(line4filtered, line3filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('pennies_MCILearnerA4_MCILearnerB43.csv');
line5 = Array(2, :);
line6 = Array(3, :);
line5filtered = cat(2, line5(1, 1:10:150), line5(1, 170:200:2000));
line6filtered = cat(2, line6(1, 1:10:150), line6(1, 170:200:2000));
plot(line6filtered, line5filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('pennies_MCILearnerA4_MCILearnerB44.csv');
line7 = Array(2, :);
line8 = Array(3, :);
line7filtered = cat(2, line7(1, 1:10:150), line7(1, 170:200:2000));
line8filtered = cat(2, line8(1, 1:10:150), line8(1, 170:200:2000));
plot(line8filtered, line7filtered, 'r', 'LineWidth',2)
hold on



xlabel('Player 1, probability of playing Heads');    
ylabel('Player 2, probability of playing Heads');  

hold off
