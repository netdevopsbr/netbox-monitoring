# Netbox plugin related import
from extras.plugins import PluginConfig

class NetboxMonitoringConfig(PluginConfig):
    name = "netbox_monitoring"
    verbose_name = "Netbox Monitoring"
    description = "Netbox Monitoring - Netbox and Zabbix integration through API"
    version = "0.0.1"
    author = "Emerson Felipe (@emersonfelipesp)"
    author_email = "emersonfelipe.2003@gmail.com"
    base_url = "netbox_zabbix"
    required_settings = []
    default_settings = {
        'netbox': {
            'domain': 'netbox.example.com',     # May also be IP address
            'http_port': 80,
            'token': '0dd7cddfaee3b38bbffbd293dd44c4a03f9c9d38',
            'ssl': False,
        },
        'zabbix': {
            'domain': 'zabbix.example.com',     # May also be IP address
            'http_port': 80,
            'token': 'zabbix_api_token_value',
            'ssl': False
        }
    }

config = NetboxMonitoringConfig