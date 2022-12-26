from collections import defaultdict
from functools import wraps
from typing import Dict, Any, List


class TryTry:

    def __init__(self):
        self.exception_: Dict[Any, List] = defaultdict(list)

    def __call__(self, *args, **kwargs):
        return self.try_(*args, **kwargs)

    def try_(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                _exceptions = self.exception_.get(func.__name__, []) + self.exception_.get('__all__', [])

                handlers = []
                for _exception in _exceptions:
                    for exception, handler in _exception.items():
                        if isinstance(e, exception):
                            handlers.append(handler)

                if not handlers:
                    raise e

                for handler in handlers:
                    handler(func, e)

        wrapper.exception = lambda *exceptions: self._except_f(wrapper, *exceptions)
        return wrapper

    def _except_f(self, wrapper, *exceptions):
        """指定函数的异常处理"""
        def decorator(f):
            for e in exceptions:
                self.exception_[wrapper.__name__].append({e: f})
            return f

        return decorator

    def exception(self, *exceptions):
        """全局异常处理"""
        def decorator(f):
            for e in exceptions:
                self.exception_['__all__'].append({e: f})
            return f

        return decorator


trytry = TryTry()
