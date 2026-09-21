"""Repository: third-party ad hosts blocked in every test.

The site's ads are not part of the system under test, and Google's "vignette"
interstitial hijacks navigation clicks (URL becomes /#google_vignette).
"""

AD_HOSTS = [
    "googlesyndication.com",
    "doubleclick.net",
    "googleadservices.com",
    "adservice.google.com",
    "fundingchoicesmessages.google.com",
]
