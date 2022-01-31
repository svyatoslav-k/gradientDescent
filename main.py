import matplotlib.pyplot as plt
from gradient_descent import GradientDescent

input_x = [1, 2, 3, 4, 5]
input_y = [1, 4, 9, 16, 26]
input_data = list(zip(input_x, input_y))
predict_for_x = 8

gd = GradientDescent(input_data)
q0, q1 = gd.calculate_coefficients()

predict_y = q0 + q1 * predict_for_x

x_values_for_line = [1, 12]
y_values_for_line = [q0 + q1 * x_values_for_line[0], q0 + q1 * x_values_for_line[1]]

plt.plot(input_x, input_y, 'go')
plt.plot(x_values_for_line, y_values_for_line)
plt.plot(predict_for_x, predict_y, 'bo')
plt.axis([0, 10, 0, 45])
plt.show()
