# TODO documentation
# TODO unittests

import call


class pySIR:
    def __init__(self, baseurl):
        # sir = pySIR('http://localhost:8080')
        self.baseurl = baseurl

    def _make_call(self, endpoint, method, params):
        return call.Call('{}{}'.format(self.baseurl, endpoint), method, params=params)

    ################
    # ANALYTICS ####
    ################
    def get_top_prefixes(self, **params):
        # r = sir.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00")
        # r = sir.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00", limit_prefixes=10, net_masks="24", exclude_net_masks=1)
        # r = sir.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00", limit_prefixes=10, net_masks="20,24")

        endpoint = "/api/v1.0/analytics/top_prefixes"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_top_asns(self, **params):
        # r = sir.get_top_asns(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00")
        endpoint = "/api/v1.0/analytics/top_asns"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def find_prefix(self, prefix, prefix_length, **params):
        # r = sir.find_prefix(prefix='2.1.1.0', prefix_length='24', date='2015-07-23T12:00:01')
        endpoint = "/api/v1.0/analytics/find_prefix/{}/{}".format(prefix, prefix_length)
        r = self._make_call(endpoint, 'GET', params)
        return r

    def find_prefixes_asn(self, asn, **params):
        # r = sir.find_prefix_asn(asn=3549, date='2015-07-23T12:00:01')
        # r = sir.find_prefix_asn(asn=3549, date='2015-07-23T12:00:01', origin_only=1)
        endpoint = "/api/v1.0/analytics/find_prefixes_asn/{}".format(asn)
        r = self._make_call(endpoint, 'GET', params)
        return r

    ################
    # VARIABLES ####
    ################
    def get_variables(self, **params):
        # r = sir.get_variables()
        endpoint = "/api/v1.0/variables"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def post_variables(self, **params):
        # r = sir.post_variables(name='this_is_a_variable', content='231', category='development', extra_vars='{"asd": "qwe" , "zxc":"poi"}')
        endpoint = "/api/v1.0/variables"
        r = self._make_call(endpoint, 'POST', params)
        return r

    def get_categories(self, **params):
        # r = sir.get_categories()
        endpoint = "/api/v1.0/variables/categories"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_variables_by_category(self, category, **params):
        # r = sir.get_variables_by_category('xcvxcv')
        endpoint = "/api/v1.0/variables/categories/{}".format(category)
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_variables_by_category_and_name(self, category, name, **params):
        # r = sir.get_variables_by_category('xcvxcv')
        endpoint = "/api/v1.0/variables/categories/{}/{}".format(category, name)
        r = self._make_call(endpoint, 'GET', params)
        return r

    def put_variables_by_category_and_name(self, q_category, q_name, **params):
        # r = sir.put_variables_by_category_and_name(development, whatever, content='231', extra_vars='{"asd": "qwe" , "zxc":"poi"}')
        endpoint = "/api/v1.0/variables/categories/{}/{}".format(q_category, q_name)
        r = self._make_call(endpoint, 'PUT', params)
        return r

    def delete_variables_by_category_and_name(self, category, name, **params):
        # sir.delete_variables_by_category_and_name(development, whatever)
        endpoint = "/api/v1.0/variables/categories/{}/{}".format(category, name)
        r = self._make_call(endpoint, 'DELETE', params)
        return r

    def get_available_dates(self, **params):
        # r = sir.get_available_dates()
        endpoint = "/api/v1.0/pmacct/dates"
        r = self._make_call(endpoint, 'GET', params)
        return r

    ################
    # PMACCT #######
    ################

    def get_flows(self, **params):
        # r = sir.get_flows(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00")
        endpoint = "/api/v1.0/pmacct/flows"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_bgp_prefixes(self, **params):
        # r = sir.get_bgp_prefixes(date="2015-07-16T11:00:01")
        endpoint = "/api/v1.0/pmacct/bgp_prefixes"
        r = self._make_call(endpoint, 'GET', params)
        return r
