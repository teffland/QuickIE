""" Defines the constants for the class of mention (corresponds to question type)
and whether or not the question needs to be explained/grounded to the text. """

class CLASSES(object):
    _EXISTENTIAL = 'EXISTENTIAL'
    _CATEGORICAL = 'CATEGORICAL'

    class __metaclass__(type):
        @property
        def EXT(cls):
            return cls._EXISTENTIAL
        @property
        def EXISTENTIAL(cls):
            return cls._EXISTENTIAL

        @property
        def CAT(cls):
            return cls._CATEGORICAL
        @property
        def CATEGORICAL(cls):
            return cls._CATEGORICAL

class EXPLANATION_TYPES(object):
    _MANDATORY = 'MANDATORY'
    _NEVER = 'NEVER'
    _OPTIONAL = 'OPTIONAL'

    class __metaclass__(type):
        def Y(cls):
            return cls._MANDATORY
        @property
        def YES(cls):
            return cls._MANDATORY
        @property
        def M(cls):
            return cls._MANDATORY
        @property
        def MANDATORY(cls):
            return cls._MANDATORY

        @property
        def N(cls):
            return cls._NEVER
        @property
        def NO(cls):
            return cls._NEVER
        @property
        def NEV(cls):
            return cls._NEVER
        @property
        def NEVER(cls):
            return cls._NEVER

        @property
        def O(cls):
            return cls._OPTIONAL
        @property
        def OPT(cls):
            return cls._OPTIONAL
        @property
        def OPTIONAL(cls):
            return cls._OPTIONAL
