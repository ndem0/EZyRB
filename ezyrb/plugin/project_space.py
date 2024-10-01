

from ..snapshot import Snapshot
from .plugin import Plugin

import copy
import matplotlib.pyplot as plt

class ProjectToSpace(Plugin):

    def __init__(self, approximator, reference_space) -> None:
        super().__init__()
        self.approximator = approximator
        self.reference_space = reference_space

    def fit_preprocessing(self, rom):
        db = rom.database

        # print(db.snapshots_matrix)
        for i, snap in enumerate(db.snapshots):
            approx = copy.deepcopy(self.approximator)
            # snap.plot()
            # plt.show()
            approx.fit(snap.space, snap.values)

            # print(snap.space)

            new_snap = Snapshot(
                values=approx.predict(self.reference_space),
                space=self.reference_space
            )

            # plt.plot(snap.space[:, 0], snap.values[:, 0], 'o')
            # plt.plot(self.reference_space[:, 0], new_snap.values)
            # plt.show()
            # print(new_snap.values)
            # print(new_snap.values.shape)
            # plt.plot(new_snap.values)
            # plt.show()
            # new_snap.plot()
            # plt.show()
            db._pairs[i] = (db._pairs[i][0], new_snap)
        # print(db.snapshots_matrix)


        rom.database = db