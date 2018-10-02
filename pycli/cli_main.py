""" core file for the pycli module """
from inspect import signature


class cli(object):
    def __init__(self):
        self.function_list = {'stop': [self.stop, 0], 'help': [self.cli_help, 1]}
        self.is_active = False
        print('functions have style --  func>arg1,arg2')

    def start(self):
        print('type help for a list of available commands!')
        self.is_active = True
        while self.is_active:
            func, args = self.usr_parse(input('--> '))
            # note use of * so func parses list as individual params
            try: 
                self.function_list[func][0](*args)
            except:
                try: 
                   print('function failed, function has args: ', list(signature(func).parameters.keys()))
                except:            
                   print('not a function!')

    def cli_input(self, usr_input):
        """ takes string as input and executes command """
        func, args = self.usr_parse(usr_input)
        # note use of * so func parses list as individual params
        try: return self.function_list[func][0](*args)
        except: return "failed"
    
    def stop(self):
        self.is_active = False
        print('CLI stopping')

    def add_func(self, function):
        try: self.function_list[function.__name__] = function, list(signature(function).parameters.keys())
        except: print('not a function!')
    
    def cli_help(self, *args):
        if len(args) == 0:
            print(self.function_list.keys())
            return str(self.function_list.keys())
        else:
            l = []
            for i in args:
                print(self.function_list[i][1])
                l += self.function_list[i][1]
            return l

    def usr_parse(self, string):
        """ internal function: gets function and parameters from string """
        split = string.split('>')
        func = split[0]

        try: args = split[1]
        except: args = []
        try: args = args.split(',')
        except: args = []
        
        
        for i in range(len(args)):
            try: args[i] = int(args[i])
            except: pass
        
        return func, args