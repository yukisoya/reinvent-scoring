import unittest

from reinvent_scoring import TransformationTypeEnum, ComponentSpecificParametersEnum, TransformationFactory


class TestScoreInvalidTransformation(unittest.TestCase):

    def setUp(self):
        self.tt_enum = TransformationTypeEnum()
        self.csp_enum = ComponentSpecificParametersEnum()
        self.specific_parameters = {self.csp_enum.TRANSFORMATION: True,
                                    self.csp_enum.TRANSFORMATION_TYPE: "NOT_IMPLEMENTED_TRANSFORMATION"}
        self.factory = TransformationFactory()

    def test_invalid_transformation(self):
        try:
            self.factory.get_transformation_function(self.specific_parameters)
        except Exception as e:
            self.assertEqual(type(e).__name__, "KeyError")
        else:
            self.fail("""Expected exception of type "KeyError" because of invalid transformation selection.""")
