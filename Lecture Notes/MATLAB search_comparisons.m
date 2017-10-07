% compare linear and binary searches
n = [.01:0.01:200 300:100:1000000];
linear = n / 2;
binary = log2(n);

hold off
plot(n, linear, 'b', 'Linewidth', 2)
hold on
plot(n, binary, 'g', 'Linewidth', 2)
legend('Linear', 'Binary')

axis([0 1000 0 20])

xlabel('Size of Search Space', 'Fontsize', 14)
ylabel('Average Number of Comparisons', 'Fontsize', 14)
title('Linear versus Binary Search', 'Fontsize', 20)
set(gca, 'Fontsize', 12)

set(gca, 'XTick', 0:200:1000)
set(gca, 'YTick', 0:4:20)

grid on