from PyQt6.QtCore import QCoreApplication


def get_language_names() -> dict[str, str]:
    return {
        "en": QCoreApplication.translate("Language", "English"),
        "de": QCoreApplication.translate("Language", "German"),
        "nl": QCoreApplication.translate("Language", "Dutch"),
        "pl": QCoreApplication.translate("Language", "Polish"),
        "ru": QCoreApplication.translate("Language", "Russian"),
        "da": QCoreApplication.translate("Language", "Danish"),
    }
