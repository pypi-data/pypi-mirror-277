"""Set logging, locale and package_dir"""

from pathlib import Path
import locale
from .__version__ import __version__

__all__ = ['__version__', 'package_dir']

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

package_dir = Path(__file__).parent
