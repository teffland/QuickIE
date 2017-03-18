""" The base class that defines a microtask. """
from constants import CLASSES as C, EXPLANATION_TYPES as E

class Task(object):
    def __init__(self,
                 name,
                 klass=C.EXT,
                 explanation=E.OPT,
                 **kwds):
        self.name = name
        self._klass = klass
        self._explanation = explanation

        # must be lists/dicts of Task instances
        self.parents = kwds.pop('parents', [])
        self.interactions = kwds.pop('interactions', {})
        self.properties = kwds.pop('properties', {})

        if self._klass == EXT:
            self._values = [True, False]
        elif self._klass == CAT:
            self._values = kwds.pop('values', [])
        elif self._klass == NUM:
            raise NotImplementedError, "Numerical tasks not yet implemented"
        else:
            raise ValueError, "Unknown task klass"

    @property
    def klass(self):
        return self._klass

    @klass.setter
    def klass(self, val):
        if val in (C.EXT, C.CAT):
            self._klass = val
        else:
            print "Invalid mention klass setting"

    @property
    def explanation(self):
        return self._explanation

    @explanation.setter
    def explanation(self, val):
        if val in (E.YES, E.NO, E.OPT):
            self._explanation = val
        else:
            print "Invalid mention explanation setting"

    @property
    def values(self):
        return self._values

    def __repr__(self):
        s = 'MicroTask: {}'.format(self.name)
        s += '\n Explanation: {}'.format(self.explanation)
        s += '\n Prereqs:'
        if self.parents:
            for parent in self.parents:
                s += '\n  '
                if type(parent) is list:
                    s += '[{}]'.format(", ".join([str(p) for p in parent]))
                else:
                    s += str(parent)
        else:
            s += ' None'
        s += '\n Interactions:'
        if self.interactions:
            for rel, objs in self.interactions.items():
                s += '\n  {}: {}'.format(str(rel), ", ".join([str(obj) for obj in objs]))
        else:
            s += ' None'
        s += '\n Properties:'
        if self.properties:
            for prop, task in self.properties.items():
                s += '\n  {}: {}'.format(str(prop), " | ".join([str(v) for v in task.values]))
        else:
            s += ' None'
        return s

    def __str__(self):
        return self.name
