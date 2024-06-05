# Readthedocs default blue theme
html_style = None

# Mock modules that are not present on readthedocs
# http://read-the-docs.readthedocs.org/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
import sys
class Mock(object):
    def __init__(self, *args, **kwargs):
        self._mock = True   # if this exists the object is a mock
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = type(name, (), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()


MOCK_MODULES = [
                 #'numpy', 'numpy.random',
                 #'scipy', 'scipy.stats', 'scipy.optimize', 'scipy.special',
                 #'scipy.ndimage', 'scipy.interpolate',
                 #'builtins',
                 #'matplotlib', 'matplotlib.pyplot', 'matplotlib.mlab',
                 #'matplotlib.patches', 'matplotlib.collections',
                 #'mpl_toolkits.axes_grid1', 'seaborn', 'lmfit',
                 #'PySide','PySide.QtCore','PySide.QtGui',
                 #'tables', 'pandas',
                 #'phconvert', 'phconvert.hdf5', 'phconvert.loader',
                 ]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()
