from typing import Union, Optional, Literal, TypedDict, cast
import urllib.parse
import subprocess
import tempfile
import secrets
import locale
import shlex
import os
import re


__version__ = "5.0"
"The version"


def _assert_func(expression: bool) -> None:
    """
    The assert keyword is not available when running Python in Optimized Mode.
    This function is a drop-in replacement.
    See https://docs.python.org/3/using/cmdline.html?highlight=pythonoptimize#cmdoption-O
    """
    if not expression:
        raise AssertionError()


def _compare_dict(first_dict: dict, second_dict: dict) -> bool:
    "Compare 2 dicts"
    if len(first_dict) != len(second_dict):
        return False

    for key, value in first_dict.items():
        if key not in second_dict:
            return False

        if value != second_dict[key]:
            return False

    return True


def _strip_list(old_list: list[str]) -> list[str]:
    "Run .strip() on all Elements of a list"
    new_list = []
    for i in old_list:
        new_list.append(i.strip())
    return new_list


def _parse_desktop_sections(content: str) -> dict[str, dict[str, str]]:
    "Parses a .desktop file"
    sections: dict[str, dict[str, str]] = {}
    current_section = None
    for line in content.splitlines():
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]
            sections[current_section] = {}
        elif current_section is None:
            continue
        else:
            try:
                key, value = line.split("=", 1)
                sections[current_section][key] = value
            except ValueError:
                continue
    return sections


def _string_to_bool(string: Optional[str]) -> Optional[bool]:
    "Converts a String to a Boolean"
    if string is None:
        return None
    elif string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False
    else:
        return None


def _is_flatpak() -> bool:
    "Checks if the lib is running inside a Flatpak"
    return os.path.isfile("/.flatpak-info")


def _remove_list_duplicates(old_list: list) -> list:
    "Removes all duplicates from a list"
    new_list = []
    for i in old_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def _parse_exec(command: Optional[str], entry: Optional["DesktopEntry"], file_list: Optional[list[str]], url_list: Optional[list[str]]) -> list[str]:
    if command is None:
        return []

    if file_list is None:
        file_list = []

    if url_list is None:
        url_list = []

    cmdline: list[str] = []
    for part in shlex.split(command):
        match part:
            case "%f":
                if len(file_list) != 0:
                    cmdline.append(file_list[0])
                    continue

                for current_url in url_list:
                    result = urllib.parse.urlparse(current_url)
                    if result.scheme == "file":
                        cmdline.append(f"{result.netloc}{result.path}")
                        break
            case "%F":
                cmdline += file_list
                for current_url in url_list:
                    result = urllib.parse.urlparse(current_url)
                    if result.scheme == "file":
                        cmdline.append(f"{result.netloc}{result.path}")
            case "%u":
                if len(url_list) != 0:
                    cmdline.append(url_list[0])
                elif len(file_list) != 0:
                    cmdline.append("file://" + os.path.abspath(file_list[0]))
            case "%U":
                cmdline += url_list
                for current_file in file_list:
                    cmdline.append("file://" + os.path.abspath(current_file))
            case "%i":
                if entry is not None and entry.Icon is not None:
                    cmdline += ["--icon", entry.Icon]
            case "%c":
                if entry is not None:
                    cmdline.append(entry.Name.get_translated_text())
            case "%k":
                if entry is not None and entry.file_path is not None and entry.file_path != "":
                    cmdline.append(entry.file_path)
                else:
                    cmdline.append("")
            case _:
                cmdline.append(part)

    return cmdline


def get_xdg_data_dirs() -> list[str]:
    """
    Get all XDG DATA DIRS

    :return: The list of XDG data Dirs
    """
    try:
        data_dirs = os.getenv("XDG_DATA_DIRS").removesuffix(":").split(":")
    except AttributeError:
        data_dirs = [os.path.expanduser("~/.local/share"), "/usr/share"]

    if _is_flatpak():
        # When running as Flatpak, these are are not in $XDG_DATA_DIRS, even if the Flatpak have Permission to access these directories
        data_dirs += ["/run/host/usr/share", "/var/lib/flatpak/exports/share", os.path.expanduser("~/.local/share"), os.path.expanduser("~/.local/share/flatpak/exports/share")]

    return _remove_list_duplicates(data_dirs)


def _get_icon_size_dirs(path: str) -> list[str]:
    size_list: list[int] = []
    for i in os.listdir(path):
        if not os.path.isdir(os.path.join(path, i)) or not re.match(r"\d+x\d+", i):
            continue

        size_list.append(int(re.search(r"^\d+", i).group()))

    size_list.sort(reverse=True)

    dir_list: list[str] = []
    for size in size_list:
        dir_list.append(f"{size}x{size}")

    return dir_list


