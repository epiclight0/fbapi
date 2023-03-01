from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

app_id = 'XXX'
app_secret = 'XXX'
access_token = 'XXX'


def fb_connector(my_app_id: str, my_app_secret: str, my_access_token: str):
    """
    Start connection to FB API
    :param my_app_id:
    :param my_app_secret:
    :param my_access_token:
    """
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

fb_connector(app_id,app_secret,access_token)
my_account = AdAccount('act_102237272813610')
campaigns = my_account.get_campaigns()
print(campaigns)
