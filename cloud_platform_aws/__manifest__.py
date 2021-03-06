# Copyright 2017-2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Cloud Platform AWS',
    'summary': 'Addons required for the Camptocamp Cloud Platform on Amazon AWS',
    'version': '13.0.1.0.0',
    'author': 'Camptocamp,Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'depends': [
        'cloud_platform',
        'attachment_s3',
        'base_attachment_object_storage',
    ],
    'website': 'https://www.camptocamp.com',
    'data': [
        'data/cloud_platform_aws_data.xml'
    ],
    'installable': True,
}
