import jeepney.io.blocking
import desktop_entry_lib
import pytest_subtests
from typing import Any
import jeepney
import pytest


class _FakeJeepneyAddress:
    def __init__(self, object_path: str, bus_name: str) -> None:
        pass

    def with_interface(self, name: str) -> str:
        return None


class _FakeJeepneyPropertiesNormal:
    def __init__(self, address: jeepney.DBusAddress) -> None:
        pass

    def get(self, name: str) -> tuple[str, str]:
        return ("Get", "Normal")


class _FakeJeepneyPropertiesError:
    def __init__(self, address: jeepney.DBusAddress) -> None:
        pass

    def get(self, name: str) -> tuple[str, str]:
        return ("Get", "Error")


class _FakeJeepneyFilter:
    def __enter__(self) -> None:
        return None

    def __exit__(self, exc_type: Any, exc_value: Any, exc_tb: Any) -> None:
        pass


class _FakeJeepneyConnection:
    def __init__(self) -> None:
        self.unique_name = "1.1"
        self._token_code = 0
        self._token = ""

    def filter(self, rule: jeepney.bus_messages.MatchRule) -> _FakeJeepneyFilter:
        return _FakeJeepneyFilter()

    def send_and_get_reply(self, args: tuple[str, str]) -> jeepney.Message:
        match args[0]:
            case "Get":
                match args[1]:
                    case "Normal":
                        header = jeepney.Header(None, jeepney.MessageType.method_return, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                        return jeepney.Message(header, (1,))
                    case "Error":
                        header = jeepney.Header(None, jeepney.MessageType.error, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                        return jeepney.Message(header, ("Error",))
            case "PrepareInstall":
                match args[1]:
                    case "NoIcon":
                        header = jeepney.Header(None, jeepney.MessageType.error, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                        return jeepney.Message(header, ("NoIcon",))
                    case "Canceled":
                        self._token_code = 1
                        header = jeepney.Header(None, jeepney.MessageType.method_return, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                        return jeepney.Message(header, None)
                    case "InvalidToken":
                        self._token = "invalid"
                        header = jeepney.Header(None, jeepney.MessageType.method_return, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                        return jeepney.Message(header, None)
                    case "Working":
                        header = jeepney.Header(None, jeepney.MessageType.method_return, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                        return jeepney.Message(header, None)
            case "Install":
                if args[1] == "invalid":
                    header = jeepney.Header(None, jeepney.MessageType.error, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                    return jeepney.Message(header, ("InvalidToken",))
                else:
                    header = jeepney.Header(None, jeepney.MessageType.method_return, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
                    return jeepney.Message(header, None)

    def recv_until_filtered(self, arg: None) -> jeepney.Message:
        header = jeepney.Header(None, jeepney.MessageType.method_return, jeepney.MessageFlag.allow_interactive_authorization, None, None, None, None)
        return jeepney.Message(header, (self._token_code, {"token": ("s", self._token), "name": ("s", "Test"), "icon": ("v", b"Test")}))

    def __enter__(self) -> "_FakeJeepneyConnection":
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, exc_tb: Any) -> None:
        pass


def _fake_new_method_call(interface: jeepney.DBusAddress, name: str, types: str, args: tuple) -> tuple[str, str]:
    return (name, args[0])


def test_install_with_portal(monkeypatch: pytest.MonkeyPatch, subtests: pytest_subtests.SubTests) -> None:
    monkeypatch.setattr(jeepney, "DBusAddress", _FakeJeepneyAddress)
    monkeypatch.setattr(jeepney.io.blocking, "open_dbus_connection", lambda: _FakeJeepneyConnection())
    monkeypatch.setattr(jeepney, "new_method_call", _fake_new_method_call)

    entry = desktop_entry_lib.DesktopEntry()

    with subtests.test("NotAvailable"):
        monkeypatch.setattr(jeepney, "Properties", _FakeJeepneyPropertiesError)
        with pytest.raises(desktop_entry_lib.InstallWithPortalsNotAvailable):
            entry.install_with_portal("NotAvailable", b"")

    monkeypatch.setattr(jeepney, "Properties", _FakeJeepneyPropertiesNormal)

    with subtests.test("NoIcon"):
        with pytest.raises(desktop_entry_lib.InstallWithPortalError) as exc_info:
            entry.install_with_portal("NoIcon", b"")
        assert exc_info.value.message == "NoIcon"

    with subtests.test("Canceled"):
        with pytest.raises(desktop_entry_lib.InstallWithPortalsCanceled) as exc_info:
            entry.install_with_portal("Canceled", b"")

    with subtests.test("InvalidToken"):
        with pytest.raises(desktop_entry_lib.InstallWithPortalError) as exc_info:
            entry.install_with_portal("InvalidToken", b"")
        assert exc_info.value.message == "InvalidToken"

    with subtests.test("Working"):
        result = entry.install_with_portal("Working", b"")
        assert result["Name"] == "Test"
        assert result["Icon"] == b"Test"
