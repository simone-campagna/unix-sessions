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

from .config import Config
from .common_config import COMMON_CONFIG, VERSION_DEFAULTS

SESSION_CONFIG = COMMON_CONFIG.copy()
SESSION_CONFIG['description'] = ''
SESSION_CONFIG['read_only'] = 'False'

class SessionConfig(Config):
    __defaults__ = {
        'session': {
            'name': '',
            'type': '',
            'creation_time': '',
        },
        'packages': {
            'loaded_packages': '',
            'sticky_packages': '',
        },
        'config': SESSION_CONFIG,
        'version_defaults': VERSION_DEFAULTS,
    }
