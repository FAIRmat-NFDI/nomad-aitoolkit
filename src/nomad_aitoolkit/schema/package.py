from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

import xml

from nomad.config import config
from nomad.datamodel.data import (
    ArchiveSection,
    EntryDataCategory,
    Schema,
)
from nomad.datamodel.data import Author as NomadAuthor
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import (
    Category,
    Datetime,
    MEnum,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

configuration = config.get_plugin_entry_point('nomad_aitoolkit.schema:package')


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


m_package = SchemaPackage(name='AI Toolkit Notebook schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(label='Tools', categories=[EntryDataCategory])


class Method(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Name'
        ),
        description='For testing subsection quantity.',
    )


class System(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Name'
        ),
        description='For testing subsection quantity.',
    )


class Author(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    first_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Name'
        ),
        description='For testing subsection quantity.',
    )

    last_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Name'
        ),
        description='For testing subsection quantity.',
    )


class Reference(ArchiveSection):
    m_def = Section(a_eln=ELNAnnotation(overview=True))

    kind = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
            props=dict(
                suggestions=[
                    'article url',
                    'article doi',
                    'repository',
                    'video',
                    'docker image',
                    'documentation',
                    'hub',
                    'other',
                ]
            ),
        ),
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Name'
        ),
        description='For testing subsection quantity.',
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='For testing enum field.',
    )

    uri = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity, label='URI'),
        description='For testing subsection quantity.',
    )

    version = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity, label='Name'
        ),
        description='For testing subsection quantity.',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class AIToolkitNotebook(Schema):
    m_def = Section(
        label='AI Toolkit Notebook',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(
            properties=dict(
                # order=[
                #     'name',
                #     'description',
                #     'date',
                #     'authors',
                #     'category',
                #     'methods',
                #     'systems',
                #     'platform',
                #     'references',
                # ]
            )
        ),
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        label='Name/Title',
        description='For testing string field.',
    )

    description = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
        description='For testing enum field.',
    )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
        description='For testing datetime field.',
    )

    authors = SubSection(section=Author, repeats=True)

    category = Quantity(
        label='User defined category',
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
            props=dict(
                suggestions=[
                    'advanced tutorial',
                    'beginner tutorial',
                    'intermediate tutorial',
                    'query tutorial',
                    'thermal transport',
                ]
            ),
        ),
    )

    methods = SubSection(section=Method, repeats=True)

    systems = SubSection(section=System, repeats=True)

    platform = Quantity(
        type=MEnum(['Python', 'Julia', 'R', 'other']),
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.AutocompleteEditQuantity,
        ),
    )

    references = SubSection(section=Reference, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if self.name:
            archive.metadata.entry_name = self.name

        if self.description:
            if self.description.startswith('<'):
                comment = remove_tags(self.description)
            else:
                comment = self.description

            archive.metadata.comment = comment

        logger.info('AIToolkitNotebook.normalize', parameter=configuration.parameter)

        # This is a workaround to use Author field on the gui
        if self.authors:
            archive.metadata.entry_coauthors = [
                NomadAuthor(**author.m_to_dict()) for author in self.authors
            ]

        if self.references:
            for reference in self.references:
                if reference.kind != 'hub':
                    continue
                print(reference.uri)
                archive.metadata.default_launch_url = reference.uri
                break


m_package.__init_metainfo__()
