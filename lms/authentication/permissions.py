
from django.shortcuts import redirect

# @permission_roles(roles=['Instructor'])
# permission decorators

def permission_roles(roles):

    def decorator(fn):

        def wrapper(request,*args,**kwargs):

            if request.user.is_authenticated and request.user.role in roles :

                return fn(request,*args,**kwargs)
            
            return redirect('login')
    
        return wrapper 
    
    return decorator
