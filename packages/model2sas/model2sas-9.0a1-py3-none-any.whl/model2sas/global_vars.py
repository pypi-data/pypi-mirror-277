import torch

PRECISION: torch.dtype = torch.float32

DEFAULT_DEVICE = 'cpu'

PRINT_LOG: bool = False

LOG_LEVEL: int = -1

LOG_FORMAT_STR: str = '<cyan>{time:YYYY-MM-DD HH:mm:ss.SSS}</cyan> | <level>{level: <8}</level> | <level>{message}</level>'

WELCOME_MESSAGE = r'''
 __  __             _        _  ____   ____      _     ____
|  \/  |  ___    __| |  ___ | ||___ \ / ___|    / \   / ___|
| |\/| | / _ \  / _` | / _ \| |  __) |\___ \   / _ \  \___ \
| |  | || (_) || (_| ||  __/| | / __/  ___) | / ___ \  ___) |
|_|  |_| \___/  \__,_| \___||_||_____||____/ /_/   \_\|____/

===== Small-angle scattering simulation from 3d models =====

🏠️ Website: https://github.com/molybd/Model2SAS
📄 Please cite: Li, Mu and Yin, Panchao, Model2SAS: software for small-angle scattering data calculation from custom shapes., J. Appl. Cryst., 2022, 55, 663-668. https://doi.org/10.1107/S1600576722003600
'''
