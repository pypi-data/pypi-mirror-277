r = '''
# #====================================
# Auther : RAJNI WEB DEVELOPER ======
# Date   : 04/06/2024 ===============
# Version : 1.0.0 ===================
# About  : personal Module ======
# Insta  : rajni.kant.mahato ========
# Whatsapp  : +919771241425 =========
# Telegram : Simplehacker1 ==========
# #====================================

# LICENCE UDYAM-JH-06-0039636
# ENTERPRISE RAJNI WEB DEVELOPER
# Copyright (c) 2022 - 2024 The SM02

# Permission is hereby granted, free of charge, to any person or MSME (Micro, Small, and Medium Enterprises) obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software with permission from the author, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons or MSMEs to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# Usage without explicit permission from the author is strictly prohibited.
# If you have any inquiries or need permission, please contact the author.

# THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
'''
import requests

rajni = print
# hello = print
bol_bhai = print

def health():
    url = 'https://rajnikantmahato.me/health'
    data = requests.get(url)
    data = data.json()

    status = data.get('status')

    kolkata_time = ''


    
    for timezone_data in data.get('timezones', []):
        if timezone_data['timezone'] == 'Asia/Kolkata':
            kolkata_time = timezone_data['current_time']
            # print("Kolkata Time:", kolkata_time)
            break
    else:
        print("Kolkata timezone data not found in the response")
    print(status,kolkata_time)

# health()

# def jab_tak_bhai(condition, body_func):
    # while condition():
        # body_func()
# def bol_bhai(msg):
#     print(msg)


# def bhai_ye_hai(var_name, value):
#     globals()[var_name] = value

# def jab_tak_bhai(condition_func, body_func):
#     while condition_func():
#         body_func()

# def agar_bhai(condition_func, if_body_func, else_body_func=None):
#     if condition_func():
#         if_body_func()
#     elif else_body_func is not None:
#         else_body_func()

# def nahi_to_bhai(condition_func, body_func):
#     if condition_func():
#         body_func()




# Implementation of your custom script
# hi_bhai = True

# if hi_bhai:
#     bol_bhai("Hello World")
    
#     bhai_ye_hai('a', 3)
#     bhai_ye_hai('b', 0)

#     def condition():
#         return b < 5

#     def body():
#         global b
#         bol_bhai(b)
#         agar_bhai(lambda: b == a, 
#                   lambda: bol_bhai("b is equal to a"), 
#                   lambda: nahi_to_bhai(lambda: b == 0, 
#                                        lambda: bol_bhai("b is equal to zero")))
#         b += 1

#     jab_tak_bhai(condition, body)

# bye_bhai = True

# if bye_bhai:
#     pass

# def hellos():
#     print('a')

# jab_tak_bhai(hellos)

# while True:
#     print ("hi")