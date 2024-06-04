import sys
import os

# This compatibility module redefines standard import mechanisms in Python. 
# It optimizes the handling of certain boolean variables by 'freezing' them, 
# ensuring they are evaluated only when needed. This optimization minimizes 
# unnecessary function calls for accessing individual variables. Once frozen, 
# a variable retains its computed value globally, eliminating the need for 
# repeated evaluation. It works similarly to Just-In-Time (JIT) compiling.

# For more advanced users, a function is provided to unfreeze all variables 
# that are actively frozen. This can be achieved by calling 'unfreeze'.

# This cache variable helps prevent repeated isinstance checks on
# values that have already been unfrozen.
_cache = {}

class FrozenContext:
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback
    
    def __call__(self):
        value = self.callback()
        _cache[self.name] = value
        globals()[self.name] = value
        return value

class FrozenModule:
    def __getattribute__(self, name):
        try:
            instance = globals()[name]
        except KeyError:
            raise ImportError(f"cannot import name '{name}' from 'mycompat' ({os.path.abspath(__file__)})")
        
        if name in _cache:
            return _cache[name]

        if isinstance(instance, FrozenContext):
            return instance()
        
        return instance

class Freezer:
    @staticmethod
    def register(name, callback):
        globals()[name] = FrozenContext(name, callback)

    @staticmethod
    def unfreeze():
        """
        Unfreezes all variables that are currently frozen.

        This function iterates over all global variables that are instances of `FrozenContext`
        and forces their evaluation, updating their values in the global namespace.
        """

        for name, instance in globals().items():
            if name in _cache:
                continue

            if name.startswith("__") and name.endswith("__"):
                continue

            if isinstance(instance, FrozenContext):
                instance()

# Override the imported 'mycompat' module for custom '__getattribute__' implementation.
sys.modules["mycompat"] = FrozenModule()

import subprocess
import platform
import re

# Utility Functions
class _Callback:
    @staticmethod
    def is_win_wine():
        try:
            import ctypes.util # noqa: E402
            return is_wine_dll(ctypes.util.find_library('kernel32'))
        except Exception:
            return False
        
# The below compatibility functions were taken from PyInstaller's compat file.
# https://github.com/pyinstaller/pyinstaller/blob/develop/PyInstaller/compat.py

# Wine detection and support
def is_wine_dll(filename):
    """
    Check if the given PE file is a Wine DLL (PE-converted built-in, or fake/placeholder one).

    Returns True if the given file is a Wine DLL, False if not (or if file cannot be analyzed or does not exist).
    """

    _WINE_SIGNATURES = (
        b'Wine builtin DLL',  # PE-converted Wine DLL
        b'Wine placeholder DLL',  # Fake/placeholder Wine DLL
    )
    _MAX_LEN = max([len(sig) for sig in _WINE_SIGNATURES])

    # Wine places their DLL signature in the padding area between the IMAGE_DOS_HEADER and IMAGE_NT_HEADERS. So we need
    # to compare the bytes that come right after IMAGE_DOS_HEADER, i.e., after initial 64 bytes. We can read the file
    # directly and avoid using the pefile library to avoid performance penalty associated with full header parsing.
    try:
        with open(filename, 'rb') as fp:
            fp.seek(64)
            signature = fp.read(_MAX_LEN)
        return signature.startswith(_WINE_SIGNATURES)
    except Exception:
        pass
    return False

