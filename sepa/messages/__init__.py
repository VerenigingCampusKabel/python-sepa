import pkgutil
import inspect

sepa_messages = {}

# Loop over all message groups
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    if '.' in name:
        continue

    # Load message group module
    module = loader.find_module(name).load_module(name)

    # Export messages from message group
    sepa_messages[name] = module.sepa_messages
