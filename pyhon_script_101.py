import argparse #สำหรับ รับ input จากภายนอก
import subprocess #สำหรับรัน terminal command 

#import flask # สำหรับทำ web app และ web service api


def print_other():
    print('something else')

if _name__=="__main_":
    parser = argparse.ArgumentParser(description='test program to learn about argparse ')
    parser.add_argument(
        'x',
        help='value of x')
    parser.add_argument(
        '--yval',
        type=int,
        default=3,
        help='value of y')
    args = parser.parse_args()

    x = args.x
    y = args.yval
    print(f'calculate {x} x {y} = {x*y}')