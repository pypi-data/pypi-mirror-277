#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Copyright (C) 2022 Authors
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.
#
# Authors:
#   Bryce Harrington <bryce@canonical.com>

"""A directive to run a DEP8 test against a source package."""

from functools import lru_cache
from urllib.parse import urlencode

from .constants import URL_AUTOPKGTEST
from ppa.text import ansi_hyperlink


class Trigger:
    """A source package and version to use when running an autopkgtest.

    A trigger indicates a source package whose autopkgtest(s) to invoke,
    after installing a particular version of that package, and possibly
    other source packages, from a given series.

    A Job can have multiple Triggers, each against a different source
    package and/or architectures, but all such Triggers must be against
    the same series as the Job itself.
    """
    def __init__(self, package, version, arch, series, ppa=None, test_package=None):
        """Initialize a new Trigger for a given package and version.

        :param str package: The source package name.
        :param str version: The version of the source package to install.
        :param str arch: The architecture for the trigger.
        :param str series: The distro release series codename.
        :param Ppa ppa: (Optional) PPA wrapper object to run tests against.
        :param str test_package: The package to run autopkgtests from.
        """
        self.package = package
        self.version = version
        self.arch = arch
        self.series = series
        self.ppa = ppa
        if test_package:
            self.test_package = test_package
        else:
            self.test_package = package

    def __repr__(self) -> str:
        """Return a machine-parsable unique representation of object.

        :rtype: str
        :returns: Official string representation of the object.
        """
        return (f'{self.__class__.__name__}('
                f'package={self.package!r}, version={self.version!r}, '
                f'arch={self.arch!r}, series={self.series!r}, ppa={self.ppa!r}, '
                f'test_package={self.test_package!r})')

    def __str__(self) -> str:
        """Return a human-readable summary of the object.

        :rtype: str
        :returns: Printable summary of the object.
        """
        if self.test_package != self.package:
            return f"({self.test_package}) {self.package}/{self.version}"
        return f"{self.package}/{self.version}"

    @lru_cache
    def to_dict(self) -> dict:
        """Return a basic dict structure of the Trigger's data."""
        return {
            'package': self.package,
            'version': self.version,
            'test_package': self.test_package,
            'arch': self.arch,
            'series': self.series,
            'ppa': self.ppa
        }

    @property
    @lru_cache
    def history_url(self) -> str:
        """Renders the trigger as a URL to the job history.

        :rtype: str
        :returns: Job history URL
        """
        if self.package.startswith('lib'):
            prefix = self.package[0:4]
        else:
            prefix = self.package[0]
        pkg_str = f"{prefix}/{self.package}"
        return f"{URL_AUTOPKGTEST}/packages/{pkg_str}/{self.series}/{self.arch}"

    @property
    @lru_cache
    def action_url(self) -> str:
        """Renders the trigger as a URL to start running the test.

        :rtype: str
        :returns: Trigger action URL
        """
        params = [
            ("release", self.series),
            ("package", self.test_package),
            ("arch", self.arch),
        ]

        # Trigger for the source package itself
        params.append(("trigger", f"{self.package}/{self.version}"))

        # TODO: Additional triggers...

        # The PPA, if one is defined for this trigger
        if self.ppa:
            params.append(("ppa", self.ppa))

        return f"{URL_AUTOPKGTEST}/request.cgi?" + urlencode(params)


def get_triggers(package, version, ppa, series, architectures,
                 sources=None) -> list[Trigger]:
    """Returns Triggers for the given criteria.

    :param str package: The source package name.
    :param str version: The version of the source package to install.
    :param Ppa ppa: Ppa wrapper object to run tests against.
    :param str series: The distro release series codename.
    :param list[str] architectures: The architectures to provide triggers for.
    :param list[str] sources: (Unimplemented)
    :rtype: list[Trigger]
    :returns: List of triggers, if any, or an empty list on error.
    """
    return [
        Trigger(package, version, arch, series, ppa, sources)
        for arch
        in architectures
    ]


def show_triggers(package, version, triggers, status,
                  show_trigger_urls=False,
                  show_trigger_names=False):
    """Prints the triggers for a given package.

    :param str package: The source package's name.
    :param str version: The source package's version.
    :param list[Trigger] triggers:  The triggers to be displayed.
    :param str status: Result of the triggered test run.
    :param bool show_trigger_urls: If true, print out the trigger URLs
        as text; otherwise triggers will be printed as a hyperlink named
        'package/version'.  This is necessary for terminals lacking ANSI
        hyperlink support, for example.
    :param bool show_trigger_names: If true, includes display of the
        package names for triggers.  This may be useful if printing
        complex triggers or triggers for multiple different packages.
    """
    url = f"https://launchpad.net/ubuntu/+source/{package}/{version}"
    source_hyperlink = ansi_hyperlink(url, f"{package}/{version}")
    print(f"  - Source {source_hyperlink}: {status}")
    if show_trigger_urls:
        for trigger in triggers:
            title = ''
            if show_trigger_names:
                title = trigger.test_package
            print(f"    + {title}@{trigger.arch}: {trigger.action_url}♻️ ")
        for trigger in triggers:
            title = ''
            if show_trigger_names:
                title = trigger.test_package
            url = trigger.action_url + "&all-proposed=1"
            print(f"    + {title}@{trigger.arch}: {url}💍")

    else:
        for trigger in triggers:
            pad = ' ' * (1 + abs(len('ppc64el') - len(trigger.arch)))
            title = ''
            if show_trigger_names:
                title = trigger.test_package

            basic_trig = ansi_hyperlink(
                trigger.action_url, f"Trigger basic {title}@{trigger.arch}♻️ "
            )
            all_proposed_trig = ansi_hyperlink(
                trigger.action_url + "&all-proposed=1",
                f"Trigger all-proposed {title}@{trigger.arch}💍"
            )
            print("    + " + pad.join([basic_trig, all_proposed_trig]))


if __name__ == "__main__":
    import json

    print('##############################')
    print('## Trigger class smoke test ##')
    print('##############################')
    print()

    print("Basic trigger")
    print("-------------")
    trigger = Trigger('my-package', '1.2.3', 'amd64', 'kinetic')
    print(trigger)
    print(trigger.history_url)
    print(trigger.action_url)
    print()

    print("Object Dump")
    print("-----------")
    t = Trigger('my-package', '1.2.3', 'amd64', 'kinetic')
    print(json.dumps(t.to_dict(), indent=4))
    print()

    print("* PPA trigger:")
    trigger = Trigger('my-ppa-package', '1.2.3', 'amd64', 'kinetic', 'my-ppa')
    print(trigger)
    print(trigger.history_url)
    print(trigger.action_url)
    print()
