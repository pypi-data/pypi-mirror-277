from typing import TypeVar as _TypeVar, Generic as _Generic, Type as _Type, Callable as _Callable, Iterable as _Iterable, Literal as _Literal
import argparse as _argparse

_T = _TypeVar('_T')

class Arguments:
    class Template:
        """
        Example blueprint::

            def __init__(self):
                #Value will be stored in property name, argument name specifiers are what is typed on the cli
                self.ToggleFlagName = Arguments.ArgumentToggle('--ToggleFlag-Name', help='...')
                self.PositionalArguments = Arguments.ArgumentList()
                self.StringList = Arguments.ArgumentList('--string-list')
                self.Number = Arguments.Argument('-n', '--number', type=int, help="...", required=True)
                self.String = Arguments.Argument('-s', '--string', default="hello", help="...")
        """
    def __init__(self, **kwargs):
        for name in kwargs['name']:
            if not(name.startswith('-')):
                raise NameError("Non positional arguments must be prefixed with '-'")
        self.default = None
        self.type:_Type = None
        self.name:tuple[str] = None
        self.help:str = None
        self.required:bool = None
        self.choices:_Iterable = None
        self.nArgs = None
        self.useBooleanToggle = False
        self.__dict__.update(kwargs)

    @classmethod
    def Argument(cls, *name:str, default=None, type:_Type[_T]|_Callable[[str], _T]=str, choices:_Iterable=None, required:bool=None, help:str=None) -> _T:
        """
        Create a new argument

        :param name: The names or flags for the argument. If no flag name is supplied then it becomes a positional argument.
        :param default: The default value of the argument.
        :param type: The type of the argument (str,int,bool) or a callback that recieves str as input.
        :param choices: Specifies which values are allowed for this argument
        :param required: Whether the argument is required.
        :param help: The help description for the argument.
        """
                
        return cls(**locals())

    @classmethod
    def ArgumentList(cls, *name:str, default=None, type:_Type[_T]|_Callable[[str], _T]=str, nArgs:int|_Literal['?','*','+','...']='+',choices:_Iterable=None, required:bool=None, help:str=None) -> list[_T]:
        """
        Create a new argument that accepts a list of values.

        :param name: The names or flags for the argument. If no flag name is supplied then it becomes a positional argument.
        :param default: The default value of the argument.
        :param type: The type of the argument (str,int,bool) or a callback that recieves str as input.
        :param nArgs: number of args to accept, special symbols(?: 0 or 1, *: 0 or more, +: atleast 1, '...': all rest of the arguments even if they are prefixed)
        :param choices: Specifies which values are allowed for this argument
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
    def __init__(self, template:_Type[_T], description:str=None, add_help=True):
        template:Arguments.Template = template()
        self._parser = _argparse.ArgumentParser(description=description, add_help=add_help)
        self._Map_Parser(self._parser, template)

    def _Map_Parser(self, parser:_argparse.ArgumentParser, template:_Type[_T]):
        for key,argument in template.__dict__.items():
            if not(isinstance(argument, Arguments)):
                continue
            
            #argparse requires some params to not be inputted at all if they are None
            kwargs = {'dest': key}
            if(argument.help is not None):
                kwargs['help'] = argument.help

            if(argument.useBooleanToggle):
                parser.add_argument(*argument.name, action="store_true", **kwargs)
                continue
            
            if(argument.nArgs is not None):
                kwargs['nargs'] = argument.nArgs
            if(argument.type is not None):
                kwargs['type'] = argument.type
            if(argument.default is not None):
                kwargs['default'] = argument.default
            if(argument.required is not None):
                kwargs['required'] = argument.required
            if(argument.choices is not None):
                kwargs['choices'] = argument.choices

            parser.add_argument(*argument.name, **kwargs)
    
    def Parse(self, arguments:list[str], ignoreUnkownArguments=True) -> _T:
        if(ignoreUnkownArguments):
            args, unkown = self._parser.parse_known_args(args=arguments)
        else:
            args = self._parser.parse_args(args=arguments)
        return args

