#!/usr/bin/python3
"""Commandline interpreter that creates objects of the project"""
import cmd
from datetime import datetime
from uuid import uuid4
from models import storage
from models.base_model import BaseModel
from models.event import Event
from models.user import User
import models
import re
import os
import shlex
import sys


class CommandLine(cmd.Cmd):
    """The class that implements the console"""

    classes = {
                "BaseModel": BaseModel, "User": User, "Event": Event
                }

    dot_cmds = ["count", "show", "all", "update", "destroy"]

    types = {

            }

    prompt = "akwaaba >> "

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('akwaaba >> ')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in CommandLine.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] =='}'\
                            and type(eval(pline)) == dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """Command to exit from the program"""
        return True
    
    def do_exit(self, line):
        """Command to exit from the program"""
        return True

    def do_quit(self, line):
        """Command to exit from the program"""
        return True

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def do_create(self, args):
        """ Create an object of any class"""
        ignored_attrs = ('id', 'created_at', 'updated_at', '__class__')
        class_name = ''
        name_pattern = r'(?P<name>(?:[a-zA-Z]|_)(?:[a-zA-Z]|\d|_)*)'
        class_match = re.match(name_pattern, args)
        obj_kwargs = {}
        if class_match is not None:
            class_name = class_match.group('name')
            params_str = args[len(class_name):].strip()
            params = params_str.split(' ')
            str_pattern = r'(?P<t_str>"([^"]|\")*")'
            float_pattern = r'(?P<t_float>[-+]?\d+\.\d+)'
            int_pattern = r'(?P<t_int>[-+]?\d+)'
            description_pattern = r'(?P<description>.+)'
            param_pattern = '{}=({}|{}|{}|{})'.format(
                name_pattern,
                str_pattern,
                float_pattern,
                int_pattern,
                description_pattern
            )
            for param in params:
                param_match = re.fullmatch(param_pattern, param)
                if param_match is not None:
                    key_name = param_match.group('name')
                    str_v = param_match.group('t_str')
                    float_v = param_match.group('t_float')
                    int_v = param_match.group('t_int')
                    desc_v = param_match.group('description')
                    if float_v is not None:
                        obj_kwargs[key_name] = float(float_v)
                    elif int_v is not None:
                        obj_kwargs[key_name] = int(int_v)
                    elif str_v is not None:
                        obj_kwargs[key_name] = str_v[1:-1].replace('_', ' ')
                    elif desc_v is not None:
                        obj_kwargs['description'] = desc_v
        else:
            class_name = args
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in CommandLine.classes:
            print("** class doesn't exist **")
            return
        if os.getenv('STORAGE_TYPE') == 'db':
            if not hasattr(obj_kwargs, 'id'):
                obj_kwargs['id'] = str(uuid4())
            if not hasattr(obj_kwargs, 'created_at'):
                obj_kwargs['created_at'] = str(datetime.now())
            if not hasattr(obj_kwargs, 'updated_at'):
                obj_kwargs['updated_at'] = str(datetime.now())
            new_instance = CommandLine.classes[class_name](**obj_kwargs)
            new_instance.save()
            print(new_instance.id)
        else:
            new_instance = CommandLine.classes[class_name]()
            for key, value in obj_kwargs.items():
                if key not in ignored_attrs:
                    setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        cls = self.parseline(line)[0]
        cls_id = self.parseline(line)[1]
        if cls is None:
            print("** class name missing **")
        elif cls not in self.classes:
            print("** class doesn't exist")
        elif cls_id == "":
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if cls_id == value.id:
                    print(value)
                    return
            print("** No Instance Found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name"""
        cls = self.parseline(line)[0]
        if line != "" and cls not in self.classes:
            print("** class doesn't exist **")
        else:
            new_list = []
            for obj in storage.all().values():
                if cls in self.classes or line == "":
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""

        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in CommandLine.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in CommandLine.types:
                    att_val = CommandLine.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        arg = parse(line)
        count = 0
        for obj in models.storage.all().values():
            if arg[0] == type(obj).__name__:
                count += 1
        print(count)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        cls = self.parseline(line)[0]
        cls_id = self.parseline(line)[1]
        if cls is None:
            print("** class name missing **")
        elif cls not in self.classes:
            print(" ** class doesn't exist **")
        elif cls_id == "":
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if cls_id == value.id:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")


if __name__ == "__main__":
    CommandLine().cmdloop()
