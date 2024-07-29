import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.translations import *  # noqa: F401,F403


class TranslationsCategory(BaseCategory):
    async def translate(
        self,
        texts: typing.List[str],
        translation_language: str,
        **kwargs: typing.Any,
    ) -> typing.Dict[str, typing.Any]:
        """Method `translations.translate()`

        :param texts:
        :param translation_language:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("translations.translate", params)
        model = TranslationsTranslateResponse
        return model(**response).response


__all__ = ("TranslationsCategory",)
