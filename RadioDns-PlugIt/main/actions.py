# -*- coding: utf-8 -*-

# Utils
from plugit.utils import action, only_orga_member_user, json_only, cache, PlugItRedirect

from models import Ecc, CountryCode


# Include homepage
@action(route="/", template="main/home.html")
@only_orga_member_user()
def main_home(request):
    """Show the home page."""

    return PlugItRedirect('stations')


# Include terms
@action(route="/terms/", template="terms.html")
@only_orga_member_user()
def terms(request):
    """Show the system status."""

    return {}


# Load the list of countries. Cached
@action(route="/ecc_list")
@json_only()
@cache(time=3600, byUser=False)
def main_ecc_list(request):
    """Return the list of ECCs"""

    list = []

    for elem in Ecc.query.order_by(Ecc.name).all():
        list.append(elem.json)

    return {'list': list}


# Load the list of country codes (cc). Cached
@action(route="/cc_list")
@json_only()
@cache(time=3600, byUser=False)
def main_cc_list(request):
    """Return the list of CCs"""

    list = []

    for cc in CountryCode.query.order_by(CountryCode.name).all():
        list.append(cc.json)

    return {'list': list}
