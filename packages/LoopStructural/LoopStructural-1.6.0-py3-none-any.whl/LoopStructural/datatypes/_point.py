from dataclasses import dataclass
import numpy as np

from typing import Optional


@dataclass
class ValuePoints:
    locations: np.ndarray
    values: np.ndarray
    name: str
    properties: Optional[dict] = None

    def to_dict(self):
        return {
            "locations": self.locations,
            "values": self.values,
            "name": self.name,
        }

    def vtk(self):
        import pyvista as pv

        points = pv.PolyData(self.locations)
        points["values"] = self.values
        return points

    def save(self, filename):
        filename = str(filename)
        ext = filename.split('.')[-1]
        if ext == 'json':
            import json

            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f)
        elif ext == 'vtk':
            self.vtk().save(filename)

        elif ext == 'geoh5':
            from LoopStructural.export.geoh5 import add_points_to_geoh5

            add_points_to_geoh5(filename, self)
        elif ext == 'pkl':
            import pickle

            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        elif ext == 'vs':
            from LoopStructural.export.gocad import _write_pointset

            _write_pointset(self, filename)
        else:
            raise ValueError(f'Unknown file extension {ext}')


@dataclass
class VectorPoints:
    locations: np.ndarray
    vectors: np.ndarray
    name: str
    properties: Optional[dict] = None

    def to_dict(self):
        return {
            "locations": self.locations,
            "vectors": self.vectors,
            "name": self.name,
        }

    def vtk(self, geom='arrow', scale=1.0, scale_function=None, tolerance=0.05):
        import pyvista as pv

        vectors = np.copy(self.vectors)
        if scale_function is not None:
            vectors /= np.linalg.norm(vectors, axis=1)[:, None]
            vectors *= scale_function(self.locations)[:, None]
        points = pv.PolyData(self.locations)
        points.point_data.set_vectors(vectors, 'vectors')
        if geom == 'arrow':
            geom = pv.Arrow(scale=scale)
        elif geom == 'disc':
            geom = pv.Disc(inner=0, outer=scale)

        # Perform the glyph
        return points.glyph(orient="vectors", geom=geom, tolerance=tolerance)

    def save(self, filename):
        filename = str(filename)
        ext = filename.split('.')[-1]
        if ext == 'json':
            import json

            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f)
        elif ext == 'vtk':
            self.vtk().save(filename)

        elif ext == 'geoh5':
            from LoopStructural.export.geoh5 import add_points_to_geoh5

            add_points_to_geoh5(filename, self)
        elif ext == 'pkl':
            import pickle

            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        elif ext == 'vs':
            from LoopStructural.export.gocad import _write_pointset

            _write_pointset(self, filename)
        else:
            raise ValueError(f'Unknown file extension {ext}')
