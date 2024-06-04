from collections.abc import MutableMapping

from mypy.options import Options
from mypy.plugin import Plugin as MypyPlugin

from .plugin import ExtendedMypyStubs


class PluginProvider:
    """
    This can be used to provide both a mypy plugin as well as a __version__ that changes
    when mypy needs to do a full restart.

    Given either the extended_mypy_django_plugin.plugin.ExtendedMypyStubs class or a subclass
    of that, usage is::

        from extended_mypy_django_plugin.plugin import ExtendedMypyStubs
        from extended_mypy_django_plugin.entry import PluginProvider

        plugin = PluginProvider(ExtendedMypyStubs, locals())
    """

    def __init__(
        self, plugin_cls: type[ExtendedMypyStubs], locals: MutableMapping[str, object], /
    ) -> None:
        self.locals = locals
        self.instance: ExtendedMypyStubs | None = None
        self.plugin_cls = plugin_cls
        self.previous_version: int | None = None

    def _change_version(self, instance: ExtendedMypyStubs) -> None:
        new_version = instance.determine_plugin_version(self.previous_version)
        self.previous_version = new_version
        self.locals["__version__"] = str(new_version)

    def __call__(self, version: str) -> type[MypyPlugin]:
        if self.instance is not None:
            self._change_version(self.instance)

            # Inside dmypy, don't create a new plugin
            return MypyPlugin

        provider = self
        major, minor, _ = version.split(".", 2)

        def __init__(instance: ExtendedMypyStubs, options: Options) -> None:
            super(instance.__class__, instance).__init__(
                options,
                mypy_version_tuple=(int(major), int(minor)),  # type: ignore[call-arg]
            )
            provider.instance = instance
            provider._change_version(instance)

        return type("Plugin", (provider.plugin_cls,), {"__init__": __init__})
