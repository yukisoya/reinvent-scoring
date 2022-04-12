import numpy as np
import numpy.testing as npt

from unittest_reinvent.fixtures.test_data import CELECOXIB, METAMIZOLE, AMOXAPINE, METHOXYHYDRAZINE, COCAINE
from unittest_reinvent.scoring_tests.physchem.base_setup import BaseSetup


class TestNumRotBondsScoreNoTransformation(BaseSetup):

    def setUp(self):
        super().setup_attrs()
        super().init(self.sf_enum.NUM_ROTATABLE_BONDS, {})
        super().setUp()

    def test_num_rot_1(self):
        smiles = [CELECOXIB, METAMIZOLE, AMOXAPINE, METHOXYHYDRAZINE, COCAINE]
        values = np.array([3., 4., 0., 1., 3.])
        score = self.sf_state.get_final_score(smiles=smiles)
        npt.assert_array_equal(score.total_score, values)
