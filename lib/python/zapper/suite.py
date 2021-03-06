#!/usr/bin/env python3
#
# Copyright 2013 Simone Campagna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__ = 'Simone Campagna'

from .package import Package
from .product import Product
from .product_suite import ProductSuite
from .utils.table import show_table, show_title


import abc

__all__ = ['Suite', 'ROOT']

class Suite(Package):
    def __init__(self, product, version, *, short_description=None, long_description=None, suite=None):
        if isinstance(product, str):
            product = ProductSuite(product)
        assert isinstance(product, Product)
        self._packages = []
        super().__init__(product, version, short_description=short_description, long_description=long_description, suite=suite)

    def packages(self):
        return iter(self._packages)

    def add_package(self, package):
        assert isinstance(package, Package)
        if package is not self:
            self._packages.append(package)
            self.add_package_requirement(package)

    def add_package_requirement(self, package):
        package.requires(self)

    def show_content(self):
        super().show_content()
        show_table("Packages", self.packages())

    def package_type(self):
        return "suite"

class _RootSuite(Suite):
    def __init__(self):
        product = ProductSuite('')
        version = ''
        short_description = 'The Root suite'
        long_description = 'The Root suite contains all available suites/packages'
        super().__init__(product, version, short_description=short_description, long_description=long_description, suite=self)

    def add_package_requirement(self, package):
        pass

ROOT = _RootSuite()