def get_icon_path(icon_name: str) -> Optional[str]:
    """
    Get the path of a Icon

    :param icon_name: The name of the Icon as found in the desktop entry
    :return: The full path to the Icon. none if the Icon was not found.
    """
    for data_dir in get_xdg_data_dirs():
        scalable_dir = os.path.join(data_dir, "icons", "hicolor", "scalable")
        if os.path.isdir(scalable_dir):
            for directory in os.listdir(scalable_dir):
                icon_path = os.path.join(scalable_dir, directory, icon_name + ".svg")
                if os.path.isfile(icon_path):
                    return icon_path
        if os.path.isdir(os.path.join(data_dir, "icons", "hicolor")):
            for size in _get_icon_size_dirs(os.path.join(data_dir, "icons", "hicolor")):
                size_dir = os.path.join(data_dir, "icons", "hicolor", size)
                for directory in os.listdir(size_dir):
                    icon_path = os.path.join(size_dir, directory, icon_name + ".png")
                    if os.path.isfile(icon_path):
                        return icon_path
        if os.path.isdir(os.path.join(data_dir, "pixmaps")):
            if os.path.isfile(os.path.join(data_dir, "pixmaps", icon_name + ".png")):
                return os.path.join(data_dir, "pixmaps", icon_name + ".png")

    return None


def is_action_identifier_valid(identifier: str) -> bool:
    """
    Checks if a Action identifier is valid

    :param identifier: The Identifier
    :return: If the identifier is valid
    """
    return re.match("^([0-9]|[a-z]|[A-Z]|-)+$", identifier) is not None


def is_custom_key_name_valid(name: str) -> bool:
    """
    Checks if the given name can be used for a custom key

    :param identifier: The name
    :return: If the name can be used
    """
    return re.match(r"^X-([0-9]|[a-z]|[A-Z]|-)+(\[([0-9]|[a-z]|[A-Z]|-)+\])?$", name) is not None


class ValidationMessageDict(TypedDict):
    "Defines the return type for :func:`~desktop_entry_lib.__init__.DesktopEntry.get_validation_messages`"
    Error: list[str]
    FutureError: list[str]
    Warning: list[str]
    Hint: list[str]


class InstallWithPortalResponse(TypedDict):
    "Defines the return type for :func:`~desktop_entry_lib.__init__.DesktopEntry.install_with_portal`"
    Name: str
    Icon: bytes


class InstallWithPortalsNotAvailable (Exception):
    "Raised by :func:`~desktop_entry_lib.__init__.DesktopEntry.install_with_portal` when the DynamicLauncher portal is not available "
    def __init__(self) -> None:
        super().__init__("The DynamicLauncher portal is not available")


class InstallWithPortalError(Exception):
    "Raised by :func:`~desktop_entry_lib.__init__.DesktopEntry.install_with_portal` when an error occures"
    def __init__(self, message: str) -> None:
        super().__init__(message)

        self.message = message


class InstallWithPortalsCanceled(Exception):
    "Raised by :func:`~desktop_entry_lib.__init__.DesktopEntry.install_with_portal` when the User canceled the Installation"
    def __init__(self) -> None:
        super().__init__("The User canceled the Installation")


class InvalidDesktopEntry(ValueError):
    "This Exception is raised, when a invalid Desktop Entry is loaded"
    def __init__(self) -> None:
        super().__init__("Invalid Desktop Entry")


class TranslatableKey:
    "Represents a Key in a Desktop Entry, that can be translated into different languages"
    def __init__(self) -> None:
        self.default_text: str = ""
        "The untranslated text"

        self.translations: dict[str, str] = {}
        "The translations"

    def get_translated_text(self) -> str:
        """
        Returns the text for the current system language

        :return: The text
        """
        current_lang = locale.getlocale()[0]
        if current_lang is None:
            return self.default_text
        elif current_lang in self.translations:
            return self.translations[current_lang]
        elif current_lang.split("_")[0] in self.translations:
            return self.translations[current_lang.split("_")[0]]
        else:
            return self.default_text

    def load_section(self, section: dict[str, str], search_key: str) -> None:
        "Loads a section from a Desktop Entry. Only for internal use."
        self.clear()

        for key, value in section.items():
            if not key.startswith(search_key):
                continue

            if search_key == key:
                self.default_text = value
            else:
                try:
                    lang = re.search(r"(?<=\[).+(?=\]$)", key).group()
                    self.translations[lang] = value
                except AttributeError:
                    continue

    def get_text(self, entry_key: str) -> str:
        "Returns the text for saving a Desktop Entry. only for internal use."
        if self.default_text == "":
            return ""

        text = f"{entry_key}={self.default_text}\n"
        for key, value in self.translations.items():
            text += f"{entry_key}[{key}]={value}\n"
        return text

    def clear(self) -> None:
        "Clear"
        self.default_text = ""
        self.translations.clear()

    def __repr__(self) -> str:
        return f"<TranslatableKey default_text='{self.default_text}'>"

    def __str__(self) -> str:
        return self.default_text

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, TranslatableKey):
            return False

        return self.default_text == obj.default_text and _compare_dict(self.translations, obj.translations)


