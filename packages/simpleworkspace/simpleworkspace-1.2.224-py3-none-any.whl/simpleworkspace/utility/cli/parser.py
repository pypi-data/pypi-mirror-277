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
        self.useMultipleArgs = False
        self.useBooleanToggle = False
        self.__dict__.update(kwargs)
    
    @classmethod
    def Argument(cls, *name:str, default=None, type:_Type[_T]|_Callable[[str], _T]=str, required:bool=None, help:str=None) -> _T:
        return cls(locals())

    @classmethod
    def ArgumentList(cls, *name:str, default=None, type:_Type[_T]|_Callable[[str], _T]=str, required:bool=None, help:str=None) -> list[_T]:
        return cls(locals(), useMultipleArgs=True)

    @classmethod
    def ArgumentToggle(cls, *name:str, help:str=None) -> bool:
        return cls(locals(), useBooleanToggle=True)

class CLIParser(_Generic[_T]):
    def __init__(self, template:_Type[_T], description:str=None):
        import argparse

        template = template()
        self._parser = argparse.ArgumentParser(description=description)
        for key,argument in template.__dict__.items():
            if not(isinstance(argument, Arguments)):
                continue
            
            if(argument.useBooleanToggle):
                self._parser.add_argument(*argument.name, action="store_true", help=argument.help, dest=key)
                continue
            
            self._parser.add_argument(
                *argument.name,
                type=argument.type,
                nargs='+' if argument.useMultipleArgs else None,
                required=argument.required, 
                default=argument.default, 
                help=argument.help, 
                dest=key)
    
    def Parse(self, ignoreUnkownArguments=True) -> _T:
        if(ignoreUnkownArguments):
            args, unkown = self._parser.parse_known_args()
        else:
            args = self._parser.parse_args()
        return args

