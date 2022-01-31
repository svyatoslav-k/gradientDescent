class GradientDescent:
    def __init__(self, data):
        self.data = data

    def calculate_coefficients(self):
        q0, q1 = 10, 10
        a = 0.1
        j_previous = self._calc_cost_function(q0, q1)
        step = 0
        while True:
            q0 = q0 - a * self._calc_derivative_q0(q0, q1)
            q1 = q1 - a * self._calc_derivative_q1(q0, q1)
            j_current = self._calc_cost_function(q0, q1)
            if j_current < j_previous:
                j_previous = j_current
                step += 1
            else:
                print(f'q0: {q0}, q1: {q1}')
                print(f'steps: {step}')
                print(f'j_previous: {j_previous}')
                return q0, q1

    def _calc_cost_function(self, q0, q1):
        res = 0
        for val in self.data:
            res += ((q0 + q1 * val[0] - val[1]) ** 2)
        return res / (2 * len(self.data))

    def _calc_derivative_q0(self, q0, q1):
        res = 0
        for val in self.data:
            res += (q0 + q1 * val[0] - val[1])
        return res / len(self.data)

    def _calc_derivative_q1(self, q0, q1):
        res = 0
        for val in self.data:
            res += ((q0 + q1 * val[0] - val[1]) * val[0])
        return res / len(self.data)
