import random
import helics as h
import logging
from dots_infrastructure.DotsInfrastructure import PublicationDescription, HelicsSimulationExecutor, HelicsCalculationInformation, generate_publications_from_value_descriptions, get_simulator_configuration_from_environment


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def battery_calculation(param_dict : dict):
    ret_val = {}
    ret_val["EV_current"] = 0.25 * random.randint(1,3)
    return ret_val


if __name__ == "__main__":

    simulator_configuration = get_simulator_configuration_from_environment()

    publictations_values = [
        PublicationDescription(True, "PVInstallation", "EV_current", "A", h.HelicsDataType.DOUBLE)
    ]

    subscriptions_values = []
    publication_values = generate_publications_from_value_descriptions(publictations_values, simulator_configuration)
    calculation_information = HelicsCalculationInformation(30, False, False, True, h.HelicsLogLevel.DEBUG, "battery_calculation", subscriptions_values, publication_values, battery_calculation)
    helics_simulation_executor = HelicsSimulationExecutor()
    helics_simulation_executor.add_calculation(calculation_information)
    helics_simulation_executor.start_simulation()