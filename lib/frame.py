from collections import deque


class Object(object):
    def __init__(self, klass):
        self.klass = klass

    def __repr__(self):
        return f'Object({self.klass.name()})'

    def __str__(self):
        return f'Object of class {self.klass.name()}'


class Frame(object):
    def __init__(self, klass, method, objectref, parameter_types, parameters):
        self.operand_stack = deque()
        self.klass = klass
        self.method = method
        self.next_ops_address = 0
        self.code = method.code()
        if not self.code:
            raise RuntimeError('Could not find code in method')
        self.local_variables = [None for _ in range(self.code.max_locals)]
        offset = 0
        if objectref:
            self.local_variables[0] = objectref
            offset = 1
        for i in range(len(parameter_types)):
            self.local_variables[i + offset] = parameters[i]
            if parameter_types[i] in ('D', 'J'):
                # Double or Long
                offset += 1

    def operand_debug_str(self):
        operand_stack_str = \
            f'[{", ".join(str(v) for v in self.operand_stack)}]'
        return f'operand stack: {operand_stack_str}'

    def local_variable_debug_str(self):
        local_variable_str = \
            f'[{", ".join(str(v) for v in self.local_variables)}]'
        return f'local variables: {local_variable_str}'
