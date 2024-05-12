from substrateinterface import SubstrateInterface


def get_substrate_interface_connection():
    return SubstrateInterface(url='ws://127.0.0.1:9944')
