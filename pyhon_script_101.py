import argparse #สำหรับรับ input จากภายนอก
import subprocess #สำหรับ run terminal command

#import flask #สำหรับทำ Webapp เเละ Web service api



def print_other():
        print('somthing else')


if __name__ == "__main__":
        x = 2
        y = 3
        print(f'calculate {x} x {y} = {x*y}')
        