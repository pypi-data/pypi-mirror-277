from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN

CDN = CommonCDN(
    name="cdn77",
    asn_patterns=["cdn77"],
    cname_suffixes=[
        CNAMEPattern(
            suffix=".rsc.cdn77.org",
            source="https://client.cdn77.com/support/knowledgebase/cdn-resource/configuring-cname",
        ),
        CNAMEPattern(suffix=".cdn77.net"),
    ],
    cidr=BGPViewCIDR(["cdn77"]),
)
