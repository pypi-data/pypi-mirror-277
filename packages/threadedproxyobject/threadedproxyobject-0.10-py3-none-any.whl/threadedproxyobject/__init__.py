import threading
import time
import ctypes

NOT_ALVAILABLE = object()


class NotYetAvailable(Exception):
    pass


class ThreadedProxyObject(threading.Thread):
    r"""
    A proxy object to run a function in a separate thread and mimic its behavior until the result is available.

    Args:
        fu (callable): The function to be executed in the thread.
        args (tuple): Positional arguments to be passed to the function.
        kwargs (dict, optional): Keyword arguments to be passed to the function.
        *_args: Additional positional arguments for threading.Thread.
        **_kwargs: Additional keyword arguments for threading.Thread.

    Examples:
        def funct(x, y):
            return random.randint(x, y)

        test = ThreadedProxyObject(funct, args=(1, 200))
        test.start()
        print(dir(test))
    """

    def __init__(self, fu=None, args=(), kwargs=None, *_args, **_kwargs):
        super().__init__(*_args, **_kwargs)
        self.fu = fu
        self.args = args
        self.kwargs = kwargs
        if not self.kwargs:
            self.kwargs = {}
        self._result = NOT_ALVAILABLE

    def __str__(self):
        if self._result is not NOT_ALVAILABLE:
            return str(self._result)
        return "NOT (YET) AVAILABLE"

    def _execute_meth(self, _method2execute, *args, **kwargs):
        try:
            return getattr(
                super(),
                _method2execute,
            )(*args, **kwargs)
        except Exception as e:
            if self._result is NOT_ALVAILABLE:
                raise NotYetAvailable(
                    f"The method {_method2execute} is not (yet) available"
                )
            return getattr(
                self._result,
                _method2execute,
            )(*args, **kwargs)

    def __abs__(self, *args, **kwargs):
        return self._execute_meth("__abs__", *args, **kwargs)

    def __add__(self, *args, **kwargs):
        return self._execute_meth("__add__", *args, **kwargs)

    def __and__(self, *args, **kwargs):
        return self._execute_meth("__and__", *args, **kwargs)

    def __bool__(self, *args, **kwargs):
        return self._execute_meth("__bool__", *args, **kwargs)

    def __bytes__(self, *args, **kwargs):
        return self._execute_meth("__bytes__", *args, **kwargs)

    def __ceil__(self, *args, **kwargs):
        return self._execute_meth("__ceil__", *args, **kwargs)

    def __complex__(self, *args, **kwargs):
        return self._execute_meth("__complex__", *args, **kwargs)

    def __contains__(self, *args, **kwargs):
        return self._execute_meth("__contains__", *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        return self._execute_meth("__delitem__", *args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        return self._execute_meth("__divmod__", *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return self._execute_meth("__eq__", *args, **kwargs)

    def __float__(self, *args, **kwargs):
        return self._execute_meth("__float__", *args, **kwargs)

    def __floor__(self, *args, **kwargs):
        return self._execute_meth("__floor__", *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        return self._execute_meth("__floordiv__", *args, **kwargs)

    def __format__(self, *args, **kwargs):
        return self._execute_meth("__format__", *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return self._execute_meth("__ge__", *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        return self._execute_meth("__getitem__", *args, **kwargs)

    def __getattribute__(self, *args, **kwargs):
        try:
            return super().__getattribute__(*args, **kwargs)
        except AttributeError:
            return self._result.__getattribute__(*args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return self._execute_meth("__gt__", *args, **kwargs)

    def __hash__(self, *args, **kwargs):
        return self._execute_meth("__hash__", *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        return self._execute_meth("__iadd__", *args, **kwargs)

    def __iand__(self, *args, **kwargs):
        return self._execute_meth("__iand__", *args, **kwargs)

    def __ifloordiv__(self, *args, **kwargs):
        return self._execute_meth("__ifloordiv__", *args, **kwargs)

    def __ilshift__(self, *args, **kwargs):
        return self._execute_meth("__ilshift__", *args, **kwargs)

    def __imatmul__(self, *args, **kwargs):
        return self._execute_meth("__imatmul__", *args, **kwargs)

    def __imod__(self, *args, **kwargs):
        return self._execute_meth("__imod__", *args, **kwargs)

    def __imul__(self, *args, **kwargs):
        return self._execute_meth("__imul__", *args, **kwargs)

    def __index__(self, *args, **kwargs):
        return self._execute_meth("__index__", *args, **kwargs)

    def __int__(self, *args, **kwargs):
        return self._execute_meth("__int__", *args, **kwargs)

    def __invert__(self, *args, **kwargs):
        return self._execute_meth("__invert__", *args, **kwargs)

    def __ior__(self, *args, **kwargs):
        return self._execute_meth("__ior__", *args, **kwargs)

    def __ipow__(self, *args, **kwargs):
        return self._execute_meth("__ipow__", *args, **kwargs)

    def __irshift__(self, *args, **kwargs):
        return self._execute_meth("__irshift__", *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        return self._execute_meth("__isub__", *args, **kwargs)

    def __itruediv__(self, *args, **kwargs):
        return self._execute_meth("__itruediv__", *args, **kwargs)

    def __ixor__(self, *args, **kwargs):
        return self._execute_meth("__ixor__", *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return self._execute_meth("__le__", *args, **kwargs)

    def __len__(self, *args, **kwargs):
        return self._execute_meth("__len__", *args, **kwargs)

    def __lshift__(self, *args, **kwargs):
        return self._execute_meth("__lshift__", *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return self._execute_meth("__lt__", *args, **kwargs)

    def __matmul__(self, *args, **kwargs):
        return self._execute_meth("__matmul__", *args, **kwargs)

    def __missing__(self, *args, **kwargs):
        return self._execute_meth("__missing__", *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return self._execute_meth("__mod__", *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return self._execute_meth("__mul__", *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return self._execute_meth("__ne__", *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        return self._execute_meth("__neg__", *args, **kwargs)

    def __or__(self, *args, **kwargs):
        return self._execute_meth("__or__", *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        return self._execute_meth("__pos__", *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        return self._execute_meth("__pow__", *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        return self._execute_meth("__radd__", *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return self._execute_meth("__rand__", *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        return self._execute_meth("__rdivmod__", *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return self.__str__()

    def __reversed__(self, *args, **kwargs):
        return self._execute_meth("__reversed__", *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        return self._execute_meth("__rfloordiv__", *args, **kwargs)

    def __rlshift__(self, *args, **kwargs):
        return self._execute_meth("__rlshift__", *args, **kwargs)

    def __rmatmul__(self, *args, **kwargs):
        return self._execute_meth("__rmatmul__", *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return self._execute_meth("__rmod__", *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return self._execute_meth("__rmul__", *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return self._execute_meth("__ror__", *args, **kwargs)

    def __round__(self, *args, **kwargs):
        return self._execute_meth("__round__", *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        return self._execute_meth("__rpow__", *args, **kwargs)

    def __rrshift__(self, *args, **kwargs):
        return self._execute_meth("__rrshift__", *args, **kwargs)

    def __rshift__(self, *args, **kwargs):
        return self._execute_meth("__rshift__", *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return self._execute_meth("__rsub__", *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        return self._execute_meth("__rtruediv__", *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return self._execute_meth("__rxor__", *args, **kwargs)

        return self._execute_meth("__set_name__", *args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        return self._execute_meth("__setattr__", *args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        return self._execute_meth("__setitem__", *args, **kwargs)

    def __str__(self, *args, **kwargs):
        if self._result is not NOT_ALVAILABLE:
            return str(self._result)
        return "N/A"

    def __sub__(self, *args, **kwargs):
        return self._execute_meth("__sub__", *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        return self._execute_meth("__truediv__", *args, **kwargs)

    def __trunc__(self, *args, **kwargs):
        return self._execute_meth("__trunc__", *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return self._execute_meth("__xor__", *args, **kwargs)

    def run(self):
        try:
            self._result = self.fu(*self.args, **self.kwargs)
        except Exception as e:
            self._result = e


def killthread(threadobject):
    r"""
    # based on https://pypi.org/project/kthread/

    Terminate a thread forcefully.

    Args:
        threadobject (threading.Thread): The thread object to terminate.

    Returns:
        bool: True if the thread was terminated, False otherwise.

    Examples:
        test = ThreadedProxyObject(funct, args=(1, 200))
        test.start()
        killthread(test)
    """
    if not threadobject.is_alive():
        return True
    tid = -1
    for tid1, tobj in threading._active.items():
        if tobj is threadobject:
            tid = tid1
            break
    if tid == -1:
        # sys.stderr.write(f"{threadobject} not found")
        return False
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(tid), ctypes.py_object(SystemExit)
    )
    if res == 0:
        return False
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        return False
    return True


class ThreadedProxyObjectMultiExecute:
    r"""
    A proxy object to run a function in multiple executions in separate threads.

    Args:
        fu (callable): The function to be executed.
        daemon (bool): Whether to run threads as daemon threads.
        args (tuple): Positional arguments to be passed to the function.
        kwargs (dict, optional): Keyword arguments to be passed to the function.

    Examples:
        def funct(x, y):
            return random.randint(x, y)

        test3 = ThreadedProxyObjectMultiExecute(fu=funct, args=(1, 200))
        test3()
        print(dir(test3))
    """

    def __init__(self, fu=None, daemon=True, args=(), kwargs=None):
        self.fu = fu
        self.args = args
        if not kwargs:
            kwargs = {}
        self.kwargs = kwargs
        self._result = NOT_ALVAILABLE
        self._timer_started = False
        self._timer_call_thread = None
        self.daemon = daemon
        self._time_interval = None

    def _timer_call(self, *args, **kwargs):
        while self._timer_started:
            self.__call__(*args, **kwargs)
            time.sleep(self._time_interval)
        return self

    def start_timer_call(self, time_interval, *args, **kwargs):
        r"""
        Start executing the function periodically.

        Args:
            time_interval (int): Time interval in seconds between function executions.

        Examples:
            test6 = ThreadedProxyObjectMultiExecute(fu=funct, daemon=False, args=(1, 200))
            test6.start_timer_call(3)
        """
        if not self._timer_started:
            self._timer_started = True

            self._time_interval = time_interval
            self._timer_call_thread = threading.Thread(
                target=self._timer_call, args=args, kwargs=kwargs, daemon=self.daemon
            )
            self._timer_call_thread.start()
        return self

    def stop_timer_call(self):
        self._timer_started = False
        return self

    def kill(self):
        self.stop_timer_call()
        try:
            killthread(self._timer_call_thread)
        except Exception:
            pass
        try:
            killthread(self._result)
        except Exception:
            pass
        return self

    def __call__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {}
        newargs = self.args + args
        newkwargs = self.kwargs | kwargs
        if self._result is NOT_ALVAILABLE:
            self._result = ThreadedProxyObject(
                fu=self.fu, args=newargs, kwargs=newkwargs, daemon=self.daemon
            )
        try:
            if self._result.is_alive():
                return self
        except AttributeError:
            pass
        try:
            self._result.start()
        except RuntimeError:
            self._result = ThreadedProxyObject(
                fu=self.fu, args=newargs, kwargs=newkwargs, daemon=self.daemon
            )
            self._result.start()
        return self

    def __abs__(self, *args, **kwargs):
        return self._result._execute_meth("__abs__", *args, **kwargs)

    def __add__(self, *args, **kwargs):
        return self._result._execute_meth("__add__", *args, **kwargs)

    def __and__(self, *args, **kwargs):
        return self._result._execute_meth("__and__", *args, **kwargs)

    def __bool__(self, *args, **kwargs):
        return self._result._execute_meth("__bool__", *args, **kwargs)

    def __bytes__(self, *args, **kwargs):
        return self._result._execute_meth("__bytes__", *args, **kwargs)

    def __ceil__(self, *args, **kwargs):
        return self._result._execute_meth("__ceil__", *args, **kwargs)

    def __complex__(self, *args, **kwargs):
        return self._result._execute_meth("__complex__", *args, **kwargs)

    def __contains__(self, *args, **kwargs):
        return self._result._execute_meth("__contains__", *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        return self._result._execute_meth("__delitem__", *args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        return self._result._execute_meth("__divmod__", *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return self._result._execute_meth("__eq__", *args, **kwargs)

    def __float__(self, *args, **kwargs):
        return self._result._execute_meth("__float__", *args, **kwargs)

    def __floor__(self, *args, **kwargs):
        return self._result._execute_meth("__floor__", *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        return self._result._execute_meth("__floordiv__", *args, **kwargs)

    def __format__(self, *args, **kwargs):
        return self._result._execute_meth("__format__", *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return self._result._execute_meth("__ge__", *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        return self._result._execute_meth("__getitem__", *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return self._result._execute_meth("__gt__", *args, **kwargs)

    def __hash__(self, *args, **kwargs):
        return self._result._execute_meth("__hash__", *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        return self._result._execute_meth("__iadd__", *args, **kwargs)

    def __iand__(self, *args, **kwargs):
        return self._result._execute_meth("__iand__", *args, **kwargs)

    def __ifloordiv__(self, *args, **kwargs):
        return self._result._execute_meth("__ifloordiv__", *args, **kwargs)

    def __ilshift__(self, *args, **kwargs):
        return self._result._execute_meth("__ilshift__", *args, **kwargs)

    def __imatmul__(self, *args, **kwargs):
        return self._result._execute_meth("__imatmul__", *args, **kwargs)

    def __imod__(self, *args, **kwargs):
        return self._result._execute_meth("__imod__", *args, **kwargs)

    def __imul__(self, *args, **kwargs):
        return self._result._execute_meth("__imul__", *args, **kwargs)

    def __index__(self, *args, **kwargs):
        return self._result._execute_meth("__index__", *args, **kwargs)

    def __int__(self, *args, **kwargs):
        return self._result._execute_meth("__int__", *args, **kwargs)

    def __invert__(self, *args, **kwargs):
        return self._result._execute_meth("__invert__", *args, **kwargs)

    def __ior__(self, *args, **kwargs):
        return self._result._execute_meth("__ior__", *args, **kwargs)

    def __ipow__(self, *args, **kwargs):
        return self._result._execute_meth("__ipow__", *args, **kwargs)

    def __irshift__(self, *args, **kwargs):
        return self._result._execute_meth("__irshift__", *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        return self._result._execute_meth("__isub__", *args, **kwargs)

    def __itruediv__(self, *args, **kwargs):
        return self._result._execute_meth("__itruediv__", *args, **kwargs)

    def __ixor__(self, *args, **kwargs):
        return self._result._execute_meth("__ixor__", *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return self._result._execute_meth("__le__", *args, **kwargs)

    def __len__(self, *args, **kwargs):
        return self._result._execute_meth("__len__", *args, **kwargs)

    def __lshift__(self, *args, **kwargs):
        return self._result._execute_meth("__lshift__", *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return self._result._execute_meth("__lt__", *args, **kwargs)

    def __matmul__(self, *args, **kwargs):
        return self._result._execute_meth("__matmul__", *args, **kwargs)

    def __missing__(self, *args, **kwargs):
        return self._result._execute_meth("__missing__", *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return self._result._execute_meth("__mod__", *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return self._result._execute_meth("__mul__", *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return self._result._execute_meth("__ne__", *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        return self._result._execute_meth("__neg__", *args, **kwargs)

    def __or__(self, *args, **kwargs):
        return self._result._execute_meth("__or__", *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        return self._result._execute_meth("__pos__", *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        return self._result._execute_meth("__pow__", *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        return self._result._execute_meth("__radd__", *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return self._result._execute_meth("__rand__", *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        return self._result._execute_meth("__rdivmod__", *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return self.__str__()

    def __reversed__(self, *args, **kwargs):
        return self._result._execute_meth("__reversed__", *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        return self._result._execute_meth("__rfloordiv__", *args, **kwargs)

    def __rlshift__(self, *args, **kwargs):
        return self._result._execute_meth("__rlshift__", *args, **kwargs)

    def __rmatmul__(self, *args, **kwargs):
        return self._result._execute_meth("__rmatmul__", *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return self._result._execute_meth("__rmod__", *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return self._result._execute_meth("__rmul__", *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return self._result._execute_meth("__ror__", *args, **kwargs)

    def __round__(self, *args, **kwargs):
        return self._result._execute_meth("__round__", *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        return self._result._execute_meth("__rpow__", *args, **kwargs)

    def __rrshift__(self, *args, **kwargs):
        return self._result._execute_meth("__rrshift__", *args, **kwargs)

    def __rshift__(self, *args, **kwargs):
        return self._result._execute_meth("__rshift__", *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return self._result._execute_meth("__rsub__", *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        return self._result._execute_meth("__rtruediv__", *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return self._result._execute_meth("__rxor__", *args, **kwargs)

        return self._result._execute_meth("__set_name__", *args, **kwargs)

    def __str__(self, *args, **kwargs):
        if self._result is not NOT_ALVAILABLE:
            return str(self._result)
        return "N/A"

    def __sub__(self, *args, **kwargs):
        return self._result._execute_meth("__sub__", *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        return self._result._execute_meth("__truediv__", *args, **kwargs)

    def __trunc__(self, *args, **kwargs):
        return self._result._execute_meth("__trunc__", *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return self._result._execute_meth("__xor__", *args, **kwargs)
