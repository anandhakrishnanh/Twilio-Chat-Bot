# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NationalList(ListResource):
    """  """

    def __init__(self, version, account_sid, country_code):
        """
        Initialize the NationalList

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param country_code: The ISO-3166-1 country code of the country.

        :returns: twilio.rest.api.v2010.account.available_phone_number.national.NationalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalList
        """
        super(NationalList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'country_code': country_code, }
        self._uri = '/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/National.json'.format(**self._solution)

    def stream(self, area_code=values.unset, contains=values.unset,
               sms_enabled=values.unset, mms_enabled=values.unset,
               voice_enabled=values.unset,
               exclude_all_address_required=values.unset,
               exclude_local_address_required=values.unset,
               exclude_foreign_address_required=values.unset, beta=values.unset,
               near_number=values.unset, near_lat_long=values.unset,
               distance=values.unset, in_postal_code=values.unset,
               in_region=values.unset, in_rate_center=values.unset,
               in_lata=values.unset, in_locality=values.unset,
               fax_enabled=values.unset, limit=None, page_size=None):
        """
        Streams NationalInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode area_code: The area code of the phone numbers to read
        :param unicode contains: The pattern on which to match phone numbers
        :param bool sms_enabled: Whether the phone numbers can receive text messages
        :param bool mms_enabled: Whether the phone numbers can receive MMS messages
        :param bool voice_enabled: Whether the phone numbers can receive calls.
        :param bool exclude_all_address_required: Whether to exclude phone numbers that require an Address
        :param bool exclude_local_address_required: Whether to exclude phone numbers that require a local address
        :param bool exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign address
        :param bool beta: Whether to read phone numbers new to the Twilio platform
        :param unicode near_number: Given a phone number, find a geographically close number within distance miles. (US/Canada only)
        :param unicode near_lat_long: Given a latitude/longitude pair lat,long find geographically close numbers within distance miles. (US/Canada only)
        :param unicode distance: The search radius, in miles, for a near_ query. (US/Canada only)
        :param unicode in_postal_code: Limit results to a particular postal code. (US/Canada only)
        :param unicode in_region: Limit results to a particular region. (US/Canada only)
        :param unicode in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. (US/Canada only)
        :param unicode in_lata: Limit results to a specific local access and transport area. (US/Canada only)
        :param unicode in_locality: Limit results to a particular locality
        :param bool fax_enabled: Whether the phone numbers can receive faxes
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number.national.NationalInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            near_number=near_number,
            near_lat_long=near_lat_long,
            distance=distance,
            in_postal_code=in_postal_code,
            in_region=in_region,
            in_rate_center=in_rate_center,
            in_lata=in_lata,
            in_locality=in_locality,
            fax_enabled=fax_enabled,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, area_code=values.unset, contains=values.unset,
             sms_enabled=values.unset, mms_enabled=values.unset,
             voice_enabled=values.unset, exclude_all_address_required=values.unset,
             exclude_local_address_required=values.unset,
             exclude_foreign_address_required=values.unset, beta=values.unset,
             near_number=values.unset, near_lat_long=values.unset,
             distance=values.unset, in_postal_code=values.unset,
             in_region=values.unset, in_rate_center=values.unset,
             in_lata=values.unset, in_locality=values.unset,
             fax_enabled=values.unset, limit=None, page_size=None):
        """
        Lists NationalInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode area_code: The area code of the phone numbers to read
        :param unicode contains: The pattern on which to match phone numbers
        :param bool sms_enabled: Whether the phone numbers can receive text messages
        :param bool mms_enabled: Whether the phone numbers can receive MMS messages
        :param bool voice_enabled: Whether the phone numbers can receive calls.
        :param bool exclude_all_address_required: Whether to exclude phone numbers that require an Address
        :param bool exclude_local_address_required: Whether to exclude phone numbers that require a local address
        :param bool exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign address
        :param bool beta: Whether to read phone numbers new to the Twilio platform
        :param unicode near_number: Given a phone number, find a geographically close number within distance miles. (US/Canada only)
        :param unicode near_lat_long: Given a latitude/longitude pair lat,long find geographically close numbers within distance miles. (US/Canada only)
        :param unicode distance: The search radius, in miles, for a near_ query. (US/Canada only)
        :param unicode in_postal_code: Limit results to a particular postal code. (US/Canada only)
        :param unicode in_region: Limit results to a particular region. (US/Canada only)
        :param unicode in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. (US/Canada only)
        :param unicode in_lata: Limit results to a specific local access and transport area. (US/Canada only)
        :param unicode in_locality: Limit results to a particular locality
        :param bool fax_enabled: Whether the phone numbers can receive faxes
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number.national.NationalInstance]
        """
        return list(self.stream(
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            near_number=near_number,
            near_lat_long=near_lat_long,
            distance=distance,
            in_postal_code=in_postal_code,
            in_region=in_region,
            in_rate_center=in_rate_center,
            in_lata=in_lata,
            in_locality=in_locality,
            fax_enabled=fax_enabled,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, area_code=values.unset, contains=values.unset,
             sms_enabled=values.unset, mms_enabled=values.unset,
             voice_enabled=values.unset, exclude_all_address_required=values.unset,
             exclude_local_address_required=values.unset,
             exclude_foreign_address_required=values.unset, beta=values.unset,
             near_number=values.unset, near_lat_long=values.unset,
             distance=values.unset, in_postal_code=values.unset,
             in_region=values.unset, in_rate_center=values.unset,
             in_lata=values.unset, in_locality=values.unset,
             fax_enabled=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of NationalInstance records from the API.
        Request is executed immediately

        :param unicode area_code: The area code of the phone numbers to read
        :param unicode contains: The pattern on which to match phone numbers
        :param bool sms_enabled: Whether the phone numbers can receive text messages
        :param bool mms_enabled: Whether the phone numbers can receive MMS messages
        :param bool voice_enabled: Whether the phone numbers can receive calls.
        :param bool exclude_all_address_required: Whether to exclude phone numbers that require an Address
        :param bool exclude_local_address_required: Whether to exclude phone numbers that require a local address
        :param bool exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign address
        :param bool beta: Whether to read phone numbers new to the Twilio platform
        :param unicode near_number: Given a phone number, find a geographically close number within distance miles. (US/Canada only)
        :param unicode near_lat_long: Given a latitude/longitude pair lat,long find geographically close numbers within distance miles. (US/Canada only)
        :param unicode distance: The search radius, in miles, for a near_ query. (US/Canada only)
        :param unicode in_postal_code: Limit results to a particular postal code. (US/Canada only)
        :param unicode in_region: Limit results to a particular region. (US/Canada only)
        :param unicode in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. (US/Canada only)
        :param unicode in_lata: Limit results to a specific local access and transport area. (US/Canada only)
        :param unicode in_locality: Limit results to a particular locality
        :param bool fax_enabled: Whether the phone numbers can receive faxes
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NationalInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalPage
        """
        params = values.of({
            'AreaCode': area_code,
            'Contains': contains,
            'SmsEnabled': sms_enabled,
            'MmsEnabled': mms_enabled,
            'VoiceEnabled': voice_enabled,
            'ExcludeAllAddressRequired': exclude_all_address_required,
            'ExcludeLocalAddressRequired': exclude_local_address_required,
            'ExcludeForeignAddressRequired': exclude_foreign_address_required,
            'Beta': beta,
            'NearNumber': near_number,
            'NearLatLong': near_lat_long,
            'Distance': distance,
            'InPostalCode': in_postal_code,
            'InRegion': in_region,
            'InRateCenter': in_rate_center,
            'InLata': in_lata,
            'InLocality': in_locality,
            'FaxEnabled': fax_enabled,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return NationalPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NationalInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NationalInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return NationalPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NationalList>'


class NationalPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the NationalPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param country_code: The ISO-3166-1 country code of the country.

        :returns: twilio.rest.api.v2010.account.available_phone_number.national.NationalPage
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalPage
        """
        super(NationalPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NationalInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.available_phone_number.national.NationalInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalInstance
        """
        return NationalInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            country_code=self._solution['country_code'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NationalPage>'


class NationalInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, country_code):
        """
        Initialize the NationalInstance

        :returns: twilio.rest.api.v2010.account.available_phone_number.national.NationalInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalInstance
        """
        super(NationalInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'lata': payload['lata'],
            'locality': payload['locality'],
            'rate_center': payload['rate_center'],
            'latitude': deserialize.decimal(payload['latitude']),
            'longitude': deserialize.decimal(payload['longitude']),
            'region': payload['region'],
            'postal_code': payload['postal_code'],
            'iso_country': payload['iso_country'],
            'address_requirements': payload['address_requirements'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'country_code': country_code, }

    @property
    def friendly_name(self):
        """
        :returns: A formatted version of the phone number
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def lata(self):
        """
        :returns: The LATA of this phone number
        :rtype: unicode
        """
        return self._properties['lata']

    @property
    def locality(self):
        """
        :returns: The locality or city of this phone number's location
        :rtype: unicode
        """
        return self._properties['locality']

    @property
    def rate_center(self):
        """
        :returns: The rate center of this phone number
        :rtype: unicode
        """
        return self._properties['rate_center']

    @property
    def latitude(self):
        """
        :returns: The latitude of this phone number's location
        :rtype: unicode
        """
        return self._properties['latitude']

    @property
    def longitude(self):
        """
        :returns: The longitude of this phone number's location
        :rtype: unicode
        """
        return self._properties['longitude']

    @property
    def region(self):
        """
        :returns: The two-letter state or province abbreviation of this phone number's location
        :rtype: unicode
        """
        return self._properties['region']

    @property
    def postal_code(self):
        """
        :returns: The postal or ZIP code of this phone number's location
        :rtype: unicode
        """
        return self._properties['postal_code']

    @property
    def iso_country(self):
        """
        :returns: The ISO country code of this phone number
        :rtype: unicode
        """
        return self._properties['iso_country']

    @property
    def address_requirements(self):
        """
        :returns: The type of Address resource the phone number requires
        :rtype: unicode
        """
        return self._properties['address_requirements']

    @property
    def beta(self):
        """
        :returns: Whether the phone number is new to the Twilio platform
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: Whether a phone number can receive calls or messages
        :rtype: unicode
        """
        return self._properties['capabilities']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NationalInstance>'
