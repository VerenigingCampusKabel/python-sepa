import pkgutil
import inspect

sepa_messages = {}

# Loop over modules in this directory
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    # Load a module
    module = loader.find_module(name).load_module(name)

    # Export the module
    sepa_messages[name] = module
