# -*- coding: UTF-8 -*-
# Copyright (c) 2018, Dirk Gütlin & Thomas Hartmann
# All rights reserved.
#
# This file is part of the pymatreader Project, see: https://gitlab.com/obob/pymatreader
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The following code is taken from the mne-python project in order to test
# loading eeglab files.

import numpy as np

class Bunch(dict):
    """Dictionnary-like object thatexposes its keys as attributes."""

    def __init__(self, **kwargs):  # noqa: D102
        dict.__init__(self, kwargs)
        self.__dict__ = self

def _dol_to_lod(dol):
    """Convert a dict of lists to a list of dicts."""
    return [dict((key, dol[key][ii]) for key in dol.keys())
            for ii in range(len(dol[list(dol.keys())[0]]))]

def _bunchify(items):
    if isinstance(items, dict):
        items = _dol_to_lod(items)
    if len(items) > 0 and isinstance(items[0], dict):
        items = [Bunch(**item) for item in items]
    return items

def prepare_events_like_mne(eeg):
    eeg = Bunch(**eeg['EEG'])

    if not hasattr(eeg, 'event'):
        events = []
    elif isinstance(eeg.event, dict) and \
            np.array(eeg.event['latency']).ndim > 0:
        events = _dol_to_lod(eeg.event)
    elif not isinstance(eeg.event, np.ndarray):
        events = [eeg.event]
    else:
        events = eeg.event
    events = _bunchify(events)

    return events