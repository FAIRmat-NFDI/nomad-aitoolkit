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


# TODO:
# - [ ] full name for filtering
# - [ ] exclude attributes
# - [ ] author list for display
# - [ ] URLAction implementation
# - [ ] app options
# - [ ] notebook parser
# - [x] remove html tags from comments

def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

m_package = SchemaPackage(name='AI Toolkit Notebook Schema')

# m_category = Category(name='Notebooks')
# m_package = Package(name='Jupyter Notebook Schema')
# m_package = Package(name='AI Toolkit Notebook Schema')


class ToolsCategory(EntryDataCategory):
    m_def = Category(label='Tools', categories=[EntryDataCategory])


# TODO: hide BaseNotebook schema because it is only an bastract class
# TODO: owerwrite label of the date (date > Date)


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


class BaseNotebook(Schema):
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

    # methods = Quantity(
    #     label='User defined tags',
    #     type=str,
    #     shape=['*'],
    #     description='Add a tag that can be used for search.',
    #     a_eln=dict(component='StringEditQuantity'),
    # )

    # methods = Quantity(
    #     label='User defined tags',
    #     type=str,
    #     shape=['*'],
    #     a_eln=ELNAnnotation(
    #         component=ELNComponentEnum.EnumEditQuantity,
    #         props=dict(
    #             suggestions=[
    #                 'Atomic features',
    #                 'Attentive response map',
    #                 'Bagging classifier',
    #                 'Bayesian deep learning',
    #                 'Classification',
    #                 'Clustering',
    #                 'Compressed sensing',
    #                 'Convolutional neural networks',
    #                 'Cumulative entropy',
    #                 'DBSCAN',
    #                 'Decision tree',
    #                 'Deep neural networks',
    #                 'DenPeak',
    #                 'Dimensionality reduction',
    #                 'Features selection',
    #                 'Fingerprint',
    #                 'Gaussian approximation potentials (GAP)',
    #                 'Gaussian mixture',
    #                 'Gaussian process regression',
    #                 'HDBSCAN',
    #                 'Hierarchical clustering',
    #                 'Information theory',
    #                 'Kernel ridge regression',
    #                 'LASSO',
    #                 'Linear least-squares regression',
    #                 'MBTR',
    #                 'MDS',
    #                 'Mutual information',
    #                 'Neural networks',
    #                 'PCA',
    #                 'PCA-UMAP-MDS',
    #                 'Random forest',
    #                 'Regression',
    #                 'SISSO',
    #                 'SOAP',
    #                 'SVM',
    #                 'Sensitivy Analysis',
    #                 'Similarity search',
    #                 'Subgroup discovery',
    #                 'Supervised learning',
    #                 'Symbolic regression',
    #                 'Symmetry functions',
    #                 'TCMI',
    #                 'UMAP',
    #                 'Unsupervised learning',
    #                 'k-means',
    #                 'n-gram',
    #                 't-SNE',
    #             ]
    #         ),
    #     ),
    # )

    def normalize(self, archive, logger) -> None:
        super().normalize(archive, logger)

        if self.name:
            archive.metadata.entry_name = self.name

        if self.description:
            archive.metadata.comment = remove_tags(self.description)

        # TODO: fix this workaround
#         if self.methods:
#             if not archive.results:
#                 archive.results = Results(eln=ELN())
#             if not archive.results.eln:
#                 archive.results.eln = ELN()
#
#             archive.results.eln.tags = self.methods




class Notebook(BaseNotebook):
    m_def = Section(
        label='Notebook',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(
            properties=dict(
                order=[
                    'name',
                    'description',
                    'category',
                    'methods',
                    'notebook_file',
                    'config_files',
                    'northtool',
                ]
            )
        ),
    )

    notebook_file = Quantity(
        type=str,
        description="""A reference to an uploaded .ipynb file.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.FileEditQuantity, label='Path of notebook'
        ),
    )

    config_files = Quantity(
        type=str,
        shape=['*'],
        description="""A reference to a configuration file(s) which used to determine the environment.
        (https://repo2docker.readthedocs.io/en/latest/config_files.html)
        """,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.FileEditQuantity, label='Configuration file(s)'
        ),
    )

    northtool = Quantity(
        label='User defined category',
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
            props=dict(
                suggestions=[
                    'jupyter',
                ]
            ),
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)


class AIToolkitNotebook(BaseNotebook):
    m_def = Section(
        label='AI Toolkit Notebook',
        categories=[ToolsCategory],
        a_eln=ELNAnnotation(
            properties=dict(
                order=[
                    'name',
                    'description',
                    'authors',
                    'date',
                    'category',
                    'methods',
                    'systems',
                    'platform',
                    'notebook_path',
                    'references',
                ]
            )
        ),
    )



    # authors = Quantity(
    #     type=Author,
    #     shape=['*'],
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.AuthorEditQuantity),
    # )

    authors = SubSection(section=Author, repeats=True)

    # authors_list = Quantity(
    #     type=str
    # )

    date = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateTimeEditQuantity),
        description='For testing datetime field.',
    )

    platform = Quantity(
        type=MEnum(['Python', 'Julia', 'R', 'other']),
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.AutocompleteEditQuantity,
        ),
    )

    # systems = Quantity(
    #     type=str,
    #     shape=['*'],
    #     a_eln=ELNAnnotation(
    #         component=ELNComponentEnum.EnumEditQuantity,
    #         props=dict(
    #             suggestions=[
    #                 'Atoms',
    #                 'Binaries',
    #                 'Bulk properties',
    #                 'CO2 activation',
    #                 'Elemental solids',
    #                 'Elements',
    #                 'GDB molecular database',
    #                 'GDB7',
    #                 'Grain boundaries',
    #                 'Heterogeneous catalysis',
    #                 'Images',
    #                 'Inorganic compounds',
    #                 'Insulators',
    #                 'Iron',
    #                 'Low-dimensional materials',
    #                 'Metals',
    #                 'OQMD database',
    #                 'Octet binaries',
    #                 'Oxygen evolution reaction',
    #                 'Oxygen reduction reaction',
    #                 'Perovskite',
    #                 'Rock salt',
    #                 'Scaling relations',
    #                 'Semicondictor oxides',
    #                 'Silicon',
    #                 'Solid State Crystals',
    #                 'Surface',
    #                 'Synthetic data',
    #                 'System',
    #                 'Ternaries',
    #                 'Tetradymites',
    #                 'Topological insulators',
    #                 'Transparent conducting oxides',
    #                 'UCI regression dataset',
    #                 'Zinc blende',
    #                 'matbench_expt_is_metal',
    #             ]
    #         ),
    #     ),
    # )

    # notebook_path = Quantity(
    #     type=str,
    #     description="""
    #     The relative path to the .ipynb file inside docker deployment.
    #     """,
    #     a_eln=ELNAnnotation(
    #         component=ELNComponentEnum.StringEditQuantity, label='Path of notebook'
    #     ),
    # )

    # references = Quantity(
    #     type=Reference,
    #     shape=['*'],
    # )

    methods = SubSection(section=Method, repeats=True)

    systems = SubSection(section=System, repeats=True)

    references = SubSection(section=Reference, repeats=True)


    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('AIToolkitNotebook.normalize', parameter=configuration.parameter)

        # if self.authors:
        #     self.authors_list = ', '.join([f"{v['first_name']} {v['last_name']}" for v in self.authors])

        # This is a workaroudn to use Author field on the gui
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