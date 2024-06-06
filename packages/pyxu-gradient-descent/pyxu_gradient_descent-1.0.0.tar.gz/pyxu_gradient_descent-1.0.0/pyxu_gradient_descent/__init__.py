import importlib.metadata

try:
    __version__ = importlib.metadata.version("pyxu_gradient_descent")
except ImportError:
    __version__ = "unknown"

from .opt import GradientDescent

__all__ = ("GradientDescent",)
