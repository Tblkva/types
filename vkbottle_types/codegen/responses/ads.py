import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    AdsAccount,
    AdsAd,
    AdsAdLayout,
    AdsCampaign,
    AdsClient,
    AdsCreateAdStatus,
    AdsCreateCampaignStatus,
    AdsCreateClientsStatus,
    AdsDemoStats,
    AdsFloodStats,
    AdsLinkStatus,
    AdsPromotedPostReach,
    AdsRejectReason,
    AdsStats,
    AdsTargetGroup,
    AdsTargetPixelInfo,
    AdsTargSettings,
    AdsTargStats,
    AdsTargSuggestions,
    AdsTargSuggestionsCities,
    AdsTargSuggestionsRegions,
    AdsTargSuggestionsSchools,
    AdsUpdateAdsStatus,
    AdsUpdateClientsStatus,
    AdsUpdateOfficeUsersResult,
    AdsUsers,
)
from vkbottle_types.responses.base_response import BaseResponse


class AdsAddOfficeUsersResponse(BaseResponse):
    response: typing.List[bool] = Field()


class AdsCheckLinkResponse(BaseResponse):
    response: "AdsLinkStatus" = Field()


class AdsCreateAdsResponse(BaseResponse):
    response: typing.List[AdsCreateAdStatus] = Field()


class AdsCreateCampaignsResponse(BaseResponse):
    response: typing.List[AdsCreateCampaignStatus] = Field()


class AdsCreateClientsResponse(BaseResponse):
    response: typing.List[AdsCreateClientsStatus] = Field()


class AdsCreateLookalikeRequestResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsCreateTargetGroupResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsCreateTargetPixelResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsDeleteAdsResponse(BaseResponse):
    response: typing.List[int] = Field()


class AdsDeleteCampaignsResponse(BaseResponse):
    response: typing.List[int] = Field()


class AdsDeleteClientsResponse(BaseResponse):
    response: typing.List[int] = Field()


class AdsGetAccountsResponse(BaseResponse):
    response: typing.List[AdsAccount] = Field()


class AdsGetAdsLayoutResponse(BaseResponse):
    response: typing.List[AdsAdLayout] = Field()


class AdsGetAdsTargetingResponse(BaseResponse):
    response: typing.List[AdsTargSettings] = Field()


class AdsGetAdsResponse(BaseResponse):
    response: typing.List[AdsAd] = Field()


class AdsGetBudgetResponse(BaseResponse):
    response: str = Field()


class AdsGetCampaignsResponse(BaseResponse):
    response: typing.List[AdsCampaign] = Field()


class AdsGetCategoriesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsGetClientsResponse(BaseResponse):
    response: typing.List[AdsClient] = Field()


class AdsGetDemographicsResponse(BaseResponse):
    response: typing.List[AdsDemoStats] = Field()


class AdsGetFloodStatsResponse(BaseResponse):
    response: "AdsFloodStats" = Field()


class AdsGetLookalikeRequestsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsGetMusiciansResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsGetOfficeUsersResponse(BaseResponse):
    response: typing.List[AdsUsers] = Field()


class AdsGetPostsReachResponse(BaseResponse):
    response: typing.List[AdsPromotedPostReach] = Field()


class AdsGetRejectionReasonResponse(BaseResponse):
    response: "AdsRejectReason" = Field()


class AdsGetStatisticsResponse(BaseResponse):
    response: typing.List[AdsStats] = Field()


class AdsGetSuggestionsCitiesResponse(BaseResponse):
    response: typing.List[AdsTargSuggestionsCities] = Field()


class AdsGetSuggestionsRegionsResponse(BaseResponse):
    response: typing.List[AdsTargSuggestionsRegions] = Field()


class AdsGetSuggestionsResponse(BaseResponse):
    response: typing.List[AdsTargSuggestions] = Field()


class AdsGetSuggestionsSchoolsResponse(BaseResponse):
    response: typing.List[AdsTargSuggestionsSchools] = Field()


class AdsGetTargetGroupsResponse(BaseResponse):
    response: typing.List[AdsTargetGroup] = Field()


class AdsGetTargetPixelsResponse(BaseResponse):
    response: typing.List[AdsTargetPixelInfo] = Field()


class AdsGetTargetingStatsResponse(BaseResponse):
    response: "AdsTargStats" = Field()


class AdsGetUploadURLResponse(BaseResponse):
    response: str = Field()


class AdsGetVideoUploadURLResponse(BaseResponse):
    response: str = Field()


class AdsImportTargetContactsResponse(BaseResponse):
    response: int = Field()


class AdsRemoveOfficeUsersResponse(BaseResponse):
    response: typing.List[bool] = Field()


class AdsRemoveTargetContactsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsSaveLookalikeRequestResultResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsShareTargetGroupResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdsUpdateAdsResponse(BaseResponse):
    response: typing.List[AdsUpdateAdsStatus] = Field()


class AdsUpdateCampaignsResponse(BaseResponse):
    response: typing.List[AdsCreateCampaignStatus] = Field()


class AdsUpdateClientsResponse(BaseResponse):
    response: typing.List[AdsUpdateClientsStatus] = Field()


class AdsUpdateOfficeUsersResponse(BaseResponse):
    response: typing.List[AdsUpdateOfficeUsersResult] = Field()
