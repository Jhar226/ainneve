"""
Evennia settings file.

The available options are found in the default settings file found
here:

{settings_default}

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Dimensions RPG"
GAME_SLOGAN = "RPG Chat Website"

# Server ports. If enabled and marked as "visible", the port
# should be visible to the outside world on a production server.
# Note that there are many more options available beyond these.

IRC_ENABLED = True
IDLE_TIMEOUT = 86400
# Telnet ports. Visible.
TELNET_ENABLED = True
TELNET_PORTS = [6000]
# (proxy, internal). Only proxy should be visible.
WEBSERVER_ENABLED = True
WEBSERVER_PORTS = [(4001, 4002)]
# Telnet+SSL ports, for supporting clients. Visible.
SSL_ENABLED = False
SSL_PORTS = [4003]
# SSH client ports. Requires crypto lib. Visible.
SSH_ENABLED = False
SSH_PORTS = [4004]
# Websocket-client port. Visible.
WEBSOCKET_CLIENT_ENABLED = True
WEBSOCKET_CLIENT_PORT = 4005
# Internal Server-Portal port. Not visible.
AMP_PORT = 4006

######################################################################
# Django web features
######################################################################

# Allow multiple sessions per account; one character per session
MULTISESSION_MODE = 2
MAX_NR_CHARACTERS = 5
IRC_ENABLED = True

# Other defaults
PROTOTYPE_MODULES = ('world.content.prototypes_armor',
                     'world.content.prototypes_items',
                     'world.content.prototypes_misc',
                     'world.content.prototypes_mobs',
                     'world.content.prototypes_weapons'
                     )

BASE_BATCHPROCESS_PATHS = ['world.content']

# Evennia game index settings
GAME_INDEX_LISTING = {
    'game_status': 'pre-alpha',
    # Optional, comment out or remove if N/A
    'game_website': 'http://http://dimensions-rpg.xyz/',
    'short_description': 'Dimensions RPG is a combo MUD and Roleplaying Game Chat.',
    # Optional but highly recommended. Markdown is supported.
    'long_description': (
        "This is the roleplaying game to-be, Dimensions RPG Chat. It is forged by "
        "ColeArkenach; this is a combination of a MUD, MUSH, and RP Chat.\n\n"
        "It is roughly based on [The Fade Tabletop 2e](https://sites.google.com/site/tftsrd/home) "
        "table-top game system, is dark fantasy-themed, and features turn-based combat.\n\n"
        "It still a work in progress, and basic game systems are still being built. "
        "However, we welcome any who are interested in testing things out and giving "
        "feedback."
    ),
    'listing_contact': 'colearkenach@gmail.com',
    # At minimum, specify this or the web_client_url options. Both is fine, too.
    'telnet_hostname': 'http://dimensions-rpg.xyz/',
    'telnet_port': 6000,
    # At minimum, specify this or the telnet_* options. Both is fine, too.
    'web_client_url': 'http://dimensions-rpg.xyz/webclient',
}
######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print ("secret_settings.py file not found or failed to import.")
