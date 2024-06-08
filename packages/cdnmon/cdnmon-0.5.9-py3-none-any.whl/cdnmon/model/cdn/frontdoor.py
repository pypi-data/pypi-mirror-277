from cdnmon.model.cdn import BGPViewCIDR
from cdnmon.model.cdn import CNAMEPattern
from cdnmon.model.cdn import CommonCDN
from cdnmon.model.cdn import DomainOwnershipVerficationStatus
from cdnmon.model.cdn import DomainOwnershipVerification
from cdnmon.model.cdn import HTTPOwnershipVerification
from cdnmon.model.cdn import OwnershipVerification

CDN = CommonCDN(
    name="frontdoor",
    asn_patterns=["frontdoor", "azure", "microsoft"],
    cname_suffixes=[
        CNAMEPattern(suffix=".azurefd.net", pattern=r"${name}.azurefd.net"),
        CNAMEPattern(suffix=".azureedge.net", pattern=r"${name}.azureedge.net"),
        CNAMEPattern(suffix=".azurewebsites.net", pattern=r"${name}.azurewebsites.net"),
        CNAMEPattern(suffix="b-msedge.net"),
        CNAMEPattern(suffix="l-msedge.net"),
        CNAMEPattern(suffix="spo-msedge.net"),
        CNAMEPattern(suffix="msappproxy.net"),
        CNAMEPattern(suffix="t-msedge.net"),
        CNAMEPattern(suffix="trafficmanager.net"),
        CNAMEPattern(suffix="azurewebsites.windows.net"),
    ],
    cidr=BGPViewCIDR(["frontdoor", "azure", "microsoft"]),
    frontend_ownership_verification=OwnershipVerification(
        txt=DomainOwnershipVerification(
            status=DomainOwnershipVerficationStatus.REQUIRED,
            prefix="_dnsauth",
            pattern=r"[0-9a-z]{32}",
        ),
    ),
    backend_ownership_verification=OwnershipVerification(
        txt=DomainOwnershipVerification(status=DomainOwnershipVerficationStatus.NOT_REQUIRED),
        http=HTTPOwnershipVerification(status=DomainOwnershipVerficationStatus.NOT_REQUIRED),
    ),
)
