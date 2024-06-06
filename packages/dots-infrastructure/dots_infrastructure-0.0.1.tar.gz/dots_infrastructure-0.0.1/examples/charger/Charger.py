# -*- coding: utf-8 -*-
"""
Created on 9/28/2020

This is a simple battery value federate that models the physics of an EV
battery as it is being charged. The federate receives a voltage signal
representing the voltage applied to the charging terminals of the battery
and based on its internally modeled SOC, calculates the current draw of
the battery and sends it back to the EV federate. Note that this SOC should
be considered the true SOC of the battery which may be different than the
SOC modeled by the charger. Each battery ceases charging when its SOC reaches 100%.

@author: Trevor Hardy
trevor.hardy@pnnl.gov
"""

import random
import matplotlib.pyplot as plt
import helics as h
import logging
import numpy as np

from dots_infrastructure import HelicsValueFederateExecutor, HelicsEsdlMessageFederateExecutor, HelicsMessageFederateInformation, PublicationDescription, HelicValueFederateInformation, SubscriptionDescription, generate_publications_from_value_descriptions, generate_subscriptions_from_value_descriptions, get_simulator_configuration_from_environment, get_single_param_with_name


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def charger_calculation(param_dict : dict):
    ev_current = get_single_param_with_name(param_dict, "EV_current")
    logger.info(f"Executing charger calculation with ev_current: {ev_current}")
    ret_val = {}
    ret_val["EV_voltage"] = ev_current * random.randint(1,3)
    return ret_val


if __name__ == "__main__":

    ##########  Registering  federate and configuring from JSON################
    simulator_configuration = get_simulator_configuration_from_environment()

    subscriptions_values = [
        SubscriptionDescription("PVInstallation", "EV_current", "A", h.HelicsDataType.DOUBLE)
    ]
    publictations_values = [
        PublicationDescription(True, "EConnection", "EV_voltage", "V", h.HelicsDataType.DOUBLE)
    ]

    esdl_message_federate = HelicsEsdlMessageFederateExecutor(simulator_configuration, HelicsMessageFederateInformation(60, False, False, True, h.HelicsLogLevel.DEBUG, 'esdl'))

    energy_system = esdl_message_federate.wait_for_esdl_file()
    logger.info("Received ESDL File continuing now with the simulation")

    subscriptions_values = generate_subscriptions_from_value_descriptions(subscriptions_values, simulator_configuration)
    publication_values = generate_publications_from_value_descriptions(publictations_values, simulator_configuration)

    federate_executor = HelicsValueFederateExecutor(simulator_configuration, HelicValueFederateInformation(60, False, True, True, h.HelicsLogLevel.DEBUG, "charger_calculation", subscriptions_values, publication_values, charger_calculation, energy_system))

    federate_executor.start_value_federate()