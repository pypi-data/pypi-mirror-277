from typing import TypeVar as _TypeVar, Generic as _Generic, Type as _Type, Callable as _Callable

_T = _TypeVar('_T')

class Arguments:
    def __init__(self, **kwargs):
        for name in kwargs['name']:
            if not(name.startswith('-')):
                raise NameError("Non positional arguments must be prefixed with '-'")
        self.default = None
        self.type:_Type = None
        self.name:tuple[str] = None
        self.help:str = None
        self.required:bool = None
        self.nArgs = None
        self.useBooleanToggle = False
        self.__dict__.update(kwargs)

    @classmethod
    def Argument(cls, *name:str, default=None, type:_Type[_T]|_Callable[[str], _T]=str, required:bool=None, help:str=None) -> _T:
        """
        Create a new argument

        :param name: The names or flags for the argument. If no flag name is supplied then it becomes a positional argument.
        :param default: The default value of the argument.
        :param type: The type of the argument (str,int,bool) or a callback that recieves str as input.
        :param required: Whether the argument is required.
        :param help: The help description for the argument.
        """
                
        return cls(**locals())

    @classmethod
    def ArgumentList(cls, *name:str, default=None, type:_Type[_T]|_Callable[[str], _T]=str, nArgs:str='+', required:bool=None, help:str=None) -> list[_T]:
        """
        Create a new argument that accepts a list of values.

        :param name: The names or flags for the argument. If no flag name is supplied then it becomes a positional argument.
        :param default: The default value of the argument.
        :param type: The type of the argument (str,int,bool) or a callback that recieves str as input.
        :param nArgs: number of args to accept, special symbols(?: 0 or 1, *: 0 or more, +: atleast 1)
        :param required: Whether the argument is required.
        :param help: The help description for the argument.
        """
        return cls(**locals())

    @classmethod
    def ArgumentToggle(cls, *name:str, help:str=None) -> bool:
        """
        Create a new boolean toggle flag without value, defaults to false when flag is not found, true otherwise
        
        :param name: The names or flags for the argument.
        :param help: The help description for the argument.
        """
        if(not name):
            raise ValueError("A Toggle flag must have a name identifier")
        return cls(**locals(), useBooleanToggle=True)

class CLIParser(_Generic[_T]):
    def __init__(self, template:_Type[_T], description:str=None):
        import argparse

        template = template()
        self._parser = argparse.ArgumentParser(description=description)
        for key,argument in template.__dict__.items():
            if not(isinstance(argument, Arguments)):
                continue
            
            #argparse requires some params to not be inputted at all if they are None
            kwargs = {'dest': key}
            if(argument.help is not None):
                kwargs['help'] = argument.help

            if(argument.useBooleanToggle):
                self._parser.add_argument(*argument.name, action="store_true", **kwargs)
                continue
            
            if(argument.nArgs is not None):
                kwargs['nargs'] = argument.nArgs
            if(argument.type is not None):
                kwargs['type'] = argument.type
            if(argument.default is not None):
                kwargs['default'] = argument.default
            if(argument.required is not None):
                kwargs['required'] = argument.required

            self._parser.add_argument(*argument.name, **kwargs)
    
    def Parse(self, arguments:list[str], ignoreUnkownArguments=True) -> _T:
        if(ignoreUnkownArguments):
            args, unkown = self._parser.parse_known_args(args=arguments)
        else:
            args = self._parser.parse_args(args=arguments)
        return args