def _pyi_machine(machine, system):
    """
    Choose an intentionally simplified architecture identifier to be used in the bootloader's directory name.

    Args:
        machine:
            The output of ``platform.machine()`` or any known architecture alias or shorthand that may be used by a
            C compiler.
        system:
            The output of ``platform.system()`` on the target machine.
    Returns:
        Either a string tag or, on platforms that don't need an architecture tag, ``None``.

    Ideally, we would just use ``platform.machine()`` directly, but that makes cross-compiling the bootloader almost
    impossible, because you need to know at compile time exactly what ``platform.machine()`` will be at run time, based
    only on the machine name alias or shorthand reported by the C compiler at the build time. Rather, use a loose
    differentiation, and trust that anyone mixing armv6l with armv6h knows what they are doing.
    """
    # See the corresponding tests in tests/unit/test_compat.py for examples.

    if platform.machine() == "sw_64" or platform.machine() == "loongarch64":
        # This explicitly inhibits cross compiling the bootloader for or on SunWay and LoongArch machine.
        return platform.machine()

    if system == "Windows":
        if machine.lower().startswith("arm"):
            return "arm"
        else:
            return "intel"

    if system != "Linux":
        # No architecture specifier for anything par Linux.
        # - macOS is on two 64 bit architectures, but they are merged into one "universal2" bootloader.
        # - BSD supports a wide range of architectures, but according to PyPI's download statistics, every one of our
        #   BSD users are on x86_64. This may change in the distant future.
        return

    if machine.startswith(("arm", "aarch")):
        # ARM has a huge number of similar and aliased sub-versions, such as armv5, armv6l armv8h, aarch64.
        return "arm"
    if machine in ("thumb"):
        # Reported by waf/gcc when Thumb instruction set is enabled on 32-bit ARM. The platform.machine() returns "arm"
        # regardless of the instruction set.
        return "arm"
    if machine in ("x86_64", "x64", "x86"):
        return "intel"
    if re.fullmatch("i[1-6]86", machine):
        return "intel"
    if machine.startswith(("ppc", "powerpc")):
        # PowerPC comes in 64 vs 32 bit and little vs big endian variants.
        return "ppc"
    if machine in ("mips64", "mips"):
        return "mips"
    if machine.startswith("riscv"):
        return "riscv"
    # Machines with no known aliases :)
    if machine in ("s390x",):
        return machine

    # Unknown architectures are allowed by default, but will all be placed under one directory. In theory, trying to
    # have multiple unknown architectures in one copy of PyInstaller will not work, but that should be sufficiently
    # unlikely to ever happen.
    return "unknown"

# The below compatibility variables were taken from PyInstaller's compat file.
# https://github.com/pyinstaller/pyinstaller/blob/develop/PyInstaller/compat.py
Freezer.register("is_64bits", lambda: sys.maxsize > 2**32)

Freezer.register("is_py33",  lambda: sys.version_info >= (3, 3))
Freezer.register("is_py34",  lambda: sys.version_info >= (3, 4))
Freezer.register("is_py35",  lambda: sys.version_info >= (3, 5))
Freezer.register("is_py36",  lambda: sys.version_info >= (3, 6))
Freezer.register("is_py37",  lambda: sys.version_info >= (3, 7))
Freezer.register("is_py38",  lambda: sys.version_info >= (3, 8))
Freezer.register("is_py39",  lambda: sys.version_info >= (3, 9))
Freezer.register("is_py310", lambda: sys.version_info >= (3, 10))
Freezer.register("is_py311", lambda: sys.version_info >= (3, 11))
Freezer.register("is_py312", lambda: sys.version_info >= (3, 12))

is_win = sys.platform.startswith('win')
Freezer.register("is_win_10", lambda: is_win and (platform.win32_ver()[0] == '10'))
Freezer.register("is_win_10", lambda: is_win and (platform.win32_ver()[0] == '11'))
Freezer.register("is_win_wine", _Callback.is_win_wine)  # Running under Wine.

is_cygwin = sys.platform == 'cygwin'
is_darwin = sys.platform == 'darwin'  # Mac OS X

# Unix platforms
is_linux = sys.platform.startswith('linux')
is_solar = sys.platform.startswith('sun')  # Solaris
is_aix = sys.platform.startswith('aix')
is_freebsd = sys.platform.startswith('freebsd')
is_openbsd = sys.platform.startswith('openbsd')
is_hpux = sys.platform.startswith('hp-ux')

# Some code parts are similar to several unix platforms (e.g. Linux, Solaris, AIX).
# Mac OS is not considered as unix since there are many platform-specific details for Mac.
is_unix = is_linux or is_solar or is_aix or is_freebsd or is_hpux or is_openbsd

# Linux distributions such as Alpine or OpenWRT use musl as their libc implementation and resultantly need specially
# compiled bootloaders. On musl systems, ldd with no arguments prints 'musl' and its version.
Freezer.register("is_musl", lambda: is_linux and "musl" in subprocess.run(["ldd"], capture_output=True, encoding="utf-8").stderr)

