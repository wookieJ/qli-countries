from model.parameter import Parameter


def run():
    parameter = Parameter('health')
    parameter.load_sub_params()
    parameter.print_sub_params_values(print_label=True)
    print('Raw values:')
    print(parameter.get_values())


if __name__ == '__main__':
    run()
