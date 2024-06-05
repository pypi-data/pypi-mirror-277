# *************************************************************** #
#               Copyright © Hero Imaging AB 2022. 				  #
#  					  All Rights Reserved.						  #
# *************************************************************** #

from heropytools import get_server_connection, HeroCommunication, NodeInputs, NodeOutputs, NodeStatus
import pathlib
from typing import Callable
import traceback


def secure_run(_file_: str, id: str, func: Callable[[NodeInputs, NodeOutputs, dict, dict, NodeStatus], None]):
    """
    Run the main script in the correct working folder. If an error is thrown it will set
    the fail flag to true. Rerunning without failing will reset it again to false
    :param id: ID string to get secure data.
    :param _file_: The path of the main file that should be in the top level folder
    :param func: The main function of the node.
    :return: nothing
    """

    # Connect to server
    with get_server_connection(str(pathlib.Path(_file_).parent) + "\\connection.cfg") as connection:

        # Get objects used for retrieving data and communicatin with Hero.
        hero_com = HeroCommunication(connection)
        specification = hero_com.get_simple_specification()
        input_connections = hero_com.get_input_connections_info()
        inputs = NodeInputs(hero_com, specification['inputs'], input_connections)
        outputs = NodeOutputs(hero_com, specification['outputs'])
        secure_data = hero_com.get_secure_data(id)
        status = NodeStatus(hero_com, specification['context'])

        try:
            # Run the main function.
            func(inputs, outputs, specification['settings'], secure_data, status)

            # Reset the fail-flag.
            hero_com.set_failed(False, "")
        except Exception as e:

            # If some exception was not caught, set the fail flag and error message from exception.
            hero_com.set_failed(True, str(e))
            traceback.print_exc()