class TranslatableListKey:
    "Represents a List in a Desktop Entry, that can be translated into different languages"
    def __init__(self) -> None:
        self.default_list: list[str] = []
        "The unstranslated list"

        self.translations: dict[str, list[str]] = {}
        "The translated lists"

    def load_section(self, section: dict[str, str], search_key: str) -> None:
        "Loads a section from a Desktop Entry. Only for internal use."
        self.clear()

        for key, value in section.items():
            if not key.startswith(search_key):
                continue

            if search_key == key:
                self.default_list = value.removesuffix(";").split(";")
            else:
                try:
                    lang = re.search(r"(?<=\[).+(?=\]$)", key).group()
                    self.translations[lang] = value.removesuffix(";").split(";")
                except AttributeError:
                    continue

    def get_text(self, entry_key: str) -> str:
        "Returns the text for saving a Desktop Entry. only for internal use."
        if len(self.default_list) == 0:
            return ""

        text = f"{entry_key}={';'.join(self.default_list)};\n"
        for key, value in self.translations.items():
            text += f"{entry_key}[{key}]={';'.join(value)};\n"
        return text

    def clear(self) -> None:
        "Clear"
        self.default_list.clear()
        self.translations.clear()

    def __repr__(self) -> str:
        return f"<TranslatableListKey default_list={str(self.default_list)}>"

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, TranslatableListKey):
            return False

        return self.default_list == obj.default_list and _compare_dict(self.translations, obj.translations)


class DesktopAction:
    "Represents a Action in a Desktop Entry"
    def __init__(self) -> None:
        self.Name: TranslatableKey = TranslatableKey()
        "The Name Key"

        self.Icon: Optional[str] = None
        "The Icon Key"

        self.Exec: Optional[str] = None
        "The Exec Key"

    @classmethod
    def from_dict(cls, action_section: dict[str, str]):
        "Load the Action from a Dict. Onyl used internaly."
        action = cls()

        action.Name.load_section(action_section, "Name")
        action.Icon = action_section.get("Icon", None)
        action.Exec = action_section.get("Exec", None)

        return action

    def get_text(self) -> str:
        "Converts the Action into a String"
        text = self.Name.get_text("Name")

        if self.Icon is not None:
            text += f"Icon={self.Icon}\n"

        if self.Exec is not None:
            text += f"Exec={self.Exec}"

        return text

    def get_icon_path(self) -> Optional[str]:
        """
        Returns full Path to the Icon

        :return: The full Path or None, if the Icon can't be found
        """
        if self.Icon is None:
            return None
        else:
            return get_icon_path(self.Icon)

    def get_command(self, file_list: Optional[list[str]] = None, url_list: Optional[list[str]] = None) -> list[str]:
        """
        Returns the command to start this action.
        Returns an empty list if the :attr:`~desktop_entry_lib.__init__.DesktopAction.Exec` Key is not set.
        Take a look at :doc:`the tutorial </tutorial/start_program>` for more information.

        :param file_list: A list of local files
        :param url_list: A list of URLs
        :return: The command
        """
        return _parse_exec(self.Exec, None, file_list, url_list)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, DesktopAction):
            return False

        return self.Name == obj.Name and self.Icon == obj.Icon and self.Exec == obj.Exec


