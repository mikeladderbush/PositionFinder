class LoginException(Exception):
    
    '''Login not working'''
    
class FilterException(Exception):
    
    '''Filters not setting correctly'''
    
class GetJobsException(Exception):
    
    '''Unable to get jobs correctly'''
    
class ApplicationStepException(Exception):
    
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        super().__init__(arg1, arg2)
        
    def __str__(self):
         return f'ApplicationStepException: Step={self.arg1}, error={self.arg2}'