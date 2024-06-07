from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN

CDN = CommonCDN(
    name="lumen",
    asn_patterns=["lumen"],
    cname_suffixes=[
        CNAMEPattern(
            suffix=".c.section.io",
            source="https://www.lumen.com/help/en-us/cdn/application-delivery-solutions/set-up-your-domain/set-up-dns.html",
            is_root=True,
            is_leaf=False,
        ),
        CNAMEPattern(
            suffix=".e.ns1.sectionedge.com",
            is_root=False,
            is_leaf=False,
        ),
        CNAMEPattern(
            suffix=".ep.section.io",
            is_root=False,
            is_leaf=True,
        ),
    ],
    cidr=BGPViewCIDR(["lumen"]),
)
