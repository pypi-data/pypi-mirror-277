def initialize_collectors(
  config_file: str | None = None,
  collector_names: str | None = None,
  create_service_collectors: bool = True,
  deduplicate_collectors: bool = True,
) -> CollectorSet():
  """Initializes collectors either from file or CLI.

  Args:
    config_file: Path to file with collector definitions.
    collector_names: Comma-separated string with collector names.

  Returns:
    All found collectors.

  Raises:
    ValueError: When neither collector_file nor collector_names were provided.
  """
  if config_file:
    collectors_registry = Registry.from_collector_definitions(config_file)
    return collectors_registry.find_collectors(
      collector_names='all', deduplicate=False, service_collectors=False
    )
  if collector_names:
    collectors_registry = Registry.from_collector_definitions()
    if not (
      active_collectors := collectors_registry.find_collectors(
        collector_names,
        deduplicate=deduplicate_collectors,
        service_collectors=create_service_collectors,
      )
    ):
      logging.warning(
        'Failed to get "%s" collectors, using default ones', collector_names
      )
      active_collectors = collectors_registry.default_collectors
  return active_collectors
  raise ValueError('Neither collector_file nor collector_names were provided')


def test_initialize_collectors_from_config_file_loads_data_from_file(tmp_path):
  config_file = tmp_path / 'config.yaml'
  config = [
    {'name': 'performance', 'query': 'SELECT customer.id FROM customer'}
  ]
  with open(config_file, mode='w', encoding='utf-8') as f:
    yaml.dump(config, f)
  collectors = collector_registry.initialize_collectors(config_file=config_file)
  assert {
    'performance',
  } == {c.name for c in collectors}


def test_initialize_collectors_from_collector_names_returns_correct_collectors(
  tmp_path,
):
  collectors = collector_registry.initialize_collectors(
    collector_names='performance', create_service_collectors=False
  )
  assert {
    'performance',
  } == {c.name for c in collectors}


def test_initialize_collectors_from_collector_names_returns_correct_collectors(
  tmp_path,
):
  collectors = collector_registry.initialize_collectors(
    collector_names='performance', create_service_collectors=True
  )
  assert {'performance', 'mapping'} == {c.name for c in collectors}
