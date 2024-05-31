from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class AIToolkitSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_aitoolkit.schema.package import m_package

        return m_package


package = AIToolkitSchemaPackageEntryPoint(
    name='AIToolkit',
    description='Describes the basic schemas for user-defined and ' \
        'ai toolkit notebooks using the new plugin mechanism.',
)
