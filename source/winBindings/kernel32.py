# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2025 NV Access Limited
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""Functions exported by kernel32.dll, and supporting data structures and enumerations."""

from ctypes import (
	c_wchar_p,
	windll,
)
from ctypes.wintypes import (
	DWORD,
	HANDLE,
	HMODULE,
)

__all__ = (
	"GetModuleHandle",
	"GetModuleFileName",
)


dll = windll.kernel32

GetModuleHandle = dll.GetModuleHandleW
"""
Retrieves a module handle for the specified module, which must have been loaded by the calling process.

.. seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlew
"""
GetModuleHandle.argtypes = (c_wchar_p,)
GetModuleHandle.restype = HMODULE

GetModuleFileName = dll.GetModuleFileNameW
"""
Retrieves the fully qualified path for the file that contains the specified module, which must have been loaded by the current process.

..seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamew
"""
GetModuleFileName.argtypes = (HANDLE, c_wchar_p, DWORD)
GetModuleFileName.restype = DWORD
