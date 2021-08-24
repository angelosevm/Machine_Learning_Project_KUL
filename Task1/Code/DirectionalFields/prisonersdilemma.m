%{
 Payoff matrices : A = [3 0; 5 1] and B = [3 5; 0 1], Symmetric game -> 1
 population model
%}

solution = @(t,z) [z(1).*(1-z(1)).*(3*z(2) - (-4)*(1-z(2))), z(2).*(1-z(2)).*(3*z(1) - (-4)*(1-z(1)))]';

[T,Z] = ode45(solution,[0 10],[0.2 0.2]);
[T2,Z2] = ode45(solution,[0 10],[0.2 0.4]);
[T3,Z3] = ode45(solution,[0 10],[0.4 0.2]);
[T4,Z4] = ode45(solution,[0 10],[0.2 0.6]);
[T5,Z5] = ode45(solution,[0 10],[0.6 0.2]);

plot(T,Z(:,1),'-',T,Z(:,2),'-.')  
%title('Prisoner''s Dilemma');
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
hold on
plot(Z4(:,1),Z4(:,2),'-')
hold on
plot(Z5(:,1),Z5(:,2),'-')

set(findobj(gca,'Type','line'),'Color','r','LineWidth',2);
%title('Prisoner''s Dilemma');
xlabel('Player 1, probability of betraying');    
ylabel('Player 2, probability of betraying');     

hold on
[X,Y] = meshgrid(0:0.05:1);
V = Y.*(1-Y).*(3*X - (-4)*(1-X));
U = X.*(1-X).*(3*Y - (-4)*(1-Y));
quiver(X,Y,U,V,0.6,'b');
axis tight;
hold off

figure
[X,Y] = meshgrid(0:0.05:1);
V = Y.*(1-Y).*(3*X - (-4)*(1-X));
U = X.*(1-X).*(3*Y - (-4)*(1-Y));
quiver(X,Y,U,V,0.6,'b');
axis tight;
hold on

Array=csvread('prisoners_QLearnerA4_QLearnerB41.csv');
line1 = Array(2, :);
line2 = Array(3, :);
line1filtered = cat(2, line1(1, 1:20:150), line1(1, 170:50:1000));
line2filtered = cat(2, line2(1, 1:20:150), line2(1, 170:50:1000));
plot(line1filtered, line2filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_QLearnerA4_QLearnerB42.csv');
line3 = Array(2, :);
line4 = Array(3, :);
line3filtered = cat(2, line3(1, 1:20:150), line3(1, 170:50:1000));
line4filtered = cat(2, line4(1, 1:20:150), line4(1, 170:50:1000));
plot(line3filtered, line4filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_QLearnerA4_QLearnerB43.csv');
line5 = Array(2, :);
line6 = Array(3, :);
line5filtered = cat(2, line5(1, 1:20:150), line5(1, 170:50:1000));
line6filtered = cat(2, line6(1, 1:20:150), line6(1, 170:50:1000));
plot(line5filtered, line6filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_QLearnerA4_QLearnerB44.csv');
line7 = Array(2, :);
line8 = Array(3, :);
line7filtered = cat(2, line7(1, 1:20:150), line7(1, 170:50:1000));
line8filtered = cat(2, line8(1, 1:20:150), line8(1, 170:50:1000));
plot(line7filtered, line8filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_QLearnerA4_QLearnerB45.csv');
line9 = Array(2, :);
line10 = Array(3, :);
line9filtered = cat(2, line9(1, 1:20:150), line9(1, 170:50:1000));
line10filtered = cat(2, line10(1, 1:20:150), line10(1, 170:50:1000));
plot(line9filtered, line10filtered, 'r', 'LineWidth',2)
hold on

%title('Prisoner''s Dilemma');
xlabel('Player 1, probability of betraying');    
ylabel('Player 2, probability of betraying');

hold off




figure
[X,Y] = meshgrid(0:0.05:1);
V = Y.*(1-Y).*(3*X - (-4)*(1-X));
U = X.*(1-X).*(3*Y - (-4)*(1-Y));
quiver(X,Y,U,V,0.6,'b');
axis tight;
hold on

Array=csvread('prisoners_MCILearnerA4_MCILearnerB41.csv');
line1 = Array(2, :);
line2 = Array(3, :);
line1filtered = cat(2, line1(1, 1:20:150), line1(1, 170:50:1500));
line2filtered = cat(2, line2(1, 1:20:150), line2(1, 170:50:1500));
plot(line1filtered, line2filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_MCILearnerA4_MCILearnerB42.csv');
line3 = Array(2, :);
line4 = Array(3, :);
line3filtered = cat(2, line3(1, 1:20:150), line3(1, 170:50:1500));
line4filtered = cat(2, line4(1, 1:20:150), line4(1, 170:50:1500));
plot(line3filtered, line4filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_MCILearnerA4_MCILearnerB43.csv');
line5 = Array(2, :);
line6 = Array(3, :);
line5filtered = cat(2, line5(1, 1:20:150), line5(1, 170:50:1500));
line6filtered = cat(2, line6(1, 1:20:150), line6(1, 170:50:1500));
plot(line5filtered, line6filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_MCILearnerA4_MCILearnerB44.csv');
line7 = Array(2, :);
line8 = Array(3, :);
line7filtered = cat(2, line7(1, 1:20:150), line7(1, 170:50:1500));
line8filtered = cat(2, line8(1, 1:20:150), line8(1, 170:50:1500));
plot(line7filtered, line8filtered, 'r', 'LineWidth',2)
hold on
Array=csvread('prisoners_MCILearnerA4_MCILearnerB45.csv');
line9 = Array(2, :);
line10 = Array(3, :);
line9filtered = cat(2, line9(1, 1:20:150), line9(1, 170:50:1500));
line10filtered = cat(2, line10(1, 1:20:150), line10(1, 170:50:1500));
plot(line9filtered, line10filtered, 'r', 'LineWidth',2)
hold on

%title('Prisoner''s Dilemma');
xlabel('Player 1, probability of betraying');    
ylabel('Player 2, probability of betraying');

hold off


