from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
import websocket
from json import dumps
import pandas as pd
from websocket import WebSocketApp

from snapi_py_client.api_client import ApiClient

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class StocknoteAPIPythonBridge(object):
    
    # Products
    PRODUCT_MIS = "MIS"
    PRODUCT_CNC = "CNC"
    PRODUCT_NRML = "NRML"
    PRODUCT_CO = "CO"
    PRODUCT_BO = "BO"
    
    
    # Exchanges
    EXCHANGE_NSE = "NSE"
    EXCHANGE_BSE = "BSE"
    EXCHANGE_NFO = "NFO"
    EXCHANGE_BFO = "BFO"
    EXCHANGE_CDS = "CDS"
    EXCHANGE_MCX = "MCX"
    
    
    # Transaction type
    TRANSACTION_TYPE_BUY = "BUY"
    TRANSACTION_TYPE_SELL = "SELL"
    
    # Order types
    ORDER_TYPE_MARKET = "MKT"
    ORDER_TYPE_LIMIT = "L"
    ORDER_TYPE_SLM = "SL-M"
    ORDER_TYPE_SL = "SL"
    
    # Validity
    VALIDITY_DAY = "DAY"
    VALIDITY_IOC = "IOC"
    
    #Position
    POSITION_TYPE_DAY ='DAY'
    POSITION_TYPE_NET ='NET'
    
    streaming=None
    
    def __init__(self,session_token=None, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
#         self.ws=websocket.WebSocketApp
        self.session_token=session_token
    
    def login(self, **kwargs):  # noqa: E501
        """User Login  # noqa: E501

        The StockNote APIs allow the user authentication using the Login API. A valid StockNote Trading Account and subscription to StockNote API Services is a pre-requisite for successful authentication. For Example, if you are going to use 3 users for Trading using APIs, all the 3 users will have to open a StockNote Trading Account and will have to subscribe to StockNote API Services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginRequest body:
        :return: LoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.login_with_http_info(**kwargs)  # noqa: E501
            return data

    def login_with_http_info(self, **kwargs):  # noqa: E501
        """User Login  # noqa: E501

        The StockNote APIs allow the user authentication using the Login API. A valid StockNote Trading Account and subscription to StockNote API Services is a pre-requisite for successful authentication. For Example, if you are going to use 3 users for Trading using APIs, all the 3 users will have to open a StockNote Trading Account and will have to subscribe to StockNote API Services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginRequest body:
        :return: LoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data=self.api_client.call_api(
            '/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        
#         if 'sessionToken' in data:
#             self.set_session_token(data['sessionToken'])
#             print('sessionToken',data['sessionToken'])
        
        return data
 
    def set_session_token(self, sessionToken):
        """Set the `session_token` received after a Login successful."""
        self.session_token = sessionToken
        if not sessionToken.strip():
            raise ValueError("Missing session token value, please provide a session token in set_session_token() ")
            
           
              
    def personal_index(self, **kwargs):  # noqa: E501
        """Trade Book  # noqa: E501

        Details of all successfully executed orders placed by the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trade_book(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: PersonalIndexResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_personal_index_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_personal_index_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def get_personal_index_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Personal Index  # noqa: E501

        Details of all successfully executed orders placed by the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_personal_index_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: PersonalIndexResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trade_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_trade_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/indexData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PersonalIndexResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)



    def market_depth(self, **kwargs):
        """Market depth

        This API is used to search equity, derivatives, and commodity scrips based on the user-provided search symbol and exchange name.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param MarketDepth body:
        :return: MarketDepthResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_depth_with_http_info(x_session_token, **kwargs)
        else:
            return self.market_depth_with_http_info(x_session_token, **kwargs)

    def market_depth_with_http_info(self, x_session_token, **kwargs):
        """Search Equity scrips

        This API is used to search equity, derivatives, and commodity scrips based on the user-provided search symbol and exchange name.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param MarketDepth body:
        :return: MarketDepthResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/marketDepth', 'POST',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MarketDepthResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )

    #------------------------------------------------------------------- All Gtt Orders---------------------------------------------------------------------------#


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                         AddGTT                                                                              #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def add_gtt(self, **kwargs):
        """Add GTT

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param AddGTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_gtt_with_http_info(x_session_token, **kwargs)
        else:
            return self.add_gtt_with_http_info(x_session_token, **kwargs)

    def add_gtt_with_http_info(self, x_session_token, **kwargs):
        """Add GTT 

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Add GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/gttoco/addGtt', 'POST',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='AddGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Modify GTT                                                                            #
    #                                                                                                                                                             #
    ###############################################################################################################################################################



    def modify_gtt(self, **kwargs):
        """ModifyGTT

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param ModifyGTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_gtt_with_http_info(x_session_token, **kwargs)
        else:
            return self.modify_gtt_with_http_info(x_session_token, **kwargs)

    def modify_gtt_with_http_info(self, x_session_token, **kwargs):
        """Modify GTT 

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Modify GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/gttoco/modifyGtt', 'PUT',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ModifyGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Delete GTT                                                                            #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def delete_gtt(self, **kwargs):
            """ModifyGTT

            Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

            :param async_req bool
            :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
            :param ModifyGTT body:
            :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
            """
            x_session_token = self.session_token
            if x_session_token is None:
                raise ValueError("Please pass sessiontoken in set_session_token() and try again")
            
            kwargs['_return_http_data_only'] = True
            if kwargs.get('async_req'):
                return self.delete_gtt_with_http_info(x_session_token, **kwargs)
            else:
                return self.delete_gtt_with_http_info(x_session_token, **kwargs)
            

    def delete_gtt_with_http_info(self, x_session_token, **kwargs):
        """Modify GTT 

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Modify GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/gttoco/deleteGtt', 'DELETE',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ModifyGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       ADD OCO                                                                               #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def add_oco(self, **kwargs):
        """Add GTT

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param AddGTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_oco_with_http_info(x_session_token, **kwargs)
        else:
            return self.add_oco_with_http_info(x_session_token, **kwargs)

    def add_oco_with_http_info(self, x_session_token, **kwargs):
        """Add GTT 

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Add GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/gttoco/addOco', 'POST',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='AddGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       MODIFY OCO                                                                            #
    #                                                                                                                                                             #
    ###############################################################################################################################################################



    def modify_oco(self, **kwargs):
        """ModifyGTT

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param ModifyGTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_oco_with_http_info(x_session_token, **kwargs)
        else:
            return self.modify_oco_with_http_info(x_session_token, **kwargs)

    def modify_oco_with_http_info(self, x_session_token, **kwargs):
        """Modify GTT 

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Modify GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/gttoco/modifyOco', 'PUT',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ModifyGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Delete OCO                                                                            #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def delete_oco(self, **kwargs):
            """ModifyGTT

            Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

            :param async_req bool
            :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
            :param ModifyGTT body:
            :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
            """
            x_session_token = self.session_token
            if x_session_token is None:
                raise ValueError("Please pass sessiontoken in set_session_token() and try again")
            
            kwargs['_return_http_data_only'] = True
            if kwargs.get('async_req'):
                return self.delete_oco_with_http_info(x_session_token, **kwargs)
            else:
                return self.delete_oco_with_http_info(x_session_token, **kwargs)
            

    def delete_oco_with_http_info(self, x_session_token, **kwargs):
        """Modify GTT 

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Modify GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/gttoco/deleteOco', 'DELETE',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ModifyGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       List GTT OCO                                                                          #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def list_gtt_oco(self, listType, **kwargs):
        """ModifyGTT

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection, or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param ModifyGTT body:
        :return: ModifyGttResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_gtt_oco_with_http_info(x_session_token, listType, **kwargs)
        else:
            return self.list_gtt_oco_with_http_info(x_session_token, listType, **kwargs)


    def list_gtt_oco_with_http_info(self, x_session_token, listType, **kwargs):
        """Modify GTT 

        Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection, or modifying the order type.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Modify GTT body:
        :return: ModifyGttResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")

        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = None
        query_params = {'listType': listType}  # Fixing the syntax error here, using curly braces for dictionary

        # API call
        return self.api_client.call_api(
            '/gttoco/listGttOco', 'GET',
            path_params={},
            query_params=query_params,  # Fixing the query_params assignment
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ModifyGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )




    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Span Margin                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def span_margin(self, **kwargs):
        """Add GTT

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param AddGTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.span_margin_with_http_info(x_session_token, **kwargs)
        else:
            return self.span_margin_with_http_info(x_session_token, **kwargs)

    def span_margin_with_http_info(self, x_session_token, **kwargs):
        """Add GTT 

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Add GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')

        # API call
        return self.api_client.call_api(
            '/spanMargin', 'POST',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='AddGttResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    

    #-------------------------------------------------------------------- QUOTE ----------------------------------------------------------------------------------#


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Stock Quote                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def get_quote(self, symbol_name, **kwargs):  # noqa: E501
        """Get Quote  # noqa: E501

        Get market depth details for a specific equity scrip including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits etc. This helps user with market picture of an equity scrip using which he will be able to place an order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quote(x_session_token, symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip.For Equity enter SymbolName of the scrip & For Derivatives enter TradingSymbol of the scrip (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :return: MarketDepthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token 
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_quote_with_http_info(x_session_token, symbol_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_quote_with_http_info(x_session_token, symbol_name, **kwargs)  # noqa: E501
            return data

    def get_quote_with_http_info(self, x_session_token, symbol_name, **kwargs):  # noqa: E501
        """Get Quote  # noqa: E501

        Get market depth details for a specific equity scrip including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits etc. This helps user with market picture of an equity scrip using which he will be able to place an order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quote_with_http_info(x_session_token, symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip.For Equity enter SymbolName of the scrip & For Derivatives enter TradingSymbol of the scrip (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :return: MarketDepthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'symbol_name', 'exchange']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_quote`")  # noqa: E501
        # verify the required parameter 'symbol_name' is set
        if ('symbol_name' not in params or
                params['symbol_name'] is None):
            raise ValueError("Missing the required parameter `symbol_name` when calling `get_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'symbol_name' in params:
            query_params.append(('symbolName', params['symbol_name']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        getQuote_path='/quote/getQuote'
        return self.api_client.call_api(
            getQuote_path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketDepthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Index Quote                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
        
    def index_quote(self, indexName, **kwargs):  # noqa: E501
        """Get Quote  # noqa: E501

        Get market depth details for a specific equity scrip including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits etc. This helps user with market picture of an equity scrip using which he will be able to place an order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quote(x_session_token, symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip.For Equity enter SymbolName of the scrip & For Derivatives enter TradingSymbol of the scrip (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :return: MarketDepthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token 
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_index_quote_with_http_info(x_session_token, indexName, **kwargs)  # noqa: E501
        else:
            (data) = self.get_index_quote_with_http_info(x_session_token, indexName, **kwargs)  # noqa: E501
            return data

    def get_index_quote_with_http_info(self, x_session_token, indexName, **kwargs):  # noqa: E501
        """Get Quote  # noqa: E501

        Get market depth details for a specific equity scrip including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits etc. This helps user with market picture of an equity scrip using which he will be able to place an order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quote_with_http_info(x_session_token, symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip.For Equity enter SymbolName of the scrip & For Derivatives enter TradingSymbol of the scrip (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :return: MarketDepthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'symbol_name', 'exchange']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_quote`")  # noqa: E501
        # verify the required parameter 'symbol_name' is set
        if ('indexName' not in params or
                params['indexName'] is None):
            raise ValueError("Missing the required parameter `indexName` when calling `get_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
    
        if 'indexName' in params:
            query_params.append(('indexName', params['indexName']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        getQuote_path='/quote/indexQuote'
        return self.api_client.call_api(
            getQuote_path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketDepthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Multi Quote                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def multi_quote(self, **kwargs):
        """Add GTT

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param AddGTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """
        x_session_token = self.session_token
        if x_session_token is None:
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.multi_quote_with_http_info(x_session_token, **kwargs)
        else:
            return self.multi_quote_with_http_info(x_session_token, **kwargs)

    def multi_quote_with_http_info(self, x_session_token, **kwargs):
        """Add GTT 

        GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order.

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated, and the previous one will get expired. (required)
        :param Add GTT body:
        :return: AddGTTResponse If the method is called asynchronously, returns the request thread.
        """

        # Check if 'x_session_token' is provided
        if x_session_token is None:
            raise ValueError("Missing the required parameter `x_session_token` when calling `market_depth`")
    
        # Set up header parameters
        header_params = {'x-session-token': x_session_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Set up body parameters if provided
        body_params = kwargs.get('body')
        print(body_params)

        # API call
        return self.api_client.call_api(
            '/quote/multiQuote', 'POST',
            path_params={},
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='multiQuoteResponse',
            auth_settings=[],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats={}
        )
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Search Equity scrips                                                                        #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    
    def search_equity_derivative(self,search_symbol_name, **kwargs):  # noqa: E501
        """Search Equity scrips  # noqa: E501

        This API is used to search equity, derivatives and commodity scrips based on user provided search symbol and exchange name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_equity_derivative(x_session_token, search_symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str search_symbol_name: Trading Symbol of the scrip to be searched (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :return: EquitySearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_equity_derivative_with_http_info(x_session_token, search_symbol_name, **kwargs)  # noqa: E501
        else:
            (data) = self.search_equity_derivative_with_http_info(x_session_token, search_symbol_name, **kwargs)  # noqa: E501
            return data

    def search_equity_derivative_with_http_info(self, x_session_token, search_symbol_name, **kwargs):  # noqa: E501
        """Search Equity scrips  # noqa: E501

        This API is used to search equity, derivatives and commodity scrips based on user provided search symbol and exchange name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_equity_derivative_with_http_info(x_session_token, search_symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str search_symbol_name: Trading Symbol of the scrip to be searched (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :return: EquitySearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'search_symbol_name', 'exchange']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_equity_derivative" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `search_equity_derivative`")  # noqa: E501
        # verify the required parameter 'search_symbol_name' is set
        if ('search_symbol_name' not in params or
                params['search_symbol_name'] is None):
            raise ValueError("Missing the required parameter `search_symbol_name` when calling `search_equity_derivative`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'search_symbol_name' in params:
            query_params.append(('searchSymbolName', params['search_symbol_name']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/eqDervSearch/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EquitySearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)



    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Option Chain                                                                                #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    
    def get_option_chain(self,search_symbol_name, **kwargs):  # noqa: E501
        """Option Chain  # noqa: E501

        This API is used to search OptionChain for  equity, derivatives and commodity scrips based on user provided search symbol and exchange name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_option_contracts(x_session_token, search_symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str search_symbol_name: Trading Symbol of the scrip to be searched (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str expiry_date: From date in yyyy-MM-dd
        :param str strike_price: The strike price is the predetermined price at which a put buyer can sell the underlying asset
        :param str option_type: Option Type (PE/CE). 
        :return: OptionChainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_option_contracts_with_http_info(x_session_token, search_symbol_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_option_contracts_with_http_info(x_session_token, search_symbol_name, **kwargs)  # noqa: E501
            return data

    def get_option_contracts_with_http_info(self, x_session_token, search_symbol_name, **kwargs):  # noqa: E501
        """Option Chain  # noqa: E501

        This API is used to search OptionChain for  equity, derivatives and commodity scrips based on user provided search symbol and exchange name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_option_contracts_with_http_info(x_session_token, search_symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str search_symbol_name: Trading Symbol of the scrip to be searched (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str expiry_date: From date in yyyy-MM-dd
        :param str strike_price: The strike price is the predetermined price at which a put buyer can sell the underlying asset
        :param str option_type: Option Type (PE/CE). 
        :return: OptionChainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'search_symbol_name', 'exchange', 'expiry_date', 'strike_price', 'option_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_option_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_option_contracts`")  # noqa: E501
        # verify the required parameter 'search_symbol_name' is set
        if ('search_symbol_name' not in params or
                params['search_symbol_name'] is None):
            raise ValueError("Missing the required parameter `search_symbol_name` when calling `get_option_contracts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'search_symbol_name' in params:
            query_params.append(('searchSymbolName', params['search_symbol_name']))  # noqa: E501
        if 'expiry_date' in params:
            query_params.append(('expiryDate', params['expiry_date']))  # noqa: E501
        if 'strike_price' in params:
            query_params.append(('strikePrice', params['strike_price']))  # noqa: E501
        if 'option_type' in params:
            query_params.append(('optionType', params['option_type']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/option/optionChain', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionChainResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    

    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Future Chain                                                                                #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    
    def get_future_chain(self,search_symbol_name, **kwargs):  # noqa: E501
        """Option Chain  # noqa: E501

        This API is used to search OptionChain for  equity, derivatives and commodity scrips based on user provided search symbol and exchange name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_option_contracts(x_session_token, search_symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str search_symbol_name: Trading Symbol of the scrip to be searched (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str expiry_date: From date in yyyy-MM-dd
        :param str strike_price: The strike price is the predetermined price at which a put buyer can sell the underlying asset
        :param str option_type: Option Type (PE/CE). 
        :return: OptionChainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_future_contracts_with_http_info(x_session_token, search_symbol_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_future_contracts_with_http_info(x_session_token, search_symbol_name, **kwargs)  # noqa: E501
            return data

    def get_future_contracts_with_http_info(self, x_session_token, search_symbol_name, **kwargs):  # noqa: E501
        """Option Chain  # noqa: E501

        This API is used to search OptionChain for  equity, derivatives and commodity scrips based on user provided search symbol and exchange name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_option_contracts_with_http_info(x_session_token, search_symbol_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str search_symbol_name: Trading Symbol of the scrip to be searched (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str expiry_date: From date in yyyy-MM-dd
        :param str strike_price: The strike price is the predetermined price at which a put buyer can sell the underlying asset
        :param str option_type: Option Type (PE/CE). 
        :return: OptionChainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'search_symbol_name', 'exchange', 'expiry_date', 'strike_price', 'option_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_option_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_option_contracts`")  # noqa: E501
        # verify the required parameter 'search_symbol_name' is set
        if ('search_symbol_name' not in params or
                params['search_symbol_name'] is None):
            raise ValueError("Missing the required parameter `search_symbol_name` when calling `get_option_contracts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'search_symbol_name' in params:
            query_params.append(('searchSymbolName', params['search_symbol_name']))  # noqa: E501
        if 'expiry_date' in params:
            query_params.append(('expiryDate', params['expiry_date']))  # noqa: E501
        if 'strike_price' in params:
            query_params.append(('strikePrice', params['strike_price']))  # noqa: E501
        if 'option_type' in params:
            query_params.append(('optionType', params['option_type']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/future/futureChain', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionChainResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        



    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 User Limit                                                                                  #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def get_limits(self, **kwargs):  # noqa: E501
        """User Limits  # noqa: E501

        Gets the user cash balances, available margin for trading in equity and commodity segments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_limits(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: LimitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_limits_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_limits_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def get_limits_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """User Limits  # noqa: E501

        Gets the user cash balances, available margin for trading in equity and commodity segments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_limits_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: LimitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_limits" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_limits`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/limit/getLimits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LimitResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        

   
   #---------------------------------------------------------------- ORDERS ---------------------------------------------------------------------------------#     
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Place Order                                                                                 #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def place_order(self,**kwargs):  # noqa: E501
        """Place Order  # noqa: E501

        This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call.This is for Placing CNC, MIS and NRML Orders   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param OrderRequest body:
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.place_order_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.place_order_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def place_order_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Place Order  # noqa: E501

        This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call.This is for Placing CNC, MIS and NRML Orders   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param OrderRequest body:
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `place_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/placeOrder', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Place CO Order                                                                              #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def place_order_co(self,**kwargs):  # noqa: E501
        """Place CO Order  # noqa: E501

        This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. This is for Placing CO Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_co(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param OrderRequestCO body:
        :return: OrderResponseCO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.place_order_co_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.place_order_co_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def place_order_co_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Place CO Order  # noqa: E501

        This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. This is for Placing CO Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_co_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param OrderRequestCO body:
        :return: OrderResponseCO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order_co" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `place_order_co`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/placeOrderCO', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderResponseCO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Place BO Order                                                                              #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def place_order_bo(self, **kwargs):  # noqa: E501
        """Place BO Order  # noqa: E501

        This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. This is for Placing BO Orders.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_bo(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param OrderRequestBO body:
        :return: OrderResponseBO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.place_order_bo_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.place_order_bo_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def place_order_bo_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Place BO Order  # noqa: E501

        This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. This is for Placing BO Orders.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_order_bo_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param OrderRequestBO body:
        :return: OrderResponseBO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order_bo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `place_order_bo`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/placeOrderBO', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderResponseBO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Order Book                                                                                  #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def get_order_book(self, **kwargs):  # noqa: E501
        """Order Book  # noqa: E501

        Orderbook retrieves and displays details of all orders placed by the user on a specific day. This API returns all states of the orders, namely, open, pending, rejected and executed ones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_book(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: OrderBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_book_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_book_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def get_order_book_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Order Book  # noqa: E501

        Orderbook retrieves and displays details of all orders placed by the user on a specific day. This API returns all states of the orders, namely, open, pending, rejected and executed ones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_book_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: OrderBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_order_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/orderBook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderBookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Order Status                                                                                #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def get_order_status(self,order_number, **kwargs):  # noqa: E501
        """Get Order Status  # noqa: E501

        Get status of an order placed previously. This API returns all states of the orders,but not limited to open, pending, and partially filled ones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  Order Number for which the user wants to check the order status (required)
        :return: OrderStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_status_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_status_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
            return data

    def get_order_status_with_http_info(self, x_session_token, order_number, **kwargs):  # noqa: E501
        """Get Order Status  # noqa: E501

        Get status of an order placed previously. This API returns all states of the orders,but not limited to open, pending, and partially filled ones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_status_with_http_info(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  Order Number for which the user wants to check the order status (required)
        :return: OrderStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'order_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_order_status`")  # noqa: E501
        # verify the required parameter 'order_number' is set
        if ('order_number' not in params or
                params['order_number'] is None):
            raise ValueError("Missing the required parameter `order_number` when calling `get_order_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number' in params:
            query_params.append(('orderNumber', params['order_number']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/getOrderStatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        
    

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Modify Order                                                                                #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def modify_order(self,order_number, **kwargs):  # noqa: E501
        """Modify Order  # noqa: E501

        User would be able to modify some attributes of an order as long as it is with open/pending status in system. For modification order identifier is mandatory. With order identifier you need to send the optional parameter(s) which needs to be modified. In case the optional parameters aren't sent, the default will be considered from the original order. Modifiable attributes include quantity, Order Type (L,MKT, SL,SL-M). This API cannot be used for modifying attributes of an executed/rejected/cancelled order. Only the attribute that needs to be modified should be sent in the request alongwith the Order Identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_order(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number: Unique Order identifier of the order which needs to be modified (required)
        :param ModifyOrderRequest body: Type of order.  MKT - Market Order,L - Limit Order, SL - Stop Loss Limit, SL-M - Stop Loss Market
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_order_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_order_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
            return data

    def modify_order_with_http_info(self, x_session_token, order_number, **kwargs):  # noqa: E501
        """Modify Order  # noqa: E501

        User would be able to modify some attributes of an order as long as it is with open/pending status in system. For modification order identifier is mandatory. With order identifier you need to send the optional parameter(s) which needs to be modified. In case the optional parameters aren't sent, the default will be considered from the original order. Modifiable attributes include quantity, Order Type (L,MKT, SL,SL-M). This API cannot be used for modifying attributes of an executed/rejected/cancelled order. Only the attribute that needs to be modified should be sent in the request alongwith the Order Identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_order_with_http_info(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number: Unique Order identifier of the order which needs to be modified (required)
        :param ModifyOrderRequest body: Type of order.  MKT - Market Order,L - Limit Order, SL - Stop Loss Limit, SL-M - Stop Loss Market
        :return: OrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'order_number', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `modify_order`")  # noqa: E501
        # verify the required parameter 'order_number' is set
        if ('order_number' not in params or
                params['order_number'] is None):
            raise ValueError("Missing the required parameter `order_number` when calling `modify_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_number' in params:
            path_params['orderNumber'] = params['order_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/modifyOrder/{orderNumber}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Trigger Order                                                                               #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def get_trigger_order_numbers(self,order_number, **kwargs):  # noqa: E501
        """TriggerOrders  # noqa: E501

        This API allows you to get the trigger order numbers in case of BO and CO orders so that their attribute values can be modified for BO orders, it will give the order identifiers. For Stop loss leg and target leg. Similarly for CO orders, it will return order identifier of stop loss leg only. Using the order identifier, the user would be able to modify the order attributes using the modifyOrder API. Refer modifyOrder API documentation for the parameters details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trigger_order_numbers(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  Order Number for which the user wants to check the order status (required)
        :return: TriggerOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trigger_order_numbers_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_trigger_order_numbers_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
            return data

    def get_trigger_order_numbers_with_http_info(self, x_session_token, order_number, **kwargs):  # noqa: E501
        """TriggerOrders  # noqa: E501

        This API allows you to get the trigger order numbers in case of BO and CO orders so that their attribute values can be modified for BO orders, it will give the order identifiers. For Stop loss leg and target leg. Similarly for CO orders, it will return order identifier of stop loss leg only. Using the order identifier, the user would be able to modify the order attributes using the modifyOrder API. Refer modifyOrder API documentation for the parameters details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trigger_order_numbers_with_http_info(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  Order Number for which the user wants to check the order status (required)
        :return: TriggerOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'order_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trigger_order_numbers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_trigger_order_numbers`")  # noqa: E501
        # verify the required parameter 'order_number' is set
        if ('order_number' not in params or
                params['order_number'] is None):
            raise ValueError("Missing the required parameter `order_number` when calling `get_trigger_order_numbers`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number' in params:
            query_params.append(('orderNumber', params['order_number']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/getTriggerOrders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TriggerOrdersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Cancel Order                                                                                #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def cancel_order(self,order_number, **kwargs):  # noqa: E501
        """Cancel Order  # noqa: E501

        An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders.This is for CNC, MIS and NRML Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  The order identifier provided as an input which needs to be cancelled (required)
        :return: CancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_order_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_order_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
            return data

    def cancel_order_with_http_info(self, x_session_token, order_number, **kwargs):  # noqa: E501
        """Cancel Order  # noqa: E501

        An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders.This is for CNC, MIS and NRML Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_with_http_info(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  The order identifier provided as an input which needs to be cancelled (required)
        :return: CancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'order_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `cancel_order`")  # noqa: E501
        # verify the required parameter 'order_number' is set
        if ('order_number' not in params or
                params['order_number'] is None):
            raise ValueError("Missing the required parameter `order_number` when calling `cancel_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number' in params:
            query_params.append(('orderNumber', params['order_number']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/cancelOrder', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Cancel BO Order                                                                             #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def cancel_order_bo(self,order_number, **kwargs):  # noqa: E501
        """Cancel BO Order  # noqa: E501

        An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders. This is for cancelling BO Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_bo(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  The main order identifier provided as an input which needs to be exited. (required)
        :return: CancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_order_bo_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_order_bo_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
            return data

    def cancel_order_bo_with_http_info(self, x_session_token, order_number, **kwargs):  # noqa: E501
        """Cancel BO Order  # noqa: E501

        An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders. This is for cancelling BO Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_bo_with_http_info(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  The main order identifier provided as an input which needs to be exited. (required)
        :return: CancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'order_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order_bo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `cancel_order_bo`")  # noqa: E501
        # verify the required parameter 'order_number' is set
        if ('order_number' not in params or
                params['order_number'] is None):
            raise ValueError("Missing the required parameter `order_number` when calling `cancel_order_bo`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number' in params:
            query_params.append(('orderNumber', params['order_number']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/exitBO', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        
    

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Cancel CO Order                                                                             #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def cancel_order_co(self,order_number, **kwargs):  # noqa: E501
        """Cancel CO Order  # noqa: E501

        An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders. This is for cancelling CO Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_co(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  The main order identifier provided as an input which needs to be exited.  (required)
        :return: CancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_order_co_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_order_co_with_http_info(x_session_token, order_number, **kwargs)  # noqa: E501
            return data

    def cancel_order_co_with_http_info(self, x_session_token, order_number, **kwargs):  # noqa: E501
        """Cancel CO Order  # noqa: E501

        An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders. This is for cancelling CO Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_order_co_with_http_info(x_session_token, order_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str order_number:  The main order identifier provided as an input which needs to be exited.  (required)
        :return: CancelOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'order_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order_co" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `cancel_order_co`")  # noqa: E501
        # verify the required parameter 'order_number' is set
        if ('order_number' not in params or
                params['order_number'] is None):
            raise ValueError("Missing the required parameter `order_number` when calling `cancel_order_co`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number' in params:
            query_params.append(('orderNumber', params['order_number']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/exitCO', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Trade Book                                                                                  #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    def get_trade_book(self, **kwargs):  # noqa: E501
        """Trade Book  # noqa: E501

        Details of all successfully executed orders placed by the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trade_book(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: TradeBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trade_book_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_trade_book_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def get_trade_book_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Trade Book  # noqa: E501

        Details of all successfully executed orders placed by the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trade_book_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: TradeBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trade_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_trade_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/trade/tradeBook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradeBookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    #------------------------------------------------------------------ POSITION ---------------------------------------------------------------------------------#
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Get Position                                                                                #
    #                                                                                                                                                             #
    ###############################################################################################################################################################

    
    def get_positions_data(self,position_type, **kwargs):  # noqa: E501
        
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_positions_with_http_info(x_session_token, position_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_positions_with_http_info(x_session_token, position_type, **kwargs)  # noqa: E501
            return data

    def get_positions_with_http_info(self, x_session_token, position_type, **kwargs):  # noqa: E501
         

        all_params = ['x_session_token', 'position_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_positions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_positions`")  # noqa: E501
        # verify the required parameter 'position_type' is set
        if ('position_type' not in params or
                params['position_type'] is None):
            raise ValueError("Missing the required parameter `position_type` when calling `get_positions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'position_type' in params:
            query_params.append(('positionType', params['position_type']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/position/getPositions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PositionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Convert Position                                                                            #
    #                                                                                                                                                             #
    ###############################################################################################################################################################


    def convert_position(self,**kwargs):  # noqa: E501
        """Position Conversion  # noqa: E501

        Convert an existing position of a margin product to a different margin product type. All or a subset of an existing position quantity can be converted to a different product type.The available margin product types are MARGIN_INTRADAY_SQUAREOFF(MIS), CASHNCARRY(CNC), NORMAL(NRML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_position(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param PositionConversionRequest body:
        :return: PositionConversionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_position_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_position_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def convert_position_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Position Conversion  # noqa: E501

        Convert an existing position of a margin product to a different margin product type. All or a subset of an existing position quantity can be converted to a different product type.The available margin product types are MARGIN_INTRADAY_SQUAREOFF(MIS), CASHNCARRY(CNC), NORMAL(NRML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_position_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param PositionConversionRequest body:
        :return: PositionConversionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_position" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `convert_position`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/position/convertPosition', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PositionConversionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                 Position  Square Off                                                                        #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
    
    def square_off_position(self,**kwargs):  # noqa: E501
        """Position Square Off  # noqa: E501

        SqareOff existing position. Mostly used in day trading, in which user buy or sell a particular quantity of a stock and later in the day reverse the transaction to earn a profit. A user Covering his buy order with a sell order or a user covering his sell order with a buy order before market close for that particular day.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.square_off_position(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param PositionSquareOffListRequest body:
        :return: PositionSquareOffListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.square_off_position_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.square_off_position_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def square_off_position_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """Position Square Off  # noqa: E501

        SqareOff existing position. Mostly used in day trading, in which user buy or sell a particular quantity of a stock and later in the day reverse the transaction to earn a profit. A user Covering his buy order with a sell order or a user covering his sell order with a buy order before market close for that particular day.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.square_off_position_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param PositionSquareOffListRequest body:
        :return: PositionSquareOffListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method square_off_position" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `square_off_position`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/position/squareOff', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PositionSquareOffListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                                       Holdings                                                                              #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
    
        
    def get_holding(self,**kwargs):  # noqa: E501
        
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_holding_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_holding_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def get_holding_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        
        all_params = ['x_session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_holding" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_holding`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/holding/getHoldings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    #-----------------------------------------------------------Intraday Candle Data -----------------------------------------------------------------------------#

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                           Index Intraday Candle Data                                                                        #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
        
    def get_index_intraday_candle_data(self,index_name, from_date, **kwargs):  # noqa: E501
        """Index IntraDay candle data  # noqa: E501

        Gets the Index intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific index.      <h3>Supports Following List of Index names:</h3><table>  <tr><td>BSE CG</td><td>SENSEX</td><td>BSE CD</td><td>NIFTY50 PR 1x INV</td></tr>  <tr><td>BSE IT</td><td>METAL</td><td>OILGAS</td><td>NIFTY50 PR 2x LEV</td></tr>  <tr><td>BSEIPO</td><td>GREENX</td><td>POWER</td><td>NIFTY50 TR 1x INV</td></tr>  <tr><td>CARBON</td><td>BASMTR</td><td>CDGS</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>BSEFMC</td><td>BSE HC</td><td>ALLCAP</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>REALTY</td><td>SMEIPO</td><td>DOL30</td><td>NIFTY Mid LIQ 15</td></tr>  <tr><td>LRGCAP</td><td>MIDSEL</td><td>SMLSEL</td><td>NIFTY100 LIQ 15</td></tr>  <tr><td>SNXT50</td><td>SNSX50</td><td>NIFTY 50</td><td>NIFTY Quality 30</td></tr>  <tr><td>NIFTY BANK</td><td>NIFTY NEXT 50</td><td>DOL100</td><td>NIFTY MIDCAP 50</td></tr>  <tr><td>NIFTY 100</td><td>NIFTY 200</td><td>NIFTY 500</td><td>NIFTY FIN SERVICE</td></tr>  <tr><td>NIFTY AUTO</td><td>NIFTY FMCG</td><td>NIFTY IT</td><td>NIFTY COMMODITIES</td></tr>  <tr><td>NIFTY MEDIA</td><td>NIFTY METAL</td><td>NIFTY PHARMA</td><td>NIFTY CONSUMPTION</td></tr>  <tr><td>NIFTY PSU BANK</td><td>NIFTY PVT BANK</td><td>NIFTY REALTY</td><td>NIFTY GROWSECT 15</td></tr>  <tr><td>NIFTY CPSE</td><td>NIFTY ENERGY</td><td>NIFTY INFRA</td><td>NIFTY DIV OPPS 50</td></tr>  <tr><td>NIFTY MNC</td><td>NIFTY PSE</td><td>NIFTY SERV SECTOR</td><td>NIFTY MID100 FREE</td></tr>  <tr><td>DOL200</td><td>TECK</td><td>BSEPSU</td><td>NIFTY SML100 FREE</td></tr>  <tr><td>AUTO</td><td>BANKEX</td><td>INDIA VIX</td><td>NIFTY50 VALUE 20</td></tr></b>   </table>    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_index_intraday_candle_data(x_session_token, index_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str index_name: Index name of the scrip (required)
        :param str from_date: From date in yyyy-MM-dd hh:mm:ss (required)
        :param str to_date: To date in yyyy-MM-dd hh:mm:ss
        :return: IndexIntraDayCandleDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_index_intraday_candle_data_with_http_info(x_session_token, index_name, from_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_index_intraday_candle_data_with_http_info(x_session_token, index_name, from_date, **kwargs)  # noqa: E501
            return data

    def get_index_intraday_candle_data_with_http_info(self, x_session_token, index_name, from_date, **kwargs):  # noqa: E501
        """Index IntraDay candle data  # noqa: E501

        Gets the Index intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific index.      <h3>Supports Following List of Index names:</h3><table>  <tr><td>BSE CG</td><td>SENSEX</td><td>BSE CD</td><td>NIFTY50 PR 1x INV</td></tr>  <tr><td>BSE IT</td><td>METAL</td><td>OILGAS</td><td>NIFTY50 PR 2x LEV</td></tr>  <tr><td>BSEIPO</td><td>GREENX</td><td>POWER</td><td>NIFTY50 TR 1x INV</td></tr>  <tr><td>CARBON</td><td>BASMTR</td><td>CDGS</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>BSEFMC</td><td>BSE HC</td><td>ALLCAP</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>REALTY</td><td>SMEIPO</td><td>DOL30</td><td>NIFTY Mid LIQ 15</td></tr>  <tr><td>LRGCAP</td><td>MIDSEL</td><td>SMLSEL</td><td>NIFTY100 LIQ 15</td></tr>  <tr><td>SNXT50</td><td>SNSX50</td><td>NIFTY 50</td><td>NIFTY Quality 30</td></tr>  <tr><td>NIFTY BANK</td><td>NIFTY NEXT 50</td><td>DOL100</td><td>NIFTY MIDCAP 50</td></tr>  <tr><td>NIFTY 100</td><td>NIFTY 200</td><td>NIFTY 500</td><td>NIFTY FIN SERVICE</td></tr>  <tr><td>NIFTY AUTO</td><td>NIFTY FMCG</td><td>NIFTY IT</td><td>NIFTY COMMODITIES</td></tr>  <tr><td>NIFTY MEDIA</td><td>NIFTY METAL</td><td>NIFTY PHARMA</td><td>NIFTY CONSUMPTION</td></tr>  <tr><td>NIFTY PSU BANK</td><td>NIFTY PVT BANK</td><td>NIFTY REALTY</td><td>NIFTY GROWSECT 15</td></tr>  <tr><td>NIFTY CPSE</td><td>NIFTY ENERGY</td><td>NIFTY INFRA</td><td>NIFTY DIV OPPS 50</td></tr>  <tr><td>NIFTY MNC</td><td>NIFTY PSE</td><td>NIFTY SERV SECTOR</td><td>NIFTY MID100 FREE</td></tr>  <tr><td>DOL200</td><td>TECK</td><td>BSEPSU</td><td>NIFTY SML100 FREE</td></tr>  <tr><td>AUTO</td><td>BANKEX</td><td>INDIA VIX</td><td>NIFTY50 VALUE 20</td></tr></b>   </table>    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_index_intraday_candle_data_with_http_info(x_session_token, index_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str index_name: Index name of the scrip (required)
        :param str from_date: From date in yyyy-MM-dd hh:mm:ss (required)
        :param str to_date: To date in yyyy-MM-dd hh:mm:ss
        :return: IndexIntraDayCandleDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'index_name', 'from_date', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_index_intraday_candle_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_index_intraday_candle_data`")  # noqa: E501
        # verify the required parameter 'index_name' is set
        if ('index_name' not in params or
                params['index_name'] is None):
            raise ValueError("Missing the required parameter `index_name` when calling `get_index_intraday_candle_data`")  # noqa: E501
        # verify the required parameter 'from_date' is set
        if ('from_date' not in params or
                params['from_date'] is None):
            raise ValueError("Missing the required parameter `from_date` when calling `get_index_intraday_candle_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'index_name' in params:
            query_params.append(('indexName', params['index_name']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/intraday/indexCandleData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IndexIntraDayCandleDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                          Intraday Candle Data                                                                               #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
  	

    def get_intraday_candle_data(self,symbol_name, from_date, **kwargs):  # noqa: E501
        """Intraday candle data  # noqa: E501

        Gets the Intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_intraday_candle_data(x_session_token, symbol_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip. (required)
        :param str from_date: From date in yyyy-MM-dd hh:mm:ss (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str to_date: To date in yyyy-MM-dd hh:mm:ss
        :return: IntraDayCandleResponses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_intraday_candle_data_with_http_info(x_session_token, symbol_name, from_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_intraday_candle_data_with_http_info(x_session_token, symbol_name, from_date, **kwargs)  # noqa: E501
            return data

    def get_intraday_candle_data_with_http_info(self, x_session_token, symbol_name, from_date, **kwargs):  # noqa: E501
        """Intraday candle data  # noqa: E501

        Gets the Intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_intraday_candle_data_with_http_info(x_session_token, symbol_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip. (required)
        :param str from_date: From date in yyyy-MM-dd hh:mm:ss (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str to_date: To date in yyyy-MM-dd hh:mm:ss
        :return: IntraDayCandleResponses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'symbol_name', 'from_date', 'exchange', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_intraday_candle_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_intraday_candle_data`")  # noqa: E501
        # verify the required parameter 'symbol_name' is set
        if ('symbol_name' not in params or
                params['symbol_name'] is None):
            raise ValueError("Missing the required parameter `symbol_name` when calling `get_intraday_candle_data`")  # noqa: E501
        # verify the required parameter 'from_date' is set
        if ('from_date' not in params or
                params['from_date'] is None):
            raise ValueError("Missing the required parameter `from_date` when calling `get_intraday_candle_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'symbol_name' in params:
            query_params.append(('symbolName', params['symbol_name']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/intraday/candleData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntraDayCandleResponses',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    

    # -------------------------------------------------------- Historical Candle Data ----------------------------------------------------------------------------#

    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                           Historical  Candle Data                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
  
    def get_historical_candle_data(self,symbol_name, from_date, **kwargs):  # noqa: E501
        """Historical candle data  # noqa: E501

        Gets the historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific symbol. From date is mandatory. End date is optional and defaults to yesterday.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_historical_candle_data(x_session_token, symbol_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip. (required)
        :param str from_date: From date in yyyy-MM-dd (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str to_date: To date in yyyy-MM-dd
        :return: HistoricalCandleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_historical_candle_data_with_http_info(x_session_token, symbol_name, from_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_historical_candle_data_with_http_info(x_session_token, symbol_name, from_date, **kwargs)  # noqa: E501
            return data

    def get_historical_candle_data_with_http_info(self, x_session_token, symbol_name, from_date, **kwargs):  # noqa: E501
        """Historical candle data  # noqa: E501

        Gets the historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific symbol. From date is mandatory. End date is optional and defaults to yesterday.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_historical_candle_data_with_http_info(x_session_token, symbol_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str symbol_name: Symbol name of the scrip. (required)
        :param str from_date: From date in yyyy-MM-dd (required)
        :param str exchange: Name of the exchange.Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS).If the user does not provide an exchange name, by default considered as NSE.For trading with BSE, NFO, CDS and MCX, exchange is mandatory.
        :param str to_date: To date in yyyy-MM-dd
        :return: HistoricalCandleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['x_session_token', 'symbol_name', 'from_date', 'exchange', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_historical_candle_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_historical_candle_data`")  # noqa: E501
        # verify the required parameter 'symbol_name' is set
        if ('symbol_name' not in params or
                params['symbol_name'] is None):
            raise ValueError("Missing the required parameter `symbol_name` when calling `get_historical_candle_data`")  # noqa: E501
        # verify the required parameter 'from_date' is set
        if ('from_date' not in params or
                params['from_date'] is None):
            raise ValueError("Missing the required parameter `from_date` when calling `get_historical_candle_data`")  # noqa: E501

#         if 'from_date' in params and not re.search(r'([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))', params['from_date']):  # noqa: E501
#             raise ValueError("Invalid value for parameter `from_date` when calling `get_historical_candle_data`, must conform to the pattern `/([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'symbol_name' in params:
            query_params.append(('symbolName', params['symbol_name']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/history/candleData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HistoricalCandleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    
    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                      Index Historical Candle Data                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
  
    def get_index_candle_data(self,index_name, from_date, **kwargs):  # noqa: E501
        """Index Historical CandleData  # noqa: E501

        Gets the Index historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific index. From date is mandatory. End date is optional and defaults to Today.      <h3>Supports Following List of Index names:</h3><table>  <tr><td>BSE CG</td><td>SENSEX</td><td>BSE CD</td><td>NIFTY50 PR 1x INV</td></tr>  <tr><td>BSE IT</td><td>METAL</td><td>OILGAS</td><td>NIFTY50 PR 2x LEV</td></tr>  <tr><td>BSEIPO</td><td>GREENX</td><td>POWER</td><td>NIFTY50 TR 1x INV</td></tr>  <tr><td>CARBON</td><td>BASMTR</td><td>CDGS</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>BSEFMC</td><td>BSE HC</td><td>ALLCAP</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>REALTY</td><td>SMEIPO</td><td>DOL30</td><td>NIFTY Mid LIQ 15</td></tr>  <tr><td>LRGCAP</td><td>MIDSEL</td><td>SMLSEL</td><td>NIFTY100 LIQ 15</td></tr>  <tr><td>SNXT50</td><td>SNSX50</td><td>NIFTY 50</td><td>NIFTY Quality 30</td></tr>  <tr><td>NIFTY BANK</td><td>NIFTY NEXT 50</td><td>DOL100</td><td>NIFTY MIDCAP 50</td></tr>  <tr><td>NIFTY 100</td><td>NIFTY 200</td><td>NIFTY 500</td><td>NIFTY FIN SERVICE</td></tr>  <tr><td>NIFTY AUTO</td><td>NIFTY FMCG</td><td>NIFTY IT</td><td>NIFTY COMMODITIES</td></tr>  <tr><td>NIFTY MEDIA</td><td>NIFTY METAL</td><td>NIFTY PHARMA</td><td>NIFTY CONSUMPTION</td></tr>  <tr><td>NIFTY PSU BANK</td><td>NIFTY PVT BANK</td><td>NIFTY REALTY</td><td>NIFTY GROWSECT 15</td></tr>  <tr><td>NIFTY CPSE</td><td>NIFTY ENERGY</td><td>NIFTY INFRA</td><td>NIFTY DIV OPPS 50</td></tr>  <tr><td>NIFTY MNC</td><td>NIFTY PSE</td><td>NIFTY SERV SECTOR</td><td>NIFTY MID100 FREE</td></tr>  <tr><td>DOL200</td><td>TECK</td><td>BSEPSU</td><td>NIFTY SML100 FREE</td></tr>  <tr><td>AUTO</td><td>BANKEX</td><td>INDIA VIX</td><td>NIFTY50 VALUE 20</td></tr></h3>   </table>    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_index_candle_data(x_session_token, index_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str index_name: Index name of the scrip (required)
        :param str from_date: From date in yyyy-MM-dd (required)
        :param str to_date: To date in yyyy-MM-dd
        :return: IndexCandleDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_index_candle_data_with_http_info(x_session_token, index_name, from_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_index_candle_data_with_http_info(x_session_token, index_name, from_date, **kwargs)  # noqa: E501
            return data

    def get_index_candle_data_with_http_info(self, x_session_token, index_name, from_date, **kwargs):  # noqa: E501
        """Index Historical CandleData  # noqa: E501

        Gets the Index historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific index. From date is mandatory. End date is optional and defaults to Today.      <h3>Supports Following List of Index names:</h3><table>  <tr><td>BSE CG</td><td>SENSEX</td><td>BSE CD</td><td>NIFTY50 PR 1x INV</td></tr>  <tr><td>BSE IT</td><td>METAL</td><td>OILGAS</td><td>NIFTY50 PR 2x LEV</td></tr>  <tr><td>BSEIPO</td><td>GREENX</td><td>POWER</td><td>NIFTY50 TR 1x INV</td></tr>  <tr><td>CARBON</td><td>BASMTR</td><td>CDGS</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>BSEFMC</td><td>BSE HC</td><td>ALLCAP</td><td>NIFTY50 TR 2x LEV</td></tr>  <tr><td>REALTY</td><td>SMEIPO</td><td>DOL30</td><td>NIFTY Mid LIQ 15</td></tr>  <tr><td>LRGCAP</td><td>MIDSEL</td><td>SMLSEL</td><td>NIFTY100 LIQ 15</td></tr>  <tr><td>SNXT50</td><td>SNSX50</td><td>NIFTY 50</td><td>NIFTY Quality 30</td></tr>  <tr><td>NIFTY BANK</td><td>NIFTY NEXT 50</td><td>DOL100</td><td>NIFTY MIDCAP 50</td></tr>  <tr><td>NIFTY 100</td><td>NIFTY 200</td><td>NIFTY 500</td><td>NIFTY FIN SERVICE</td></tr>  <tr><td>NIFTY AUTO</td><td>NIFTY FMCG</td><td>NIFTY IT</td><td>NIFTY COMMODITIES</td></tr>  <tr><td>NIFTY MEDIA</td><td>NIFTY METAL</td><td>NIFTY PHARMA</td><td>NIFTY CONSUMPTION</td></tr>  <tr><td>NIFTY PSU BANK</td><td>NIFTY PVT BANK</td><td>NIFTY REALTY</td><td>NIFTY GROWSECT 15</td></tr>  <tr><td>NIFTY CPSE</td><td>NIFTY ENERGY</td><td>NIFTY INFRA</td><td>NIFTY DIV OPPS 50</td></tr>  <tr><td>NIFTY MNC</td><td>NIFTY PSE</td><td>NIFTY SERV SECTOR</td><td>NIFTY MID100 FREE</td></tr>  <tr><td>DOL200</td><td>TECK</td><td>BSEPSU</td><td>NIFTY SML100 FREE</td></tr>  <tr><td>AUTO</td><td>BANKEX</td><td>INDIA VIX</td><td>NIFTY50 VALUE 20</td></tr></h3>   </table>    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_index_candle_data_with_http_info(x_session_token, index_name, from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :param str index_name: Index name of the scrip (required)
        :param str from_date: From date in yyyy-MM-dd (required)
        :param str to_date: To date in yyyy-MM-dd
        :return: IndexCandleDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token', 'index_name', 'from_date', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_index_candle_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `get_index_candle_data`")  # noqa: E501
        # verify the required parameter 'index_name' is set
        if ('index_name' not in params or
                params['index_name'] is None):
            raise ValueError("Missing the required parameter `index_name` when calling `get_index_candle_data`")  # noqa: E501
        # verify the required parameter 'from_date' is set
        if ('from_date' not in params or
                params['from_date'] is None):
            raise ValueError("Missing the required parameter `from_date` when calling `get_index_candle_data`")  # noqa: E501

#         if 'from_date' in params and not re.search(r'([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))', params['from_date']):  # noqa: E501
#             raise ValueError("Invalid value for parameter `from_date` when calling `get_index_candle_data`, must conform to the pattern `/([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'index_name' in params:
            query_params.append(('indexName', params['index_name']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/history/indexCandleData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IndexCandleDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    ###############################################################################################################################################################
    #                                                                                                                                                             #
    #                                                           Log Out                                                                                           #
    #                                                                                                                                                             #
    ###############################################################################################################################################################
  


    def logout(self, **kwargs):  # noqa: E501
        """User Logout  # noqa: E501

        Logging out user from the application  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: SimpleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        x_session_token=self.session_token
        if(x_session_token is None):
            raise ValueError("Please pass sessiontoken in set_session_token() and try again")
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_with_http_info(x_session_token, **kwargs)  # noqa: E501
        else:
            (data) = self.logout_with_http_info(x_session_token, **kwargs)  # noqa: E501
            return data

    def logout_with_http_info(self, x_session_token, **kwargs):  # noqa: E501
        """User Logout  # noqa: E501

        Logging out user from the application  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_with_http_info(x_session_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_session_token: Session token that should be used with API request is given in the response. It is used as an authenticator. A session token is valid for 24 hours or until a new login request is given, where you a new session token will be generated and the previous one will get expired. (required)
        :return: SimpleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_token' is set
        if ('x_session_token' not in params or
                params['x_session_token'] is None):
            raise ValueError("Missing the required parameter `x_session_token` when calling `logout`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_token' in params:
            header_params['x-session-token'] = params['x_session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logout', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
    


    #------------------------------------------------------------- Streaming Code --------------------------------------------------------------------------------#
 
    

    def set_streaming_data(self,value=None):
        if value is None:
            raise ValueError("Missing value attribute, please give value of symbols")
        self.streaming = value
        # print("Set_stream function given input symbols:", value)

    def on_message(ws,err, msg):
        print("packet start")
        print("Actual Market Data  Value ::"+ msg +"\n")
        print("packet end")


    def on_error(error_msg, error_code, additional_info):
        print("Error:", error_msg)
        print("Error Code:", error_code)
        print("Additional Info:", additional_info)


    def on_close():
        print("Streaming Connection Closed")
        
    def on_open(self, open_info):
        print("Connection opened")
        # value = dumps(self.streaming)

        df_symbols = pd.DataFrame({"symbol": self.streaming})
        # Convert the DataFrame to a JSON string
        json_data = df_symbols.to_json(orient="records")
        # print(json_data)

        data = '{"request":{"streaming_type":"quote2", "data":{"symbols":' + json_data + '}, "request_type":"subscribe", "response_format":"json"}}'
        # print("Sending JSON")

        self.ws.send(data)
        self.ws.send("\n")


    def start_streaming(self):
        x_session_token = self.session_token
     
        headers = {'x-session-token': x_session_token}

        websocket.enableTrace(True)

        self.ws = WebSocketApp("wss://stream.stocknote.com", on_open = self.on_open, on_message=self.on_message,
                               on_error=self.on_error, on_close = self.on_close, header=headers)

        self.ws.run_forever()


        
