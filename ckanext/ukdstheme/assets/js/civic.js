document.addEventListener("DOMContentLoaded", function(event) {

    var cookies_config = {
        apiKey: cookieControlSettings.apiKey,
        product: cookieControlSettings.product,
        encodeCookie: true, // some libraries break if the cookie has unencoded characters e.g. "
        consentCookieExpiry: 90,
        subDomains: false,
    
        // configuration, List of cookies
        necessaryCookies: NECESSARY_COOKIES,
        statement: COOKIES_PRIVACY_STATEMENT,
        text: CIVIC_CONTROL_TEXT,
    
        // Layout and designing
        position: "right",
        theme:"dark",
        toggleType: "slider",
    
        branding: CIVIC_BRANDING
    
    };

	CookieControl.load( cookies_config );
});