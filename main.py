# This program downloads all relevent Facebook traffic info as a csv file
# This program requires info from the Facebook Ads API: https://github.com/facebook/facebook-python-ads-sdk

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.business import Business

# Import th csv writer and the date/time function
import datetime

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

# Create a business object for the business account
business = Business('****')

# Get yesterday's date for the filename, and the csv data
yesterdaybad = datetime.datetime.now() - datetime.timedelta(days=1)
yesterdayslash = yesterdaybad.strftime('%m/%d/%Y')
yesterdayhyphen = yesterdaybad.strftime('%m-%d-%Y')

# Get all ad accounts on the business account
accounts = business.get_owned_ad_accounts(fields=[AdAccount.Field.id])


# Iterate through the adaccounts
for account in accounts:
    # Create an addaccount object from the adaccount id to make it possible to get insights
    tempaccount = AdAccount(account[AdAccount.Field.id])

    # Grab insight info for all ads in the adaccount
    ads = tempaccount.get_insights(params={'date_preset':'yesterday',
                                           'level':'ad'
                                          },
                                   fields=[AdsInsights.Field.account_id,
                                           AdsInsights.Field.account_name,
                                           AdsInsights.Field.ad_id,
                                           AdsInsights.Field.ad_name,
                                           AdsInsights.Field.adset_id,
                                           AdsInsights.Field.adset_name,
                                           AdsInsights.Field.campaign_id,
                                           AdsInsights.Field.campaign_name,
                                           AdsInsights.Field.cost_per_outbound_click,
                                           AdsInsights.Field.outbound_clicks,
                                           AdsInsights.Field.spend
                                          ]
    );

    # Iterate through all accounts in the business account
    for ad in ads:
        # Set default values in case the insight info is empty
        date = yesterdayslash
        accountid = ad[AdsInsights.Field.account_id]
        accountname = ""
        adid = ""
        adname = ""
        adsetid = ""
        adsetname = ""
        campaignid = ""
        campaignname = ""
        costperoutboundclick = ""
        outboundclicks = ""
        spend = ""

        # Set values from insight data
        if ('account_id' in ad) :
            accountid = ad[AdsInsights.Field.account_id]
        if ('account_name' in ad) :
            accountname = ad[AdsInsights.Field.account_name]
        if ('ad_id' in ad) :
            adid = ad[AdsInsights.Field.ad_id]
        if ('ad_name' in ad) :
            adname = ad[AdsInsights.Field.ad_name]
        if ('adset_id' in ad) :
            adsetid = ad[AdsInsights.Field.adset_id]
        if ('adset_name' in ad) :
            adsetname = ad[AdsInsights.Field.adset_name]
        if ('campaign_id' in ad) :
            campaignid = ad[AdsInsights.Field.campaign_id]
        if ('campaign_name' in ad) :
            campaignname = ad[AdsInsights.Field.campaign_name]
        if ('cost_per_outbound_click' in ad) : # This is stored strangely, takes a few steps to break through the layers
            costperoutboundclicklist = ad[AdsInsights.Field.cost_per_outbound_click]
            costperoutboundclickdict = costperoutboundclicklist[0]
            costperoutboundclick = costperoutboundclickdict.get('value')
        if ('outbound_clicks' in ad) : # This is stored strangely, takes a few steps to break through the layers
            outboundclickslist = ad[AdsInsights.Field.outbound_clicks]
            outboundclicksdict = outboundclickslist[0]
            outboundclicks = outboundclicksdict.get('value')
        if ('spend' in ad) :
            spend = ad[AdsInsights.Field.spend]

