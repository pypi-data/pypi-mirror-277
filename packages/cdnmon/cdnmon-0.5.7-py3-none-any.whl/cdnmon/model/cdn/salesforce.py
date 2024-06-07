from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN

CDN = CommonCDN(
    name="salesforce",
    asn_patterns=["salesforce"],
    cname_suffixes=[
        CNAMEPattern(
            suffix="siteforce.com", source="https://help.salesforce.com/s/articleView?id=sf.siteforce_domains.htm&type=5"
        ),
        CNAMEPattern(
            suffix="edge2.salesforce.com",
            source="https://help.salesforce.com/s/articleView?id=sf.siteforce_domains.htm&type=5",
        ),
        CNAMEPattern(
            suffix="salesforceliveagent.com",
            source="https://help.salesforce.com/s/articleView?id=sf.siteforce_domains.htm&type=5",
        ),
    ],
    cidr=BGPViewCIDR(query_term_list=["salesforce"]),
)
