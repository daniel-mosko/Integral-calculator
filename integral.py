import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Vypocet integralu... ** "
                                             "VSTUP V TVARE: python3 integral.py '((np.sin(x)*np.e^(x))/ln(x))*x^2' 2 3 0.0001",
                                 epilog="Pozn.: Vsetky goniometricke funkcie a exponencialu treba zapisat v tvare: np.cos(x), np.e^(x) a pod.; log s lubovolnym zakladom treba napisat ako podiel prirodzenych logaritmov")
parser.add_argument("function", type=str, help="Funkcia s premennou x      -> napr. '((np.sin(x)*np.e^(x))/ln(x))*x^2'")
parser.add_argument("lower_bound", type=int, help="Spodna hranica (a)      -> napr. 2")
parser.add_argument("upper_bound", type=int, help="Horna hranica (b)      -> napr. 3")
parser.add_argument("error", type=float, help="Pozadovana chyba mensia ako *error*      -> napr. 0.0001")
args = parser.parse_args()

replace_array = ['^', 'ln']


def to_np():
    fun = args.function
    for i in replace_array:
        if i in fun:
            if i == '^':
                fun = fun.replace(i, "**")
            if i == 'ln':
                fun = fun.replace(i, f'np.log')
    return fun


function = to_np()
print("Kontrola prepisu funkcie: ", function, " pôvodný vstup: ", args.function)


def integrate():
    integral_sum = 0
    n = number_of_intervals()
    if n == 0 or n == -1:
        print("Neviem spocitat")
        return
    step = (args.upper_bound - args.lower_bound) / n
    print("Pocet intervalov:", n, " , krok:", step)
    print("Pocitam...")
    for i in range(n):
        # print(args.lower_bound + i * step, " ", value(args.lower_bound + i * step), " ", step * value(args.lower_bound + i * step))
        integral_sum += step * value(args.lower_bound + i * step)
    print("Integralny sucet:", integral_sum)


# https://imgur.com/a/ZW3pIDw - inspiracia z cvika
def number_of_intervals():
    fx0 = abs(value(args.lower_bound))
    fxk = abs(value(args.upper_bound))
    n = 0
    # zoberme ekvidistancne delenie 1/n a riesime nerovnicu
    while pow(args.error, -1) * abs(fxk - fx0) >= n:
        n += 1
        # rucna brzda :)
        if n > 10_000_000:
            return -1
    return n


# vypocet funkcnej hodnoty
def value(x):
    return eval(function)


integrate()
