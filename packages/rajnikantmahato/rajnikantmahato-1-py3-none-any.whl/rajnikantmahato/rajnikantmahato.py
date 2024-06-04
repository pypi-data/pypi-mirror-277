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

def rajni(*args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        # print("No arguments provided")
        return
        
    if len(args) == 1 and len(kwargs) == 0:
        # print("Only one value")
        print(args[0])
        return
    

    for arg in args:
        print(arg)
    

    for key, value in kwargs.items():
        print(f"{key}: {value}")
# rajni(1+5,"hi")