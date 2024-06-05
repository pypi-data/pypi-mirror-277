from typing import List
import logging
import subprocess
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinitionName

def _get_multivalued_slots(schema: SchemaDefinition) -> List[SlotDefinitionName]:
    return [s.name for s in schema.slots.values() if s.multivalued]


def bulkload_file(f,
                  format='csv',
                  base_url=None,
                  core=None,
                  schema: SchemaDefinition = None,
                  processor: str = None,
                  ):
    """
    Bulkload a file using solr bulkload API

    :param f:
    :param format:
    :param base_url:
    :param core:
    :param schema:
    :param processor: Processor argument to pass when bulk loading to Solr
    :return:
    """
    mvslots = _get_multivalued_slots(schema)
    print(f'MV = {mvslots}')
    separator = '%09'
    internal_separator = '%7C'
    parts = [f'f.{s}.split=true&f.{s}.separator={internal_separator}' for s in mvslots]
    url = f'{base_url}/{core}/update?{"&".join(parts)}&commit=true&separator={separator}'
    if (processor is not None):
        url = f'{url}&processor={processor}'
    if format == 'csv':
        ct = 'application/csv'
    elif format == 'json':
        ct = 'application/json'
    else:
        raise Exception(f'Unknown format {format}')
    command = ['curl', url, '-T', f'{f}', '-X', 'POST', '-H', f'Content-type:{ct}']
    print(command)
    subprocess.run(command)

