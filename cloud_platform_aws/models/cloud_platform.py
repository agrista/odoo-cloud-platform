# Copyright 2016-2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)

try:
    from odoo.addons.cloud_platform.models.cloud_platform import FilestoreKind
    from odoo.addons.cloud_platform.models.cloud_platform import PlatformConfig
except ImportError:
    FilestoreKind = None
    PlatformConfig = None
    _logger.debug("Cannot 'import from cloud_platform'")


class CloudPlatform(models.AbstractModel):
    _inherit = 'cloud.platform'

    @api.model
    def _platform_kinds(self):
        kinds = super(CloudPlatform, self)._platform_kinds()
        kinds.append('aws')
        return kinds

    @api.model
    def _config_by_server_env_for_aws(self):
        configs = {
            'prod': PlatformConfig(filestore=FilestoreKind.s3),
            'stage': PlatformConfig(filestore=FilestoreKind.s3),
            'dev': PlatformConfig(filestore=FilestoreKind.db),
        }
        return configs

    @api.model
    def install_aws(self):
        self.install('aws')
