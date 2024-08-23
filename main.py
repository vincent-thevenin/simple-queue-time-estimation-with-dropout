import time
import numpy as np

def test():
    cum_time_list = [0, 120, 184]
    n_list = [294, 239, 200]

    n = n_list[-1]
    estimate, _, _, _, rcond = np.polyfit(n_list, cum_time_list, 2, full=True)

    b = -estimate[0]*2
    a = -estimate[1]
    gn = estimate[2]
    formula_gn = a*n_list[0] + b/2 * n_list[0]**2

    print("Found: b = {}, a = {}, gn = {}, formula_gn = {}".format(b, a, gn, formula_gn))
    print("Rcond: {}".format(rcond))

    # time left
    time_left = a*n + b/2 * n**2
    print("Time left: {} min, {} sec".format(int(time_left//60), int(time_left%60)))

    print("n_list: {}".format(n_list))
    print("cum_time_list: {}".format(cum_time_list))

    print()

def add_cum_time(cum_time_list, start):
    cum_time = time.time() - start

    # round to nearest 8
    cum_time = round(cum_time/8)*8
    print("Interval: {}s".format(cum_time - cum_time_list[-1]))

    cum_time_list.append(cum_time)
    return cum_time_list 

def main():
    cum_time_list = []
    n_list = []

    n = 1
    while n:
        n = input("Enter queue position:")
        if n == "":
            break
        try:
            n = int(n)
        except:
            n = 1
            print("Invalid input. Please enter a number.")
            continue

        if not n_list:  # initialize
            start = time.time()
            cum_time_list.append(0)
            n_list.append(n)
        else:
            cum_time_list = add_cum_time(cum_time_list, start)
            n_list.append(n)

            # predicting time left from start to now
            estimate, _, _, _, rcond = np.polyfit(n_list, cum_time_list, 2, full=True)
            linear_estimate = np.polyfit(n_list, cum_time_list, 1, full=False)

            b = -estimate[0] * 2
            a = -estimate[1]
            C = estimate[2]
            formula_C = a*n_list[0] + b/2 * n_list[0]**2

            a_linear = -linear_estimate[0]
            c_linear = linear_estimate[1]

            print("Found: b = {}, a = {}, C = {}, formula_C = {}".format(b, a, C, formula_C))
            print("Linear estimate: a = {}, c = {}".format(a_linear, c_linear))
            print("Rcond: {}".format(rcond))

            # time left
            time_left = a*n + b/2 * n**2
            linear_time_left = a_linear*n + c_linear
            print("Time left: {} min, {} sec".format(int(time_left//60), int(time_left%60)))
            print("Linear time left: {} min, {} sec".format(int(linear_time_left//60), int(linear_time_left%60)))

        print("n_list: {}".format(n_list[-8:]))
        print("cum_time_list: {}".format(cum_time_list[-8:]))

        print()

if __name__ == "__main__":
    main()


