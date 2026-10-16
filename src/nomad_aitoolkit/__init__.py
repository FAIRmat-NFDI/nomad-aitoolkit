from nomad.config.models.plugins import SchemaPackageEntryPoint


class AIToolkitSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_aitoolkit.schema import m_package  # noqa: PLC0415

        return m_package


aitoolkit = AIToolkitSchemaPackageEntryPoint(
    name='AIToolkit',
    description='Describes the basic schemas for AI Toolkit notebooks.',
)