class DesktopEntry:
    "Represents a Desktop Entry"
    def __init__(self) -> None:
        self.Type: Literal["Application", "Link", "Directory"] = "Application"
        "The Type Key"

        self.Version: Optional[Literal["1.0", "1.1", "1.2", "1.3", "1.4", "1.5"]] = None
        "The Version Key"

        self.Name: TranslatableKey = TranslatableKey()
        "The Name Key"

        self.GenericName: TranslatableKey = TranslatableKey()
        "The GenericName Key"

        self.NoDisplay: Optional[bool] = None
        "The NoDisplay Key"

        self.Comment: TranslatableKey = TranslatableKey()
        "The Comment Key"

        self.Icon: Optional[str] = None
        "The Icon Key"

        self.Hidden: Optional[bool] = None
        "The Hidden Key"

        self.OnlyShowIn: list[str] = []
        "The OnlyShowIn Key"

        self.NotShowIn: list[str] = []
        "The NotShowIn Key"

        self.DBusActivatable: Optional[bool] = None
        "The DBusActivatable Key"

        self.TryExec: Optional[str] = None
        "The TryExec Key"

        self.Exec: Optional[str] = None
        "The Exec Key"

        self.Path: Optional[str] = None
        "The Path Key"

        self.Terminal: Optional[bool] = None
        "The Terminal Key"

        self.MimeType: list[str] = []
        "The MimeType Key"

        self.Categories: list[str] = []
        "The Categories Key"

        self.Implements: list[str] = []
        "The Implements Key"

        self.Keywords: TranslatableListKey = TranslatableListKey()
        "The Keywords Key"

        self.StartupNotify: Optional[bool] = None
        "The StartupNotify Key"

        self.StartupWMClass: Optional[str] = None
        "The StartupWMClass Key"

        self.URL: Optional[str] = None
        "The URL Key"

        self.PrefersNonDefaultGPU: Optional[bool] = None
        "The PrefersNonDefaultGPU Key"

        self.SingleMainWindow: Optional[bool] = None
        "The SingleMainWindow Key"

        self.Actions: dict[str, DesktopAction] = {}
        "The Actions"

        self.CustomKeys: dict[str, str] = {}
        "The Keys starting with X-"

        self.file_path: Optional[str] = None
        "The path to the .desktop file"

        self.desktop_id: Optional[str] = None
        "The ID of the .desktop file"

        self.leading_comment: Optional[str] = None
        """If you set this, the given Comment will be added at the top of the Desktop Entry.
        You can use it for stuff like 'Created with foo'."""

    def _execute_validate_command(self) -> subprocess.CompletedProcess:
        "Executes desktop-file-validate and returns the result"
        file_handle, temp_path = tempfile.mkstemp(suffix=".desktop")
        try:
            os.close(file_handle)
            self.write_file(temp_path)
            return subprocess.run(["desktop-file-validate", temp_path], capture_output=True)
        finally:
            os.remove(temp_path)

    def is_valid(self) -> bool:
        """
        Returns, if the Desktop Entry is valid. desktop-file-validate needs to be installed.

        :return: If the entry is valid
        """
        return self._execute_validate_command().returncode == 0

    def get_validation_messages(self) -> ValidationMessageDict:
        """
        Returns all messages from desktop-file-validate

        :return: A dict which contains the validation messages
        """
        message_dict: ValidationMessageDict = {"Error": [], "FutureError": [], "Warning": [], "Hint": []}
        for i in self._execute_validate_command().stdout.decode("utf-8").splitlines():
            file_name, message_type, message = _strip_list(i.split(":", 2))
            if message_type == "error":
                if message.startswith("(will be fatal in the future): "):
                    message_dict["FutureError"].append(message.removeprefix("(will be fatal in the future): "))
                else:
                    message_dict["Error"].append(message)
            elif message_type == "warning":
                message_dict["Warning"].append(message)
            elif message_type == "hint":
                message_dict["Hint"].append(message)
        return message_dict

    def should_show(self) -> bool:
        "Returns if Desktop Entry should be showed"
        if self.Hidden:
            return False

        try:
            # According to the documentation, this is colon-separated list, in most cases it is just a single string
            desktop_list = os.getenv("XDG_CURRENT_DESKTOP").removesuffix(":").split(";")
        except AttributeError:
            return True

        for i in self.NotShowIn:
            if i in desktop_list:
                return False

        if len(self.OnlyShowIn) != 0:
            for i in self.OnlyShowIn:
                if i in desktop_list:
                    return True
            return False
        else:
            return True

    def should_show_in_menu(self) -> bool:
        "Returns if a dektop entry should be displayed in the menu"
        return not self.NoDisplay and self.should_show()

    def get_icon_path(self) -> Optional[str]:
        "Returns the full path to the Icon"
        if self.Icon is None:
            return None
        else:
            return get_icon_path(self.Icon)

    def get_working_directory(self) -> str:
        """
        Returns the working directory for this program.
        When the :attr:`~desktop_entry_lib.__init__.DesktopEntry.Path` Key is set, the value of this Key is returned.
        If not, the Home directory is returned.

        :return: The working directory
        """
        if self.Path is not None:
            return self.Path
        else:
            return os.path.expanduser("~")

    def get_command(self, file_list: Optional[list[str]] = None, url_list: Optional[list[str]] = None) -> list[str]:
        """
        Returns the command to start this program.
        Returns an empty list if the :attr:`~desktop_entry_lib.__init__.DesktopEntry.Exec` Key is not set.
        Take a look at :doc:`the tutorial </tutorial/start_program>` for more information.

        :param file_list: A list of local files
        :param url_list: A list of URLs
        :return: The command
        """
        return _parse_exec(self.Exec, self, file_list, url_list)

    def is_empty(self) -> bool:
        "Checks if the Desktop Entry is empty"
        return self == DesktopEntry()

    def get_text(self) -> str:
        "Returns the content of the Desktop Entry"
        text = ""

        if self.leading_comment is not None:
            text += f"# {self.leading_comment}\n"

        text += "[Desktop Entry]\n"
        text += f"Type={self.Type}\n"

        if self.Version is not None:
            text += f"Version={self.Version}\n"

        text += self.Name.get_text("Name")
        text += self.GenericName.get_text("GenericName")

        if self.NoDisplay is not None:
            text += f"NoDisplay={str(self.NoDisplay).lower()}\n"

        text += self.Comment.get_text("Comment")

        if self.Icon is not None:
            text += f"Icon={self.Icon}\n"

        if self.Hidden is not None:
            text += f"Hidden={str(self.Hidden).lower()}\n"

        if len(self.OnlyShowIn) != 0:
            text += "OnlyShowIn=" + ";".join(self.OnlyShowIn) + ";\n"

        if len(self.NotShowIn) != 0:
            text += "NotShowIn=" + ";".join(self.NotShowIn) + ";\n"

        if self.DBusActivatable is not None:
            text += f"DBusActivatable={str(self.DBusActivatable).lower()}\n"

        if self.TryExec is not None:
            text += f"TryExec={self.TryExec}\n"

        if self.Exec is not None:
            text += f"Exec={self.Exec}\n"

        if self.Path is not None:
            text += f"Path={self.Path}\n"

        if self.Terminal is not None:
            text += f"Terminal={str(self.Terminal).lower()}\n"

        if len(self.MimeType) != 0:
            text += "MimeType=" + ";".join(self.MimeType) + ";\n"

        if len(self.Categories) != 0:
            text += "Categories=" + ";".join(self.Categories) + ";\n"

        if len(self.Implements) != 0:
            text += "Implements=" + ";".join(self.Implements) + ";\n"

        text += self.Keywords.get_text("Keywords")

        if self.StartupNotify is not None:
            text += f"StartupNotify={str(self.StartupNotify).lower()}\n"

        if self.StartupWMClass is not None:
            text += f"StartupWMClass={self.StartupWMClass}\n"

        if self.URL is not None:
            text += f"URL={self.URL}\n"

        if self.PrefersNonDefaultGPU is not None:
            text += f"PrefersNonDefaultGPU={str(self.PrefersNonDefaultGPU).lower()}\n"

        if self.SingleMainWindow is not None:
            text += f"SingleMainWindow={str(self.SingleMainWindow).lower()}\n"

        if len(self.Actions) != 0:
            text += "Actions=" + ";".join(self.Actions.keys()) + ";\n"

        for key, value in self.CustomKeys.items():
            if key.startswith("X-"):
                text += f"{key}={value}\n"

        for key, action in self.Actions.items():
            text += f"\n[Desktop Action {key}]\n"
            text += action.get_text() + "\n"

        return text

    def write_file(self, path: Union[str, os.PathLike]) -> None:
        "Writes a .desktop file"
        try:
            os.makedirs(os.path.dirname(path))
        except (FileExistsError, FileNotFoundError):
            pass

        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(self.get_text())

    def install_with_portal(self, window_dentifier: str, icon: bytes, *, editable_name: bool = True, editable_icon: bool = False) -> InstallWithPortalResponse:
        """
        Installs the entry using the `DynamicLauncher Portal <https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.DynamicLauncher.html>`_.
        Take a look at :doc:`the tutorial </tutorial/install_with_portal>` for more information.

        :param window_dentifier: The `Window Identifier <https://flatpak.github.io/xdg-desktop-portal/docs/window-identifiers.html>`_
        :param icon: The Icon
        :param editable_name: If the User should be able to edit the Name, defaults to True
        :param editable_icon: If the User should be able to edit the Icon, defaults to False
        :raises InstallWithPortalsNotAvailable: The DynamicLauncher portal is not available
        :raises InstallWithPortalError: A error occured
        :raises InstallWithPortalsCanceled: The user canceled the Installation
        :raises ModuleNotFoundError: jeepney is not installed
        :return: The name and the icon of the shortcut
        """
        import jeepney.io.blocking
        import jeepney

        portal = jeepney.DBusAddress(
            object_path="/org/freedesktop/portal/desktop",
            bus_name="org.freedesktop.portal.Desktop",
        )
        dynamic_launcher = portal.with_interface("org.freedesktop.portal.DynamicLauncher")

        with jeepney.io.blocking.open_dbus_connection() as conn:
            version_reply = conn.send_and_get_reply(jeepney.Properties(dynamic_launcher).get("version"))
            if version_reply.header.message_type == jeepney.MessageType.error:
                raise InstallWithPortalsNotAvailable()

            token = f"desktop_entry_lib_install_{secrets.token_hex()}"
            sender_name = conn.unique_name[1:].replace(".", "_")
            handle = f"/org/freedesktop/portal/desktop/request/{sender_name}/{token}"

            response_rule = jeepney.bus_messages.MatchRule(
                type="signal", interface="org.freedesktop.portal.Request", path=handle
            )

            with conn.filter(response_rule) as responses:
                prepare_req = jeepney.new_method_call(dynamic_launcher, "PrepareInstall", "ssva{sv}", (
                    window_dentifier, self.Name.default_text, ("(sv)", ("bytes", ("ay", list(icon)))), {"handle_token": ("s", token), "editable_name": ("b", editable_name), "editable_icon": ("b", editable_icon)}
                ))

                prepare_resp = conn.send_and_get_reply(prepare_req)
                if prepare_resp.header.message_type == jeepney.MessageType.error:
                    raise InstallWithPortalError(prepare_resp.body[0])

                token_resp = conn.recv_until_filtered(responses)
                if token_resp.body[0] != 0:
                    raise InstallWithPortalsCanceled()

                response_dict: InstallWithPortalResponse = {
                    "Name": token_resp.body[1]["name"][1],
                    "Icon": token_resp.body[1]["icon"][1]
                }
                token = token_resp.body[1]["token"][1]

            install_req = jeepney.new_method_call(dynamic_launcher, "Install", "sssa{sv}", (
                token, f"{self.desktop_id}.desktop", self.get_text(), {}
            ))

            install_resp = conn.send_and_get_reply(install_req)
            if install_resp.header.message_type == jeepney.MessageType.error:
                raise InstallWithPortalError(install_resp.body[0])

            return response_dict

    @classmethod
    def from_string(cls, text: str) -> "DesktopEntry":
        "Loads the content of a .desktop file from a string"
        entry = cls()

        sections = _parse_desktop_sections(text)

        if "Desktop Entry" not in sections:
            raise InvalidDesktopEntry()

        entry.Type = cast(Literal['Application', 'Link', 'Directory'], sections["Desktop Entry"].get("Type", "Application"))
        entry.Version = cast(Optional[Literal['1.0', '1.1', '1.2', '1.3', '1.4', '1.5']], sections["Desktop Entry"].get("Version", None))
        entry.Name.load_section(sections["Desktop Entry"], "Name")
        entry.GenericName.load_section(sections["Desktop Entry"], "GenericName")
        entry.NoDisplay = _string_to_bool(sections["Desktop Entry"].get("NoDisplay", None))
        entry.Comment.load_section(sections["Desktop Entry"], "Comment")
        entry.Icon = sections["Desktop Entry"].get("Icon", None)
        entry.Hidden = _string_to_bool(sections["Desktop Entry"].get("Hidden", None))

        if "OnlyShowIn" in sections["Desktop Entry"]:
            entry.OnlyShowIn = sections["Desktop Entry"]["OnlyShowIn"].removesuffix(";").split(";")

        if "NotShowIn" in sections["Desktop Entry"]:
            entry.NotShowIn = sections["Desktop Entry"]["NotShowIn"].removesuffix(";").split(";")

        entry.DBusActivatable = _string_to_bool(sections["Desktop Entry"].get("DBusActivatable", None))
        entry.TryExec = sections["Desktop Entry"].get("TryExec", None)
        entry.Exec = sections["Desktop Entry"].get("Exec", None)
        entry.Path = sections["Desktop Entry"].get("Path", None)
        entry.Terminal = _string_to_bool(sections["Desktop Entry"].get("Terminal", None))

        if "MimeType" in sections["Desktop Entry"]:
            entry.MimeType = sections["Desktop Entry"]["MimeType"].removesuffix(";").split(";")

        if "Categories" in sections["Desktop Entry"]:
            entry.Categories = sections["Desktop Entry"]["Categories"].removesuffix(";").split(";")

        if "Implements" in sections["Desktop Entry"]:
            entry.Implements = sections["Desktop Entry"]["Implements"].removesuffix(";").split(";")

        entry.Keywords.load_section(sections["Desktop Entry"], "Keywords")
        entry.StartupNotify = _string_to_bool(sections["Desktop Entry"].get("StartupNotify", None))
        entry.StartupWMClass = sections["Desktop Entry"].get("StartupWMClass", None)
        entry.URL = sections["Desktop Entry"].get("URL", None)
        entry.PrefersNonDefaultGPU = _string_to_bool(sections["Desktop Entry"].get("PrefersNonDefaultGPU", None))
        entry.SingleMainWindow = _string_to_bool(sections["Desktop Entry"].get("SingleMainWindow", None))

        if "Actions" in sections["Desktop Entry"]:
            for i in sections["Desktop Entry"]["Actions"].removesuffix(";").split(";"):
                entry.Actions[i] = DesktopAction.from_dict(sections[f"Desktop Action {i}"])

        for key, value in sections["Desktop Entry"].items():
            if key.startswith("X-"):
                entry.CustomKeys[key] = value

        return entry

    @classmethod
    def from_file(cls, path: Union[str, os.PathLike]) -> "DesktopEntry":
        "Returns a Desktop Entry from the given file"
        with open(path, "r", encoding="utf-8", newline="\n") as f:
            entry = cls.from_string(f.read())
            entry.file_path = os.path.abspath(path)
            entry.desktop_id = os.path.basename(path).removesuffix(".desktop")
            return entry

    @classmethod
    def from_id(cls, desktop_id: str) -> Optional["DesktopEntry"]:
        "Returns a Desktop Entry from the given id"
        for i in get_xdg_data_dirs():
            entry_path = os.path.join(i, "applications", desktop_id + ".desktop")
            if os.path.isfile(entry_path):
                return cls.from_file(entry_path)
        return None

    def __repr__(self) -> str:
        return f"<DesktopEntry Name='{self.Name.default_text}'>"

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, DesktopEntry):
            return False

        try:
            _assert_func(self.Type == obj.Type)
            _assert_func(self.Version == obj.Version)
            _assert_func(self.Name == obj.Name)
            _assert_func(self.GenericName == obj.GenericName)
            _assert_func(self.NoDisplay == obj.NoDisplay)
            _assert_func(self.Comment == obj.Comment)
            _assert_func(self.Icon == obj.Icon)
            _assert_func(self.Hidden == obj.Hidden)
            _assert_func(self.OnlyShowIn == obj.OnlyShowIn)
            _assert_func(self.NotShowIn == obj.NotShowIn)
            _assert_func(self.DBusActivatable == obj.DBusActivatable)
            _assert_func(self.TryExec == obj.TryExec)
            _assert_func(self.Exec == obj.Exec)
            _assert_func(self.Path == obj.Path)
            _assert_func(self.Terminal == obj.Terminal)
            _assert_func(self.MimeType == obj.MimeType)
            _assert_func(self.Categories == obj.Categories)
            _assert_func(self.Implements == obj.Implements)
            _assert_func(self.Keywords == obj.Keywords)
            _assert_func(self.StartupNotify == obj.StartupNotify)
            _assert_func(self.StartupWMClass == obj.StartupWMClass)
            _assert_func(self.URL == obj.URL)
            _assert_func(self.PrefersNonDefaultGPU == obj.PrefersNonDefaultGPU)
            _assert_func(self.SingleMainWindow == obj.SingleMainWindow)
            _assert_func(_compare_dict(self.Actions, obj.Actions))
            _assert_func(_compare_dict(self.CustomKeys, obj.CustomKeys))
            return True
        except AssertionError:
            return False

    @staticmethod
    def get_keywords() -> list[str]:
        """
        Returns the list of Keywords of a Desktop Entry

        :return: The list of Keys
        """
        return [
            "Type",
            "Version",
            "Name",
            "GenericName",
            "NoDisplay",
            "Comment",
            "Icon",
            "Hidden",
            "OnlyShowIn",
            "NotShowIn",
            "DBusActivatable",
            "TryExec",
            "Exec",
            "Path",
            "Terminal",
            "MimeType",
            "Categories",
            "Implements",
            "Keywords",
            "StartupNotify",
            "URL",
            "PrefersNonDefaultGPU",
            "SingleMainWindow"
        ]


class DesktopEntryCollection:
    "Represents a Collection of multiple Desktop Entries"
    def __init__(self) -> None:
        self.desktop_entries: dict[str, DesktopEntry] = {}
        "The desktop entries"

    def load_file(self, path: Union[str, os.PathLike]) -> None:
        """
        Loads the given desktop entry file and adds it to the collection

        :param path: The path to the desktop entry
        """
        entry = DesktopEntry.from_file(path)
        self.desktop_entries[os.path.basename(path).removesuffix(".desktop")] = entry

    def load_directory(self, path: Union[str, os.PathLike]) -> bool:
        """
        Loads all desktop entries from the given directory

        :param path: The directory
        :return: True if all desktop entries could be loaded, False if some couldn't be loaded
        """
        no_error = True
        for i in os.listdir(path):
            if i.endswith(".desktop"):
                try:
                    self.load_file(os.path.join(path, i))
                except Exception:
                    no_error = False
        return no_error

    def load_menu(self) -> bool:
        """
        Loads all desktop entries from the menu

        :return: True if all desktop entries could be loaded, False if some couldn't be loaded
        """
        no_error = True
        for i in get_xdg_data_dirs():
            menu_dir = os.path.join(i, "applications")
            if os.path.isdir(menu_dir):
                if not self.load_directory(menu_dir):
                    no_error = False
        return no_error

    def load_desktop(self) -> bool:
        """
        Loads all desktop entries files from the Desktop

        :return: True if all desktop entries could be loaded, False if some couldn't be loaded
        """
        desktop_path = subprocess.check_output(["xdg-user-dir", "DESKTOP"]).decode("utf-8").strip()
        if os.path.isdir(desktop_path):
            return self.load_directory(desktop_path)
        return False

    def load_autostart(self) -> bool:
        """
        Loads all autostart entries

        :return: True if all desktop entries could be loaded, False if some couldn't be loaded
        """
        no_error = True
        for i in ("/run/host/etc/xdg/autostart" if _is_flatpak() else "/etc/xdg/autostart", os.path.expanduser("~/.config/autostart/")):
            if os.path.isdir(i):
                if not self.load_directory(i):
                    no_error = False
        return no_error

    def get_entries_by_category(self, category: str) -> list[DesktopEntry]:
        """
        Returns a list of all desktop entries that have the given category

        :param category: The category
        :return: The list of desktop entries
        """
        entry_list: list[DesktopEntry] = []
        for i in self.desktop_entries.values():
            if category in i.Categories:
                entry_list.append(i)
        return entry_list

    def get_entries_by_mime_type(self, mime_type: str) -> list[DesktopEntry]:
        """
        Returns a list of all desktop entries that can open the given MimeType

        :param mime_type: The MimeType
        :return: The list of desktop entries
        """
        entry_list: list[DesktopEntry] = []
        for i in self.desktop_entries.values():
            if mime_type in i.MimeType:
                entry_list.append(i)
        return entry_list

    def get_visible_entries(self) -> list[DesktopEntry]:
        """
        Returns a list of all desktop entries that should be shown to the User

        :return: The list of desktop entries
        """
        entry_list: list[DesktopEntry] = []
        for i in self.desktop_entries.values():
            if i.should_show():
                entry_list.append(i)
        return entry_list

    def get_menu_entries(self) -> list[DesktopEntry]:
        """
        Returns a list of all desktop entries that should be shown in the Menu

        :return: The list of desktop entries
        """
        entry_list: list[DesktopEntry] = []
        for i in self.desktop_entries.values():
            if i.should_show_in_menu():
                entry_list.append(i)
        return entry_list

    def get_entry_by_name(self, name: str, include_translations: bool = True) -> Optional[DesktopEntry]:
        """
        Returns the entry with the given Name. Returns None if no Entry exists with this Name.

        :param name: The Name
        :param include_translations: Search also the translations
        :return: The Entry
        """
        for i in self.desktop_entries.values():
            if i.Name.default_text == name or (include_translations and name in i.Name.translations.values()):
                return i
        return None

    def __len__(self) -> int:
        return len(self.desktop_entries)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, DesktopEntryCollection):
            return False

        return _compare_dict(self.desktop_entries, obj.desktop_entries)

    def __getitem__(self, name: str) -> DesktopEntry:
        return self.desktop_entries[name]

    def __setitem__(self, key: str, value: DesktopEntry) -> None:
        if not isinstance(key, str):
            raise ValueError("Key must be a string")

        if not isinstance(value, DesktopEntry):
            raise ValueError("Value must be a DesktopEntry")

        self.desktop_entries[key] = value

    def __contains__(self, name: str) -> bool:
        return name in self.desktop_entries
