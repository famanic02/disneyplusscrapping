from contants import clientApiKey

DisneyPages = {
    'getAssertionKey': {
        'method': 'post',
        'url': 'https://global.edge.bamgrid.com/devices',
        'headers': {
            'authority': 'global.edge.bamgrid.com',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'authorization': 'Bearer {api_key}'.format(api_key=clientApiKey),
            'content-type': 'application/json; charset=UTF-8',
            'x-bamsdk-version': '4.4',
            'accept': 'application/json; charset=utf-8',
            'sec-fetch-dest': 'empty',
            'origin': 'https://www.disneyplus.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.disneyplus.com/en-gb/login',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    },
    'getToken': {
        'method': 'post',
        'url': 'https://global.edge.bamgrid.com/token',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': 'Bearer {api_key}'.format(api_key=clientApiKey),
            'Accept-Language': 'en-gb',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'global.edge.bamgrid.com',
            'Origin': 'https://www.disneyplus.com',
            'Referer': 'https://www.disneyplus.com/',
            'Content-Length': '601',
            'Connection': 'keep-alive',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'x-bamsdk-version': '4.4',
        }

    },
    'login': {
        'method': 'post',
        'url': 'https://global.edge.bamgrid.com/idp/login',
        'headers': {
            'authority': 'global.edge.bamgrid.com',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'content-type': 'application/json; charset=UTF-8',
            'x-bamsdk-version': '4.4',
            'accept': 'application/json; charset=utf-8',
            'sec-fetch-dest': 'empty',
            'origin': 'https://www.disneyplus.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.disneyplus.com/login/password',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    },
    'grant': {
        'method': 'post',
        'url': 'https://global.edge.bamgrid.com/accounts/grant',
        'headers': {
            'authority': 'global.edge.bamgrid.com',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'content-type': 'application/json; charset=UTF-8',
            'x-bamsdk-version': '4.4',
            'accept': 'application/json; charset=utf-8',
            'sec-fetch-dest': 'empty',
            'origin': 'https://www.disneyplus.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.disneyplus.com/login/password',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    },
    'newToken': {
        'method': 'post',
        'url': 'https://global.edge.bamgrid.com/token',
        'headers': {
            'authority': 'global.edge.bamgrid.com',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'authorization': 'Bearer {api_key}'.format(api_key=clientApiKey),
            'content-type': 'application/x-www-form-urlencoded',
            'x-bamsdk-version': '4.4',
            'accept': 'application/json',
            'sec-fetch-dest': 'empty',
            'origin': 'https://www.disneyplus.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.disneyplus.com/login/password',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    },
    'collectionSet': {
        'method': 'get',
        'url': 'https://search-api-disney.svcs.dssott.com/svc/search/v2/graphql/persisted/query/core/CollectionBySlug',
        'headers': {
            'Connection': 'keep-alive',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'accept': 'application/json',
            'x-bamsdk-version': '4.4',
            'Sec-Fetch-Dest': 'empty',
            'Origin': 'https://www.disneyplus.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://www.disneyplus.com/',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'If-None-Match': '9ba6d14e07a75fc303229734c63db871209aeb5d',
        }
    },
    'section': {
        'method': 'get',
        'url': 'https://search-api-disney.svcs.dssott.com/svc/search/v2/graphql/persisted/query/core/SetBySetId',
        'headers': {
            'Connection': 'keep-alive',
            'x-bamsdk-platform': 'macintosh',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'accept': 'application/json',
            'x-bamsdk-version': '4.4',
            'Sec-Fetch-Dest': 'empty',
            'Origin': 'https://www.disneyplus.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://www.disneyplus.com/',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'If-None-Match': '0bcba097f16a9a7c5f054b361923693fd43e7ca3',
        }
    }
}
