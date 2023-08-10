#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""
Contains the entry point of the command interpreter:
"""
class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point of my command 
    interpreter.
    """
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """
        Command for exiting the program.
        """
        return True
    def do_EOF(self, arg):
        """
        Command to handle CTRL + D
        """
        return True

    def emptyline(self):
        """
        empty line + ENTER shouldn’t execute anything
        """
        return
    def help_emptyline(self):
        """Help emptyline"""
        print("Helpcommand to handle emptyline + enter")
    def help_quit(self):
        """Help quit"""
        print("Quit command to exit the program")
    def help_EOF(self):
        """Help EOF"""
        print("EOF command to handle ctrl + d")
    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. Ex: $ create
         """
        arg = line.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            basemodel = BaseModel()
            print(basemodel.id)

    def foundFunc(self, line):
        """Checks whether an argument is present or not"""
        arg = line.split()
        try:
            my_string = "{}.{}".format(arg[0], arg[1])
        except(IndexError):
            return

        storage = FileStorage()
        my_dict = storage.all()
        basemodel = BaseModel()
        foundValue = False
        for id_num in my_dict.keys():
            if id_num == my_string:
                foundValue = True
                break
        return foundValue


#do_create method to be checked.

    def help_create(self):
        """
        Creates a new instance of BaseModel.
        Usage >> help create
        """
        print("Creates a new instance of BaseModel.\
        Usage >> help create")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel
        """
        arg = line.split()
        line = line
        found = self.foundFunc(line)
        basemodel = BaseModel()
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 2:
            print("** instance id missing **")
        elif found == False:
            print("** no instance found **")
        else:
            print(basemodel.__str__())


    def help_show():
        """
        Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel
        """
        print("Prints the string representation of an instance.\
                Usage >>show classname id")
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy
        BaseModel 1234-1234-1234.
        """
        arg = line.split()
        line = line
        found = self.foundFunc(line)
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg[1] is None:
            print("** instance id missing **")
        elif found == False:
            print("** no instance found **")
        else:
            del my_dict[my_string]
            FileStorage.object_setter(my_dict)
            FileStorage.save()

    def help_destroy(self):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy
        BaseModel 1234-1234-1234.
        """
        print("Deletes an instance based on the class name.\
        Usage >> destroy classname id")


    #Check the function below later
    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.
        """
        arg = line.split()
        if (line not in globals() or not isinstance(globals()[arg[0]], type)) and (len(arg) > 0):
            print("** class doesn't exist **")
        else:
            print(BaseModel.__str__())
            

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        arg = line.split()
        my_string = "{}.{}".format(arg[0], arg[1])
        storage = FileStorage()
        my_dict = storage.all()
        basemodel = BaseModel()
        found = False
        for id_num in my_dict.keys():
            if id_num == my_string:
                found = True
                break
        if not arg:
            print("** class name missing **")
        elif arg[0] not in globals() or not isinstance(globals()[arg[0]], type):
            print("** class doesn't exist **")
        elif arg[1] is None:
            print("** instance id missing **")
        elif found == False:
            print("** no instance found **")
        elif arg[2] is None:
            print("** attribute name missing **")
        elif arg[3] is None:
            print("** value missing **")
        else:
            my_dict[arg[2]] = arg[3]
            FileStorage().object_setter(my_dict)
            FileStorage.save(self)


    def help_update(self):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        print("Updates an instance based on the classname.\
                Usage >> update classname id")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
