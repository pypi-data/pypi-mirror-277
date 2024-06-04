#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Author:  Bryce Harrington <bryce@canonical.com>
#
# Copyright (C) 2022 Bryce W. Harrington
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.

"""Trigger class tests."""

import os
import sys

import json
import pytest

sys.path.insert(0, os.path.realpath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")))

from ppa.trigger import Trigger, get_triggers, show_triggers


def test_object():
    """Checks that Trigger objects can be instantiated."""
    trigger = Trigger('a', 'b', 'c', 'd', 'e')
    assert trigger


@pytest.mark.parametrize('pkg, ver, arch, series, ppa, testpkg, expected_repr', [
    ('a', 'b', 'c', 'd', 'e', 'f',
     "Trigger(package='a', version='b', arch='c', series='d', ppa='e', test_package='f')"),
    ('a', 'b', 'c', 'd', 'e', None,
     "Trigger(package='a', version='b', arch='c', series='d', ppa='e', test_package='a')"),
])
def test_repr(pkg, ver, arch, series, ppa, testpkg, expected_repr):
    """Checks Trigger object representation."""
    trigger = Trigger(pkg, ver, arch, series, ppa, testpkg)
    assert repr(trigger) == expected_repr


def test_str():
    """Checks Trigger object textual presentation."""
    trigger = Trigger('a', 'b', 'c', 'd', 'e')
    assert f"{trigger}" == 'a/b'

    trigger = Trigger('dovecot', '1:2.3.19.1+dfsg1-2ubuntu2', 'i386', 'kinetic', None)
    assert f"{trigger}" == 'dovecot/1:2.3.19.1+dfsg1-2ubuntu2'


def test_to_dict():
    """Checks Trigger object structural representation."""
    trigger = Trigger('a', 'b', 'c', 'd', 'e')
    expected_keys = [
        'package', 'version', 'test_package', 'arch', 'series', 'ppa'
    ]
    expected_types = [str]

    d = trigger.to_dict()
    assert isinstance(d, dict), f"type of d is {type(d)} not dict"

    # Verify expected keys are present
    assert sorted(d.keys()) == sorted(expected_keys)

    # Verify values are within set of expected types
    for k, v in d.items():
        assert type(v) in expected_types, f"'{k}={v}' is unexpected type {type(v)}"

    # Verify full dict can be written as JSON
    try:
        assert json.dumps(d)
    except UnicodeDecodeError as e:
        assert False, f"Wrong UTF codec detected: {e}"
    except json.JSONDecodeError as e:
        assert False, f"JSON decoding error: {e.msg}, {e.doc}, {e.pos}"


@pytest.mark.parametrize('trigger, expected', [
    (
        Trigger('a', 'b', 'c', 'd', 'e'),
        "/packages/a/a/d/c"
    ), (
        Trigger('apache2', '2.4', 'amd64', 'kinetic', None),
        "/packages/a/apache2/kinetic/amd64"
    ), (
        Trigger('libwebsockets', '4.1.6-3', 'armhf', 'jammy', None),
        "/packages/libw/libwebsockets/jammy/armhf"
    )
])
def test_history_url(trigger, expected):
    """Checks that Trigger objects generate valid autopkgtest history urls."""
    assert expected in trigger.history_url


@pytest.mark.parametrize('trigger, expected', [
    (
        Trigger('a', 'b', 'c', 'd', 'e'),
        "/request.cgi?release=d&package=a&arch=c&trigger=a%2Fb&ppa=e"
    ), (
        Trigger('a', '1.2+git345', 'c', 'd', None),
        "/request.cgi?release=d&package=a&arch=c&trigger=a%2F1.2%2Bgit345"
    ), (
        Trigger('apache2', '2.4', 'amd64', 'kinetic', None),
        "/request.cgi?release=kinetic&package=apache2&arch=amd64&trigger=apache2%2F2.4"
    ), (
        Trigger('nut', '2.7.4-1', 'armhf', 'jammy', None),
        "/request.cgi?release=jammy&package=nut&arch=armhf&trigger=nut%2F2.7.4-1"
    ), (
        Trigger('apache2', '2.4', 'amd64', 'kinetic', 'ppa:aaa/bbb'),
        "/request.cgi?release=kinetic&package=apache2&arch=amd64&trigger=apache2%2F2.4&ppa=ppa%3Aaaa%2Fbbb"
    ), (
        Trigger('apache2', '2.4', 'amd64', 'kinetic', 'ppa:aaa/bbb', 'cinder'),
        "/request.cgi?release=kinetic&package=cinder&arch=amd64&trigger=apache2%2F2.4&ppa=ppa%3Aaaa%2Fbbb"
    )
])
def test_action_url(trigger, expected):
    """Checks that Trigger objects generate valid autopkgtest action urls."""
    assert expected in trigger.action_url


@pytest.mark.parametrize('params, expected', [
    (
        ['a', 'b', 'c', 'd', ['x', 'y', 'z'], ['1', '2', '3']],
        [
            Trigger('a', 'b', 'x', 'd', 'c', ['1', '2', '3']),
            Trigger('a', 'b', 'y', 'd', 'c', ['1', '2', '3']),
            Trigger('a', 'b', 'z', 'd', 'c', ['1', '2', '3']),
        ],
    ),
])
def test_get_triggers(params, expected):
    """Checks that Trigger objects get generated properly from inputs."""
    for trigger in get_triggers(*params):
        assert repr(trigger) in [repr(t) for t in expected]


@pytest.mark.parametrize('triggers, params, expected_in_stdout', [
    (
        # Basic function parameters, no triggers
        [],
        {'package': 'pkg', 'version': '123', 'status': 'OK'},
        ["  - Source \x1b]8;;https://launchpad.net/ubuntu/+source/pkg/123\x1b\\pkg/123\x1b]8;;\x1b\\: OK\n"]
    ),
    (
        # Specified trigger (clickable)
        [('pkg', '123', 'i386')],
        {'show_trigger_urls': False},
        [
            "&trigger=pkg%2F123&ppa=z\x1b\\Trigger basic @i386♻️ \x1b]8;;\x1b",
            "&trigger=pkg%2F123&ppa=z&all-proposed=1\x1b\\Trigger all-proposed @i386💍\x1b]8;;\x1b\\\n"
        ]
    ),
    (
        # Specified trigger (display plain URLs)
        [('pkg', '123', 'i386')],
        {'show_trigger_urls': True},
        [
            "&trigger=pkg%2F123&ppa=z♻️ \n",
            "&trigger=pkg%2F123&ppa=z&all-proposed=1💍\n"
        ]
    ),
    (
        # Display names of packages in trigger lines
        [('pkg', '123', 'i386')],
        {'show_trigger_names': True},
        ["Trigger basic x@i386♻️ ", "Trigger all-proposed x@i386💍"]
    ),
    (
        # Omit package names if specified
        [('pkg', '123', 'i386')],
        {'show_trigger_names': False},
        ["Trigger basic @i386", "Trigger all-proposed @i386"]
    ),
    (
        # Display names of packages in trigger lines when trigger URLs are shown
        [('pkg', '123', 'i386')],
        {'show_trigger_urls': True, 'show_trigger_names': True},
        ["x@i386: https:", "trigger=pkg%2F123"]
    ),
    (
        # Multiple triggers
        [('pkg', '123', 'i386'), ('lib', '321', 'i386')],
        {'show_trigger_urls': True},
        ["trigger=pkg%2F123", "trigger=lib%2F321"]
    ),
])
def test_show_triggers(capfd, triggers, params, expected_in_stdout):
    params.setdefault('package', 'x')
    params.setdefault('version', '1.x')
    params.setdefault('triggers', [])
    params.setdefault('status', 'x')
    for t in triggers:
        params['triggers'].append(Trigger(t[0], t[1], t[2], 'y', 'z', 'x'))
    show_triggers(**params)
    out, err = capfd.readouterr()
    print(out)
    for text in expected_in_stdout:
        assert text in out
