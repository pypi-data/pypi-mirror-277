from flask import Blueprint

from wlkc_core import ResHelper
from wlkc_core.utils import RedisHelper

mod = Blueprint('config', __name__, url_prefix='/system/config/')


@mod.route('/configKey/<key>')
def configKey(key):
    config = RedisHelper.get_str(f"sys_config:{key}")
    return ResHelper.success(message=config)
