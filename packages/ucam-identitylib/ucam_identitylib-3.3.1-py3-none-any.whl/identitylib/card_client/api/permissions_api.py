# coding: utf-8

"""
    University Card API

     ## Introduction  The Card API allows access to information about University Cards.  The API broadly follows the principles of REST and strives to provide an interface that can be easily consumed by downstream systems.  ### Stability  This release of the Card API is a `beta` offering: a service we are moving towards live but which requires wider testing with a broader group of users. We consider the Card API as being at least as stable as the legacy card system which it aims to replace, so we encourage users to make use of the Card API rather than relying on the legacy card system.  ### Versioning  The Card API is versioned using url path prefixes in the format: `/v1beta1/cards`. This follows the pattern established by the [GCP API](https://cloud.google.com/apis/design/versioning). Breaking changes will not be made without a change in API major version, however non-breaking changes will be introduced without changes to the version path prefix. All changes will be documented in the project's [CHANGELOG](https://gitlab.developers.cam.ac.uk/uis/devops/iam/card-database/card-api/-/blob/master/CHANGELOG.md).  The available versions of the API are listed at the API's root.  ### Domain  The Card API has been designed to only expose information about University Cards and the identifiers which link a Card to a person. The API does not expose information about cardholders or the institutions that a cardholder belongs to. This is in order to combat domain crossover and to ensure the Card API does not duplicate information which is held and managed within systems such as Lookup, CamSIS or CHRIS.  It is expected that the Card API should be used alongside APIs such as Lookup which allow personal and institutional membership information to be retrieved. A tool has been written in order to allow efficient querying of the Card API using information contained within, CamSIS or CHRIS. [Usage and installation instructions for this tool can be found here](https://gitlab.developers.cam.ac.uk/uis/devops/iam/card-database/card-client).  ### Data source  The data exposed in the Card API is currently a mirror of data contained within the [Card Database](https://webservices.admin.cam.ac.uk/uc/). With data being synced from the Card Database to the Card API hourly.  In future, card data will be updated and created directly using the Card API so changes will be reflected in the Card API 'live' without this hourly sync.  ## Core entities  ### The `Card` Entity  The `Card` entity is a representation of a physical University Card. The entity contains fields indicating the status of the card and when the card has moved between different statuses. Cards held by individuals (such as students or staff) and temporary cards managed by institutions are both represented by the `Card` entity, with the former having a `cardType` of `MIFARE_PERSONAL` and the latter having a `cardType` of `MIFARE_TEMPORARY`.  Each card should have a set of `CardIdentifiers` which allow the card to be linked to an entity in another system (e.g. a person in Lookup), or record information about identifiers held within the card, such as Mifare ID.  The full `Card` entity contains a `cardNotes` field which holds a set of notes made by administrator users related to the card, as well as an `attributes` field which holds the data that is present on the physical presentation of a card. Operations which list many cards return `CardSummary` entities which omit these fields for brevity.  ### The `CardIdentifier` Entity  The `CardIdentifier` entity holds the `value` and `scheme` of a given identifier. The `value` field of a `CardIdentifier` is a simple ID string - e.g. `wgd23` or `000001`. The `scheme` field of a `CardIdentifier` indicates what system this identifier relates to or was issued by. This allows many identifiers which relate to different systems to be recorded against a single `Card`.  > **WARNING!** > > A barcode identifier (`barcode.v1.card.university.identifiers.cam.ac.uk`) may be associated with more than one user. See `Known Issues` for more details.  The supported schemes are: * `v1.person.identifiers.cam.ac.uk`: The CRSid of the person who holds this card * `person.v1.student-records.university.identifiers.cam.ac.uk`: The CamSIS identifier (USN) of the person who holds this card * `person.v1.human-resources.university.identifiers.cam.ac.uk`: The CHRIS identifier (staff number) of the person who holds this card * `person.v1.board-of-graduate-studies.university.identifiers.cam.ac.uk`: The Board of Graduate Studies identifier of the person who holds this card * `person.v1.legacy-card.university.identifiers.cam.ac.uk`: The legacy card holder ID for the person who holds this card * `mifare-identifier.v1.card.university.identifiers.cam.ac.uk`: The Mifare ID which is embedded in this card (this     identifier uniquely identifies a single card) * `mifare-number.v1.card.university.identifiers.cam.ac.uk`: The Mifare Number which is embedded in this card     (this identifier is a digest of card's legacy cardholder ID and issue number, so is not     guaranteed to be unique) * `card.v1.legacy-card.university.identifiers.cam.ac.uk`: The legacy card ID from the card database * `temporary-card.v1.card.university.identifiers.cam.ac.uk`: The temporary card ID from the card database * `photo.v1.photo.university.identifiers.cam.ac.uk`: The ID of the photo printed on this card * `barcode.v1.card.university.identifiers.cam.ac.uk`: The barcode printed on this card * `institution.v1.legacy-card.university.identifiers.cam.ac.uk`: The legacy institution ID from the card database (only populated on temporary cards)   ## Using the API  ### Auth  To authenticate against the Card API, an application must be registered within the API Service, the application must be owned by a team account as opposed to an individual account and the application must be granted access to the `University Card` product. Details of how to register an application and grant access to products can be found in the [API Service Getting Started Guide](https://developer.api.apps.cam.ac.uk/start-using-an-api).  #### Principal  Throughout this specification the term `principal` is used to describe the user or service who is making use of the API. When authenticating using the OAuth2 client credentials flow the principal shall be the application registered within the API Gateway. When authenticating using the authorization code flow, e.g. via a Single Page Application, the principal shall be the user who has authenticated and consented to give the application access to the data contained within this API - identified by their CRSid.  This specification references permissions which can be granted to any principal - please contact the API maintainers to grant a principal a specific permission.  ### Content Type  The Card API responds with JSON data. The `Content-Type` request header should be omitted or set to `application/json`. If an invalid `Content-Type` header is sent the API will respond with `415 Unsupported Media Type`.  ### Pagination  For all operations where multiple entities will be returned, the API will return a paginated result. This is to account for too many entities needing to be returned within a single response. A Paginated response has the structure:  ```json {   \"next\": \"https://<gateway_host>/card/v1beta1/cards/?cursor=cD0yMDIxLTAxL   \"previous\": null,   \"results\": [       ... the data for the current page   ] }  ```  The `next` field holds the url of the next page of results, containing a cursor which indicates to the API which page of results to return. If the `next` field is `null` no further results are available. The `previous` field can be used to navigate backwards through pages of results.  The `page_size` query parameter can be used to control the number of results to return. This defaults to 200 but can be set to a maximum of 500, if set to greater than this no error will be returned but only 500 results will be given in the response.  ## Known Issues  ### Barcodes  There are barcodes in the Card API that are associated with multiple users. The two main causes of this are:   - imported records from the previous card system   - a bug that existed in the current system were the same barcode is assigned to multiple users     created at the same time  The Card API service team are working towards no active cards (status=ISSUED) sharing the same barcode. Defences have been put it place to prevent new duplicate barcodes occurring.  **Clients of the Card API should expect expired cards and card requests to potentially be associated with a barcode that is also associated with cards and card requests of a different user. As the `card-identifiers` endpoint uses all cards/card requests to link identifiers, when looking up using effected barcodes, multiple users (via identifiers) will always remain associated.**  The `discontinued-identifiers` endpoint provides details of identifiers that are no longer to be **reused**. Records in `discontinued-identifiers` prevent reusing the specified identifier with **new** card requests. This endpoint can be queried for barcodes that have been identified as being associated with multiple users.  

    The version of the OpenAPI document: v1beta1
    Contact: universitycard-dev@uis.cam.ac.uk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from identitylib.card_client.models.permissions import Permissions

from identitylib.card_client.api_client import ApiClient, RequestSerialized
from identitylib.card_client.api_response import ApiResponse
from identitylib.card_client.rest import RESTResponseType


class PermissionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def permissions_retrieve(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Permissions:
        """List permissions

        List the permissions of the current principal

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._permissions_retrieve_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Permissions",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def permissions_retrieve_with_http_info(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Permissions]:
        """List permissions

        List the permissions of the current principal

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._permissions_retrieve_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Permissions",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def permissions_retrieve_without_preload_content(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List permissions

        List the permissions of the current principal

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._permissions_retrieve_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Permissions",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _permissions_retrieve_serialize(
        self,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'apiGatewayAuthorizationCodeSecurityScheme', 
            'apiGatewayClientCredentialsSecurityScheme'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/permissions',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


