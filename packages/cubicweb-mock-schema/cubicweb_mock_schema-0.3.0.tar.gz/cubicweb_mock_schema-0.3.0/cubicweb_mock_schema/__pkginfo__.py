# copyright 2024 Logilab, all rights reserved.
# contact https://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of a CubicWeb-mock-schema.
#
# CubicWeb is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# CubicWeb is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with CubicWeb.  If not, see <https://www.gnu.org/licenses/>.

modname = distname = "cubicweb-mock-schema"

numversion = (0, 3, 0)
version = ".".join(str(num) for num in numversion)

description = "a repository of schemas for testing"
author = "Logilab"
author_email = "contact@logilab.fr"
web = "https://forge.extranet.logilab.fr/cubicweb/cubicweb-mock-schema/"
license = "LGPL"

# data files that shall be copied into the main package directory
package_data = {}

__depends__ = {
    "yams": ">= 1.0.0",
    "pytz": ">= 2023.3",
}

classifiers = [
    "Framework :: CubicWeb",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
]
