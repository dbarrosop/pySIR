# TODO documentation
# TODO unittests

import call


class pySIR:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.reported_methods = call.Call('{}/methods'.format(baseurl), 'GET')

    def _make_call(self, endpoint, method, params):
        return call.Call('{}{}'.format(self.baseurl, endpoint), method, params=params)

    def get_top_prefixes(self, **params):
        # r = p.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00")
        # r = p.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00", limit_prefixes=10, net_masks="24", exclude_net_masks=1)
        # r = p.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00", limit_prefixes=10, net_masks="20,24")

        endpoint = "/analytics/top_prefixes"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_top_asns(self, **params):
        # r = p.get_top_asns(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00")
        endpoint = "/analytics/top_asns"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_variables(self, **params):
        # r = p.get_variables()
        endpoint = "/variables"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def post_variables(self, **params):
        # r = p.post_variables(name='this_is_a_variable', content='231', category='development', extra_vars='{"asd": "qwe" , "zxc":"poi"}')
        endpoint = "/variables"
        r = self._make_call(endpoint, 'POST', params)
        return r

    def get_categories(self, **params):
        # r = p.get_categories()
        endpoint = "/variables/categories"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_variables_by_category(self, category, **params):
        # r = p.get_variables_by_category('xcvxcv')
        endpoint = "/variables/categories/{}".format(category)
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_variables_by_category_and_name(self, category, name, **params):
        # r = p.get_variables_by_category('xcvxcv')
        endpoint = "/variables/categories/{}/{}".format(category, name)
        r = self._make_call(endpoint, 'GET', params)
        return r

    def put_variables_by_category_and_name(self, q_category, q_name, **params):
        # r = p.put_variables_by_category_and_name(development, whatever, content='231', extra_vars='{"asd": "qwe" , "zxc":"poi"}')
        endpoint = "/variables/categories/{}/{}".format(q_category, q_name)
        r = self._make_call(endpoint, 'PUT', params)
        return r

    def delete_variables_by_category_and_name(self, category, name, **params):
        # p.delete_variables_by_category_and_name(development, whatever)
        endpoint = "/variables/categories/{}/{}".format(category, name)
        r = self._make_call(endpoint, 'DELETE', params)
        return r

    def get_available_dates(self, **params):
        # r = p.get_available_dates()
        endpoint = "/pmacct/dates"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_flows(self, **params):
        # r = p.get_flows(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00")
        endpoint = "/pmacct/flows"
        r = self._make_call(endpoint, 'GET', params)
        return r

    def get_bgp_prefixes(self, **params):
        # r = p.get_bgp_prefixes(date="2015-07-16T11:00:01")
        endpoint = "/pmacct/bgp_prefixes"
        r = self._make_call(endpoint, 'GET', params)
        return r
