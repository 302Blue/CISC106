% estimate pi with the Monte Carlo Method

% plot circle with radius 1
% x ^ 2 + y ^ 2 = 1, y = (1 - x ^ 2) ^ 0.5
% x = -1:0.01:1;
% y = (1 - x .^ 2) .^ 0.5;
% hold off
% plot(x, y, 'k', x, -y, 'k', 'Linewidth', 2)
% axis image
% title('Monte Carlo Estimation of Pi', 'Fontsize', 20)

% ask user for number of darts
total_darts = get_num_darts();
circle_darts = 0;

tic

hold on
for dart = 1:total_darts
    % randomly pick dart location
    x = 2 * rand() - 1;
    y = 2 * rand() - 1;
    
    % plot dart
    %scatter(x, y, 20, 'fill')
    
    % draw every 50 darts
%     if mod(dart, 50) == 0
%         drawnow
%     end
    
    % did dart land in circle?
    if (x ^ 2 + y ^ 2) ^ 0.5 < 1
        circle_darts = circle_darts + 1;
    end
end

mc_pi = 4 * circle_darts / total_darts;

toc

%mc_pi
disp(['Monte Carlo estimate of pi = ' num2str(mc_pi, 9)])

