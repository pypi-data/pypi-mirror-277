from .front_end_types import * 

# from utils import query_checker
def query_checker():
    pass

class RowBase:
    def __init__(self, types_allowed: TypesAllowed, args_mapping: ArgsMapping, runtime_checking):
        self.types_allowed = types_allowed
        self.runtime_checking = runtime_checking
        
        self.args_order, self.args_types = args_mapping
        self.length = len(self.args_order)
        
    def map_type(self, arg: Any, checking: str = 'High', architecture='polars') -> TypeMapping
        caught_type, serializaed_arg = get_type(arg, backend)
        
        # Granular control over user-defined types within their tables... great for working with multiple types of data!
        if not in caught_type in self.types_allowed:
            raise Exception(f'{caught_type} not in allowed types!')
        
        # Fix based on SQLite, Polars, mmap, and PostgreSQL
        ## Wont be a simple if else statement, but dependent on the directional usage
        if caught_type not in orm_types:
            raise Exception(f'{caught_type} not allowed in orm_types')
        
        match checking:
            case 'High':
                return (arg, type(arg))
            case _:
                return arg
        
class Table(RowBase):
    dataframe_options: Options = ('pandas', 'polars', 'custom_cache')
    runtime_checking_options: Options = ('high', 'medium', 'low')
    
    def __init__(self, name: str, types_allowed: TypesAllowed, args_mapping: ArgsMapping, runtime_checking: bool = 'High', dataframe_backend: str = None):
        if runtime_checking not in self.runtime_checking_options:
            raise Exception(f'{runtime_checking} not supported!')
            
        super().__init__(types_allowed, args_mapping, runtime_checking)
        
        self.name = name
        
        # Deal with backends later!

    def create(self, row_items: ArgsData, rely_to: str = 'stdout') -> bool:
        match self.runtime_checking:
            case 'high':
                res = ((arg_name: self.map_type(arg_name, row_items[arg_name])) for arg_name in self.args_order])
            case 'medium':
                res = (self.map_type(arg_name, row_items[arg_name]) for arg_name in self.args_order])
            case _:
                res = (args_data[arg_name] for arg_name in self.args_order) 
        
        match rely_to:
            case 'stdout':
                print(res)
            case 'database':
                pass
            case 'backend':
                pass
        
        return True
        
    def verify_row(self, row: Row) -> bool | str:
        if len(row) != self.length:
            return 'Lengths do not match'
            
        for idx, arg_mapping in enumerate(row):
            arg_name, type_mapping = arg_mapping
            
            if arg_name != self.args_order[idx]:
                return f'{arg_name} != {self.args_order[idx]}'
            if type_mapping[1] != self.args_types[idx]:
                return f'{type_mapping[1]} != {self.args_types[idx]}'
                
        return True
    
class Connection:
    def __init__(self, uri, connection_pool, connection_strategy):
        pass
    
class Session(Connection):
    def __init__(self, uri: URI, connection_pool: int, connection_strategy: str, safe_queries: bool = True):
        super().__init__(uri, connection_pool, connection_strategy)
        self.safe_queries = safe_queries
        
    async def submit_query(self, query: Query) -> TaskIdentifier:
        return await self.submit_query(query)
        
    async def getter(self, query: Query, timeout: Time, limit: int = None) -> Results:
        task_identifier = await self.submit_query(query, limit, timeout)
        
        return await self.get_data(task_identifier)
        
    def check_query(self, query: Query) -> bool:
        return query_checker(query)
        
    async def handler(self, query: Query, limit: int = None, timeout: Time = 2000):
        if self.safe_queries and not self.check_query(query):
            raise Exception(f'{query} isn\'t acceptable')
            
        match limit:
            case 1:
                return await self.getter(query, timeout, limit=1)
            case _:
                return await self.getter(query, timeout)
