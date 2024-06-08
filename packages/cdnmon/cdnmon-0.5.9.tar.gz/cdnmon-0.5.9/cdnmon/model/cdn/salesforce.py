from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN

CDN = CommonCDN(
    name="salesforce",
    asn_patterns=["salesforce"],
    cname_suffixes=[
        CNAMEPattern(
            suffix=".live.siteforce.com",
            source="https://help.salesforce.com/s/articleView?id=sf.siteforce_domains.htm&type=5",
            is_root=True,
            is_leaf=False,
        ),
        CNAMEPattern(
            suffix=".edge2.salesforce.com",
            source="https://help.salesforce.com/s/articleView?id=sf.siteforce_domains.htm&type=5",
            is_leaf=True,
            is_root=False,
        ),
        CNAMEPattern(
            suffix=".r.salesforceliveagent.com",
            source="https://help.salesforce.com/s/articleView?id=sf.siteforce_domains.htm&type=5",
            is_root=False,
            is_leaf=True,
        ),
    ],
    cidr=BGPViewCIDR(query_term_list=["salesforce"]),
)
