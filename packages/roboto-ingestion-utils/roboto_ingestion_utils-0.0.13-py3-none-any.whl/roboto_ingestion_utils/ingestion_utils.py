import os
import tempfile
from typing import Tuple
import pathlib
import logging

from roboto.association import (
    Association,
    AssociationType,
)

from roboto.domain import actions, datasets, files, topics
from roboto.exceptions import RobotoConflictException

from roboto.env import default_env

from roboto.http import (
    HttpClient,
    SigV4AuthDecorator,
)


def setup_output_folder_structure(
        file_path: str,
        input_dir: str
) -> Tuple[str, str]:
    """
    This function sets up the output folder structure for the visualization assets.

    Args:
    - file_path: The path to the input file.
    - input_dir: The input directory.

    Returns:
    - output_folder_path: The path to the output folder.
    - temp_dir: The path to the temporary directory.
    """
    relative_folder_path_of_file = os.path.split(file_path.split(input_dir)[1])[0]

    file_name = os.path.split(file_path)[1]

    output_folder_name_mcap, extension = os.path.splitext(file_name)

    relative_folder_path_of_file = relative_folder_path_of_file.lstrip("/")
    temp_dir = str(tempfile.TemporaryDirectory().name)

    output_folder_path = os.path.join(
        temp_dir,
        ".VISUALIZATION_ASSETS",
        relative_folder_path_of_file,
        output_folder_name_mcap,
    )

    print(f"Output folder path: {output_folder_path}")
    os.makedirs(output_folder_path, exist_ok=True)

    return output_folder_path, temp_dir


def create_topic(
    topic_association: Association,
    org_id: str,
    msgtype: str,
    topic_name: str,
    topic_delegate,
    message_path_requests,
    nr_msgs: int,
    first_timestamp: int,
    last_timestamp: int,
) -> topics.Topic:
    """
    Create a new topic or get an existing one.

    Args:
        topic_association: Topic association object.
        org_id: Organization ID.
        msgtype: Message type.
        topic_name: Topic name.
        topic_delegate: Topic delegate object.
        message_path_requests: Message path requests.
        nr_msgs: Number of messages.
        first_timestamp: First timestamp of the messages.
        last_timestamp: Last timestamp of the messages.

    Returns:
        topics.Topic: The created or retrieved topic.
    """
    try:
        topic = topics.Topic.create(
            request=topics.CreateTopicRequest(
                association=topic_association,
                org_id=org_id,
                schema_name=msgtype,
                schema_checksum="1",  # TODO: Get schema checksum
                topic_name=topic_name,
                message_count=nr_msgs,
                start_time=first_timestamp,
                end_time=last_timestamp,
                message_paths=message_path_requests,
            ),
            topic_delegate=topic_delegate,
        )
    except RobotoConflictException:
        topic = topics.Topic.from_name_and_association(
            topic_name=topic_name,
            association=topic_association,
            org_id=org_id,
            topic_delegate=topic_delegate,
        )
        print(f"Topic already exists: {topic_name}")

    return topic


def set_default_representation(
    topic: topics.Topic,
        topic_name: str,
        file_id: str,
        org_id: str
) -> None:
    """
    Set the default representation for a topic.

    Args:
        topic: Topic object.
        topic_name: Topic name.
        file_id: File ID of the MCAP file.
        org_id: Organization ID.
    """
    try:
        topic.set_default_representation(
            request=topics.SetDefaultRepresentationRequest(
                association=Association(
                    association_type=AssociationType.File,
                    association_id=file_id
                ),
                org_id=org_id,
                storage_format=topics.RepresentationStorageFormat.MCAP,
                version=1,
            )
        )
    except RobotoConflictException:
        print(
            f"Conflict exception while setting default representation for topic: {topic_name}"
        )


def setup_env():
    """
    Set up the environment for the action.

    Returns:
    - A tuple containing the organization ID, input directory, output directory, topic delegate, and dataset.
    """
    roboto_service_url = default_env.roboto_service_url
    org_id = default_env.org_id
    invocation_id = default_env.invocation_id
    input_dir = default_env.input_dir
    output_dir = default_env.output_dir

    http_client = HttpClient(default_auth=SigV4AuthDecorator("execute-api"))

    topic_delegate = topics.TopicHttpDelegate(
        roboto_service_base_url=roboto_service_url, http_client=http_client
    )

    invocation = actions.Invocation.from_id(
        invocation_id,
        invocation_delegate=actions.InvocationHttpDelegate(
            roboto_service_base_url=roboto_service_url, http_client=http_client
        ),
    )
    dataset = datasets.Dataset.from_id(
        invocation.data_source.data_source_id,
        datasets.DatasetHttpDelegate(
            roboto_service_base_url=roboto_service_url, http_client=http_client
        ),
        files.FileClientDelegate(
            roboto_service_base_url=roboto_service_url, http_client=http_client
        )
    )

    return org_id, input_dir, output_dir, topic_delegate, dataset


def setup_logger(logger_name: str, print_to_console: bool = True, print_to_file: bool = False):
    """
    Set up the logger for the action.

    Returns:
    - None
    """

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Remove any existing handlers
    logger.handlers = []

    if print_to_file:
        output_dir = default_env.output_dir if default_env.output_dir else pathlib.Path.cwd()
        invocation_id = default_env.invocation_id if default_env.invocation_id else "local"

        log_file = (
                pathlib.Path(output_dir)
                / ".metrics"
                / f"process_timing_{invocation_id}.csv"
        )
        log_file.parent.mkdir(parents=True, exist_ok=True)
        # File handler
        file_handler = logging.FileHandler(str(log_file))
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    if print_to_console:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger
