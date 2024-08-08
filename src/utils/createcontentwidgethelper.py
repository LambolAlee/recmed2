from pathlib import Path


def createContentWidgetPlugin(pluginName: str, namespace: str='global') -> bool:
    cwpath = Path(__file__).parent.parent / 'contentwidget' / 'plugins'
    if pluginName == '': 
        return False

    if namespace == 'global':
        pluginDir = cwpath / pluginName
    else:
        pluginDir = cwpath / namespace / pluginName

    if pluginDir.exists(): 
        return False

    # Plugin directory
    # | _ui
    # |  | __init__.py
    # |  | viewport.py
    # | __init__.py
    # | plugin.py
    # | datapipe.py
    # | viewport.py
    # | mapping.json
    # | metadata.json

    pluginDir.mkdir(parents=True)
    (pluginDir / '_ui').mkdir()
    (pluginDir / '_ui' / '__init__.py').touch()
    (pluginDir / '_ui' / 'viewport.py').touch()
    (pluginDir / '__init__.py').touch()
    (pluginDir / 'plugin.py').touch()
    (pluginDir / 'datapipe.py').touch()
    (pluginDir / 'viewport.py').touch()
    (pluginDir / 'mapping.json').touch()
    (pluginDir / 'metadata.json').touch()

    return True


if __name__ == '__main__':
    from sys import argv
    print(createContentWidgetPlugin(*argv[1:]))
