from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN

CDN = CommonCDN(
    name="adobe",
    asn_patterns=["adobe"],
    cname_suffixes=[
        CNAMEPattern(
            suffix="cdn.adobeaemcloud.com",
            source="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/configure-dns-settings",
        ),
    ],
    cidr=BGPViewCIDR(["adobe"]),
)
