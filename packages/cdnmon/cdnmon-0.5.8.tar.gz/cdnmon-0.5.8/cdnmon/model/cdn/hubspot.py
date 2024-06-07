from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN

CDN = CommonCDN(
    name="hubspot",
    asn_patterns=["hubspot"],
    cname_suffixes=[
        CNAMEPattern(
            suffix="hubspot.net", source="https://www.hubspot.com/products/cms/cdn", is_root=True, is_leaf=False
        ),
        CNAMEPattern(suffix="group13.sites.hscoscdn10.net", is_root=False, is_leaf=True),
    ],
    cidr=BGPViewCIDR(query_term_list=["hubspot"]),
)
