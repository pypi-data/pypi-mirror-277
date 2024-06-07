#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

import allure
import pytest

from ibm_watson_machine_learning._wrappers import requests
from ibm_watson_machine_learning import APIClient
from ibm_watson_machine_learning.tests.foundation_models.tests_steps.data_storage import DataStorage
from ibm_watson_machine_learning.tests.foundation_models.tests_steps.prompt_template_steps import PromptTemplateSteps
from ibm_watson_machine_learning.tests.foundation_models.tests_steps.prompt_tuning_steps import PromptTuningSteps
from ibm_watson_machine_learning.tests.foundation_models.tests_steps.universal_steps import UniversalSteps
from ibm_watson_machine_learning.tests.utils import get_wml_credentials, get_cos_credentials, get_space_id
from ibm_watson_machine_learning.tests.utils.cleanup import space_cleanup
from ibm_watson_machine_learning.wml_client_error import ApiRequestFailure


def pytest_collection_modifyitems(items):
    """
    Because UnitTest do not like to cooperate with fixtures other than with param `autouse=False`
    there is a need to enumerate test BY MODEL and then ALPHANUMERICAL, which this function does.
    """
    for i, item in enumerate(items):
        if 'foundation_models' in item.nodeid:
            timeout = 35 * 60 if 'prompt_tuning' in item.name else 2 * 60  # 35 minutes for prompt tuning, 2 mins for other tests
            item.add_marker(pytest.mark.timeout(timeout))


class Credentials(dict):
    """
    Wrapper to search thought the credentials `keys` and search for `secret values`
    then replace them with `****` so they will not be shown in console log
    """

    def __repr__(self):
        secret_dict = {'apikey': '****'}
        tmp = dict(self)
        for el in secret_dict:
            if el in self:
                tmp[el] = secret_dict[el]
        return tmp.__repr__()


@pytest.fixture(scope="session", name="credentials")
def fixture_credentials():
    """
    Fixture responsible for getting credentials from `config.ini` file
        return:
            dict: Credentials for WML
    """
    credentials = get_wml_credentials()
    return Credentials(credentials)


@pytest.fixture(scope="session", name="project_id")
def fixture_project_id(create_project):
    project_id = create_project
    return project_id


@pytest.fixture(scope="session", name="set_project_id", autouse=False)
def fixture_set_project_id(api_client, project_id):
    api_client.set.default_project(project_id)


@pytest.fixture(scope="session", name="create_project", autouse=False)
def fixture_create_project(request, api_client, cos_credentials):
    from datetime import datetime
    """
           Fixture responsible for returning project ID
               Args:
                    request
                    api_client
                    cos_credentials
               return:
                   str: Project ID
           """
    crn_for_tests = cos_credentials['crn_for_tests']
    guid_for_tests = cos_credentials['guid_for_tests']
    crn_instance_for_tests = cos_credentials['crn_instance_for_tests']
    guid_instance_for_tests = cos_credentials['guid_instance_for_tests']
    creation_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = {
        "name": f"Auto-created Project - QA - {creation_time}",
        "generator": "wx-registration-sandbox",
        "description": "A project to try things in",
        "storage": {
            "type": "bmcos_object_storage",
            "resource_crn": crn_for_tests,
            "guid": guid_for_tests
        },
        "compute": [
            {
                "type": "machine_learning",
                "name": "ML for WML-WX Cracow team",
                "crn": crn_instance_for_tests,
                "guid": guid_instance_for_tests
            }
        ],
        "type": "wx",
        "public": False
    }
    response = requests.post(
        url=f"{api_client.PLATFORM_URL}/transactional/v2/projects",
        json=data,
        headers=api_client._get_headers()
    )
    project_location = response.text
    project_embedded = project_location.split("/")[-1].replace('"}', '')
    DataStorage.project_id = project_embedded
    api_client.set.default_project(project_embedded)

    print(f'Created Project ID: {project_embedded}')

    yield project_embedded

    response = requests.delete(
        url=f"{api_client.PLATFORM_URL}/transactional/v2/projects/{project_embedded}",
        headers=api_client._get_headers()
    )
    print(response)


@pytest.fixture(scope="session", name="space_id")
def fixture_space_id(credentials):
    """
    Fixture responsible for returning space ID
        Args:
            credentials:

        return:
            str: Space ID
    """
    space_id = credentials.get('space_id')
    return space_id


@pytest.fixture(scope="session", name="api_client")
def fixture_api_client(credentials):
    """
    Fixture responsible for setup API Client with given credentials.
        Args:
            credentials:
            project_id:
        return:
            APIClient Object:
    """
    api_client = APIClient(credentials)

    return api_client


@pytest.fixture(scope="session", name="cos_credentials")
def fixture_cos_credentials():
    """
    Fixture responsible for getting COS credentials
        return:
            dict: COS Credentials
    """
    cos_credentials = get_cos_credentials()
    return Credentials(cos_credentials)


@pytest.fixture(scope="session", name="cos_endpoint")
def fixture_cos_endpoint(cos_credentials):
    """
    Fixture responsible for getting COS endpoint.
        Args:
            cos_credentials:

        return:
            str: COS Endpoint
    """
    cos_endpoint = cos_credentials['endpoint_url']
    return cos_endpoint


@pytest.fixture(scope="session", name="cos_resource_instance_id")
def fixture_cos_resource_instance_id(cos_credentials):
    """
    Fixture responsible for getting COS Instance ID from cos_credentials part of config.ini file
        Args:
            cos_credentials:

        return:
            str: COS resource instance ID
    """
    cos_resource_instance_id = cos_credentials['resource_instance_id']
    return cos_resource_instance_id


@pytest.fixture(name="space_cleanup")
def fixture_space_clean_up(data_storage, request):
    space_checked = False
    while not space_checked:
        space_cleanup(data_storage.api_client,
                      get_space_id(data_storage.api_client, data_storage.space_name,
                                   cos_resource_instance_id=data_storage.cos_resource_instance_id),
                      days_old=7)
        space_id = get_space_id(data_storage.api_client, data_storage.space_name,
                                cos_resource_instance_id=data_storage.cos_resource_instance_id)
        try:
            assert space_id is not None, "space_id is None"
            data_storage.api_client.spaces.get_details(space_id)

            space_checked = True
        except AssertionError or ApiRequestFailure:
            space_checked = False

    data_storage.space_id = space_id

    if data_storage.SPACE_ONLY:
        data_storage.api_client.set.default_space(data_storage.space_id)
    else:
        data_storage.api_client.set.default_project(data_storage.project_id)


@allure.title("Data Storage Class - initialization")
@pytest.fixture(scope="function", name="data_storage")
def fixture_data_storage_init(api_client, prompt_mgr, project_id):
    """
    Every step will be using the same object of DataStorage
    """
    data_storage = DataStorage()
    data_storage.api_client = api_client
    data_storage.prompt_mgr = prompt_mgr
    return data_storage


@allure.title("Universal Steps - initialization")
@pytest.fixture(scope="function", name="universal_step")
def fixture_universal_step_init(data_storage):
    return UniversalSteps(data_storage)


@allure.title("Prompt Tuning Steps - initialization")
@pytest.fixture(scope="function", name="prompt_tuning_step")
def fixture_prompt_tuning_step_init(data_storage):
    return PromptTuningSteps(data_storage)


@allure.title("Prompt Template Steps - initialization")
@pytest.fixture(scope="function", name="prompt_template_step")
def fixture_prompt_template_step_init(data_storage):
    return PromptTemplateSteps(data_storage)