# macOS version
Freezer.register("_macos_ver", lambda: tuple(int(x) for x in platform.mac_ver()[0].split('.')) if is_darwin else None)

# macOS 11 (Big Sur): if python is not compiled with Big Sur support, it ends up in compatibility mode by default, which
# is indicated by platform.mac_ver() returning '10.16'. The lack of proper Big Sur support breaks find_library()
# function from ctypes.util module, as starting with Big Sur, shared libraries are not visible on disk anymore. Support
# for the new library search mechanism was added in python 3.9 when compiled with Big Sur support. In such cases,
# platform.mac_ver() reports version as '11.x'. The behavior can be further modified via SYSTEM_VERSION_COMPAT
# environment variable; which allows explicitly enabling or disabling the compatibility mode. However, note that
# disabling the compatibility mode and using python that does not properly support Big Sur still leaves find_library()
# broken (which is a scenario that we ignore at the moment).
# The same logic applies to macOS 12 (Monterey).
Freezer.register("is_macos_11_compat", lambda: bool(_macos_ver) and _macos_ver[0:2] == (10, 16)) # Big Sur or newer in compat mode
Freezer.register("is_macos_11_native", lambda: bool(_macos_ver) and _macos_ver[0:2] >= (11, 0))  # Big Sur or newer in native mode
Freezer.register("is_macos_11", lambda: is_macos_11_compat or is_macos_11_native)

# In a virtual environment created by virtualenv (github.com/pypa/virtualenv) there exists sys.real_prefix with the path
# to the base Python installation from which the virtual environment was created. This is true regardless of the version
# of Python used to execute the virtualenv command.
#
# In a virtual environment created by the venv module available in the Python standard lib, there exists sys.base_prefix
# with the path to the base implementation. This does not exist in a virtual environment created by virtualenv.
#
# The following code creates compat.is_venv and is.virtualenv that are True when running a virtual environment, and also
# compat.base_prefix with the path to the base Python installation.
Freezer.register("base_prefix", lambda: os.path.abspath(getattr(sys, 'real_prefix', getattr(sys, 'base_prefix', sys.prefix))))

# Ensure `base_prefix` is not containing any relative parts.
Freezer.register("is_venv", lambda: base_prefix != os.path.abspath(sys.prefix))
Freezer.register("is_virtualenv", lambda: is_venv)

# Conda environments sometimes have different paths or apply patches to packages that can affect how a hook or package
# should access resources. Method for determining conda taken from https://stackoverflow.com/questions/47610844#47610844
Freezer.register("is_conda", lambda: os.path.isdir(os.path.join(base_prefix, 'conda-meta')))

# Similar to ``is_conda`` but is ``False`` using another ``venv``-like manager on top.
Freezer.register("is_pure_conda", lambda: os.path.isdir(os.path.join(sys.prefix, 'conda-meta')))

# Full path to python interpreter.
python_executable = getattr(sys, '_base_executable', sys.executable)

# Is this Python from Microsoft App Store (Windows only)? Python from Microsoft App Store has executable pointing at
# empty shims.
Freezer.register("is_ms_app_store", lambda: is_win and os.path.getsize(python_executable) == 0)

# Gets the system machine type.
machine = platform.machine()

# macOS's platform.architecture() can be buggy, so we do this manually here. Based off the python documentation:
# https://docs.python.org/3/library/platform.html#platform.architecture
if is_darwin:
    Freezer.register("architecture", lambda: '64bit' if sys.maxsize > 2**32 else '32bit')
else:
    Freezer.register("architecture", lambda: platform.architecture()[0])

# Machine suffix for bootloader.
if is_win:
    # On Windows ARM64 using an x64 Python environment, platform.machine() returns ARM64 but
    # we really want the bootloader that matches the Python environment instead of the OS.
    Freezer.register("simple_machine", lambda: _pyi_machine(os.environ.get("PROCESSOR_ARCHITECTURE", platform.machine()), platform.system()))
else:
    Freezer.register("simple_machine", lambda: _pyi_machine(platform.machine(), platform.system()))

# Detects if a python script has been packaged into an executable.
Freezer.register("is_frozen", lambda: getattr(sys, "frozen", False))

# Register 'unfreeze' function in the global namespace.
unfreeze = Freezer.unfreeze