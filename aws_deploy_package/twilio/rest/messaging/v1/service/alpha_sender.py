# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class AlphaSenderList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the AlphaSenderList

        :param Version version: Version that contains the resource
        :param service_sid: The 34 character unique sid of the Messaging Service.

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderList
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderList
        """
        super(AlphaSenderList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/AlphaSenders'.format(**self._solution)

    def create(self, alpha_sender):
        """
        Create a new AlphaSenderInstance

        :param unicode alpha_sender: An Alphanumeric Sender ID string, up to 11 characters.

        :returns: Newly created AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        """
        data = values.of({'AlphaSender': alpha_sender, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return AlphaSenderInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams AlphaSenderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AlphaSenderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AlphaSenderInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return AlphaSenderPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AlphaSenderInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return AlphaSenderPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a AlphaSenderContext

        :param sid: The sid

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        """
        return AlphaSenderContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a AlphaSenderContext

        :param sid: The sid

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        """
        return AlphaSenderContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.AlphaSenderList>'


class AlphaSenderPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the AlphaSenderPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The 34 character unique sid of the Messaging Service.

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderPage
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderPage
        """
        super(AlphaSenderPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AlphaSenderInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        """
        return AlphaSenderInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.AlphaSenderPage>'


class AlphaSenderContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the AlphaSenderContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        """
        super(AlphaSenderContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/AlphaSenders/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a AlphaSenderInstance

        :returns: Fetched AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AlphaSenderInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the AlphaSenderInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.AlphaSenderContext {}>'.format(context)


class AlphaSenderInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the AlphaSenderInstance

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        """
        super(AlphaSenderInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'alpha_sender': payload['alpha_sender'],
            'capabilities': payload['capabilities'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AlphaSenderContext for this AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderContext
        """
        if self._context is None:
            self._context = AlphaSenderContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The 34 character unique sid of the Alpha Sender ID.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The 34 character unique sid of the Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The 34 character unique sid of the Messaging Service.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def alpha_sender(self):
        """
        :returns: An Alphanumeric Sender ID string, up to 11 characters.
        :rtype: unicode
        """
        return self._properties['alpha_sender']

    @property
    def capabilities(self):
        """
        :returns: An array of values that indicate whether the number can receive calls or messages.
        :rtype: dict
        """
        return self._properties['capabilities']

    @property
    def url(self):
        """
        :returns: The absolute URL for this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a AlphaSenderInstance

        :returns: Fetched AlphaSenderInstance
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the AlphaSenderInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.AlphaSenderInstance {}>'.format(context)
